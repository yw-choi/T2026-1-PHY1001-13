---
title: "4장: 2차원·3차원 운동"
week: 4
chapters: "4장"
topics: "위치와 변위, 속도와 가속도, 포물체 운동, 등속 원운동, 상대 운동"
---

# 4장: 2차원·3차원 운동

Motion in Two and Three Dimensions

---

## 이번 장에서 배울 내용

- **위치(position)** 와 **변위(displacement)** 를 벡터로 표현하기
- **속도(velocity)** 와 **가속도(acceleration)** 의 벡터 정의
- **포물체 운동(projectile motion)**: 수평·수직 독립 운동
- **등속 원운동(uniform circular motion)** 과 구심가속도
- **상대 운동(relative motion)**: 기준틀에 따라 달라지는 속도

---

## 왜 2차원·3차원을 다루는가?

지금까지 1차원(직선) 운동만 다뤘다. 하지만 현실의 운동은 대부분 **2차원 이상** 이다.

- 축구 프리킥: 공은 앞으로 날아가면서 동시에 위로 올라갔다 내려온다
- 놀이공원 회전 기구: 원을 따라 계속 방향이 바뀐다
- KBO 홈런: 타구는 포물선 궤적을 그린다

핵심 아이디어: 2차원 운동은 **서로 독립인 두 개의 1차원 운동** 으로 분해할 수 있다!

---

## 2차원 운동의 핵심 전략

이전 장에서 배운 **1차원 운동학** 을 그대로 활용한다.

- $x$축 방향: $x$에 대한 1차원 운동
- $y$축 방향: $y$에 대한 1차원 운동

두 방향을 **독립적으로** 분석한 뒤, 벡터로 합치면 된다.

벡터 덧셈과 성분 분해(3장)가 여기서 본격적으로 활용된다.

---

## 4.1 위치와 변위

### 위치 벡터 (Position Vector)

입자의 **위치** 는 원점에서 입자까지의 벡터 $\vec{r}$로 나타낸다:

$$\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$$

2차원에서는:

$$\vec{r} = x\hat{i} + y\hat{j}$$

---

### 변위 (Displacement)

입자가 위치 $\vec{r}_1$에서 $\vec{r}_2$로 이동할 때, **변위** 는:

$$\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$$

성분으로 쓰면:

$$\Delta\vec{r} = (x_2 - x_1)\hat{i} + (y_2 - y_1)\hat{j} = \Delta x\,\hat{i} + \Delta y\,\hat{j}$$

<img src="/img/ch04/position-displacement.svg" style="max-height:50vh">

---

## 4.2 평균 속도와 순간 속도

### 평균 속도 (Average Velocity)

시간 $\Delta t$ 동안 변위 $\Delta\vec{r}$가 일어났다면, **평균 속도** 는:

$$\vec{v}_\text{avg} = \frac{\Delta\vec{r}}{\Delta t}$$

성분으로:

$$\vec{v}_\text{avg} = \frac{\Delta x}{\Delta t}\hat{i} + \frac{\Delta y}{\Delta t}\hat{j}$$

- 평균 속도의 **방향** 은 변위 $\Delta\vec{r}$의 방향과 같다
- 스칼라인 "평균 속력"과 구별할 것

---

### 순간 속도 (Instantaneous Velocity)

$\Delta t \to 0$의 극한을 취하면 **순간 속도** :

$$\vec{v} = \lim_{\Delta t \to 0} \frac{\Delta\vec{r}}{\Delta t} = \frac{d\vec{r}}{dt}$$

성분으로:

$$\vec{v} = v_x\hat{i} + v_y\hat{j} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j}$$

속력(speed)은 속도 벡터의 크기:

$$v = |\vec{v}| = \sqrt{v_x^2 + v_y^2}$$

---

### 순간 속도의 방향 = 접선 방향

순간 속도 $\vec{v}$의 방향은 그 순간 경로의 **접선 방향** 이다.

