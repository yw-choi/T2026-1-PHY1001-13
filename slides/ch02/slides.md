---
theme: default
background: /cover.jpg
title: "Chapter 2: 직선 운동 (Motion Along a Straight Line)"
info: |
  일반물리 I — Chapter 2: 직선 운동 (Motion Along a Straight Line)
  Principles of Physics, 12th Edition
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
math: katex
---

# Chapter 2: 직선 운동 (Motion Along a Straight Line)

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

- 물리학의 핵심 주제 중 하나: **물체의 운동(motion)** 연구
- 물체가 얼마나 빠르게, 얼마나 멀리 이동하는가?

</v-clicks>

<v-click>

<div class="mt-6 p-4 bg-blue-500 bg-opacity-10 rounded-lg">

이 장에서는 물체가 **하나의 축(single axis)** 을 따라 움직이는 **1차원 운동(one-dimensional motion)** 을 다룬다.

</div>

</v-click>

<v-clicks>

- 운동은 **직선** 위에서만 일어남 (수직, 수평, 또는 기울어진 직선)
- **힘(force)** 은 아직 다루지 않음 (→ Chapter 5) — 운동 자체와 변화에 집중
- 물체를 **입자(particle)** 로 취급: 점 입자이거나, 모든 부분이 같은 방향·같은 속도로 움직이는 물체

</v-clicks>

---
layout: section
---

# 2.1 위치, 변위, 평균속도

Position, Displacement, and Average Velocity

---

# 위치와 변위 (Position and Displacement)

<div class="grid grid-cols-2 gap-8">
<div>

### 위치 (Position)

<v-clicks>

- **기준점(origin)** 에 대한 물체의 위치를 $x$ 축 위의 좌표로 나타냄
- **양의 방향**: 좌표가 증가하는 방향
- **음의 방향**: 그 반대 방향

</v-clicks>

<v-click>

### 변위 (Displacement)

위치 $x_1$에서 $x_2$로의 **변화량**:

$$
\boxed{\Delta x = x_2 - x_1}
$$

</v-click>

<v-clicks>

- $\Delta x > 0$: 양의 방향 이동
- $\Delta x < 0$: 음의 방향 이동
- 변위는 **벡터량(vector quantity)** — 크기와 방향을 가짐

</v-clicks>

</div>
<div>

<img src="/img/c0201f001_high_resolution.jpg" class="w-full rounded-lg mt-4" />

<div class="text-xs text-gray-400 mt-1">Fig 2.1.1 — 위치 축과 원점</div>

<v-click>

<img src="/img/c0201f003_high_resolution.jpg" class="w-full rounded-lg mt-4" />

<div class="text-xs text-gray-400 mt-1">Fig 2.1.3 — 움직이는 아르마딜로의 x(t) 그래프</div>

</v-click>

</div>
</div>

---

# 평균속도 (Average Velocity)

<div class="grid grid-cols-2 gap-8">
<div>

위치를 시간 $t$의 함수 $x(t)$로 나타낼 때, 시간 간격 $\Delta t$ 동안의 **평균속도**:

$$
\boxed{v_\text{avg} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}}
$$

<v-clicks>

- 단위: m/s (길이/시간)
- **벡터량**: 부호가 이동 방향을 나타냄
- $x$-$t$ 그래프에서 **두 점을 잇는 직선의 기울기**

</v-clicks>

<v-click>

<div class="mt-4 p-3 bg-yellow-500 bg-opacity-10 rounded-lg text-sm">

**주의**: 평균속도는 실제 이동 경로가 아닌, **처음과 끝 위치**에만 의존한다!

</div>

</v-click>

</div>
<div>

<img src="/img/c0201f004_high_resolution.jpg" class="w-full rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.1.4 — x-t 그래프에서 평균속도는 두 점을 잇는 직선의 기울기</div>

</div>
</div>

---

# 평균속력 (Average Speed)

<div class="grid grid-cols-2 gap-8">
<div>

평균속력은 **총 이동 거리**를 시간 간격으로 나눈 값:

