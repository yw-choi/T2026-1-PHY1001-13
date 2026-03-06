---
theme: default
title: "Chapter 3: 벡터 (Vectors)"
info: |
  일반물리 I — Chapter 3: 벡터 (Vectors)
  Principles of Physics, 12th Edition
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
math: katex
---

# Chapter 3: 벡터 (Vectors)

일반물리 I · Principles of Physics 12/E

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
transition: fade-out
layout: default
---

# What Is Physics?

<v-clicks>

- 물리학은 **크기(magnitude)** 와 **방향(direction)** 을 모두 갖는 양을 다루는 경우가 많다
- 이를 기술하기 위한 특별한 수학적 언어가 필요 → **벡터(vector)** 의 언어

</v-clicks>

<v-click>

<div class="mt-6 p-4 bg-blue-500 bg-opacity-10 rounded-lg">

벡터는 일상에서도 사용된다: "이 길을 5블록 직진한 뒤 좌회전하라" — 이것이 바로 벡터의 언어이다.

</div>

</v-click>

<v-clicks>

- **항해(navigation)** 는 벡터에 기반
- 물리학과 공학에서는 **회전**, **자기력** 등을 설명하는 데 벡터가 필수
- 이 장에서는 벡터의 **기본 언어**에 집중한다

</v-clicks>

---
layout: section
---

# 3.1 벡터와 그 성분

Vectors and Their Components

---

# 벡터와 스칼라 (Vectors and Scalars)

<div class="grid grid-cols-2 gap-8">
<div>

<v-clicks>

### 스칼라 (Scalar)

- **크기**만 가진 양 (온도, 에너지, 질량, 시간 등)
- 숫자와 단위로 지정 (예: 10°C)
- 일반 산술과 대수 법칙을 따름

### 벡터 (Vector)

- **크기**와 **방향**을 모두 가진 양
- 예: 변위 (5 m, 북쪽), 속도, 가속도
- 벡터 대수 법칙을 따름

</v-clicks>

<v-click>

<div class="mt-4 p-3 bg-yellow-500 bg-opacity-10 rounded-lg text-sm">

가장 단순한 벡터량 = **변위(displacement)**: 위치의 변화

</div>

</v-click>

</div>
<div>

<v-click>

<img src="/img/c0301f001.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.1 — (a) 같은 크기·방향의 화살표는 같은 변위 벡터 (b) 두 점 사이의 경로가 달라도 변위 벡터는 동일</div>

</v-click>

</div>
</div>

---

# 벡터의 기하학적 덧셈 (Adding Vectors Geometrically)

<div class="grid grid-cols-2 gap-8">
<div>

입자가 $A$에서 $B$로, 다시 $B$에서 $C$로 이동하면:

<v-clicks>

- 두 변위 벡터 $\vec{AB}$와 $\vec{BC}$의 합 = **알짜 변위(net displacement)** $\vec{AC}$
- $\vec{AC}$를 **벡터 합(vector sum)** 또는 **합력(resultant)** 이라 부름

### 머리-꼬리 방법 (Head-to-Tail)

1. 벡터 $\vec{a}$를 적당한 축척으로 그림
2. $\vec{b}$의 **꼬리**를 $\vec{a}$의 **머리**에 배치
3. $\vec{a}$의 꼬리에서 $\vec{b}$의 머리까지 = 합 $\vec{s}$

</v-clicks>

<v-click>

$$
\boxed{\vec{s} = \vec{a} + \vec{b}} \tag{3.1.1}
$$

</v-click>

</div>
<div>

<img src="/img/c0301f002.jpg" class="h-48 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.2 — (a) 벡터 합 AC (b) 머리-꼬리 방법으로 재배치</div>

<v-click>

<img src="/img/c0301f003.jpg" class="h-40 rounded-lg mt-2" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.3 — 교환법칙: 벡터 덧셈의 순서를 바꿔도 결과 동일</div>

</v-click>

</div>
</div>

---

# 벡터 덧셈의 법칙

<div class="grid grid-cols-2 gap-8">
<div>

### 교환법칙 (Commutative Law)

$$
\vec{a} + \vec{b} = \vec{b} + \vec{a} \tag{3.1.2}
$$