<img src="/img/ch04/velocity-tangent.svg" style="max-height:50vh">

속도 벡터가 $x$축과 이루는 각도:

$$\tan\theta = \frac{v_y}{v_x}$$

---

## 4.3 평균 가속도와 순간 가속도

### 평균 가속도 (Average Acceleration)

속도가 $\vec{v}_1$에서 $\vec{v}_2$로 변했다면:

$$\vec{a}_\text{avg} = \frac{\Delta\vec{v}}{\Delta t} = \frac{\vec{v}_2 - \vec{v}_1}{\Delta t}$$

---

### 순간 가속도 (Instantaneous Acceleration)

$$\vec{a} = \frac{d\vec{v}}{dt} = a_x\hat{i} + a_y\hat{j}$$

여기서

$$a_x = \frac{dv_x}{dt}, \quad a_y = \frac{dv_y}{dt}$$

중요: 가속도는 속도의 **크기** 가 변해도, **방향** 이 변해도 존재한다!

- 직선 가속: 크기만 변함
- 등속 원운동: 방향만 변함
- 일반적인 곡선 운동: 크기와 방향 모두 변함

---

### 2차원 등가속도 운동

가속도 $\vec{a}$가 일정할 때, 1차원 운동 방정식을 각 성분에 적용:

**$x$방향:**

$$v_x = v_{0x} + a_x t$$

$$x = x_0 + v_{0x}t + \frac{1}{2}a_x t^2$$

**$y$방향:**

$$v_y = v_{0y} + a_y t$$

$$y = y_0 + v_{0y}t + \frac{1}{2}a_y t^2$$

두 축은 **완전히 독립** 이다. $x$방향의 운동은 $y$방향에 영향을 주지 않는다!

---

## 4.4 포물체 운동 — 개념 도입

### 포물체 운동이란?

**포물체 운동(projectile motion)** 은 초기 속도를 가진 물체가 **중력만** 받으며 운동하는 것이다.

핵심 가정:

- 공기 저항 무시
- 중력 가속도 $\vec{g}$는 일정하고 아래 방향
- $a_x = 0$, $a_y = -g$

**수평·수직 독립 원리:**

- **수평** ($x$): 등속 운동 (힘이 없으므로)
- **수직** ($y$): 등가속도 운동 (중력에 의해)

이 두 운동은 **서로 완전히 독립** 이다!

---

### 수평·수직 독립을 이해하기

동시에 두 공을 놓는다고 상상해 보자:

- 공 A: 수평으로 던진다
- 공 B: 같은 높이에서 자유낙하시킨다

두 공은 **동시에** 땅에 도달한다!

수평 속도가 아무리 빨라도, 수직 방향의 운동에는 영향을 주지 않기 때문이다.

---

## 포물체 운동 — 수식 유도

### 초기 조건 설정

발사점을 원점 $(0, 0)$, 초기 속력 $v_0$, 발사각 $\theta_0$로 놓으면:

$$v_{0x} = v_0\cos\theta_0, \quad v_{0y} = v_0\sin\theta_0$$

---

### 수평 운동 ($a_x = 0$)

$$v_x = v_0\cos\theta_0 \quad (\text{일정!})$$

$$x = (v_0\cos\theta_0)\,t$$

수평 속도는 **변하지 않는다**. 처음부터 끝까지 같은 값이다.

---

### 수직 운동 ($a_y = -g$)

$$v_y = v_0\sin\theta_0 - gt$$

$$y = (v_0\sin\theta_0)\,t - \frac{1}{2}gt^2$$

수직 운동은 자유낙하와 동일한 가속도를 받는다.

<img src="/img/ch04/projectile-decomposition.svg" style="max-height:50vh">

---

### 궤적 방정식 (Trajectory Equation)

$x = (v_0\cos\theta_0)\,t$에서 $t = \frac{x}{v_0\cos\theta_0}$를 $y$ 식에 대입:

$$y = (\tan\theta_0)\,x - \frac{g}{2(v_0\cos\theta_0)^2}\,x^2$$

이것은 $y = ax - bx^2$ 형태의 **포물선(parabola)** 이다!

그래서 "포물체 운동"이라 부른다.

---

### 도달거리와 최고점

**최고점 높이** $H$: $v_y = 0$일 때의 높이

$v_y = v_0\sin\theta_0 - gt_H = 0$에서 $t_H = \frac{v_0\sin\theta_0}{g}$

$$H = v_0\sin\theta_0 \cdot t_H - \frac{1}{2}g\,t_H^2 = \frac{v_0^2\sin^2\theta_0}{2g}$$

**도달거리(range)** $R$: $y = 0$으로 되돌아오는 수평 거리

체공 시간 $T = 2t_H = \frac{2v_0\sin\theta_0}{g}$ (대칭)

$$R = v_0\cos\theta_0 \cdot T = \frac{v_0^2 \sin 2\theta_0}{g}$$

($\sin 2\theta_0 = 2\sin\theta_0\cos\theta_0$ 이용)

---

### 발사각에 따른 도달거리

$R = \frac{v_0^2\sin 2\theta_0}{g}$에서:

- $\sin 2\theta_0 = 1$일 때 최대 → $\theta_0 = 45°$에서 **최대 도달거리**
- $\theta_0$와 $90° - \theta_0$는 같은 도달거리 (보각 관계)

<img src="/img/ch04/range-vs-angle.svg" style="max-height:50vh">

---

### 공기 저항의 효과

실제로는 공기 저항이 있어 이상적인 포물선과 차이가 난다.

- 도달거리가 **줄어든다**
- 궤적이 **비대칭** 이 된다 (하강이 더 가파름)
- 최대 도달거리 각도가 45°보다 **작아진다**

KBO 홈런을 예로 들면:

- 공기 저항이 없다면 도달거리가 약 200 m에 이를 타구도 있지만
- 실제로는 140 m 정도에 그친다
- 최적 타구 각도는 약 35° (45°가 아니다!)

---

<!-- sim:projectile-motion.html -->
포물체 운동 시뮬레이션

---

### 포물체 운동 예제 1

**문제:** 축구공을 지면에서 초기 속력 25 m/s, 발사각 30°로 찬다. (공기 저항 무시, $g = 9.8$ m/s$^2$)

(a) 최고점 높이는?
(b) 체공 시간은?
(c) 도달거리는?

---

### 풀이

**(a)** 최고점 높이:

$$H = \frac{v_0^2\sin^2\theta_0}{2g} = \frac{(25)^2\sin^2 30°}{2(9.8)} = \frac{625 \times 0.25}{19.6} = 7.97 \text{ m}$$

**(b)** 체공 시간:

$$T = \frac{2v_0\sin\theta_0}{g} = \frac{2(25)\sin 30°}{9.8} = \frac{25}{9.8} = 2.55 \text{ s}$$

**(c)** 도달거리:

$$R = \frac{v_0^2\sin 2\theta_0}{g} = \frac{(25)^2\sin 60°}{9.8} = \frac{625 \times 0.866}{9.8} = 55.2 \text{ m}$$

---

## 4.5 등속 원운동

### 등속 원운동이란?

**등속 원운동(uniform circular motion)** 은 입자가 일정한 **속력** 으로 원을 따라 운동하는 것이다.

- **속력** $v$는 일정
- 하지만 **속도** $\vec{v}$는 계속 변한다 (방향이 바뀌므로)
- 속도가 변하면 → **가속도** 가 존재한다!

---

### 구심가속도 (Centripetal Acceleration)

등속 원운동하는 입자의 가속도:

$$a = \frac{v^2}{r}$$