$$
\boxed{s_\text{avg} = \frac{\text{총 거리 (total distance)}}{\Delta t}}
$$

<v-clicks>

- **스칼라량**: 방향 없음, 항상 양수
- 평균속도 ≠ 평균속력 (일반적으로)

</v-clicks>

<v-click>

### 예시

$x = 5$ m → $x = 200$ m → $x = 5$ m로 이동:

- **변위**: $\Delta x = 0$ → $v_\text{avg} = 0$
- **총 거리**: $195 + 195 = 390$ m → $s_\text{avg} > 0$

</v-click>

</div>
<div>

<v-click>

<div class="p-4 bg-green-500 bg-opacity-10 rounded-lg">

### 비교 정리

| | 평균속도 $v_\text{avg}$ | 평균속력 $s_\text{avg}$ |
|---|---|---|
| 정의 | $\Delta x / \Delta t$ | 총 거리 / $\Delta t$ |
| 종류 | 벡터 | 스칼라 |
| 부호 | +, −, 0 | 항상 ≥ 0 |
| 의존 | 처음·끝 위치 | 전체 경로 |

</div>

</v-click>

</div>
</div>

---

# 예제: 평균속도 (Sample Problem 2.1.1)

<div class="text-sm">

자동차로 동쪽 10.0 km를 40.0 km/h로 이동 후, 같은 방향으로 3.00 km를 0.500 h 동안 조깅.

</div>

<div class="grid grid-cols-2 gap-6">
<div>

<v-clicks>

**(a) 전체 변위:** $\Delta x = 10.0 + 3.00 = 13.0$ km

**(b) 전체 시간:** $\Delta t_\text{car} = 10.0/40.0 = 0.250$ h → $\Delta t = 0.250 + 0.500 = 0.750$ h

**(c) 평균속도:** $v_\text{avg} = 13.0 / 0.750 = 17.3$ km/h

**(d) 돌아올 때 평균속력:**

총 거리 $= 10.0 + 3.00 + 3.00 = 16.0$ km, 총 시간 $= 1.25$ h

$$s_\text{avg} = 16.0 / 1.25 = 12.8 \text{ km/h}$$

</v-clicks>

</div>
<div>

<img src="/img/c0201f005_high_resolution.jpg" class="w-full rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.1.5 — x-t 그래프에서 기울기가 평균속도</div>

</div>
</div>

---

# Checkpoint 2.1.1

다음 세 쌍의 초기·최종 위치 중, **음의 변위**를 주는 것은?

<div class="grid grid-cols-3 gap-6 mt-8">
<div class="p-4 bg-gray-500 bg-opacity-10 rounded-lg text-center">

### (a)

$x_1 = -3$ m, $x_2 = +5$ m

<v-click>

$\Delta x = 5 - (-3) = +8$ m

**양의 변위**

</v-click>

</div>
<div class="p-4 bg-gray-500 bg-opacity-10 rounded-lg text-center">

### (b)

$x_1 = -3$ m, $x_2 = -7$ m

<v-click>

$\Delta x = -7 - (-3) = -4$ m

**음의 변위** ✓

</v-click>

</div>
<div class="p-4 bg-gray-500 bg-opacity-10 rounded-lg text-center">

### (c)

$x_1 = 7$ m, $x_2 = -3$ m

<v-click>

$\Delta x = -3 - 7 = -10$ m

**음의 변위** ✓

</v-click>

</div>
</div>

---
layout: section
---

# 2.2 순간속도와 속력

Instantaneous Velocity and Speed

---

# 순간속도 (Instantaneous Velocity)

<div class="grid grid-cols-2 gap-8">
<div>

$\Delta t$를 점점 줄여가면 평균속도가 **한 순간의 속도**에 수렴:

$$
\boxed{v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}}
$$

<v-clicks>

- $v$는 $x(t)$의 **시간에 대한 도함수(미분)**
- $x$-$t$ 그래프에서 **접선(tangent)의 기울기**
- 벡터량: 부호가 이동 방향을 나타냄

</v-clicks>

