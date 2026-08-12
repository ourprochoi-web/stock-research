#!/usr/bin/env python3
"""
상장사 전체 자사주 현황 조사 스크립트
DART OpenAPI를 사용하여 KOSPI/KOSDAQ 전 상장사의 자기주식 보유 현황을 수집합니다.

사용법:
    python3 dart_treasury_stock.py --api-key YOUR_40_CHAR_KEY
    python3 dart_treasury_stock.py --api-key YOUR_40_CHAR_KEY --year 2025
    python3 dart_treasury_stock.py --api-key YOUR_40_CHAR_KEY --resume  # 중단된 작업 이어서

출력:
    treasury_stock_YYYY_YYYYMMDD.csv  — 전체 결과
    treasury_stock_top50_YYYYMMDD.csv — 자사주 비율 상위 50 요약
"""

import argparse
import io
import json
import os
import sys
import time
import zipfile
from datetime import datetime
from xml.etree import ElementTree as ET

import pandas as pd
import requests

BASE_URL = "https://opendart.fss.or.kr/api"
CORP_CODE_URL = f"{BASE_URL}/corpCode.xml"
TREASURY_URL = f"{BASE_URL}/tesstkAcqsDspsSttus.json"

# 보고서 코드: 사업보고서(연간)
REPRT_CODES = {
    "사업보고서": "11011",
    "반기보고서": "11012",
    "1분기보고서": "11013",
    "3분기보고서": "11014",
}

PROGRESS_FILE = "treasury_stock_progress.json"
RATE_LIMIT_DELAY = 0.15  # 초 (분당 ~400건, 안전 마진)


def get_corp_codes(api_key: str) -> pd.DataFrame:
    """DART에서 전체 기업 고유번호 목록을 다운로드하고 상장사만 필터링"""
    cache_file = "dart_corp_codes.csv"

    # 캐시 확인 (당일 것만 사용)
    if os.path.exists(cache_file):
        mtime = datetime.fromtimestamp(os.path.getmtime(cache_file))
        if mtime.date() == datetime.now().date():
            print(f"[INFO] 캐시 사용: {cache_file}")
            return pd.read_csv(cache_file, dtype=str)

    print("[1/4] DART 기업코드 목록 다운로드 중...")
    resp = requests.get(CORP_CODE_URL, params={"crtfc_key": api_key})
    if resp.status_code != 200:
        print(f"[ERROR] 기업코드 다운로드 실패: HTTP {resp.status_code}")
        sys.exit(1)

    # ZIP 파일 해제 → XML 파싱
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        xml_name = zf.namelist()[0]
        xml_data = zf.read(xml_name)

    root = ET.fromstring(xml_data)
    corps = []
    for item in root.findall("list"):
        corp_code = item.findtext("corp_code", "")
        corp_name = item.findtext("corp_name", "")
        stock_code = item.findtext("stock_code", "")
        modify_date = item.findtext("modify_date", "")
        if stock_code and stock_code.strip():  # 상장사만 (주식코드 있는 것)
            corps.append({
                "corp_code": corp_code,
                "corp_name": corp_name,
                "stock_code": stock_code.strip(),
                "modify_date": modify_date,
            })

    df = pd.DataFrame(corps)
    df.to_csv(cache_file, index=False)
    print(f"[INFO] 상장사 {len(df)}개 확인 (전체 {len(root.findall('list'))}개 중)")
    return df


def fetch_treasury_stock(api_key: str, corp_code: str, year: int, reprt_code: str = "11011"):
    """개별 기업의 자기주식 취득·처분 현황 조회"""
    params = {
        "crtfc_key": api_key,
        "corp_code": corp_code,
        "bsns_year": str(year),
        "reprt_code": reprt_code,
    }
    try:
        resp = requests.get(TREASURY_URL, params=params, timeout=10)
        data = resp.json()
        status = data.get("status", "")
        if status == "000":  # 정상
            return data.get("list", [])
        elif status == "013":  # 조회된 데이터 없음
            return []
        else:
            return None  # 기타 에러
    except Exception:
        return None