### 결합법칙 (Associative Law)

$$
(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c}) \tag{3.1.3}
$$

<v-click>

세 개 이상의 벡터도 **어떤 순서로든** 더할 수 있다.

</v-click>

</div>
<div>

<img src="/img/c0301f004.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.4 — 결합법칙: 세 벡터를 어떤 순서로 묶어도 같은 결과</div>

</div>
</div>

---

# 벡터 뺄셈 (Vector Subtraction)

<div class="grid grid-cols-2 gap-8">
<div>

### 음의 벡터

$-\vec{b}$는 $\vec{b}$와 **같은 크기**, **반대 방향**:

$$
\vec{b} + (-\vec{b}) = 0
$$

<v-click>

### 벡터 뺄셈

$$
\boxed{\vec{d} = \vec{a} - \vec{b} = \vec{a} + (-\vec{b})} \tag{3.1.4}
$$

$\vec{a}$에서 $\vec{b}$를 빼려면 → $-\vec{b}$를 $\vec{a}$에 더한다!

</v-click>

<v-click>

<div class="mt-4 p-3 bg-green-500 bg-opacity-10 rounded-lg text-sm">

**Checkpoint 3.1.1**: $|\vec{a}| = 3$ m, $|\vec{b}| = 4$ m, $\vec{c} = \vec{a} + \vec{b}$일 때, $|\vec{c}|$의 최댓값은? → **7 m** (같은 방향). 최솟값은? → **1 m** (반대 방향).

</div>

</v-click>

</div>
<div>

<img src="/img/c0301f005.jpg" class="h-36 mx-auto rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.5 — b와 −b: 같은 크기, 반대 방향</div>

<v-click>

<img src="/img/c0301f006.jpg" class="max-h-52 rounded-lg mt-2" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.6 — (a) a, b, −b (b) d = a − b를 머리-꼬리로 구함</div>

</v-click>

</div>
</div>

---

# 벡터의 성분 (Components of Vectors)

<div class="grid grid-cols-2 gap-8">
<div>

벡터를 **직교 좌표축**에 분해하면 대수적 계산이 가능:

<v-clicks>

### 성분 정의

$\vec{a}$가 $x$축 양의 방향과 각도 $\theta$를 이룰 때:

$$
\boxed{a_x = a\cos\theta \quad \text{and} \quad a_y = a\sin\theta} \tag{3.1.5}
$$

- $a_x$: **$x$ 성분** (수평 사영)
- $a_y$: **$y$ 성분** (수직 사영)
- 벡터의 **분해(resolving)**: 축 위로 수선을 내림

</v-clicks>

<v-click>

### 성분 → 크기·방향

$$
\boxed{a = \sqrt{a_x^2 + a_y^2} \quad \text{and} \quad \tan\theta = \frac{a_y}{a_x}} \tag{3.1.6}
$$

</v-click>

</div>
<div>

<img src="/img/c0301f007.jpg" class="h-44 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.7 — (a)(b) 벡터 a의 x, y 성분. (c) 성분과 벡터가 직각삼각형을 이룸</div>

<v-click>

<img src="/img/c0301f008.jpg" class="h-36 rounded-lg mt-2" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.8 — 성분의 부호: x성분은 양, y성분은 음</div>

</v-click>

</div>
</div>

---

# 삼각함수 복습 (Trig Functions Review)

<div class="grid grid-cols-2 gap-8">
<div>

### 기본 삼각함수

$$
\begin{aligned}
\sin\theta &= \frac{\text{대변}}{\text{빗변}}, \quad \cos\theta = \frac{\text{인접변}}{\text{빗변}} \\[4pt]
\tan\theta &= \frac{\text{대변}}{\text{인접변}}
\end{aligned}
$$

<v-click>

### 각도와 라디안

$$
\theta_\text{rad} = \theta_\text{deg} \times \frac{2\pi}{360°}
$$

예: $40° = 40° \times \frac{2\pi}{360°} = 0.70$ rad

</v-click>

<v-click>

### 역삼각함수 주의사항

- 계산기의 $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$에는 **작동 범위**가 있음
- 항상 결과가 **합리적인지 확인** — 사분면을 고려!

</v-click>