- 방향: 항상 **원의 중심을 향한다** (구심 = "중심을 향하는")
- 속력이 빠를수록, 반지름이 작을수록 가속도가 크다

<img src="/img/ch04/centripetal-acceleration.svg" style="max-height:50vh">

---

### 주기와 각속도

**주기(period)** $T$: 원을 한 바퀴 도는 데 걸리는 시간

$$T = \frac{2\pi r}{v}$$

원둘레 $2\pi r$을 속력 $v$로 나눈 것이다.

이를 구심가속도 공식에 대입하면:

$$a = \frac{4\pi^2 r}{T^2}$$

---

### 구심가속도 유도

반지름 $r$인 원 위에서 등속으로 움직이는 입자의 위치:

$$\vec{r} = r\cos\theta\,\hat{i} + r\sin\theta\,\hat{j}$$

등속 원운동에서 각도 $\theta = \omega t$ ($\omega$: 각속도, $\omega = v/r$)

$$\vec{r} = r\cos(\omega t)\,\hat{i} + r\sin(\omega t)\,\hat{j}$$

속도: 미분하면

$$\vec{v} = \frac{d\vec{r}}{dt} = -r\omega\sin(\omega t)\,\hat{i} + r\omega\cos(\omega t)\,\hat{j}$$

속력을 확인하면:

$$|\vec{v}| = r\omega = v \quad \checkmark$$

---

### 구심가속도 유도 (계속)

가속도: 한 번 더 미분하면

$$\vec{a} = \frac{d\vec{v}}{dt} = -r\omega^2\cos(\omega t)\,\hat{i} - r\omega^2\sin(\omega t)\,\hat{j}$$

이것을 정리하면:

$$\vec{a} = -\omega^2\left[r\cos(\omega t)\,\hat{i} + r\sin(\omega t)\,\hat{j}\right] = -\omega^2\vec{r}$$

따라서:

- **크기:** $a = \omega^2 r = \frac{v^2}{r}$ ($v = r\omega$ 이용) $\quad\checkmark$
- **방향:** $\vec{a} = -\omega^2\vec{r}$ → $\vec{r}$의 **반대 방향**, 즉 **중심을 향한다** $\quad\checkmark$

미분으로 구심가속도 공식이 정확히 유도된다!

---

<!-- sim:circular-motion.html -->
등속 원운동 시뮬레이션

---

### 원운동 예제: 에버랜드 회전 놀이기구

**문제:** 에버랜드의 회전 놀이기구가 반지름 $r = 12$ m, 주기 $T = 4.0$ s로 등속 원운동한다.

(a) 탑승자의 속력은?
(b) 구심가속도의 크기는? ($g$의 몇 배인가?)

**풀이:**

(a) $v = \frac{2\pi r}{T} = \frac{2\pi(12)}{4.0} = 18.8$ m/s (약 68 km/h)

(b) $a = \frac{v^2}{r} = \frac{(18.8)^2}{12} = 29.5$ m/s$^2$

$$\frac{a}{g} = \frac{29.5}{9.8} = 3.0g$$

탑승자는 자기 몸무게의 3배에 해당하는 가속도를 느낀다!

---

## 4.6-4.7 상대 운동

### 상대 운동이란?

같은 물체라도 **관측자(기준틀)에 따라** 속도가 다르게 측정된다.

예시:

- KTX 안에서 통로를 걷는 승객
  - 다른 승객이 보면: 걷는 속도 (약 1 m/s)
  - 지면의 관측자가 보면: KTX 속도 + 걷는 속도 (약 301 m/s)

---

### 상대 속도 공식

<img src="/img/ch04/relative-motion-frames.svg" style="max-height:50vh">

두 기준틀 A, B가 있고, 입자 P가 운동할 때:

$$\vec{r}_{PA} = \vec{r}_{PB} + \vec{r}_{BA}$$

시간에 대해 미분하면:

$$\vec{v}_{PA} = \vec{v}_{PB} + \vec{v}_{BA}$$

