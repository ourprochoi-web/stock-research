# Stock Research Archive

산업 & 기업 심층 분석 리서치를 모아두는 GitHub Pages 사이트.

**Live**: https://ourprochoi-web.github.io/stock-research/

---

## 사이트 구조

```
stock-research/
├── index.html              ← 메인 페이지 (히어로 애니메이션 + 섹션별 카드)
├── data/
│   └── research.json       ← 리서치 메타데이터 (참조용, 실 데이터는 index.html 인라인)
├── ai-infra/               ← AI 인프라 카테고리
│   ├── ai_value_chain_guide_v2.html
│   └── ai_valuechain_deep_dive_20260611.html
├── physical-ai/            ← Physical AI 카테고리
│   └── physical-ai-investment-map_1.html
└── README.md
```

## 새 리서치 추가 방법

### 1. HTML 파일 배치

해당 카테고리 폴더에 HTML 파일을 넣는다. 새 카테고리면 폴더를 새로 만든다.

```
# 기존 카테고리에 추가
ai-infra/my_new_research.html

# 새 카테고리
semiconductor/samsung_analysis.html
```

### 2. index.html 데이터 업데이트

`index.html` 상단의 `DATA` 배열에 항목을 추가한다.

```js
{
  "title": "리서치 제목",
  "file": "카테고리폴더/파일명.html",
  "date": "2026-07-01",
  "category": "카테고리명",
  "type": "산업 개관 | 종목 심화 | 투자 지도",
  "series": "시리즈명 또는 null",
  "desc": "한 줄 설명"
}
```

### 3. (새 카테고리인 경우) 섹션 설정 추가

`index.html`의 `SECTIONS` 객체에 새 카테고리 설정을 추가한다.

```js
SECTIONS['반도체'] = {
  cssClass: 'semiconductor',
  title: 'Semiconductor',
  desc: '섹션 설명',
  badgeMap: { '산업 개관': 'badge-overview', '종목 심화': 'badge-deep', '투자 지도': 'badge-map' }
};
```

CSS에서 `.sec-label.semiconductor` 색상도 추가한다.

### 4. 커밋 & 푸시

```bash
git add . && git commit -m "Add: 리서치 제목" && git push
```

GitHub Pages가 자동 배포됨.

## 카테고리 색상 매핑

| 카테고리 | CSS 클래스 | 색상 |
|---------|-----------|------|
| AI 인프라 | `ai-infra` | 인디고 (#818cf8) |
| Physical AI | `physical-ai` | 에메랴드 (#34d399) |
| 반도체 | `semiconductor` | 보라 (#7c3aed) — 예비 |
| 바이오 | `biotech` | 레드 (#dc2626) — 예비 |
| 에너지 | `energy` | 앰버 (#a16207) — 예비 |

## 페이지 기능

### index.html
- 풀스크린 히어로: 파티클 + 오로라 그라디언트 + 텍스트 fade-up 애니메이션
- 통계 바: 리서치 수, 테마 수 카운트업 애니메이션
- 카테고리별 섹션: 스크롤 시 카드 IntersectionObserver fade-in
- 시리즈 그루핑: 같은 시리즈 리서치는 세로 라인으로 연결

### 리서치 페이지
- 좌측 상단 고정 Home 버튼 → index로 복귀
- 각 페이지는 독립적인 단일 HTML (외부 의존성: Pretendard 폰트 CDN만 사용)

## 기술 스택

- 순수 HTML/CSS/JS (프레임워크 없음)
- GitHub Pages (정적 호스팅)
- Pretendard 웹폰트 (CDN)