</div>
<div>

<img src="/img/c0301f010.jpg" class="w-64 mx-auto rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.10 — 삼각함수 정의에 사용되는 직각삼각형</div>

<v-click>

<img src="/img/c0301f011.jpg" class="max-h-48 rounded-lg mt-2" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.11 — sin, cos, tan 함수의 그래프와 역함수의 범위(진한 부분)</div>

</v-click>

</div>
</div>

---

# 예제: 동굴 탐험 (Sample Problem 3.1.1)

<div class="text-sm">

동굴 탐험팀이 서쪽 2.6 km, 남쪽 3.9 km, 위로 25 m 이동. 알짜 변위의 크기와 방향은?

</div>

<div class="grid grid-cols-2 gap-6">
<div>

<v-clicks>

**수평 변위:**

$$d_h = \sqrt{(2.6)^2 + (3.9)^2} = 4.69 \text{ km}$$

**수평 방향:** (서쪽에서 남쪽으로의 각도)

$$\theta_h = \tan^{-1}\frac{3.9}{2.6} = 56°$$

서쪽 기준 남쪽으로 56° 방향

**전체 변위:**

$$d = \sqrt{(4.69)^2 + (0.025)^2} \approx 4.7 \text{ km}$$

수평 대비 수직 각도:

$$\theta_v = \tan^{-1}\frac{0.025}{4.69} = 0.3°$$

</v-clicks>

</div>
<div>

<img src="/img/c0301f009a.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.1.9 — Mammoth-Flint Ridge 동굴 탐험 경로와 변위 벡터</div>

</div>
</div>

---
layout: section
---

# 3.2 단위벡터, 성분을 이용한 벡터 덧셈

Unit Vectors, Adding Vectors by Components

---

# 단위벡터 (Unit Vectors)

<div class="grid grid-cols-2 gap-8">
<div>

**단위벡터**: 크기가 정확히 1이고 특정 방향을 가리키는 벡터

<v-clicks>

### $\hat{\imath}$, $\hat{\jmath}$, $\hat{k}$ 단위벡터

- $\hat{\imath}$: $x$축 양의 방향
- $\hat{\jmath}$: $y$축 양의 방향
- $\hat{k}$: $z$축 양의 방향
- **오른손 좌표계(right-handed coordinate system)** 를 사용

</v-clicks>

<v-click>

### 벡터를 단위벡터로 표현

$$
\boxed{\vec{a} = a_x\hat{\imath} + a_y\hat{\jmath}} \tag{3.2.1}
$$

$$
\vec{b} = b_x\hat{\imath} + b_y\hat{\jmath} \tag{3.2.2}
$$

$a_x\hat{\imath}$, $a_y\hat{\jmath}$: **벡터 성분**, $a_x$, $a_y$: **스칼라 성분**

</v-click>

</div>
<div>

<img src="/img/c0302f001.jpg" class="h-48 mx-auto rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.2.1 — i, j, k 단위벡터와 오른손 좌표계</div>

<v-click>

<img src="/img/c0302f002.jpg" class="max-h-48 rounded-lg mt-2" />

<div class="text-xs text-gray-400 mt-1">Fig 3.2.2 — (a) 벡터 a의 성분 (b) 벡터 b의 성분</div>

</v-click>

</div>
</div>

---

# 성분을 이용한 벡터 덧셈 (Adding Vectors by Components)

<div class="grid grid-cols-2 gap-8">
<div>

$\vec{r} = \vec{a} + \vec{b}$일 때, 각 성분별로 더한다:

$$
\boxed{r_x = a_x + b_x} \tag{3.2.4}
$$

$$
\boxed{r_y = a_y + b_y} \tag{3.2.5}
$$

$$
\boxed{r_z = a_z + b_z} \tag{3.2.6}
$$

<v-click>

<div class="mt-2 p-3 bg-yellow-500 bg-opacity-10 rounded-lg text-sm">

**핵심**: 벡터 연산 = **축별(axis by axis)** 스칼라 연산!

뺄셈도 동일: $d_x = a_x - b_x$, $d_y = a_y - b_y$, $d_z = a_z - b_z$

</div>

</v-click>

</div>
<div>

<v-click>

