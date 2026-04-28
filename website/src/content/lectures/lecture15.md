---
title: "15장: 진동"
week: 15
chapters: "15장"
topics: "단순조화운동, 에너지, 각진동수, 진자, 단순조화운동과 등속 원운동, 감쇠진동, 강제진동과 공명"
---

# 15장: 진동

Oscillations

---

## 이번 장에서 배울 내용

- **단순조화운동(simple harmonic motion, SHM)** : 자연에서 가장 기본적인 주기 운동
- **변위, 속도, 가속도** 의 시간 함수: $x(t)$, $v(t)$, $a(t)$
- **에너지 보존** : 운동에너지와 퍼텐셜에너지의 교환
- **진자(pendulum)** : 단진자와 물리 진자
- **등속 원운동과 SHM** 의 관계
- **감쇠진동(damped oscillation)** 과 **강제진동(forced oscillation)**
- **공명(resonance)** : 왜 특정 진동수에서 진폭이 폭발적으로 커지는가

---

## 진동은 어디에나 있다

우리 주변은 진동으로 가득하다.

- 스마트폰의 진동 모터, 시계의 진자
- 지진파에 의한 건물의 흔들림
- 바이올린 현의 진동이 만드는 소리
- 심장 박동의 주기적 운동, 전기 회로의 교류

모든 진동 시스템에는 **"탄성"** (복원력을 제공)과 **"관성"** (운동을 유지)이라는 두 요소가 존재한다. 이 장에서는 가장 기본적인 진동인 **단순조화운동** 을 깊이 이해한다.

---

## 15.1 단순조화운동

### 주기 운동의 기본 개념

주기적으로 반복되는 운동을 **주기 운동(periodic motion)** 이라 한다.

- **진동수(frequency)** $f$: 단위 시간당 진동 횟수. 단위는 Hz ($1\;\text{Hz} = 1\;\text{s}^{-1}$)
- **주기(period)** $T$: 한 번의 완전한 진동에 걸리는 시간

$$T = \frac{1}{f}$$

주기 운동 중에서 **사인 함수(또는 코사인 함수)** 로 기술되는 운동을 **단순조화운동(SHM)** 이라 한다.

---

### SHM의 변위 함수

SHM을 하는 입자의 위치:

$$x(t) = x_m \cos(\omega t + \phi)$$

- $x_m$: **진폭(amplitude)** — 평형 위치에서 최대 변위까지의 거리 (항상 양수)
- $\omega$: **각진동수(angular frequency)** — 단위 rad/s
- $\phi$: **위상 상수(phase constant)** — 초기 조건에 의해 결정
- $\omega t + \phi$: **위상(phase)**

---

### 각진동수, 주기, 진동수의 관계

한 주기 $T$ 동안 위상이 $2\pi$ 변하므로:

$$\omega T = 2\pi$$

$$\omega = \frac{2\pi}{T} = 2\pi f$$

| 물리량 | 기호 | 단위 | 관계 |
|---|---|---|---|
| 주기 | $T$ | s | $T = 1/f = 2\pi/\omega$ |
| 진동수 | $f$ | Hz | $f = 1/T = \omega/2\pi$ |
| 각진동수 | $\omega$ | rad/s | $\omega = 2\pi f = 2\pi/T$ |

---

### SHM의 속도

$x(t)$를 시간에 대해 미분하면:

$$v(t) = \frac{dx}{dt} = -\omega x_m \sin(\omega t + \phi)$$

- **속도 진폭(velocity amplitude)** : $v_m = \omega x_m$
- $x = 0$ (평형점)에서 속력이 최대: $|v| = \omega x_m$
- $x = \pm x_m$ (양 끝)에서 속력이 0

---

### SHM의 가속도

$v(t)$를 다시 미분하면:

$$a(t) = \frac{dv}{dt} = -\omega^2 x_m \cos(\omega t + \phi)$$

- **가속도 진폭(acceleration amplitude)** : $a_m = \omega^2 x_m$
- 가속도와 변위의 관계:

$$\boxed{a(t) = -\omega^2 x(t)}$$

이것이 **SHM의 핵심 특징** 이다: 가속도가 변위에 비례하고 방향이 반대!

---

### x(t), v(t), a(t) 그래프

<img src="/img/ch15/xva-graphs.svg" style="max-height:55vh">

세 그래프는 90°(=$T/4$) 위상씩 어긋나며, 진폭은 각각 $x_m$, $\omega x_m$, $\omega^2 x_m$.

---

### 용수철-질량 계: SHM의 대표적 예

<img src="/img/ch15/spring-mass.svg" style="max-height:50vh">

