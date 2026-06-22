# Stock Research Archive

산업 & 기업 심층 분석 리서치를 모아두는 GitHub Pages 사이트.

**Live**: https://ourprochoi-web.github.io/stock-research/

---

## 사이트 구조

```
stock-research/
├── index.html              ← 메인 페이지 (히어로 애니메이션 + 섹션별 카드)
├── sitemap.xml             ← SEO 사이트맵
├── robots.txt              ← 크롤러 설정
├── .nojekyll               ← GitHub Pages Jekyll 비활성화
├── data/                   ← 리서치 데이터 (MD)
│   ├── research.json
│   ├── research-backlog.md
│   ├── research_ai_power_*.md      (8개)
│   ├── research_hbm_pkg_*.md       (4개)
│   ├── research_ai_bio_*.md        (4개)
│   ├── research_robot_*.md         (4개)
│   ├── research_space_*.md         (4개)
│   └── research_new_topic_*.md     (3개, 로드맵)
├── ai-infra/               ← AI 인프라 (HTML 3개)
├── hbm-packaging/          ← HBM/패키징 (HTML 11개)
├── defense/                ← K-방산 (HTML 16개)
├── physical-ai/            ← Physical AI (HTML 1개)
└── README.md
```

## 완성된 리서치 시리즈 (6개, 리서치 MD 24개+)

### 1. AI 전력 인프라 시리즈 (8 MD)
- 글로벌/한국 기업 재무 심화, 크로스 밸류에이션, 테마 분석 (SMR, 가스터빈, 송배전, 냉각)
- `data/research_ai_power_*.md`

### 2. HBM/패키징 시리즈 (4 MD + 11 HTML)
- 글로벌/한국 기업 재무 심화, 테마 분석 (CoWoS, 하이브리드 본딩, HBM4)
- `data/research_hbm_pkg_*.md`, `hbm-packaging/*.html`

### 3. K-방산 시리즈 (16 HTML)
- 한국 방산 밸류체인, 기업 심화, 투자 지도
- `defense/*.html`

### 4. AI 바이오 시리즈 (4 MD, ~2,820줄) — 2026-06-23
- `data/research_ai_bio_companies_global.md` — 글로벌 7사 (Recursion-Exscientia, Tempus AI, Insilico Medicine, Schrodinger, Veracyte, Guardant Health, PathAI)
- `data/research_ai_bio_companies_kr.md` — 한국 5사 (삼성바이오로직스, 셀트리온, 루닛, 뷰노, 에임메드)
- `data/research_ai_bio_investment.md` — 크로스 밸류에이션 프레임워크
- `data/research_ai_bio_themes.md` — AI 신약개발 + 정밀의료 + 디지털치료제

### 5. 로봇/휴머노이드 시리즈 (4 MD, ~2,515줄) — 2026-06-23
- `data/research_robot_companies_global.md` — 글로벌 7사+ (Tesla/Optimus, Figure AI, Agility, Fanuc, ABB, ISRG, Symbotic)
- `data/research_robot_companies_kr.md` — 한국 5사 (현대차/BD, 레인보우, 두산, 뉴로메카, 로보티즈)
- `data/research_robot_investment.md` — 크로스 밸류에이션 프레임워크
- `data/research_robot_themes.md` — 휴머노이드 경제학 + 로봇 두뇌 + 부품 서플라이체인

### 6. 우주 경제 시리즈 (4 MD, ~2,885줄) — 2026-06-23
- `data/research_space_companies_global.md` — 글로벌 7사+ (SpaceX, Rocket Lab, Planet Labs, Iridium, AST SpaceMobile, L3Harris, Redwire)
- `data/research_space_companies_kr.md` — 한국 5사 (한화에어로스페이스, 이노스페이스, 쎄트렉아이, 한화시스템, AP위성)
- `data/research_space_investment.md` — 크로스 밸류에이션 프레임워크
- `data/research_space_themes.md` — 발사 비용 혁명 + 메가 컨스텔레이션 + 다운스트림 골드러시

## 예정된 리서치

### 7. AI 소프트웨어 레이어 — 에이전트·엔터프라이즈 AI 투자 지도
- AI Agent, Vertical SaaS, 코딩 자동화, AI 보안
- Microsoft, Palantir, ServiceNow + 한국 AI SW주

### 7-1. AI 투자 의사결정 프레임워크 — 돈의 흐름·병목·해자·비대칭성
- 병목, 해자, 비대칭성 3대 조건 / 소버린 AI / 닷컴버블 비교
- 소스: `data/note-ai-money-flow_20260618.md`

## 향후 후보

| # | 주제 | 키워드 |
|---|------|--------|
| 8 | 에너지 전환/2차전지 | LG엔솔, 삼성SDI, 전고체, ESS |
| 9 | AI 반도체 설계 | NVIDIA vs Broadcom ASIC, FuriosaAI, Rebellions |
| 10 | K-조선/해양플랜트 | HD한국조선, 한화오션, LNG운반선 |

---

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
| Physical AI | `physical-ai` | 에메랄드 (#34d399) |
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
