---
title: "12장: 평형과 탄성"
week: 12
chapters: "12장"
topics: "평형 조건, 정적 평형, 무게중심, 탄성, 응력, 변형률, 영률"
---

# 12장: 평형과 탄성

Equilibrium and Elasticity

---

## 이번 장에서 배울 내용

- **평형(equilibrium)** 의 조건: 알짜힘 = 0, 알짜 돌림힘 = 0
- **정적 평형(static equilibrium)**: 물체가 정지해 있고 회전하지 않는 상태
- **무게중심(center of gravity)** 과 안정성
- 평형 문제 풀이 전략과 예제
- **탄성(elasticity)**: 응력과 변형률의 관계
- **영률(Young's modulus)**, 전단 탄성률(shear modulus), 체적 탄성률(bulk modulus)

---

## 왜 평형이 중요한가?

건물, 다리, 크레인. 이 모든 구조물은 **정적 평형** 상태에 있어야 안전하다.

서울 잠실의 **롯데월드타워** (555 m)는 한국에서 가장 높은 건물이다. 이 건물이 쓰러지지 않으려면, 모든 층에서 힘과 돌림힘의 균형이 맞아야 한다.

건설 현장의 **타워크레인** 은 수십 톤의 하중을 들어올리면서도 넘어지지 않아야 한다. 이것이 가능한 이유는 크레인 설계자가 평형 조건을 정밀하게 적용했기 때문이다.

---

## 12.1 평형의 조건

물체가 **평형(equilibrium)** 상태에 있으려면 두 가지 조건을 만족해야 한다.

**병진 평형** (translational equilibrium):

$$\vec{F}_\text{net} = \sum \vec{F} = 0$$

**회전 평형** (rotational equilibrium):

$$\vec{\tau}_\text{net} = \sum \vec{\tau} = 0$$

두 조건을 모두 만족하면 물체의 선운동량과 각운동량이 변하지 않는다.

---

### 정적 평형 vs. 동적 평형

**정적 평형(static equilibrium):**
- $\vec{F}_\text{net} = 0$, $\vec{\tau}_\text{net} = 0$
- **추가 조건**: $\vec{v} = 0$, $\vec{\omega} = 0$ (정지해 있고 회전하지 않음)

**동적 평형:**
- $\vec{F}_\text{net} = 0$, $\vec{\tau}_\text{net} = 0$
- 일정한 속도로 운동하거나 일정한 각속도로 회전

이 장에서는 주로 **정적 평형** 을 다룬다.

---

### 성분별 평형 조건

2차원 문제에서 평형 조건을 성분으로 쓰면:

$$\sum F_x = 0$$

$$\sum F_y = 0$$

$$\sum \tau_z = 0$$

3개의 미지수를 구할 수 있는 **3개의 방정식** 이다.

> **참고**: 돌림힘의 피벗(축)은 **어디든** 선택할 수 있다. 현명한 피벗 선택이 풀이를 단순하게 만든다!

---

## 12.2 무게중심

### 무게중심(center of gravity)이란?

중력은 물체의 모든 부분에 작용한다. 그러나 돌림힘 계산에서 중력은 **무게중심(center of gravity, cog)** 이라는 한 점에 집중된다고 생각할 수 있다.

$$x_\text{cog} = \frac{\sum m_i g_i x_i}{\sum m_i g_i}$$

중력 가속도 $g$가 물체 전체에서 균일하면 ($g_i = g$):

$$x_\text{cog} = \frac{\sum m_i x_i}{\sum m_i} = x_\text{com}$$

**무게중심 = 질량중심** (중력이 균일할 때)

---

### 안정성(Stability)

<img src="/img/ch12/stability-comparison.svg" style="max-height:50vh">

물체를 살짝 밀었을 때, 무게중심이 어떻게 변하는지가 안정성을 결정한다.

---

### 안정 평형, 불안정 평형, 중립 평형

판정 기준: 평형 위치에서 **살짝 밀었을 때 무게중심의 높이가 어떻게 변하는가**.

**안정 평형(stable equilibrium):**
- 작은 변위에서 **무게중심이 올라간다** → 중력이 복원력으로 작용
- 예: 그릇 바닥의 공, 천장에 매달린 진자

**불안정 평형(unstable equilibrium):**
- 작은 변위에서 **무게중심이 내려간다** → 평형에서 벗어남
- 예: 산 정상의 공, 거꾸로 세운 연필

**중립 평형(neutral equilibrium):**
- 변위해도 무게중심 높이가 그대로 → 새 위치도 평형
- 예: 평면 위의 공

> **세워 놓은 물체의 안정성**: 무게중심에서 내린 수직선이 **지지 기저면(base of support)** 안쪽에 떨어지면 안정. 기저면 밖으로 나가면 넘어진다.

---

## 12.3 평형 문제 풀이 전략

### 풀이 순서

1. **물체 선택**: 평형 상태에 있는 물체를 하나 선택한다
2. **자유 물체 다이어그램(FBD)** 을 그린다: 모든 힘을 표시
3. **좌표축 설정**: $x$, $y$ 축을 정한다
4. **피벗 선택**: 돌림힘 방정식에서 미지력이 사라지도록 피벗을 선택
5. **방정식 세우기**: $\sum F_x = 0$, $\sum F_y = 0$, $\sum \tau = 0$
6. **풀기**: 미지수를 구한다

> **팁**: 피벗을 미지력의 작용점에 놓으면, 그 힘의 돌림힘이 0이 되어 방정식이 간단해진다!

---

## 12.4 예제: 보 위의 블록

<img src="/img/ch12/beam-block-fbd.svg" style="max-height:50vh">

---

### 보 위의 블록: 풀이

균일한 보(질량 $m$, 길이 $L$)가 양쪽 끝에서 지지되고, 왼쪽 끝으로부터 거리 $x$인 위치에 블록(질량 $M$)이 놓여 있다.

**$\sum \tau = 0$** (왼쪽 끝 피벗):

$$F_R \cdot L - mg \cdot \frac{L}{2} - Mg \cdot x = 0$$

$$F_R = \frac{mg}{2} + \frac{Mg \cdot x}{L}$$

**$\sum F_y = 0$**:

$$F_L + F_R - mg - Mg = 0$$

$$F_L = (m + M)g - F_R = \frac{mg}{2} + Mg\left(1 - \frac{x}{L}\right)$$

블록이 오른쪽으로 갈수록 $F_R$ 증가, $F_L$ 감소!

---

## 12.5 예제: 크레인 붐

<img src="/img/ch12/crane-boom-fbd.svg" style="max-height:50vh">

---

### 크레인 붐: 풀이

질량 $m$, 길이 $L$인 균일한 붐이 각도 $\theta$로 벽에 힌지 연결되어 있다. 끝에 질량 $M$의 하중이 매달려 있고, 수평 케이블이 붐의 끝과 벽을 연결한다.

**$\sum \tau = 0$** (힌지 피벗):

$$T \cdot L\sin\theta - mg \cdot \frac{L}{2}\cos\theta - Mg \cdot L\cos\theta = 0$$

$$T = \frac{(m/2 + M)g\cos\theta}{\sin\theta} = \frac{(m/2 + M)g}{\tan\theta}$$

**$\sum F_x = 0$**: $F_h = T$

**$\sum F_y = 0$**: $F_v = (m + M)g$

> $\theta$가 작아질수록 (붐이 수평에 가까워질수록) 케이블 장력 $T$가 급격히 증가한다!

---

## 12.6 예제: 사다리 문제

<img src="/img/ch12/ladder-fbd.svg" style="max-height:50vh">

---

### 사다리 문제: 풀이

질량 $m$, 길이 $L$인 균일한 사다리가 마찰 없는 수직 벽에 기대어 있고, 사다리와 **바닥** 이 이루는 각도가 $\theta$이다. 바닥의 정지마찰계수는 $\mu_s$.

**$\sum \tau = 0$** (바닥 접촉점 피벗):

$$F_w \cdot L\sin\theta - mg \cdot \frac{L}{2}\cos\theta = 0$$

$$F_w = \frac{mg\cos\theta}{2\sin\theta} = \frac{mg}{2\tan\theta}$$

**$\sum F_x = 0$**: $f = F_w$

**$\sum F_y = 0$**: $N = mg$

---

### 사다리가 미끄러지지 않을 조건 (1)

마찰력이 최대 정지마찰력보다 작아야 한다:

$$f \leq \mu_s N$$

앞 슬라이드에서 $f = mg/(2\tan\theta)$, $N = mg$ 이므로:

$$\frac{mg}{2\tan\theta} \leq \mu_s \cdot mg$$

$mg$를 약분:

$$\frac{1}{2\tan\theta} \leq \mu_s$$

---

### 사다리가 미끄러지지 않을 조건 (2)

부등식을 $\theta$에 대해 정리하면:

$$\tan\theta \geq \frac{1}{2\mu_s} \quad\Rightarrow\quad \theta \geq \arctan\!\left(\frac{1}{2\mu_s}\right)$$

사다리 각도가 이 최소 각도보다 **작으면** 미끄러진다.

> 예) $\mu_s = 0.40$ → 최소 각도 $\arctan(1.25) \approx 51.3°$. 더 누이면 미끄러짐.