### Checkpoint 3.2.1

<img src="/img/c0302f004.jpg" class="max-h-72 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.2.4 — 세 벡터의 성분별 합</div>

</v-click>

</div>
</div>

---

# 벡터와 물리 법칙 (Vectors and the Laws of Physics)

<div class="grid grid-cols-2 gap-8">
<div>

좌표축을 **회전**하면 벡터의 성분은 바뀌지만, 벡터 자체는 바뀌지 않는다.

<v-clicks>

- 좌표축을 각도 $\phi$만큼 회전하면 성분이 $a_x', a_y'$으로 변환
- 하지만 **크기**는 동일:

$$
a = \sqrt{a_x^2 + a_y^2} = \sqrt{a_x'^2 + a_y'^2} \tag{3.2.8}
$$

- **방향**: $\theta = \theta' + \phi$ $\tag{3.2.9}$

</v-clicks>

<v-click>

<div class="mt-4 p-3 bg-blue-500 bg-opacity-10 rounded-lg text-sm">

물리 법칙은 좌표계 선택에 **무관**하다. 벡터 언어로 표현된 물리 방정식 하나가 성분별로 여러 관계식을 대표한다.

</div>

</v-click>

</div>
<div>

<img src="/img/c0302f003.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.2.3 — (a) 벡터 a와 성분 (b) 좌표축을 회전하면 성분은 바뀌지만 벡터는 동일</div>

</div>
</div>

---

# 예제: 단위벡터 성분 덧셈 (Sample Problem 3.2.1)

<div class="text-sm">

$\vec{a} = (4.2\text{ m})\hat{\imath} - (1.5\text{ m})\hat{\jmath}$, $\vec{b} = (-1.6\text{ m})\hat{\imath} + (2.9\text{ m})\hat{\jmath}$, $\vec{c} = (-3.7\text{ m})\hat{\jmath}$일 때, 벡터 합 $\vec{r}$은?

</div>

<div class="grid grid-cols-2 gap-6">
<div>

<v-clicks>

**$x$ 성분:**

$$r_x = 4.2 + (-1.6) + 0 = 2.6 \text{ m}$$

**$y$ 성분:**

$$r_y = -1.5 + 2.9 + (-3.7) = -2.3 \text{ m}$$

**단위벡터 표기:**

$$\vec{r} = (2.6\text{ m})\hat{\imath} - (2.3\text{ m})\hat{\jmath}$$

</v-clicks>

<v-click>

**크기와 각도:**

$$r = \sqrt{(2.6)^2 + (-2.3)^2} \approx 3.5 \text{ m}$$

$$\theta = \tan^{-1}\!\left(\frac{-2.3}{2.6}\right) = -41°$$

(시계 방향 = $+x$축 아래 41°)

</v-click>

</div>
<div>

<img src="/img/c0302f004.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.2.4 — 세 벡터의 성분별 합산 과정</div>

</div>
</div>

---

# 예제: 사막 개미 (Sample Problem 3.2.2)

<div class="text-xs">

사막 개미가 6.0 cm씩 5번 이동 (방향: 0°, 150°, 180°, −120°, 90°). 알짜 변위의 크기와 각도는?

</div>

<div class="grid grid-cols-2 gap-6 text-sm">
<div>

<v-click>

| Run | $d_x$ (cm) | $d_y$ (cm) |
|---|---|---|
| 1 | +6.0 | 0 |
| 2 | −5.2 | +3.0 |
| 3 | −6.0 | 0 |
| 4 | −3.0 | −5.2 |
| 5 | 0 | +6.0 |
| **합** | **−8.2** | **+3.8** |

</v-click>

<v-click>

$$d_\text{net} = \sqrt{(-8.2)^2 + (3.8)^2} = 9.0 \text{ cm at } 155°$$

</v-click>

</div>
<div>

<v-click>

<div class="p-3 bg-green-500 bg-opacity-10 rounded-lg">

**귀환 벡터**: 알짜 변위와 **같은 크기, 반대 방향**

$$d_\text{home} = 9.0 \text{ cm}, \quad \theta = -25°$$

사막 개미는 수천 번의 이동을 머릿속 좌표계로 합산하여 집을 찾아간다!

</div>

