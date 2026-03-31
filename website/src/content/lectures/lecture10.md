---
title: "10장: 회전"
week: 10
chapters: "10장"
topics: "각위치, 각속도, 각가속도, 등각가속도 운동, 관성모멘트, 토크, 회전 운동에너지"
---

# 10장: 회전

Rotation

---

## 이번 장에서 배울 내용

- **각변수(angular variables)**: 각위치 $\theta$, 각속도 $\omega$, 각가속도 $\alpha$
- **등각가속도 운동**: 2장의 등가속도 공식과의 대응
- **선형-각 관계**: $v = \omega r$, $a_t = \alpha r$, $a_r = \omega^2 r$
- **관성모멘트(moment of inertia)** $I$: 회전의 "질량" 역할
- **토크(torque)** $\tau$: 회전의 "힘" 역할
- **회전 운동에너지**: $K = \frac{1}{2}I\omega^2$
- **회전의 뉴턴 제2법칙**: $\tau_\text{net} = I\alpha$

---

## 왜 회전을 배우는가?

지금까지는 물체를 **질점(입자)** 으로 취급했다. 크기와 모양은 무시하고, 위치만 추적했다.

하지만 현실의 물체는 크기가 있고, **회전** 한다:

- 자동차 바퀴, 선풍기 날개, 지구의 자전
- 피겨 스케이터의 스핀, 팽이의 회전

이번 장에서는 **고정된 축** 을 중심으로 회전하는 **강체(rigid body)** 의 운동을 다룬다.

> **강체** 란 변형되지 않는 이상적인 물체로, 물체 내 모든 점 사이의 거리가 일정하다.

---

## 10.1 각위치

<img src="/img/ch10/angular-position.svg" style="max-height:50vh">

---

### 각위치(angular position) 의 정의

고정 축(회전축)을 중심으로 회전하는 강체 위의 한 점 P를 생각하자.

**기준선** 에서 점 P까지 측정한 각도가 **각위치(angular position)** $\theta$이다.

$$\theta = \frac{s}{r}$$

여기서 $s$는 호의 길이, $r$은 반지름이다.

- 단위: **라디안(radian, rad)**
- 반시계 방향이 양(+), 시계 방향이 음(-)
- $1 \text{ rev} = 2\pi \text{ rad} = 360°$

---

### 각도 단위 변환

$$1 \text{ rad} = \frac{360°}{2\pi} \approx 57.3°$$

$$\theta(\text{rad}) = \frac{\pi}{180°} \times \theta(°)$$

예시: 반바퀴 회전 = $\pi$ rad = 180°

강체가 회전할 때, 강체 위의 **모든 점** 은 같은 각도 $\theta$만큼 회전한다.

이것이 각변수의 장점이다 — 하나의 $\theta$로 전체 강체의 상태를 기술할 수 있다.

---

## 10.2 각변위, 각속도, 각가속도

### 각변위(angular displacement)

$$\Delta\theta = \theta_2 - \theta_1$$

2장에서 $\Delta x = x_2 - x_1$에 대응된다.

---

### 각속도(angular velocity)

**평균 각속도:**

$$\omega_\text{avg} = \frac{\Delta\theta}{\Delta t}$$

**순간 각속도:**

$$\omega = \frac{d\theta}{dt}$$

- 단위: **rad/s**
- $\omega > 0$: 반시계 방향 회전
- $\omega < 0$: 시계 방향 회전

---

### 각가속도(angular acceleration)

**평균 각가속도:**

$$\alpha_\text{avg} = \frac{\Delta\omega}{\Delta t}$$

**순간 각가속도:**

$$\alpha = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$$

- 단위: **rad/s²**
- $\alpha$와 $\omega$가 같은 부호 → 회전 빨라짐
- $\alpha$와 $\omega$가 다른 부호 → 회전 느려짐

---

## 10.3 등각가속도 운동

$\alpha$가 일정할 때, 2장의 등가속도 공식과 **정확히 같은 구조** 의 식이 성립한다:

| 병진 운동 ($a$ 일정) | 회전 운동 ($\alpha$ 일정) |
|---|---|
| $v = v_0 + at$ | $\omega = \omega_0 + \alpha t$ |
| $x = x_0 + v_0 t + \frac{1}{2}at^2$ | $\theta = \theta_0 + \omega_0 t + \frac{1}{2}\alpha t^2$ |
| $v^2 = v_0^2 + 2a(x - x_0)$ | $\omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0)$ |
| $x = x_0 + \frac{1}{2}(v_0 + v)t$ | $\theta = \theta_0 + \frac{1}{2}(\omega_0 + \omega)t$ |

$x \leftrightarrow \theta$, $v \leftrightarrow \omega$, $a \leftrightarrow \alpha$로 치환하면 된다!

---

### 예제: 등각가속도

선풍기 날개가 정지 상태에서 $\alpha = 2.0$ rad/s²로 일정하게 가속된다.

(a) 5.0 s 후의 각속도는?

$$\omega = \omega_0 + \alpha t = 0 + 2.0 \times 5.0 = 10 \text{ rad/s}$$

(b) 5.0 s 동안 회전한 각도는?

$$\theta = \omega_0 t + \frac{1}{2}\alpha t^2 = 0 + \frac{1}{2}(2.0)(5.0)^2 = 25 \text{ rad}$$

회전 수: $25/(2\pi) \approx 4.0$ 바퀴

---

<!-- sim:rotation-kinematics.html -->
회전 운동학 시뮬레이션

---

## 10.4 선형량과 각량의 관계

회전축에서 거리 $r$인 점 P의 선형량:

<img src="/img/ch10/linear-angular-relation.svg" style="max-height:50vh">

---

### 호의 길이

$$s = \theta r$$

$\theta$는 반드시 **라디안** 으로!

---

### 접선 속력(tangential speed)

$$v = \frac{ds}{dt} = \frac{d(\theta r)}{dt} = \omega r$$

- 같은 강체 위라도, $r$이 큰 점은 더 빠르게 움직인다
- 각속도 $\omega$는 모든 점에서 동일하지만, 선속도 $v$는 $r$에 비례

---

### 접선 가속도와 구심 가속도

**접선 가속도(tangential acceleration):**

$$a_t = \frac{dv}{dt} = \alpha r$$

속력의 **크기** 변화를 담당

**구심 가속도(centripetal acceleration):**

$$a_r = \frac{v^2}{r} = \omega^2 r$$

속도의 **방향** 변화를 담당 (항상 중심을 향한다)

---

### 총 가속도

$$\vec{a} = \vec{a}_t + \vec{a}_r$$

$$|\vec{a}| = \sqrt{a_t^2 + a_r^2} = r\sqrt{\alpha^2 + \omega^4}$$

- 등속 원운동($\alpha = 0$)이면 $a_t = 0$, $|\vec{a}| = a_r = \omega^2 r$ (구심 가속도만)
- $\omega = 0$인 순간(출발 직후)이면 $a_r = 0$, $|\vec{a}| = a_t = \alpha r$ (접선 가속도만)

---

## 10.5 회전 운동에너지

회전하는 강체의 운동에너지는 어떻게 구할까?

강체를 질량 $m_i$, 축으로부터 거리 $r_i$인 작은 조각들로 나누자.

각 조각의 속력: $v_i = \omega r_i$

각 조각의 운동에너지: $\frac{1}{2}m_i v_i^2 = \frac{1}{2}m_i \omega^2 r_i^2$

전체 운동에너지:

$$K = \sum_i \frac{1}{2}m_i v_i^2 = \frac{1}{2}\left(\sum_i m_i r_i^2\right)\omega^2$$

---

### 관성모멘트(moment of inertia)

$$I = \sum_i m_i r_i^2$$

이 양을 **관성모멘트** 또는 **회전관성(rotational inertia)** 이라 한다.

따라서 회전 운동에너지:

$$K = \frac{1}{2}I\omega^2$$

