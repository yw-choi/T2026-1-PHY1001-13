---
title: "3장: 벡터"
week: 3
chapters: "3장"
topics: "스칼라와 벡터, 벡터의 덧셈과 뺄셈, 성분 분해, 단위벡터, 스칼라곱, 벡터곱"
---

# 3장: 벡터

Vectors

---

## 이번 장에서 배울 내용

- **스칼라(scalar)** 와 **벡터(vector)** 의 차이
- 벡터의 **덧셈** 과 **뺄셈** — 기하학적 방법
- 벡터의 **성분 분해** — 직교 좌표계
- **단위벡터(unit vector)** 와 성분별 벡터 연산
- **스칼라곱(내적, dot product)** — 일(work) 계산의 핵심
- **벡터곱(외적, cross product)** — 토크, 각운동량의 핵심

---

## 왜 벡터가 필요한가?

자동차 내비게이션이 "서울역에서 37 km 이동하세요"라고만 안내한다면?

**방향** 없이 거리만으로는 목적지에 도달할 수 없다.

물리에서도 마찬가지다:

- **변위(displacement)**: 어디로 얼마나 이동했는가
- **속도(velocity)**: 어느 방향으로 얼마나 빠른가
- **힘(force)**: 어느 방향으로 얼마나 세게 미는가

이 양들은 모두 **크기** 와 **방향** 을 동시에 가진다 → **벡터**

---

## 3.1 벡터와 그 성분

### 스칼라 vs 벡터

| | 스칼라 (scalar) | 벡터 (vector) |
|---|---|---|
| 정의 | 크기만 있는 양 | 크기 + 방향 |
| 예시 | 온도, 질량, 시간, 에너지 | 변위, 속도, 가속도, 힘 |
| 표기 | $m$, $T$, $t$ | $\vec{a}$, $\vec{F}$, $\vec{v}$ |
| 연산 | 보통의 대수 | 벡터 대수 (이 장에서 배움) |

벡터의 크기(magnitude)는 항상 $\geq 0$이며, $|\vec{a}|$ 또는 $a$로 쓴다.

---

### 변위 벡터

**변위(displacement)** 는 가장 직관적인 벡터다.

<img src="/img/ch03/displacement-vector.svg" style="max-height:50vh">

- **거리(distance)**: 실제로 이동한 경로의 총 길이 (스칼라)
- **변위(displacement)**: 출발점에서 도착점으로의 직선 화살표 (벡터)

같은 경로를 걸어도, 변위는 시작점과 끝점만으로 결정된다.

---

### 벡터 덧셈: 머리-꼬리 방법

두 변위 $\vec{a}$와 $\vec{b}$를 연속으로 수행하면?

<img src="/img/ch03/vector-addition.svg" style="max-height:50vh">

**머리-꼬리(head-to-tail) 방법**:
1. $\vec{a}$를 그린다
2. $\vec{a}$의 머리(끝점)에 $\vec{b}$의 꼬리(시작점)를 붙인다
3. $\vec{a}$의 꼬리에서 $\vec{b}$의 머리까지 → 합 벡터 $\vec{s} = \vec{a} + \vec{b}$

---

### 벡터 덧셈의 법칙

**교환법칙** (commutative law):

$$\vec{a} + \vec{b} = \vec{b} + \vec{a}$$

순서를 바꿔도 결과는 같다. 평행사변형 방법으로 확인할 수 있다.

**결합법칙** (associative law):

