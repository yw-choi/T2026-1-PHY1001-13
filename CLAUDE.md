# Project Instructions

## 프로젝트 디렉토리 구조

- `website/`: Astro 기반 강의 웹사이트 (메인)
  - `src/content/lectures/`: 강의 마크다운 파일
  - `src/content/homework/`: 숙제 마크다운 파일
  - `src/simulations/`: 시뮬레이션 소스 HTML 파일
  - `src/data/simulations.ts`: 시뮬레이션 메타데이터 (id, 파일명, 제목, 챕터)
  - `src/pages/simulations/[id].astro`: 개별 시뮬레이션 페이지 (BaseLayout + iframe)
  - `public/simulations/` → `src/simulations/` 심볼릭 링크 (Astro가 자동 서빙)
  - `src/components/SlideEngine.astro`: 슬라이드 엔진 (드로잉, 네비게이션, 스크래치패드 등)
  - `src/styles/global.css`: 테마 변수 및 슬라이드 콘텐츠 스타일
  - `src/pages/lectures/[id].astro`: 강의 렌더러 (KaTeX 서버 사이드 렌더링)
- `exams/`: 시험문제 (예전 시험 문제 포함)
- `homeworks/`: 숙제 — 매 챕터별 연습문제, 솔루션
- `illustrations/`: 할리데이 교재 이미지 파일들 (저작권 문제로 강의 공개 자료에 직접 사용 불가)
- `syllabus/`: 강의 실라버스
- `testbank/`: 할리데이 교재 testbank
- `textbook/`: 할리데이 교재 챕터별 pdf 파일
- `gh-pages/`: GitHub Pages 배포용 로컬 클론 (`yw-choi/yw-choi.github.io`)

`.gitignore`에 의해 `textbook/`, `testbank/`, `illustrations/`, `gh-pages/`는 버전 관리에서 제외된다.

## 강의 슬라이드 제작

### 대상 & 수준

- **대상**: 물리학과, 공대 1학년 (일반물리)
- **수준**: 개념 기반, 간단한 미적분 포함 가능. 
- **분량**: 한 챕터당 1시간 15분 강의에 맞춤

### 컨텐츠 원칙

- 교재(할리데이) 각 챕터의 컨텐츠 구성을 따른다.
- 번역체 금지. 자연스러운 한국어로 작성
- 교재의 미국문화 레퍼런스 → 한국 학생이 이해 가능한 예시로 대체
- 유용한 실생활 예시나 데모 영상이 있으면 삽입
- 실생활 예시에는 오픈 라이선스 사진 활용 (Unsplash, Wikimedia Commons, Pexels 등 → `public/img/chNN/`에 다운로드)
- **교재 일러스트는 사용 불가** (저작권). 필요한 다이어그램은 직접 생성 (SVG)

### 언어 & 표기

- 본문: 한국어, 주요 용어는 영어 병기 (첫 등장 시 "가속도(acceleration)" 식으로)
- 번역이 어색한 용어는 영어 그대로 사용 가능
- 벡터 표기: $\vec{v}$ 스타일
- 단위계: SI

### 수식

- 수식 유도는 처음부터 끝까지, 중간 과정 생략 없이
- KaTeX 문법 (`$...$` 인라인, `$$...$$` 블록)
- KaTeX는 `[id].astro`에서 서버 사이드 렌더링됨 (클라이언트 사이드 아님)

### 마크다운 주의사항

- `marked` 라이브러리 제약: `**볼드**` 닫는 `**` 바로 뒤에 공백 없이 한글이 붙으면 볼드가 작동하지 않는다
  - ❌ `**에너지(energy)**는` → 볼드 실패
  - ✅ `**에너지(energy)** 는` → 볼드 성공
  - 닫는 `**` 뒤에 반드시 공백을 넣을 것 (한글·괄호 등이 바로 이어질 때)

### 슬라이드 구성

1. **타이틀 슬라이드**: `# N장: 제목` + 영문 부제
2. **도입**: 이번 장에서 배울 내용 개요, 한국 학생에게 친숙한 실생활 예시
3. **섹션별 구성** (`## N.1 제목`, `## N.2 제목` 등): 교재 섹션 순서
   - 핵심 개념 + 수식 유도 (상세하게)
   - 직접 생성한 다이어그램/그림 (SVG inline 또는 `public/img/`에 저장)
   - 시뮬레이션 삽입 (`<!-- sim:파일명.html -->`)
4. **Review & Summary**: 핵심 공식과 개념 정리 (1~2 슬라이드)

- 판서 페이지(`<!-- blank -->`)는 사용하지 않음 → 필요 시 스크래치패드 활용
- 콘텐츠 오버플로 주의: 한 슬라이드에 display 수식 3~4개, bullet 6~7개, 테이블 행 6개 이하
- 슬라이드 구분: `---` (수평선)으로 페이지 분리

### 다이어그램 디자인 스펙

모든 다이어그램은 SVG로 생성하며, 아래 규격을 반드시 따른다:

- **색상 팔레트** (4색 고정):
  - 주색: `#8B0029` (서강대 빨간) — 힘 벡터, 주요 요소, 강조
  - 보조색: `#2563EB` (파랑) — 속도 벡터, 보조 요소
  - 중립: `#6B7280` (회색) — 보조선, 치수선, 참고 텍스트
  - 배경 요소: `#F3F4F6` (밝은 회색) — 물체 내부 채움, 바닥 등
- **선 굵기**:
  - 물체 외곽선: `stroke-width="2"`
  - 벡터 화살표: `stroke-width="2.5"`
  - 보조선/치수선: `stroke-width="1"`, `stroke-dasharray="4 3"`