<v-click>

### 속력 (Speed)

$$
\text{speed} = |v|
$$

- 속도의 **크기(magnitude)**
- 방향 정보 없음 (스칼라)
- 자동차 속도계(speedometer)는 속력을 측정

</v-click>

</div>
<div>

<v-click>

### Checkpoint 2.2.1

$x(t)$가 다음과 같을 때 ($x$: m, $t$: s, $t > 0$):

| | $x(t)$ | $v(t)$ |
|---|---|---|
| (1) | $3t - 2$ | $3$ |
| (2) | $-4t^2 - 2$ | $-8t$ |
| (3) | $2/t^2$ | $-4/t^3$ |
| (4) | $-2$ | $0$ |

**(a)** $v$가 일정한 것? → **(1)**, **(4)**

**(b)** $v$가 음의 $x$ 방향인 것? → **(2)**, **(3)**

</v-click>

</div>
</div>

---

# 예제: 엘리베이터 캡 (Sample Problem 2.2.1)

<div class="grid grid-cols-2 gap-6">
<div>

엘리베이터가 정지 → 위로 이동 → 정지하는 과정의 $x(t)$, $v(t)$, $a(t)$ 그래프:

<v-clicks>

- **0~1 s, 8~9 s**: 기울기 = 0 → $v = 0$ (정지)
- **1~3 s**: 기울기 증가 → $v$ 증가 (가속)
- **3~8 s**: 기울기 일정 → $v = 4.0$ m/s (등속)

$$
v = \frac{24 \text{ m} - 4.0 \text{ m}}{8.0 \text{ s} - 3.0 \text{ s}} = +4.0 \text{ m/s}
$$

- **8~9 s**: 기울기 감소 → $v$ 감소 (감속)

</v-clicks>

<v-click>

<div class="mt-2 p-3 bg-blue-500 bg-opacity-10 rounded-lg text-sm">

**핵심**: $x(t)$ 그래프의 기울기 → $v(t)$ 값, $v(t)$ 그래프의 기울기 → $a(t)$ 값

</div>

</v-click>

</div>
<div>

<img src="/img/c0202f001_high_resolution.jpg" class="max-h-[420px] object-contain rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.2.1 — x(t), v(t), a(t) 그래프 간의 관계</div>

</div>
</div>

---
layout: section
---

# 2.3 가속도

Acceleration

---

# 가속도 (Acceleration)

<div class="grid grid-cols-2 gap-8">
<div>

### 평균 가속도 (Average Acceleration)

$$
\boxed{a_\text{avg} = \frac{\Delta v}{\Delta t} = \frac{v_2 - v_1}{t_2 - t_1}}
$$

### 순간 가속도 (Instantaneous Acceleration)

$$
\boxed{a = \frac{dv}{dt} = \frac{d^2 x}{dt^2}}
$$

<v-clicks>

- $v$-$t$ 그래프에서 **접선의 기울기**
- 단위: m/s² (또는 m/(s·s))
- **벡터량**: 부호가 방향을 나타냄

</v-clicks>

</div>
<div>

<v-click>

### $g$ 단위

큰 가속도를 표현할 때 자주 사용:

$$
1g = 9.8 \text{ m/s}^2
$$

- 롤러코스터: 약 $3g$까지 경험
- 전투기 조종사: 약 $7\text{--}9g$

</v-click>

<v-click>

### 가속도 부호의 의미

<div class="p-3 bg-yellow-500 bg-opacity-10 rounded-lg">

$v$와 $a$의 부호가 **같으면** → 속력 증가

$v$와 $a$의 부호가 **다르면** → 속력 감소

</div>

양의 가속도 ≠ "빨라진다" (음의 방향 감속도 양의 가속도!)

</v-click>

</div>
</div>

---

# 가속도의 부호와 운동 방향

<div class="grid grid-cols-2 gap-6">
<div>

<img src="/img/c0203f002_high_resolution.jpg" class="w-full rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.3.2 — 입자 운동의 4단계</div>

</div>
<div>

<v-clicks>