$$(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$$

세 벡터를 더할 때, 어떤 두 개를 먼저 더해도 결과가 같다.

---

### 벡터 뺄셈

벡터 뺄셈 $\vec{d} = \vec{a} - \vec{b}$는 **음의 벡터** 를 더하는 것이다:

$$\vec{d} = \vec{a} - \vec{b} = \vec{a} + (-\vec{b})$$

<img src="/img/ch03/vector-subtraction.svg" style="max-height:50vh">

$-\vec{b}$는 $\vec{b}$와 크기가 같고 **방향이 반대** 인 벡터다.

---

### 벡터의 성분 분해

벡터를 직교 좌표축을 따라 분해하면 계산이 편리하다.

<img src="/img/ch03/vector-components.svg" style="max-height:50vh">

벡터 $\vec{a}$가 $x$축과 각도 $\theta$를 이루면:

$$a_x = a\cos\theta, \quad a_y = a\sin\theta$$

---

### 성분에서 벡터로 (역변환)

성분 $a_x$, $a_y$를 알면 크기와 방향을 구할 수 있다:

$$a = \sqrt{a_x^2 + a_y^2}$$

$$\tan\theta = \frac{a_y}{a_x}$$

$$\theta = \tan^{-1}\frac{a_y}{a_x}$$

주의: $\tan^{-1}$은 두 개의 해를 줄 수 있다. 벡터가 어느 사분면에 있는지 반드시 확인해야 한다.

---

### 각도 단위: 도와 라디안

물리에서는 **라디안(radian)** 을 기본 단위로 사용한다.

$$\pi \text{ rad} = 180°$$

변환: $\theta_\text{rad} = \theta_\text{deg} \times \frac{\pi}{180}$

| 도(degree) | 라디안(radian) |
|---|---|
| $0°$ | $0$ |
| $30°$ | $\pi/6$ |
| $45°$ | $\pi/4$ |
| $90°$ | $\pi/2$ |
| $180°$ | $\pi$ |
| $360°$ | $2\pi$ |

---

### 예제: 서울에서 수원까지의 변위

서울역에서 수원역까지 직선거리 약 34 km. 방향은 남쪽에서 서쪽으로 $15°$ (남남서).

좌표계: $x$ = 동쪽, $y$ = 북쪽으로 설정하면:

$$\theta = 180° + 75° = 255° \quad (\text{남남서 방향})$$

$$d_x = 34\cos 255° = 34 \times (-0.259) \approx -8.8 \text{ km}$$

$$d_y = 34\sin 255° = 34 \times (-0.966) \approx -32.8 \text{ km}$$

음의 $x$ 성분(서쪽)과 음의 $y$ 성분(남쪽)이므로 남남서가 맞다.

---

## 3.2 단위벡터

### 단위벡터란?

**단위벡터(unit vector)** 는 크기가 1이고 특정 방향을 가리키는 벡터다.

<img src="/img/ch03/unit-vectors.svg" style="max-height:50vh">

직교 좌표계의 단위벡터:
- $\hat{i}$: 양의 $x$ 방향, $|\hat{i}| = 1$
- $\hat{j}$: 양의 $y$ 방향, $|\hat{j}| = 1$
- $\hat{k}$: 양의 $z$ 방향, $|\hat{k}| = 1$

---

### 단위벡터를 이용한 벡터 표현

임의의 벡터 $\vec{a}$를 단위벡터로 표현:

$$\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$$

예: $\vec{a} = 3\hat{i} - 2\hat{j} + 5\hat{k}$이면
- $a_x = 3$, $a_y = -2$, $a_z = 5$
- $a = \sqrt{3^2 + (-2)^2 + 5^2} = \sqrt{38} \approx 6.16$

---

### 성분별 벡터 덧셈

$\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$, $\vec{b} = b_x\hat{i} + b_y\hat{j} + b_z\hat{k}$일 때:

$$\vec{r} = \vec{a} + \vec{b} = (a_x + b_x)\hat{i} + (a_y + b_y)\hat{j} + (a_z + b_z)\hat{k}$$

각 성분끼리 더하면 된다! 기하학적 방법보다 훨씬 간단하다.

뺄셈도 마찬가지:

$$\vec{d} = \vec{a} - \vec{b} = (a_x - b_x)\hat{i} + (a_y - b_y)\hat{j} + (a_z - b_z)\hat{k}$$

---

### 예제: 세 벡터의 성분별 덧셈

$\vec{a} = 4\hat{i} - 3\hat{j}$, $\vec{b} = -2\hat{i} + 5\hat{j}$, $\vec{c} = \hat{i} + 2\hat{j}$일 때 $\vec{r} = \vec{a} + \vec{b} + \vec{c}$를 구하라.

$x$ 성분: $r_x = 4 + (-2) + 1 = 3$

$y$ 성분: $r_y = (-3) + 5 + 2 = 4$

$$\vec{r} = 3\hat{i} + 4\hat{j}$$

크기: $r = \sqrt{3^2 + 4^2} = 5$

방향: $\theta = \tan^{-1}(4/3) = 53.1°$

---

### 좌표계 선택의 자유

좌표축의 방향은 자유롭게 선택할 수 있다.

- 물리 법칙은 좌표계 선택에 의존하지 않는다
- 문제에 맞게 **편리한 방향** 을 선택하면 계산이 간단해진다

예: 빗면 문제 → 빗면을 따라 $x$축, 빗면에 수직으로 $y$축

중요한 것은 한 번 선택한 좌표계를 문제 풀이 내내 **일관되게** 사용하는 것이다.

---

<!-- sim:vector-addition.html -->
벡터 덧셈 시뮬레이션

---

## 3.3 벡터의 곱셈

물리에서 벡터의 곱셈은 **두 가지** 가 있다:

| | 스칼라곱 (내적) | 벡터곱 (외적) |
|---|---|---|
| 기호 | $\vec{a} \cdot \vec{b}$ | $\vec{a} \times \vec{b}$ |
| 결과 | **스칼라** | **벡터** |
| 물리 응용 | 일(work) | 토크(torque) |

각각의 정의와 계산법을 배워보자.

---

### 스칼라곱 (내적, dot product)

두 벡터 $\vec{a}$와 $\vec{b}$ 사이의 각도가 $\phi$일 때:

$$\vec{a} \cdot \vec{b} = ab\cos\phi$$

<img src="/img/ch03/dot-product.svg" style="max-height:50vh">

기하학적 의미: $\vec{b}$를 $\vec{a}$ 방향으로 **사영(projection)** 한 것에 $a$를 곱한 값

---

### 내적의 부호

$\phi$의 범위에 따라 내적의 부호가 결정된다:

- $0 \leq \phi < 90°$: $\cos\phi > 0$ → $\vec{a} \cdot \vec{b} > 0$
- $\phi = 90°$: $\cos\phi = 0$ → $\vec{a} \cdot \vec{b} = 0$ (수직)
- $90° < \phi \leq 180°$: $\cos\phi < 0$ → $\vec{a} \cdot \vec{b} < 0$

**두 벡터가 수직이면 내적이 0이다** — 매우 중요한 성질!

교환법칙 성립: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$

---

### 내적의 성분 형태

$\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$, $\vec{b} = b_x\hat{i} + b_y\hat{j} + b_z\hat{k}$일 때:

단위벡터의 내적:
$\hat{i}\cdot\hat{i} = \hat{j}\cdot\hat{j} = \hat{k}\cdot\hat{k} = 1$,
$\hat{i}\cdot\hat{j} = \hat{j}\cdot\hat{k} = \hat{k}\cdot\hat{i} = 0$

따라서:

$$\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y + a_z b_z$$

각 성분끼리 곱해서 더하면 된다!

---

### 내적 예제

$\vec{a} = 3\hat{i} - 4\hat{j} + 2\hat{k}$, $\vec{b} = 2\hat{i} + 3\hat{j} - \hat{k}$일 때:

$$\vec{a} \cdot \vec{b} = (3)(2) + (-4)(3) + (2)(-1) = 6 - 12 - 2 = -8$$

두 벡터 사이의 각도:

$$a = \sqrt{9 + 16 + 4} = \sqrt{29}, \quad b = \sqrt{4 + 9 + 1} = \sqrt{14}$$

$$\cos\phi = \frac{\vec{a}\cdot\vec{b}}{ab} = \frac{-8}{\sqrt{29}\cdot\sqrt{14}} = \frac{-8}{\sqrt{406}} \approx -0.397$$

$$\phi = \cos^{-1}(-0.397) \approx 113.4°$$

---

### 벡터곱 (외적, cross product)

두 벡터 $\vec{a}$와 $\vec{b}$의 외적 $\vec{c} = \vec{a} \times \vec{b}$:

**크기:**

$$|\vec{a} \times \vec{b}| = ab\sin\phi$$

**방향:** 오른손 법칙으로 결정 — $\vec{a}$와 $\vec{b}$가 이루는 평면에 **수직**

<img src="/img/ch03/cross-product.svg" style="max-height:50vh">

---

### 외적의 성질

**반교환:** $\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})$ (순서를 바꾸면 방향이 반대!)