---

<!-- sim:ladder-equilibrium.html -->
사다리 평형 시뮬레이션

---

## 12.7 탄성(Elasticity)

### 탄성이란?

실제 물체는 완전히 강체가 아니다. 힘을 가하면 **변형(deformation)** 이 생긴다.

- **탄성 변형**: 힘을 제거하면 원래 모양으로 돌아옴
- **소성 변형**: 힘을 제거해도 영구적으로 변형됨
- **파단**: 변형이 한계를 넘으면 부러짐

세 가지 기본 변형:

<img src="/img/ch12/three-deformations.svg" style="max-height:50vh">

---

## 12.8 응력과 변형률

### 응력(Stress)과 변형률(Strain)

**응력(stress)** $\sigma$: 단위 면적당 힘

$$\sigma = \frac{F}{A}$$

단위: Pa (= N/m$^2$), 보통 MPa나 GPa 사용

**변형률(strain)** $\varepsilon$: 변형의 상대적 크기 (무차원)

$$\varepsilon = \frac{\Delta L}{L}$$

---

### 인장과 압축 (Tension & Compression)

봉의 양 끝을 당기거나 누를 때, 응력과 변형률의 정의:

$$\sigma = \frac{F}{A}, \qquad \varepsilon = \frac{\Delta L}{L}$$