</v-click>

</div>
</div>

---
layout: section
---

# 3.3 벡터의 곱셈

Multiplying Vectors

---

# 벡터에 스칼라 곱하기 (Multiplying a Vector by a Scalar)

벡터 $\vec{v}$에 스칼라 $s$를 곱하면:

<v-clicks>

- **크기**: $|s| \cdot |\vec{v}|$
- **방향**: $s > 0$이면 $\vec{v}$와 같은 방향, $s < 0$이면 반대 방향
- $\vec{v}$를 $s$로 나누려면 $\vec{v}$에 $1/s$를 곱하면 됨

</v-clicks>

<v-click>

<div class="mt-6 p-4 bg-blue-500 bg-opacity-10 rounded-lg">

벡터의 곱셈에는 두 가지 종류가 있다:

| | **스칼라곱 (dot product)** | **벡터곱 (cross product)** |
|---|---|---|
| 표기 | $\vec{a} \cdot \vec{b}$ | $\vec{a} \times \vec{b}$ |
| 결과 | **스칼라** | **벡터** |
| 교환법칙 | $\vec{a}\cdot\vec{b} = \vec{b}\cdot\vec{a}$ ✓ | $\vec{a}\times\vec{b} = -(\vec{b}\times\vec{a})$ ✗ |

</div>

</v-click>

---

# 스칼라곱 (The Scalar / Dot Product)

<div class="grid grid-cols-2 gap-8">
<div>

### 크기-각도 표기

$$
\boxed{\vec{a} \cdot \vec{b} = ab\cos\phi} \tag{3.3.1}
$$

$\phi$: 두 벡터 사이의 각도

<v-clicks>

- 결과는 **스칼라** (부호 있음)
- $\phi = 0°$ → $\vec{a}\cdot\vec{b} = ab$ (최대)
- $\phi = 90°$ → $\vec{a}\cdot\vec{b} = 0$ (직교)
- $\phi = 180°$ → $\vec{a}\cdot\vec{b} = -ab$

</v-clicks>

<v-click>

### 단위벡터 표기

$$
\boxed{\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y + a_z b_z} \tag{3.3.4}
$$

</v-click>

<v-click>

**물리적 의미**: 한 벡터의 크기 $\times$ 다른 벡터 방향의 성분

</v-click>

</div>
<div>

<img src="/img/c0303f001.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.3.1 — (a) 각도 φ인 두 벡터 (b) 각 벡터는 상대 벡터 방향의 성분을 가짐</div>

</div>
</div>

---

# 예제: 스칼라곱으로 각도 구하기 (Sample Problem 3.3.1)

<div class="text-sm">

$\vec{a} = 3.0\hat{\imath} - 4.0\hat{\jmath}$, $\vec{b} = -2.0\hat{\imath} + 3.0\hat{k}$ 사이의 각도 $\phi$는?

</div>

<div class="grid grid-cols-2 gap-6">
<div>

<v-clicks>

**크기 계산:**

$$a = \sqrt{3.0^2 + (-4.0)^2} = 5.00$$

$$b = \sqrt{(-2.0)^2 + 3.0^2} = 3.61$$

**단위벡터 표기로 스칼라곱:**

$$\vec{a}\cdot\vec{b} = (3.0)(-2.0) + (-4.0)(0) + (0)(3.0) = -6.0$$

</v-clicks>

<v-click>

**Eq. 3.3.1 적용:**

$$-6.0 = (5.00)(3.61)\cos\phi$$

$$\phi = \cos^{-1}\!\left(\frac{-6.0}{18.05}\right) \approx 109° \approx 110°$$

</v-click>

</div>
<div>

<v-click>

<div class="p-4 bg-green-500 bg-opacity-10 rounded-lg">

### Checkpoint 3.3.1

$|\vec{C}| = 3$, $|\vec{D}| = 4$이고 $\vec{C}\cdot\vec{D}$가 다음일 때 사이각은?

| $\vec{C}\cdot\vec{D}$ | 각도 |
|---|---|
| 0 | **90°** |
| 12 | **0°** (같은 방향) |
| −12 | **180°** (반대 방향) |

</div>

</v-click>

</div>
</div>

---