병진 운동에너지 $K = \frac{1}{2}mv^2$에서 $m \to I$, $v \to \omega$로 바꾼 것이다!

- $I$의 단위: $\text{kg}\cdot\text{m}^2$
- $I$는 질량 분포와 **회전축의 위치** 에 의존한다

---

### 연속체의 관성모멘트

질량이 연속적으로 분포된 물체:

$$I = \int r^2\, dm$$

$r$: 회전축에서 질량 요소 $dm$까지의 수직 거리

---

### 주요 물체의 관성모멘트

<img src="/img/ch10/moment-of-inertia-table.svg" style="max-height:50vh">

---

### 평행축 정리(Parallel-axis Theorem)

질량 중심을 지나는 축에 대한 관성모멘트가 $I_\text{com}$일 때, 이와 **평행** 한 임의 축에 대한 관성모멘트:

$$I = I_\text{com} + Mh^2$$

$h$: 두 축 사이의 거리, $M$: 전체 질량

- 이 정리를 사용하면, 질량 중심의 관성모멘트만 알면 다른 평행축에 대한 관성모멘트를 바로 구할 수 있다
- 질량 중심을 지나는 축이 항상 **최소** 관성모멘트를 가진다

---

### 평행축 정리 유도

질량 중심이 원점인 좌표계에서, 질량 요소 $dm$의 위치를 $(x', y')$이라 하자.

평행축은 질량 중심에서 $(a, b)$만큼 떨어져 있으므로:

$$I = \int [(x'-a)^2 + (y'-b)^2]\, dm$$

$$= \int (x'^2 + y'^2)\, dm - 2a\int x'\, dm - 2b\int y'\, dm + (a^2+b^2)\int dm$$

질량 중심 정의에서 $\int x'\, dm = 0$, $\int y'\, dm = 0$이므로:

$$I = I_\text{com} + M(a^2 + b^2) = I_\text{com} + Mh^2$$

---

### 예제: 평행축 정리

질량 $M = 2.0$ kg, 길이 $L = 1.0$ m인 가느다란 막대.

중심을 지나는 축: $I_\text{com} = \frac{1}{12}ML^2 = \frac{1}{12}(2.0)(1.0)^2 = 0.167$ kg$\cdot$m²

끝을 지나는 축: $h = L/2 = 0.5$ m

$$I = I_\text{com} + Mh^2 = 0.167 + 2.0 \times 0.5^2 = 0.167 + 0.500 = 0.667 \text{ kg}\cdot\text{m}^2$$

확인: $\frac{1}{3}ML^2 = \frac{1}{3}(2.0)(1.0)^2 = 0.667$ kg$\cdot$m² $\checkmark$

---

## 10.6 토크

### 토크(torque)의 정의

**토크(torque)** 는 물체를 회전시키는 능력을 나타내는 양이다.

병진 운동에서 **힘** 이 가속도를 일으키듯, 회전 운동에서는 **토크** 가 각가속도를 일으킨다.

<img src="/img/ch10/torque-definition.svg" style="max-height:50vh">

---

### 토크의 크기

$$\tau = rF\sin\phi$$

여기서

- $r$: 회전축에서 힘의 작용점까지의 거리
- $F$: 힘의 크기
- $\phi$: $\vec{r}$과 $\vec{F}$ 사이의 각도

동등한 표현:

$$\tau = r \times (F\sin\phi) = r \times F_\perp$$

$$\tau = (r\sin\phi) \times F = r_\perp \times F$$

$r_\perp = r\sin\phi$를 **모멘트 팔(moment arm)** 이라 한다.

---

### 토크의 부호와 단위

- **양의 토크** ($\tau > 0$): 반시계 방향 회전을 유발
- **음의 토크** ($\tau < 0$): 시계 방향 회전을 유발
- **단위**: $\text{N}\cdot\text{m}$ (뉴턴미터)

> 주의: 토크의 단위 $\text{N}\cdot\text{m}$와 에너지의 단위 $\text{J} = \text{N}\cdot\text{m}$는 같은 차원이지만, 물리적 의미가 다르다. 토크는 J로 쓰지 않는다.