---

### 훅 법칙과 SHM

질량 $m$인 물체에 용수철 상수 $k$인 용수철이 연결되어 있을 때:

$$F = -kx \quad \text{(훅 법칙)}$$

뉴턴 제2법칙 $F = ma$에서:

$$ma = -kx \implies a = -\frac{k}{m}x$$

SHM 조건 $a = -\omega^2 x$와 비교하면 $\omega^2 = k/m$이므로:

$$\boxed{\omega = \sqrt{\frac{k}{m}}}$$

$$\boxed{T = 2\pi\sqrt{\frac{m}{k}}}$$

---

### 주기의 물리적 의미

$$T = 2\pi\sqrt{\frac{m}{k}}$$

- $k$가 크면 (빳빳한 용수철) → $T$ 감소 → 빠른 진동
- $m$이 크면 (무거운 물체) → $T$ 증가 → 느린 진동
- **진폭 $x_m$에 무관** — 진폭이 커져도 주기는 같다! (SHM의 등시성)

모든 진동계에는 **"탄성" 요소** (에너지를 저장하는 용수철 역할)와 **"관성" 요소** (운동에너지를 저장하는 질량 역할)가 있다.

---

### 위상 상수의 결정

초기 조건 $x(0) = x_0$, $v(0) = v_0$에서:

$$x_0 = x_m\cos\phi, \quad v_0 = -\omega x_m\sin\phi$$

이 두 식을 나누면:

$$\tan\phi = -\frac{v_0}{\omega x_0}$$

진폭은:

$$x_m = \sqrt{x_0^2 + \left(\frac{v_0}{\omega}\right)^2}$$

---

### 예제: SHM의 기본량 구하기

용수철 상수 $k = 200\;\text{N/m}$에 질량 $m = 0.50\;\text{kg}$인 물체가 매달려 있다. 진폭 $x_m = 0.10\;\text{m}$으로 진동할 때:

$$\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{200}{0.50}} = 20\;\text{rad/s}$$

$$T = \frac{2\pi}{\omega} = \frac{2\pi}{20} = 0.314\;\text{s}, \quad f = \frac{1}{T} = 3.18\;\text{Hz}$$

최대 속력: $v_m = \omega x_m = 20 \times 0.10 = 2.0\;\text{m/s}$

최대 가속도: $a_m = \omega^2 x_m = 400 \times 0.10 = 40\;\text{m/s}^2$

---

## 15.2 단순조화운동의 에너지

### 에너지의 교환

<img src="/img/ch15/energy-vs-position.svg" style="max-height:50vh">

---

### 운동에너지와 퍼텐셜에너지

**퍼텐셜에너지(elastic potential energy)** :

$$U(t) = \frac{1}{2}kx^2 = \frac{1}{2}kx_m^2\cos^2(\omega t + \phi)$$

**운동에너지(kinetic energy)** :

$$K(t) = \frac{1}{2}mv^2 = \frac{1}{2}m\omega^2 x_m^2\sin^2(\omega t + \phi) = \frac{1}{2}kx_m^2\sin^2(\omega t + \phi)$$

(여기서 $m\omega^2 = k$를 사용했다.)

---

### 역학적 에너지 보존

$$E = K + U = \frac{1}{2}kx_m^2\sin^2(\omega t + \phi) + \frac{1}{2}kx_m^2\cos^2(\omega t + \phi)$$

$$= \frac{1}{2}kx_m^2[\sin^2(\omega t + \phi) + \cos^2(\omega t + \phi)]$$

$$\boxed{E = \frac{1}{2}kx_m^2 = \text{일정}}$$

- $x = 0$에서: $K = E$ (모두 운동에너지), $U = 0$
- $x = \pm x_m$에서: $U = E$ (모두 퍼텐셜에너지), $K = 0$

에너지가 운동에너지와 퍼텐셜에너지 사이를 끊임없이 교환하지만, **전체 역학적 에너지는 보존** 된다.

---

### 속력과 변위의 관계

에너지 보존 $\frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \frac{1}{2}kx_m^2$에서:

$$v = \pm\omega\sqrt{x_m^2 - x^2}$$

이 관계를 사용하면 임의의 위치 $x$에서의 속력을 바로 구할 수 있다.

---

## 15.3 각 단순조화진동자

### 비틀림 진자

**비틀림 진자(torsion pendulum)** : 와이어에 매달린 원판이 비틀림으로 진동

복원 돌림힘:

$$\tau = -\kappa\theta$$

여기서 $\kappa$는 **비틀림 상수(torsion constant)** 이다.