| 단계 | $v$ | $a$ | 속력 | 설명 |
|---|---|---|---|---|
| (a) | − | 0 | 일정 | 왼쪽 등속 |
| (b) | − | + | 감소 | 감속 중 |
| (c) | 0 | + | — | 순간 정지 |
| (d) | + | + | 증가 | 오른쪽 가속 |

</v-clicks>

<v-click>

<div class="mt-4 p-3 bg-green-500 bg-opacity-10 rounded-lg">

**Checkpoint 2.3.1**: 양의 방향으로 속력이 증가하면 $a > 0$, 감소하면 $a < 0$. 음의 방향으로 속력이 증가하면 $a < 0$, 감소하면 $a > 0$.

</div>

</v-click>

</div>
</div>

---

# 예제: 가속도와 $dv/dt$ (Sample Problem 2.3.1)

<div class="text-sm">

$x(t) = 4 - 27t + t^3$ ($x$: m, $t$: s)

</div>

<div class="grid grid-cols-2 gap-6">
<div>

<v-clicks>

**(a)** $v(t) = dx/dt = -27 + 3t^2$ (m/s), $a(t) = dv/dt = 6t$ (m/s²)

**(b)** $v = 0$: $0 = -27 + 3t^2 \implies t = 3$ s

</v-clicks>

<v-click>

**(c)** 운동 분석:

| $t$ | $v$ | $a$ | 운동 |
|---|---|---|---|
| $0$ | $-27$ m/s | $0$ | 왼쪽 등속 |
| $0 < t < 3$ | 음 | 양 | 감속 |
| $3$ s | $0$ | $18$ m/s² | 순간 정지 |
| $t > 3$ | 양 | 양 | 오른쪽 가속 |

</v-click>

</div>
<div>

<v-click>

$t = 3$ s일 때 위치:

$$
x(3) = 4 - 27(3) + 3^3 = -50 \text{ m}
$$

원점 왼쪽 50 m — 가장 멀리 간 지점!

</v-click>

</div>
</div>

---
layout: section
---

# 2.4 등가속도 운동

Constant Acceleration

---

# 등가속도 운동: 기본 방정식 유도

가속도가 일정할 때 ($a = a_\text{avg} = \text{const}$):

<div class="grid grid-cols-2 gap-8">
<div>

<v-clicks>

### 첫 번째 기본식

$a = (v - v_0) / (t - 0)$에서:

$$
\boxed{v = v_0 + at} \tag{2.4.1}
$$

### 두 번째 기본식

$v_\text{avg} = (x - x_0)/t$이고, 등가속도이므로 $v_\text{avg} = \frac{1}{2}(v_0 + v)$

$$
x = x_0 + v_\text{avg} \, t = x_0 + \tfrac{1}{2}(v_0 + v)\,t
$$

$v = v_0 + at$를 대입하면:

$$
\boxed{x - x_0 = v_0 t + \tfrac{1}{2}at^2} \tag{2.4.5}
$$

</v-clicks>

</div>
<div>

<img src="/img/c0204f001_high_resolution.jpg" class="max-h-[420px] object-contain rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.4.1 — 등가속도: x(t) 포물선, v(t) 직선, a(t) 상수</div>

</div>
</div>

---

# 등가속도 5대 방정식

<div class="text-sm">기본 2개 + 파생 3개 = 총 5개</div>

| 번호 | 방정식 | 빠진 변수 |
|---|---|---|
| 2.4.1 | $v = v_0 + at$ | $x - x_0$ |
| 2.4.5 | $x - x_0 = v_0 t + \frac{1}{2}at^2$ | $v$ |
| 2.4.6 | $v^2 = v_0^2 + 2a(x - x_0)$ | $t$ |
| 2.4.7 | $x - x_0 = \frac{1}{2}(v_0 + v)\,t$ | $a$ |
| 2.4.8 | $x - x_0 = vt - \frac{1}{2}at^2$ | $v_0$ |

<v-click>

<div class="mt-2 p-3 bg-yellow-500 bg-opacity-10 rounded-lg text-sm">