- $\vec{v}_{PA}$: A에서 본 P의 속도
- $\vec{v}_{PB}$: B에서 본 P의 속도
- $\vec{v}_{BA}$: A에서 본 B의 속도

---

### 상대 속도 — 읽는 법

$$\vec{v}_{PA} = \vec{v}_{PB} + \vec{v}_{BA}$$

아래 첨자 규칙:

- 앞 글자: 관찰 대상, 뒤 글자: 기준틀
- $\vec{v}_{PA}$ = "A 기준으로 본 P의 속도"
- **안쪽 첨자가 같으면** 소거할 수 있다: $P\underline{B} + \underline{B}A = PA$

$$\vec{v}_{AB} = -\vec{v}_{BA}$$

A에서 본 B의 속도와, B에서 본 A의 속도는 크기가 같고 방향이 반대이다.

---

### 상대 운동 예제: 강을 건너는 배

**문제:** 강폭 200 m. 배의 정수 속력 5.0 m/s, 강물의 유속 3.0 m/s (동쪽).

배가 북쪽을 향해 출발하면:

(a) 지면에서 본 배의 속력과 방향은?
(b) 강 건너편에 도착하는 데 걸리는 시간은?
(c) 배는 출발점에서 얼마나 동쪽으로 밀려나는가?

---

### 풀이

$\vec{v}_{BS}$ (물 기준 배의 속도) = 5.0 m/s (북쪽)
$\vec{v}_{SG}$ (지면 기준 물의 속도) = 3.0 m/s (동쪽)

**(a)** 지면 기준 배의 속도:

$$\vec{v}_{BG} = \vec{v}_{BS} + \vec{v}_{SG}$$

$$v_{BG} = \sqrt{5.0^2 + 3.0^2} = \sqrt{34} = 5.83 \text{ m/s}$$

방향: $\theta = \arctan\frac{3.0}{5.0} = 31°$ (북쪽에서 동쪽으로)

**(b)** 강을 건너는 데는 북쪽 성분만 관여:

$$t = \frac{200}{5.0} = 40 \text{ s}$$

**(c)** 동쪽 밀림:

$$\Delta x = 3.0 \times 40 = 120 \text{ m}$$

---

<!-- sim:relative-motion-2d.html -->
상대 운동 시뮬레이션

---

## Review & Summary

### 핵심 개념

| 개념 | 공식 |
|---|---|
| 위치 벡터 | $\vec{r} = x\hat{i} + y\hat{j}$ |
| 변위 | $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$ |
| 순간 속도 | $\vec{v} = d\vec{r}/dt$ |
| 순간 가속도 | $\vec{a} = d\vec{v}/dt$ |
| 포물체 수평 | $x = (v_0\cos\theta_0)\,t$ |
| 포물체 수직 | $y = (v_0\sin\theta_0)\,t - \frac{1}{2}gt^2$ |

---

### 핵심 개념 (계속)

| 개념 | 공식 |
|---|---|
| 궤적 방정식 | $y = (\tan\theta_0)\,x - \frac{g}{2v_0^2\cos^2\theta_0}\,x^2$ |
| 도달거리 | $R = v_0^2\sin 2\theta_0 / g$ |
| 최고점 높이 | $H = v_0^2\sin^2\theta_0 / (2g)$ |
| 구심가속도 | $a = v^2/r = 4\pi^2 r/T^2$ |
| 상대 속도 | $\vec{v}_{PA} = \vec{v}_{PB} + \vec{v}_{BA}$ |

**기억할 것:**
- 2차원 운동은 **독립인 두 개의 1차원 운동** 으로 분해
- 포물체 운동: 수평은 등속, 수직은 등가속도
- 등속 원운동: 속력은 일정하나 **방향** 이 계속 변한다
- 상대 속도: 아래 첨자의 "안쪽"이 같으면 소거 가능