**평행하면 외적이 0:** $\vec{a} \times \vec{b} = \vec{0}$ ($\phi = 0°$ 또는 $180°$이면 $\sin\phi = 0$)

**수직이면 외적이 최대:** $|\vec{a} \times \vec{b}| = ab$ ($\phi = 90°$이면 $\sin\phi = 1$)

단위벡터의 외적:

$$\hat{i} \times \hat{j} = \hat{k}, \quad \hat{j} \times \hat{k} = \hat{i}, \quad \hat{k} \times \hat{i} = \hat{j}$$

$$\hat{j} \times \hat{i} = -\hat{k}, \quad \hat{k} \times \hat{j} = -\hat{i}, \quad \hat{i} \times \hat{k} = -\hat{j}$$

---

### 외적의 성분 형태

$\vec{a} \times \vec{b}$를 성분으로 전개하면:

$$\vec{a} \times \vec{b} = (a_y b_z - a_z b_y)\hat{i} + (a_z b_x - a_x b_z)\hat{j} + (a_x b_y - a_y b_x)\hat{k}$$

행렬식으로 쓰면 기억하기 쉽다:

$$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}$$

---

### 외적 예제

$\vec{a} = 2\hat{i} + 3\hat{j}$, $\vec{b} = -\hat{i} + 4\hat{j}$일 때 $\vec{a} \times \vec{b}$를 구하라.