**풀이 전략**: 5개 변수 ($x - x_0$, $v$, $v_0$, $a$, $t$) 중 3개를 알면 나머지 2개를 구할 수 있다. "빠진 변수" 열을 보고 적절한 식을 선택!

**가장 간단한 전략**: Eq. 2.4.1과 2.4.5만 기억하고, 나머지는 연립방정식으로 유도.

</div>

</v-click>

---

# 예제: 자율주행 추월 (Sample Problem 2.4.1)

<div class="grid grid-cols-2 gap-6">
<div>

차량 B가 $v_0 = 22.0$ m/s로 주행 중, $a = 3.50$ m/s²으로 가속하여 $v = 27.0$ m/s에 도달 후 추월.

<v-clicks>

**(a) 가속 시간:**

$$
t_1 = \frac{v - v_0}{a} = \frac{27.0 - 22.0}{3.50} \approx 1.43 \text{ s}
$$

**(b) 가속 중 이동 거리:**

$$
v^2 = v_0^2 + 2a \, d_1
$$

$$
d_1 = \frac{v^2 - v_0^2}{2a} = \frac{27.0^2 - 22.0^2}{2(3.50)} = 35.0 \text{ m}
$$

</v-clicks>

</div>
<div>

<div class="grid grid-cols-2 gap-2">
<img src="/img/c0204f002a_high_resolution.jpg" class="rounded" />
<img src="/img/c0204f002b_high_resolution.jpg" class="rounded" />
<img src="/img/c0204f002c_high_resolution.jpg" class="rounded" />
<img src="/img/c0204f002d_high_resolution.jpg" class="rounded" />
</div>

<div class="text-xs text-gray-400 mt-1">Fig 2.4.2 — 추월 과정의 4단계</div>

</div>
</div>

---

# 예제: 딱따구리 가속도 (Sample Problem 2.4.2)

딱따구리 머리가 $v_0 = 7.49$ m/s로 나무에 부딪혀 $1.87$ mm 관통 후 정지.

<v-clicks>

**주어진 것**: $v_0 = 7.49$ m/s, $v = 0$, $x - x_0 = 1.87 \times 10^{-3}$ m — **빠진 변수**: $t$ → Eq. 2.4.6!

$$
v^2 = v_0^2 + 2a(x - x_0) \implies 0 = (7.49)^2 + 2a(1.87 \times 10^{-3})
$$

$$
a = -\frac{(7.49)^2}{2(1.87 \times 10^{-3})} = -1.50 \times 10^4 \text{ m/s}^2
$$

</v-clicks>

<v-click>

<div class="mt-3 p-3 bg-green-500 bg-opacity-10 rounded-lg">

$g$ 단위: $|a| = 1.50 \times 10^4 / 9.8 \approx 1530\,g$ — Colonel Stapp 로켓 썰매 실험의 약 **70배**!

</div>

</v-click>

---

# 적분을 통한 유도 (Another Look at Constant Acceleration)

<div class="grid grid-cols-2 gap-6">
<div>

### $v = v_0 + at$ 유도

<v-clicks>

$a = dv/dt$에서 $dv = a\,dt$

$$\int dv = \int a\,dt = a \int dt \implies v = at + C$$

$t = 0$일 때 $v = v_0$이므로 $C = v_0$ → $v = v_0 + at$

</v-clicks>

</div>
<div>

### $x - x_0 = v_0 t + \frac{1}{2}at^2$ 유도

<v-clicks>

$v = dx/dt$에서 $dx = v\,dt$

$$\int dx = \int (v_0 + at)\,dt \implies x = v_0 t + \tfrac{1}{2}at^2 + C'$$

$t = 0$일 때 $x = x_0$이므로 $C' = x_0$ → $x - x_0 = v_0 t + \tfrac{1}{2}at^2$

</v-clicks>

</div>
</div>

<v-click>

<div class="mt-3 p-3 bg-blue-500 bg-opacity-10 rounded-lg text-sm">