탄성 한계 내에서 **영률(Young's modulus)** $E$로 두 양이 비례:

$$\sigma = E \varepsilon$$

---

### 영률 식의 변형

응력·변형률 정의를 대입하면:

$$\frac{F}{A} = E \frac{\Delta L}{L} \quad\Rightarrow\quad \Delta L = \frac{FL}{AE}$$

- $E$가 클수록 같은 힘에 대해 덜 변형 (더 뻣뻣함)
- 같은 재료라도 단면적 $A$를 키우거나 길이 $L$을 줄이면 변형 ↓

---

### 주요 재료의 탄성 특성

| 재료 | 영률 $E$ (GPa) | 극한 강도 $S_u$ (MPa) | 항복 강도 $S_y$ (MPa) |
|---|---|---|---|
| 강철 (ASTM-A36) | 200 | 400 | 250 |
| 알루미늄 | 70 | 110 | 95 |
| 유리 | 65 | 50 (인장) | - |
| 콘크리트 | 30 | 40 (압축) | - |
| 나무 (더글러스 전나무) | 13 | 50 (압축) | - |
| 뼈 | 9 | 170 (압축) | - |

> **롯데월드타워** 는 주로 강철과 콘크리트로 지어졌다. 강철은 인장에 강하고, 콘크리트는 압축에 강하다. 이 둘을 결합한 **철근콘크리트** 가 현대 건축의 핵심이다.

---

## 12.9 전단 탄성률과 체적 탄성률

### 전단(Shear)

물체의 면에 평행한 힘이 작용할 때:

**전단 응력**: $\sigma_s = \frac{F}{A}$

**전단 변형률**: $\varepsilon_s = \frac{\Delta x}{L}$

**전단 탄성률(shear modulus)** $G$:

$$\sigma_s = G \varepsilon_s \quad \Rightarrow \quad \frac{F}{A} = G \frac{\Delta x}{L}$$

---

### 체적(Hydraulic / Bulk)

모든 방향에서 균일한 압력이 작용할 때:

**체적 응력**: $\Delta p$ (압력 변화)

**체적 변형률**: $\frac{\Delta V}{V}$

**체적 탄성률(bulk modulus)** $B$:

$$\Delta p = -B \frac{\Delta V}{V}$$

음수 부호: 압력이 증가하면 부피가 감소하므로.

---

### 세 가지 탄성률 비교

| 변형 유형 | 응력 | 변형률 | 탄성률 |
|---|---|---|---|
| 인장/압축 | $F/A$ | $\Delta L / L$ | 영률 $E$ |
| 전단 | $F/A$ | $\Delta x / L$ | 전단 탄성률 $G$ |
| 체적 | $\Delta p$ | $\Delta V / V$ | 체적 탄성률 $B$ |

세 경우 모두 **선형 관계**: 응력 $\propto$ 변형률 (탄성 한계 내에서)

이것은 훅 법칙 $F = kx$의 일반화이다!

---

## 12.10 응력-변형률 곡선

<img src="/img/ch12/stress-strain-curve.svg" style="max-height:50vh">

---

### 응력-변형률 곡선의 영역 (1)

**1. 탄성 영역 (Elastic region):**
- 응력-변형률이 **선형** 관계 ($\sigma = E\varepsilon$)
- 힘을 제거하면 원래로 돌아옴
- 기울기 = 영률 $E$

**2. 항복점 (Yield point, $S_y$):**
- 이 응력을 넘으면 **영구 변형** 이 시작된다
- 강철의 경우 $S_y = 250$ MPa

**3. 소성 영역 (Plastic region):**
- 영구 변형 발생, 힘을 제거해도 원래로 돌아가지 않음
- 변형 경화(strain hardening): 변형이 진행될수록 더 큰 응력이 필요

---

### 응력-변형률 곡선의 영역 (2)

**4. 극한 강도 (Ultimate strength, $S_u$):**
- 재료가 버틸 수 있는 **최대 응력**
- 이 점을 지나면 목(neck)이 형성되며 단면적이 급격히 줄어든다

**5. 파단 (Fracture):**
- 재료가 끊어짐
- 취성 재료(유리, 콘크리트)는 소성 영역 없이 바로 파단

---

<!-- sim:stress-strain.html -->
응력-변형률 곡선 시뮬레이션

---

## Review & Summary

### 평형 조건

| 조건 | 수식 |
|---|---|
| 병진 평형 | $\vec{F}_\text{net} = \sum \vec{F} = 0$ |
| 회전 평형 | $\vec{\tau}_\text{net} = \sum \vec{\tau} = 0$ |
| 정적 평형 (추가) | $\vec{v} = 0$, $\vec{\omega} = 0$ |

---

### 탄성

| 개념 | 공식 |
|---|---|
| 영률 (인장/압축) | $\frac{F}{A} = E \frac{\Delta L}{L}$ |
| 전단 탄성률 | $\frac{F}{A} = G \frac{\Delta x}{L}$ |
| 체적 탄성률 | $\Delta p = -B \frac{\Delta V}{V}$ |

**기억할 것:**
- 평형 문제의 핵심은 **자유 물체 다이어그램** 과 **현명한 피벗 선택**
- 돌림힘의 피벗은 어디든 자유롭게 선택할 수 있다
- 무게중심이 지지 기저면 안에 있으면 안정하다
- 응력-변형률 관계는 훅 법칙의 일반화
- 항복 강도 $S_y$ 를 넘으면 영구 변형, 극한 강도 $S_u$ 를 넘으면 파단