# 벡터곱 (The Vector / Cross Product)

<div class="grid grid-cols-2 gap-8">
<div>

### 크기-각도 표기

$$
\boxed{|\vec{a} \times \vec{b}| = ab\sin\phi} \tag{3.3.5}
$$

<v-clicks>

- 결과는 **벡터** $\vec{c}$
- $\vec{c}$의 방향: $\vec{a}$와 $\vec{b}$ 평면에 **수직**
- **오른손 법칙**으로 방향 결정:
  1. $\vec{a}$에서 $\vec{b}$로 손가락을 감아쥠
  2. 엄지가 가리키는 방향 = $\vec{c}$ 방향

</v-clicks>

<v-click>

### 교환법칙 성립 안 됨!

$$
\vec{b} \times \vec{a} = -(\vec{a} \times \vec{b}) \tag{3.3.6}
$$

순서가 바뀌면 방향이 **반대**!

</v-click>

</div>
<div>

<img src="/img/c0303f002.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.3.2 — 오른손 법칙: (a) c = a × b (b) b × a = −c</div>

</div>
</div>

---

# 벡터곱: 단위벡터 표기

<div class="grid grid-cols-2 gap-8">
<div>

### 단위벡터 곱셈 규칙

$$
\hat{\imath} \times \hat{\jmath} = \hat{k}, \quad \hat{\jmath} \times \hat{k} = \hat{\imath}, \quad \hat{k} \times \hat{\imath} = \hat{\jmath}
$$

$$
\hat{\jmath} \times \hat{\imath} = -\hat{k}, \quad \hat{k} \times \hat{\jmath} = -\hat{\imath}, \quad \hat{\imath} \times \hat{k} = -\hat{\jmath}
$$

<v-click>

### 전개 공식

$$
\begin{aligned}
\vec{a} \times \vec{b} = \;&(a_y b_z - a_z b_y)\hat{\imath} \\
+\;&(a_z b_x - a_x b_z)\hat{\jmath} \\
+\;&(a_x b_y - a_y b_x)\hat{k}
\end{aligned}
\tag{3.3.8}
$$

</v-click>

<v-click>

<div class="mt-4 p-3 bg-yellow-500 bg-opacity-10 rounded-lg text-sm">

**평행** ($\phi = 0°, 180°$) → $\vec{a}\times\vec{b} = 0$

**수직** ($\phi = 90°$) → $|\vec{a}\times\vec{b}| = ab$ (최대)

</div>

</v-click>

</div>
<div>

<v-click>

### 예제: 벡터곱 (Sample Problem 3.3.3)

$\vec{a} = 3\hat{\imath} - 4\hat{\jmath}$, $\vec{b} = -2\hat{\imath} + 3\hat{k}$일 때 $\vec{c} = \vec{a}\times\vec{b}$?

$$\vec{c} = (3\hat{\imath} - 4\hat{\jmath}) \times (-2\hat{\imath} + 3\hat{k})$$

항별 전개:

$$= 3\hat{\imath}\times(-2\hat{\imath}) + 3\hat{\imath}\times 3\hat{k}$$
$$+ (-4\hat{\jmath})\times(-2\hat{\imath}) + (-4\hat{\jmath})\times 3\hat{k}$$

$$= 0 + 9(\hat{\imath}\times\hat{k}) + 8(\hat{\jmath}\times\hat{\imath}) + (-12)(\hat{\jmath}\times\hat{k})$$

$$= 9(-\hat{\jmath}) + 8(-\hat{k}) + (-12)\hat{\imath}$$

$$\boxed{\vec{c} = -12\hat{\imath} - 9\hat{\jmath} - 8\hat{k}}$$

</v-click>

</div>
</div>

---

# 예제: 벡터곱과 오른손 법칙 (Sample Problem 3.3.2)

<div class="grid grid-cols-2 gap-6">
<div>

$\vec{a}$는 $xy$ 평면에서 크기 18, 방향 250° ($+x$축 기준).
$\vec{b}$는 $+z$ 방향, 크기 12.

$\vec{c} = \vec{a} \times \vec{b}$의 크기와 방향은?

<v-clicks>

**크기:**

$\vec{a}$와 $\vec{b}$는 수직이므로 ($\phi = 90°$):