**핵심**: 등가속도 방정식은 $a = \text{const}$ 조건에서 미분/적분의 직접적인 결과이다.

</div>

</v-click>

---
layout: section
---

# 2.5 자유낙하 가속도

Free-Fall Acceleration

---

# 자유낙하 (Free-Fall Acceleration)

<div class="grid grid-cols-2 gap-8">
<div>

공기 저항을 무시하면, 모든 물체는 **같은 가속도**로 낙하:

$$
\boxed{g = 9.8 \text{ m/s}^2}
$$

<v-clicks>

- 질량, 밀도, 모양에 **무관**
- $y$축을 위쪽 양의 방향으로 설정:

$$
a = -g = -9.8 \text{ m/s}^2
$$

- **주의**: $g$는 크기(항상 양수), $a = -g$는 방향 포함

</v-clicks>

<v-click>

<div class="mt-4 p-3 bg-yellow-500 bg-opacity-10 rounded-lg text-sm">

**등가속도 방정식 적용**: Table 2.4.1에서 $x → y$, $a → -g$로 치환하면 그대로 사용 가능!

</div>

</v-click>

</div>
<div>

<img src="/img/c0205f001_high_resolution.jpg" class="h-80 mx-auto rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.5.1 — 진공에서 깃털과 사과는 같은 속도로 낙하</div>

</div>
</div>

---

# 자유낙하 방정식

$y$축 위쪽을 양의 방향, $a = -g$로 놓으면:

<div class="grid grid-cols-2 gap-6 mt-2">
<div>

$$v = v_0 - gt$$

$$y - y_0 = v_0 t - \tfrac{1}{2}g t^2$$

$$v^2 = v_0^2 - 2g(y - y_0)$$

</div>
<div>

<v-click>

### 위로 던진 물체

- 상승 중: $v$ 감소 ($v > 0$, $a < 0$)
- 최고점: $v = 0$ (순간 정지)
- 하강 중: $|v|$ 증가 ($v < 0$, $a < 0$)
- 가속도는 **항상** $-g$ (최고점에서도!)

</v-click>

</div>
</div>

<v-click>

<div class="mt-2 p-3 bg-green-500 bg-opacity-10 rounded-lg text-sm">

**Checkpoint 2.5.1**: 공을 위로 던졌을 때 — (a) 상승 변위 부호? **양** (b) 하강 변위 부호? **음** (c) 최고점 가속도? $-g = -9.8$ m/s² (0이 아님!)

</div>

</v-click>

---

# 예제: 나이아가라 폭포 (Sample Problem 2.5.1)

<div class="text-sm">Dave Munday가 강철 공에 탑승하여 나이아가라 폭포에서 48 m 낙하. $v_0 = 0$.</div>

<div class="grid grid-cols-2 gap-6">
<div>

<v-clicks>

**(a) 수면 도달 시간:** $y_0 = 0$, $y = -48$ m

$$-48 = -\tfrac{1}{2}(9.8)t^2 \implies t = \sqrt{48/4.9} = 3.1 \text{ s}$$

**(c) 수면 도달 속도:**

$$v^2 = -2(9.8)(-48) = 940.8 \implies v \approx -31 \text{ m/s} \approx -100 \text{ km/h}$$

**(d) 매 초 속도:** $v = -9.8t$

| $t$ (s) | $v$ (m/s) | $y$ (m) |
|---|---|---|
| 1 | −9.8 | −4.9 |
| 2 | −19.6 | −19.6 |
| 3 | −29.4 | −44.1 |

</v-clicks>

</div>
<div>

<img src="/img/c0205f002_high_resolution.jpg" class="max-h-[380px] object-contain mx-auto rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.5.2 — 매 초 위치, 속도, 가속도</div>

</div>
</div>

---
layout: section
---

# 2.6 그래프를 이용한 운동 해석

Graphical Integration in Motion Analysis

---

# 그래프 적분 (Graphical Integration)

<div class="grid grid-cols-2 gap-8">
<div>

### 가속도 적분 → 속도 변화