$a_z = 0$, $b_z = 0$이므로:

$$\vec{a} \times \vec{b} = (3 \cdot 0 - 0 \cdot 4)\hat{i} + (0 \cdot(-1) - 2 \cdot 0)\hat{j} + (2 \cdot 4 - 3 \cdot(-1))\hat{k}$$

$$= 0\hat{i} + 0\hat{j} + (8 + 3)\hat{k} = 11\hat{k}$$

결과가 $\hat{k}$ 방향 — 두 벡터가 $xy$ 평면에 있으므로, 외적은 $z$ 방향이다.

크기: $|\vec{a} \times \vec{b}| = 11$

---

<!-- sim:dot-cross-product.html -->
내적과 외적 시뮬레이션

---

## Review & Summary

### 핵심 개념

| 개념 | 공식 |
|---|---|
| 벡터의 성분 | $a_x = a\cos\theta$, $a_y = a\sin\theta$ |
| 벡터의 크기 | $a = \sqrt{a_x^2 + a_y^2}$ |
| 벡터의 방향 | $\theta = \tan^{-1}(a_y / a_x)$ |
| 단위벡터 표현 | $\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$ |
| 성분별 덧셈 | $r_x = a_x + b_x$, $r_y = a_y + b_y$, $r_z = a_z + b_z$ |

---

### 핵심 개념 (계속)

| 개념 | 공식 |
|---|---|
| 스칼라곱 (내적) | $\vec{a}\cdot\vec{b} = ab\cos\phi = a_xb_x + a_yb_y + a_zb_z$ |
| 벡터곱 (외적) 크기 | $|\vec{a}\times\vec{b}| = ab\sin\phi$ |
| 벡터곱 (외적) 성분 | $(a_yb_z - a_zb_y)\hat{i} + (a_zb_x - a_xb_z)\hat{j} + (a_xb_y - a_yb_x)\hat{k}$ |

**기억할 것:**
- 벡터의 덧셈은 **성분별로** 계산하는 것이 가장 편리하다
- 내적의 결과는 **스칼라**, 외적의 결과는 **벡터** 이다
- 두 벡터가 **수직** 이면 내적 = 0, **평행** 이면 외적 = 0
- 외적은 **순서가 중요** 하다 ($\vec{a}\times\vec{b} = -\vec{b}\times\vec{a}$)