$$c = ab\sin 90° = (18)(12)(1) = 216$$

**방향:**

오른손 법칙: $\vec{a}$에서 $\vec{b}$로 감으면 →

$\vec{c}$는 $xy$ 평면에 놓이며, $+x$축에서 $250° - 90° = 160°$ 방향

</v-clicks>

</div>
<div>

<img src="/img/c0303f003.jpg" class="max-h-80 rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 3.3.3 — c = a × b: xy 평면에 놓이며, a와 b 모두에 수직</div>

</div>
</div>

---

# Review & Summary

<div class="grid grid-cols-2 gap-4 text-sm">
<div>

### 벡터와 스칼라
- **스칼라**: 크기만 (온도, 질량) / **벡터**: 크기 + 방향 (변위, 속도)

### 기하학적 덧셈
- 머리-꼬리 방법, 교환법칙·결합법칙 성립
- 뺄셈: $\vec{d} = \vec{a} + (-\vec{b})$

### 성분
- $a_x = a\cos\theta$, $a_y = a\sin\theta$
- $a = \sqrt{a_x^2 + a_y^2}$, $\tan\theta = a_y / a_x$

### 단위벡터
- $\hat{\imath}$, $\hat{\jmath}$, $\hat{k}$: 각 축 방향, 크기 1
- $\vec{a} = a_x\hat{\imath} + a_y\hat{\jmath} + a_z\hat{k}$

</div>
<div>

### 성분별 덧셈
- $r_x = a_x + b_x$, $r_y = a_y + b_y$, $r_z = a_z + b_z$

### 스칼라곱 (Dot Product)
$$\vec{a}\cdot\vec{b} = ab\cos\phi = a_x b_x + a_y b_y + a_z b_z$$

- 결과: 스칼라, 교환법칙 성립

### 벡터곱 (Cross Product)
$$|\vec{a}\times\vec{b}| = ab\sin\phi$$

$$\vec{a}\times\vec{b} = (a_y b_z\!-\!a_z b_y)\hat{\imath} + (a_z b_x\!-\!a_x b_z)\hat{\jmath} + (a_x b_y\!-\!a_y b_x)\hat{k}$$

- 결과: 벡터, 오른손 법칙으로 방향 결정
- 교환법칙 **불성립**: $\vec{b}\times\vec{a} = -(\vec{a}\times\vec{b})$

</div>
</div>

---

# 연습 문제

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

### 문제 1: 성분과 크기

$\vec{a} = (4.0\text{ m})\hat{\imath} - (3.0\text{ m})\hat{\jmath}$이고 $\vec{b} = (6.0\text{ m})\hat{\imath} + (10.0\text{ m})\hat{\jmath}$일 때, $\vec{a} + \vec{b}$의 크기와 $+x$축과의 각도는?

<v-click>

**풀이:**

$$\vec{r} = (10.0)\hat{\imath} + (7.0)\hat{\jmath}$$

$$r = \sqrt{10.0^2 + 7.0^2} = 12.2 \text{ m}$$

$$\theta = \tan^{-1}(7.0/10.0) = 35.0°$$

</v-click>

</div>
<div>

### 문제 2: 스칼라곱

$\vec{a} = 3.0\hat{\imath} + 3.0\hat{\jmath} + 3.0\hat{k}$, $\vec{b} = 2.0\hat{\imath} + 1.0\hat{\jmath} + 5.0\hat{k}$일 때 두 벡터 사이의 각도는?

<v-click>

**풀이:**

$$\vec{a}\cdot\vec{b} = 6.0 + 3.0 + 15.0 = 24.0$$

$$a = \sqrt{27} = 5.20, \quad b = \sqrt{30} = 5.48$$

$$\phi = \cos^{-1}\!\left(\frac{24.0}{5.20 \times 5.48}\right) = \cos^{-1}(0.842) \approx 32.6°$$

</v-click>

</div>
</div>

---
layout: center
class: text-center
---

# 감사합니다

Chapter 3: 벡터 (Vectors) 끝

<div class="mt-8 text-gray-400">

다음: Chapter 4 — 2차원·3차원 운동 (Motion in Two and Three Dimensions)

</div>