$$
v_1 - v_0 = \int_{t_0}^{t_1} a \, dt
$$

= $a$-$t$ 그래프와 시간축 사이의 **넓이**

### 속도 적분 → 위치 변화

$$
x_1 - x_0 = \int_{t_0}^{t_1} v \, dt
$$

= $v$-$t$ 그래프와 시간축 사이의 **넓이**

<v-click>

<div class="mt-4 p-3 bg-blue-500 bg-opacity-10 rounded-lg text-sm">

**정리**: 기울기 = 미분, 넓이 = 적분

- $x$-$t$ 그래프의 **기울기** → $v$
- $v$-$t$ 그래프의 **기울기** → $a$
- $a$-$t$ 그래프의 **넓이** → $\Delta v$
- $v$-$t$ 그래프의 **넓이** → $\Delta x$

</div>

</v-click>

</div>
<div>

<img src="/img/c0206f001_high_resolution.jpg" class="w-full rounded-lg" />

<div class="text-xs text-gray-400 mt-1">Fig 2.6.1 — (a) a-t 그래프 아래 넓이 = 속도 변화, (b) v-t 그래프 아래 넓이 = 위치 변화</div>

<v-click>

<div class="mt-4 p-3 bg-yellow-500 bg-opacity-10 rounded-lg text-sm">

**Checkpoint 2.6.1**: $v$-$t$ 그래프에서 $\Delta x$를 구하려면? → **적분** (넓이). 가속도를 구하려면? → **미분** (기울기).

</div>

</v-click>

</div>
</div>

---

# Review & Summary

<div class="grid grid-cols-2 gap-4 text-sm">
<div>

### 위치와 변위
- **위치** $x$: 기준점 대비 좌표 / **변위**: $\Delta x = x_2 - x_1$ (벡터)

### 속도
- **평균속도**: $v_\text{avg} = \Delta x / \Delta t$ / **순간속도**: $v = dx/dt$ / **속력**: $|v|$

### 가속도
- **평균**: $a_\text{avg} = \Delta v / \Delta t$ / **순간**: $a = dv/dt = d^2 x / dt^2$

### 자유낙하
- $a = -g = -9.8$ m/s² (아래 방향), 질량·모양에 무관

### 그래프 해석
- 기울기 = 미분, 넓이 = 적분

</div>
<div>

### 등가속도 5대 방정식

$$v = v_0 + at$$

$$x - x_0 = v_0 t + \tfrac{1}{2}at^2$$

$$v^2 = v_0^2 + 2a(x - x_0)$$

$$x - x_0 = \tfrac{1}{2}(v_0 + v)\,t$$

$$x - x_0 = vt - \tfrac{1}{2}at^2$$

</div>
</div>

---

# 연습 문제

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

### 문제 1: 등가속도

자동차가 정지 상태에서 출발하여 $a = 2.0$ m/s²으로 등가속. 5.0 s 후의 속도와 이동 거리는?

<v-click>

**풀이:**

$$
v = v_0 + at = 0 + 2.0 \times 5.0 = 10 \text{ m/s}
$$

$$
x = v_0 t + \tfrac{1}{2}at^2 = 0 + \tfrac{1}{2}(2.0)(5.0)^2 = 25 \text{ m}
$$

</v-click>

</div>
<div>

### 문제 2: 자유낙하

건물 옥상에서 공을 $v_0 = 12$ m/s로 위로 던졌다. (a) 최고점까지의 시간? (b) 최고점 높이?

<v-click>

**풀이:**

(a) 최고점에서 $v = 0$:

$$
0 = 12 - 9.8t \implies t = 1.2 \text{ s}
$$

(b)

$$
\Delta y = 12(1.2) - \tfrac{1}{2}(9.8)(1.2)^2 = 7.3 \text{ m}
$$

</v-click>

</div>
</div>

---
layout: center
class: text-center
---

# 감사합니다

Chapter 2: 직선 운동 (Motion Along a Straight Line) 끝

<div class="mt-8 text-gray-400">

다음: Chapter 3 — 벡터 (Vectors)

</div>