- **화살표**: `marker-end`로 삼각형 화살촉 사용, 크기 일관되게
- **텍스트**: `font-family="sans-serif"`, 레이블 `font-size="14"`, 수식 `font-style="italic"`
- **크기**: `viewBox` 기준 가로 600~800, 세로 300~500. 슬라이드 내에서 `max-height:50vh`로 제한
- **여백**: 모든 요소에서 SVG 경계까지 최소 20px 여백
- **파일 위치**: `website/public/img/chNN/파일명.svg`
- **슬라이드 참조**: `<img src="/img/chNN/파일명.svg" style="max-height:50vh">`

### 제작 에이전트 구조 (Plan-first Pipeline)

강의 슬라이드 제작 요청 시 다음 순서로 진행한다:

1. **Planner**: 교재 PDF(`textbook/cNN.pdf`) + 웹 조사 → 챕터별 강의 계획
   - 섹션 구성, 핵심 개념, 수식 목록
   - 시뮬레이션 주제 1~3개 선정
   - 필요한 다이어그램 목록 (각 다이어그램의 목적과 포함할 요소 명시)
   - 실생활 사진이 필요한 슬라이드 명시
2. **Simulation**: 계획된 시뮬레이션 구현 + 자체 UI 테스트
   - 기존 시뮬레이션 코드 참조하여 UI 일관성 유지
   - Planner 완료 후 병렬 실행 가능
3. **Writer + Review**: 계획 기반 슬라이드 작성
   - 다이어그램 직접 생성 (위 디자인 스펙 준수)
   - 오픈 라이선스 사진 다운로드 및 삽입
   - 시뮬레이션 삽입
   - 완성 후 물리/수학 오류 검토
   - `src/data/simulations.ts`에 메타데이터 추가
4. **Diagram Reviewer**: 생성된 모든 SVG 다이어그램을 검토
   - 요소 겹침 없는지 확인
   - 레이블이 선이나 도형에 가려지지 않는지
   - 화살표 방향과 크기가 물리적으로 올바른지
   - 색상 팔레트와 선 굵기가 스펙을 따르는지
   - 전체적으로 보기에 어색한 부분이 없는지
   - 문제가 있으면 수정 후 재검토

### 새 강의 파일 추가

1. `website/src/content/lectures/weekNN.md` 파일 생성
2. Frontmatter:
   ```yaml
   ---
   title: "강의 제목"
   week: 5
   chapters: "10장"
   topics: "주제1, 주제2, 주제3"
   ---
   ```
3. 특수 디렉티브:
   - `<!-- sim:파일명.html -->` → `src/simulations/파일명.html` 시뮬레이션 임베드 (다음 줄에 제목 텍스트)

### 새 시뮬레이션 추가

1. `website/src/simulations/이름.html` 파일 생성 (단일 HTML, 외부 의존성 없이)
2. `website/src/data/simulations.ts`에 메타데이터 추가 (id, file, title, chapter, description)
3. 테마: 서강대 빨간색 `#8B0029` + 흰색 배경
4. 레이아웃: 왼쪽 캔버스 + 오른쪽 컨트롤 패널 (260px)
5. 반응형: 모바일에서는 세로 배치 (`@media max-width: 700px`)
6. HiDPI 대응: `window.devicePixelRatio` 사용
7. 파라미터: 슬라이더 2~3개 + 시작/정지 정도. 직관적 UI, 즉각적 시각 피드백
8. 강의에서 사용: `<!-- sim:이름.html -->` 디렉티브로 임베드
9. 독립 페이지(`/simulations/id/`)로도, 슬라이드 내 iframe으로도 사용 가능
10. **물리 개념 명시**: 시뮬레이션이 확인하고자 하는 물리적 개념을 화면에 명확하게 표시한다 (예: "일-운동에너지 정리: ΔK = W")
11. **수식·물리량 표시**: 관련 수식과 물리량(현재 값)을 실시간으로 화면에 표시한다. 단순히 숫자만 보여주지 말고, 해당 수식이 어떤 물리 법칙에서 나온 것인지 맥락을 제공한다

### 배포

```bash
cd website && npm run build
cp -r dist/* ../gh-pages/static/2026-PHY1001-13/
cd ../gh-pages && git add -A && git commit -m "Update" && git push
```

## 연습문제 출제 지침

- `testbank/`, `exams/`, `textbook/`을 참조하여 출제한다.
- 숫자 계산 문제
- 개념을 묻고 공식을 유도하는 문제
- 주어진 상황을 파악하고 답을 숫자가 아니라 식으로 유도하는 문제
- 출제 워크플로: Agent A(출제자)가 문제를 작성한 후, Agent B(검토자)가 각 문제의 오류·풀이 정합성·난이도를 검수한다. Agent A와 Agent B가 합의할 때까지 반복 수정한다.
- 출력 형식: md 파일과 pdf 파일을 모두 생성한다. md → pdf 변환은 `pandoc`을 사용한다.
- 숙제 수식은 최대한 LaTeX(`$...$`, `$$...$$`)를 활용하여 작성한다.

## 테마 & 스타일

- 서강대 빨간색: `#8B0029`, 밝은 변형: `#a3003a`
- 배경: 흰색, 텍스트: `#1a1a1a`
- CSS 변수는 `website/src/styles/global.css`에 정의
- 슬라이드 콘텐츠 스타일(`.slide-content`)도 `global.css`에서 관리 — 새 강의는 자동 적용