예시: 문을 열 때, 손잡이(경첩에서 먼 곳)를 밀면 쉽게 열린다. 경첩 가까이를 밀면 같은 힘으로도 토크가 작아 열기 어렵다.

---

## 10.7 회전의 뉴턴 제2법칙

$$\tau_\text{net} = I\alpha$$

**알짜 토크** 는 **관성모멘트** 와 **각가속도** 의 곱과 같다.

이것은 병진 운동의 뉴턴 제2법칙 $F_\text{net} = ma$와 정확히 같은 구조이다:

- $F \to \tau$ (힘 → 토크)
- $m \to I$ (질량 → 관성모멘트)
- $a \to \alpha$ (가속도 → 각가속도)

---

### 뉴턴 제2법칙(회전) 유도

회전축에서 $r_i$만큼 떨어진 질량 $m_i$에 접선 힘 $F_{t,i}$가 작용:

$$F_{t,i} = m_i a_{t,i} = m_i \alpha r_i$$

이 힘에 의한 토크:

$$\tau_i = r_i F_{t,i} = m_i r_i^2 \alpha$$

전체 알짜 토크:

$$\tau_\text{net} = \sum_i \tau_i = \sum_i m_i r_i^2 \alpha = \left(\sum_i m_i r_i^2\right)\alpha = I\alpha$$

---

<!-- sim:moment-of-inertia.html -->
관성모멘트와 토크 시뮬레이션

---

## 10.8 일과 회전 운동에너지

### 토크가 하는 일

일정한 토크 $\tau$가 각변위 $\Delta\theta$만큼 회전시킬 때 한 일:

$$W = \tau \Delta\theta$$

변하는 토크:

$$W = \int_{\theta_i}^{\theta_f} \tau\, d\theta$$

병진 운동에서 $W = F \cdot d$와 대응: $F \to \tau$, $d \to \theta$

---

### 일-운동에너지 정리 (회전)

$$\Delta K = K_f - K_i = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2 = W$$

토크가 한 알짜 일 = 회전 운동에너지의 변화량

유도:

$$W = \int \tau\, d\theta = \int I\alpha\, d\theta = I\int \frac{d\omega}{dt}\, d\theta$$

$$= I\int \omega\, d\omega = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2$$

---

### 회전의 일률(power)

$$P = \frac{dW}{dt} = \tau \frac{d\theta}{dt} = \tau\omega$$

병진 운동의 $P = Fv$와 대응: $F \to \tau$, $v \to \omega$

---

## Review & Summary

### 병진-회전 대응

<img src="/img/ch10/translation-rotation-comparison.svg" style="max-height:50vh">

---

### 핵심 공식

| 개념 | 공식 |
|---|---|
| 각위치 | $\theta = s/r$ (rad) |
| 각속도 | $\omega = d\theta/dt$ |
| 각가속도 | $\alpha = d\omega/dt$ |
| 선형-각 관계 | $v = \omega r$, $a_t = \alpha r$, $a_r = \omega^2 r$ |
| 관성모멘트 | $I = \sum m_i r_i^2 = \int r^2\, dm$ |
| 평행축 정리 | $I = I_\text{com} + Mh^2$ |

---

### 핵심 공식 (계속)

| 개념 | 공식 |
|---|---|
| 토크 | $\tau = rF\sin\phi$ |
| 뉴턴 제2법칙 (회전) | $\tau_\text{net} = I\alpha$ |
| 회전 운동에너지 | $K = \frac{1}{2}I\omega^2$ |
| 일 (회전) | $W = \tau\Delta\theta$ |
| 일률 (회전) | $P = \tau\omega$ |

**기억할 것:**
- 회전 운동은 병진 운동과 **완벽하게 대응** 된다
- 관성모멘트 $I$는 질량 분포와 **회전축** 에 의존한다
- 같은 물체라도 축이 바뀌면 $I$가 달라진다 (평행축 정리)
- 모든 각량은 **라디안** 단위를 사용해야 한다