훅 법칙 $F = -kx$와 같은 구조! ($x \to \theta$, $k \to \kappa$, $m \to I$)

$$\boxed{T = 2\pi\sqrt{\frac{I}{\kappa}}}$$

$I$는 회전축에 대한 관성 모멘트이다.

---

## 15.4 진자

### 단진자

<img src="/img/ch15/pendulum-geometry.svg" style="max-height:50vh">

---

### 단진자의 주기 유도

길이 $L$, 질량 $m$인 단진자. 피벗에 대한 복원 돌림힘:

$$\tau = -L(mg\sin\theta)$$

회전의 뉴턴 제2법칙 $\tau = I\alpha$에서 ($I = mL^2$):

$$-mgL\sin\theta = mL^2\alpha \implies \alpha = -\frac{g}{L}\sin\theta$$

**작은 각도 근사** ($\sin\theta \approx \theta$, $\theta$는 rad 단위):

$$\alpha \approx -\frac{g}{L}\theta$$

이것은 $a = -\omega^2 x$ 형태! 따라서 SHM이며:

$$\omega = \sqrt{\frac{g}{L}}, \quad \boxed{T = 2\pi\sqrt{\frac{L}{g}}}$$

---

### 단진자의 핵심 특징

$$T = 2\pi\sqrt{\frac{L}{g}}$$

- 주기는 **줄의 길이 $L$** 에만 의존
- **질량 $m$에 무관** — 무거운 추나 가벼운 추나 같은 주기!
- **진폭에 무관** (작은 각도 범위에서)
- $g$를 정밀하게 측정하는 데 사용 가능: $g = 4\pi^2 L / T^2$

갈릴레오가 피사 대성당의 샹들리에 진동을 관찰하고 이 성질을 발견했다고 전해진다.

---

### 물리 진자

**물리 진자(physical pendulum)** : 임의의 형태를 가진 강체 진자

피벗 O에서 질량 중심까지의 거리를 $h$라 하면:

$$\tau = -mgh\sin\theta$$

$\tau = I\alpha$에서 ($I$는 피벗에 대한 관성 모멘트):

$$\alpha = -\frac{mgh}{I}\sin\theta \approx -\frac{mgh}{I}\theta$$

$$\boxed{T = 2\pi\sqrt{\frac{I}{mgh}}}$$

단진자와 비교: $I = mL^2$, $h = L$을 대입하면 $T = 2\pi\sqrt{L/g}$로 환원된다.

---

### 예제: 막대의 진동

길이 $L$의 균일한 막대를 한쪽 끝에서 매달아 진동시키면:

$$I = \frac{1}{3}mL^2 \quad (\text{한쪽 끝 기준}), \quad h = \frac{L}{2}$$

$$T = 2\pi\sqrt{\frac{I}{mgh}} = 2\pi\sqrt{\frac{\frac{1}{3}mL^2}{mg\cdot\frac{L}{2}}} = 2\pi\sqrt{\frac{2L}{3g}}$$

$L = 1.00$ m일 때: $T = 2\pi\sqrt{\frac{2(1.00)}{3(9.80)}} = 1.64\;\text{s}$

---

## 15.5 단순조화운동과 등속 원운동

### SHM은 원운동의 투영이다

<img src="/img/ch15/reference-circle.svg" style="max-height:50vh">

---

### 원운동과 SHM의 대응

반지름 $x_m$인 원 위에서 각속도 $\omega$로 등속 원운동하는 입자 P'을 생각하자.

시각 $t$에서의 각도: $\omega t + \phi$

P'의 **$x$축 투영** :

$$x(t) = x_m \cos(\omega t + \phi)$$

이것은 정확히 SHM의 변위 함수이다!

마찬가지로:
- 속도의 $x$축 투영: $v(t) = -\omega x_m \sin(\omega t + \phi)$
- 구심 가속도의 $x$축 투영: $a(t) = -\omega^2 x_m \cos(\omega t + \phi)$

**SHM은 등속 원운동을 직경 위에 투영한 것이다.**

---

<!-- sim:shm-spring.html -->
용수철-질량 SHM 시뮬레이션

---

<!-- sim:oscillation-shm.html -->
단순조화운동 시뮬레이션

---

## 15.6 감쇠 단순조화운동

### 감쇠력

현실의 진동은 마찰이나 공기 저항 때문에 점차 줄어든다. 이를 **감쇠진동(damped oscillation)** 이라 한다.

감쇠력이 속도에 비례한다고 가정하면:

$$F_d = -bv$$

여기서 $b$는 **감쇠 상수(damping constant)** 이다.

---

### 감쇠진동의 운동 방정식