def load_progress():
    """중단 지점 로드"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"completed": [], "results": []}


def save_progress(progress):
    """진행 상황 저장"""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, ensure_ascii=False)


def run(api_key: str, year: int, resume: bool = False):
    """메인 실행"""
    today = datetime.now().strftime("%Y%m%d")
    output_file = f"treasury_stock_{year}_{today}.csv"
    top_file = f"treasury_stock_top50_{today}.csv"

    # 1. 기업코드 목록
    corps = get_corp_codes(api_key)
    total = len(corps)

    # 2. 진행 상황 복원 또는 초기화
    if resume:
        progress = load_progress()
        completed_set = set(progress["completed"])
        results = progress["results"]
        print(f"[INFO] 이전 진행 복원: {len(completed_set)}/{total} 완료")
    else:
        completed_set = set()
        results = []

    remaining = [
        row for _, row in corps.iterrows()
        if row["corp_code"] not in completed_set
    ]

    print(f"[2/4] 자사주 현황 조회 시작 (대상: {len(remaining)}사, 연도: {year})")
    print(f"       예상 소요: ~{len(remaining) * RATE_LIMIT_DELAY / 60:.0f}분")
    print()

    errors = 0
    has_data_count = 0

    for i, row in enumerate(remaining):
        corp_code = row["corp_code"]
        corp_name = row["corp_name"]
        stock_code = row["stock_code"]

        data = fetch_treasury_stock(api_key, corp_code, year)

        if data is None:
            errors += 1
        elif len(data) > 0:
            has_data_count += 1
            for item in data:
                results.append({
                    "corp_code": corp_code,
                    "corp_name": corp_name,
                    "stock_code": stock_code,
                    "취득방법_대": item.get("acqs_mth1", ""),
                    "취득방법_중": item.get("acqs_mth2", ""),
                    "취득방법_소": item.get("acqs_mth3", ""),
                    "주식종류": item.get("stock_knd", ""),
                    "기초수량": item.get("bsis_qy", ""),
                    "취득수량": item.get("change_qy_acqs", ""),
                    "처분수량": item.get("change_qy_dsps", ""),
                    "소각수량": item.get("change_qy_incnr", ""),
                    "기말수량": item.get("trmend_qy", ""),
                    "비고": item.get("rm", ""),
                })

        completed_set.add(corp_code)

        # 진행률 표시 (50건마다)
        done = len(completed_set)
        if (i + 1) % 50 == 0 or (i + 1) == len(remaining):
            pct = done / total * 100
            print(f"  [{done:,}/{total:,}] {pct:.1f}% | 데이터 있음: {has_data_count} | 에러: {errors} | 현재: {corp_name}")

        # 200건마다 중간 저장
        if (i + 1) % 200 == 0:
            save_progress({"completed": list(completed_set), "results": results})

        time.sleep(RATE_LIMIT_DELAY)

    # 3. 결과 저장
    print(f"\n[3/4] 결과 저장 중...")

    if not results:
        print("[WARN] 자사주 데이터가 있는 기업이 없습니다.")
        return

    df = pd.DataFrame(results)

    # 숫자 컬럼 정리 (콤마 제거 → 숫자 변환)
    num_cols = ["기초수량", "취득수량", "처분수량", "소각수량", "기말수량"]
    for col in num_cols:
        df[col] = df[col].astype(str).str.replace(",", "").str.replace("-", "0").str.strip()
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

    # 보통주만 필터 (주요 분석용)
    df_common = df[df["주식종류"].str.contains("보통", na=False)].copy()

    # 전체 저장
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"  전체 결과: {output_file} ({len(df)}행, {df['corp_name'].nunique()}사)")

    # 4. 상위 50 요약 (보통주 기말수량 기준)
    print(f"[4/4] 자사주 보유 상위 50 요약 생성...")

    if len(df_common) > 0:
        # 기업별 보통주 자사주 합계
        summary = df_common.groupby(["corp_code", "corp_name", "stock_code"]).agg(
            기초수량_합=("기초수량", "sum"),
            취득수량_합=("취득수량", "sum"),
            처분수량_합=("처분수량", "sum"),
            소각수량_합=("소각수량", "sum"),
            기말수량_합=("기말수량", "sum"),
        ).reset_index()

        summary = summary.sort_values("기말수량_합", ascending=False)
        top50 = summary.head(50)
        top50.to_csv(top_file, index=False, encoding="utf-8-sig")
        print(f"  상위 50: {top_file}")

        # 콘솔 출력
        print(f"\n{'='*80}")
        print(f"  자사주 보유 상위 20 (보통주 기말수량 기준, {year}년 사업보고서)")
        print(f"{'='*80}")
        for idx, row in top50.head(20).iterrows():
            print(f"  {row['corp_name']:>16s} ({row['stock_code']})  "
                  f"기말: {row['기말수량_합']:>15,}주  "
                  f"취득: {row['취득수량_합']:>12,}  "
                  f"소각: {row['소각수량_합']:>12,}")

        # 소각 활발 기업
        active_cancel = summary[summary["소각수량_합"] > 0].sort_values("소각수량_합", ascending=False)
        if len(active_cancel) > 0:
            cancel_file = f"treasury_stock_canceled_{today}.csv"
            active_cancel.to_csv(cancel_file, index=False, encoding="utf-8-sig")
            print(f"\n{'='*80}")
            print(f"  자사주 소각 실행 기업 ({len(active_cancel)}사)")
            print(f"{'='*80}")
            for idx, row in active_cancel.head(20).iterrows():
                print(f"  {row['corp_name']:>16s} ({row['stock_code']})  "
                      f"소각: {row['소각수량_합']:>12,}주  "
                      f"기말 잔여: {row['기말수량_합']:>15,}")
            print(f"\n  소각 기업 전체: {cancel_file}")

    # 진행 파일 정리
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)

    print(f"\n[DONE] 완료! 총 {df['corp_name'].nunique()}사 조회, {len(df)}건 데이터 수집.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="상장사 전체 자사주 현황 조사")
    parser.add_argument("--api-key", required=True, help="DART OpenAPI 인증키 (40자리)")
    parser.add_argument("--year", type=int, default=2025, help="조회 사업연도 (기본: 2025)")
    parser.add_argument("--resume", action="store_true", help="중단된 작업 이어서 실행")
    args = parser.parse_args()

    if len(args.api_key) != 40:
        print("[ERROR] 인증키는 40자리여야 합니다.")
        sys.exit(1)

    run(args.api_key, args.year, args.resume)