뉴턴 제2법칙: $-kx - bv = ma$

$$m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = 0$$

이 미분방정식의 해 ($b < 2\sqrt{km}$인 **약감쇠** 의 경우):

$$\boxed{x(t) = x_m e^{-bt/2m}\cos(\omega' t + \phi)}$$

---

### 감쇠진동의 각진동수와 에너지

감쇠 진동의 각진동수:

$$\omega' = \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}}$$

- $b = 0$이면 $\omega' = \omega_0 = \sqrt{k/m}$ (비감쇠)
- $b$가 커지면 $\omega'$이 감소 (진동이 느려짐)
- $b = 2\sqrt{km}$이면 **임계 감쇠(critical damping)** — 진동 없이 평형으로 복귀

감쇠가 작을 때 ($b \ll \sqrt{km}$) 역학적 에너지:

$$\boxed{E(t) \approx \frac{1}{2}kx_m^2 e^{-bt/m}}$$

에너지가 지수적으로 감소한다.

---

### 감쇠 진동의 시각화

<img src="/img/ch15/damped-envelope.svg" style="max-height:50vh">

---

<!-- sim:damped-oscillation.html -->
감쇠진동 시뮬레이션

---

## 15.7 강제진동과 공명

### 강제진동

감쇠 진동계에 외부에서 주기적 힘을 가하면:

$$F_\text{ext} = F_0 \cos(\omega_d t)$$

여기서 $\omega_d$는 **구동 각진동수(driving angular frequency)** 이다.

충분한 시간이 지나면 계는 **구동 진동수** 로 진동한다 (고유 진동수가 아니라!):

$$x(t) = A\cos(\omega_d t + \phi')$$

---

### 공명

<img src="/img/ch15/resonance-curve.svg" style="max-height:50vh">

진폭 $A$는 $\omega_d$에 의존한다. $\omega_d$가 계의 고유 진동수 $\omega_0 = \sqrt{k/m}$에 가까워지면 진폭이 급격히 증가한다.

$$\omega_d \approx \omega_0 \quad \Rightarrow \quad \text{진폭 최대!}$$

이것이 **공명(resonance)** 이다.

감쇠가 작을수록:
- 공명 peak가 **더 높고 날카로워진다**
- 공명 진동수에서의 진폭이 매우 커질 수 있다

---

### 공명의 실생활 예시

- **다리의 공명** : 1940년 타코마 내로우즈 다리(Tacoma Narrows Bridge)가 바람에 의한 공명으로 붕괴
- **건물의 내진 설계** : 지진파의 진동수가 건물의 고유 진동수와 일치하지 않도록 설계. 1985년 멕시코시티 지진에서 중층 건물이 공명으로 집중 붕괴
- **악기** : 현의 고유 진동수에서 공명하여 소리 증폭
- **MRI** : 자기장에서 수소 원자핵의 공명 진동을 이용
- **전자레인지** : 물 분자의 고유 진동수(~2.45 GHz)에 맞춘 마이크로파

---

## Review & Summary

### 핵심 개념

| 개념 | 공식 |
|---|---|
| SHM 변위 | $x(t) = x_m \cos(\omega t + \phi)$ |
| SHM 속도 | $v(t) = -\omega x_m \sin(\omega t + \phi)$ |
| SHM 가속도 | $a(t) = -\omega^2 x(t)$ |
| 용수철 각진동수 | $\omega = \sqrt{k/m}$ |
| 용수철 주기 | $T = 2\pi\sqrt{m/k}$ |
| 역학적 에너지 | $E = \frac{1}{2}kx_m^2$ |

---

### 핵심 개념 (계속)

| 개념 | 공식 |
|---|---|
| 단진자 주기 | $T = 2\pi\sqrt{L/g}$ |
| 물리 진자 주기 | $T = 2\pi\sqrt{I/(mgh)}$ |
| 비틀림 진자 주기 | $T = 2\pi\sqrt{I/\kappa}$ |
| 감쇠 진동 | $x(t) = x_m e^{-bt/2m}\cos(\omega' t + \phi)$ |
| 감쇠 에너지 | $E(t) \approx \frac{1}{2}kx_m^2 e^{-bt/m}$ |
| 공명 조건 | $\omega_d \approx \omega_0$ |

**기억할 것:**

- SHM에서 가속도는 변위에 비례, 방향 반대: $a = -\omega^2 x$
- 에너지는 $K$와 $U$ 사이를 교환하지만, 전체는 보존
- 단진자 주기는 **질량과 무관** , 길이에만 의존
- 감쇠는 진폭을 지수적으로 감소시키고, 공명은 진폭을 극대화한다
