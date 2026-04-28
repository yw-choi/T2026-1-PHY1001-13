---
title: "16장: 파동 I"
week: 16
chapters: "16장"
topics: "횡파와 종파, 파장과 진동수, 파동의 속력, 파동 방정식, 중첩 원리, 파동의 간섭, 위상자, 정상파와 공명"
---

# 16장: 파동 I

Waves. I

---

## 이번 장에서 배울 내용

- **횡파(transverse wave)** 와 **종파(longitudinal wave)** 의 구분
- **파장(wavelength)** , **진동수(frequency)** , **주기(period)** 의 관계
- 줄 위의 **파동 속력(wave speed)** : $v = \sqrt{\tau/\mu}$
- **파동 방정식(wave equation)** 유도
- **중첩 원리(superposition principle)** 와 **간섭(interference)**
- **위상자(phasor)** 를 이용한 파동 합성
- **정상파(standing wave)** 와 **공명(resonance)**

---

## 16.1 횡파와 종파

### 파동이란?

파동은 매질을 통해 에너지와 정보를 전달하는 교란이다.

파동의 네 가지 유형:

- **역학파(mechanical wave)** : 물결, 소리, 지진파. 매질이 필요하다
- **전자기파(electromagnetic wave)** : 빛, 전파, X선. 진공에서도 전파
- **물질파(matter wave)** : 전자, 양성자 등의 파동성
- **중력파(gravitational wave)** : 시공간의 파동 (2015년 LIGO에서 최초 검출)

이 장에서는 주로 **역학파** 를 다룬다.

---

### 횡파와 종파

<img src="/img/ch16/transverse-longitudinal.svg" style="max-height:50vh">

**횡파(transverse wave)** : 매질의 진동 방향이 파동의 전파 방향에 **수직**

- 예: 줄 위의 파동, 전자기파

**종파(longitudinal wave)** : 매질의 진동 방향이 파동의 전파 방향에 **평행**

- 예: 소리(음파), 스프링 위의 파동

핵심: 이동하는 것은 **파동의 형태(wave form)** 이지, 매질 자체가 아니다!

---

## 16.2 파장과 진동수

### 사인파의 수학적 표현

$+x$ 방향으로 진행하는 사인파:

$$y(x, t) = y_m \sin(kx - \omega t)$$

- $y$: 변위 (줄 위 입자의 평형 위치로부터의 이탈)
- $y_m$: **진폭(amplitude)**. 최대 변위의 크기
- $kx - \omega t$: **위상(phase)**
- $k$: **각파수(angular wave number)**
- $\omega$: **각진동수(angular frequency)**

---

### 파동의 매개변수

<img src="/img/ch16/wave-parameters.svg" style="max-height:50vh">

---

### 파장과 각파수

**파장(wavelength)** $\lambda$: 파동의 한 주기에 해당하는 공간적 거리

사인 함수의 주기 조건: $y_m \sin(kx) = y_m \sin(k(x + \lambda))$

이 조건이 성립하려면 $k\lambda = 2\pi$이므로:

$$\boxed{k = \frac{2\pi}{\lambda}} \quad \text{(각파수, 단위: rad/m)}$$

---

### 주기, 진동수, 각진동수

고정된 위치 $x = 0$에서 변위를 시간의 함수로 보면:

$$y(0, t) = y_m \sin(-\omega t) = -y_m \sin(\omega t)$$

매질의 한 원소가 완전한 진동 한 번을 마치는 시간이 **주기(period)** $T$이다.

$\omega T = 2\pi$이므로:

$$\boxed{\omega = \frac{2\pi}{T}} \quad \text{(각진동수, 단위: rad/s)}$$

**진동수(frequency)** $f$:

$$\boxed{f = \frac{1}{T} = \frac{\omega}{2\pi}} \quad \text{(단위: Hz)}$$

---

### 파동의 속력

파동의 위상이 일정한 점을 추적하면:

$$kx - \omega t = \text{상수}$$

시간 미분하면:

$$k\frac{dx}{dt} - \omega = 0$$

$$\boxed{v = \frac{dx}{dt} = \frac{\omega}{k} = \frac{\lambda}{T} = \lambda f} \quad \text{(파동 속력)}$$

물리적 의미: 파동은 한 주기 동안 파장 하나만큼 이동한다.

---

### 위상 상수와 진행 방향

일반적인 사인파:

$$y(x, t) = y_m \sin(kx - \omega t + \phi)$$

- $\phi$: **위상 상수(phase constant)**. $t = 0$, $x = 0$에서의 초기 위상 결정

진행 방향:

- $y = y_m \sin(kx - \omega t)$: **$+x$ 방향** 으로 진행
- $y = y_m \sin(kx + \omega t)$: **$-x$ 방향** 으로 진행

기억법: $kx$와 $\omega t$ 부호가 **반대** 이면 $+x$ 방향, **같으면** $-x$ 방향

---

### 줄 원소의 횡속도와 횡가속도

위치 $x$가 고정된 줄 원소의 **횡속도(transverse velocity)** :

$$u = \frac{\partial y}{\partial t} = -\omega y_m \cos(kx - \omega t)$$

- $u$의 최댓값: $u_\text{max} = \omega y_m$ (진폭 $\times$ 각진동수)

**횡가속도(transverse acceleration)** :

$$a_y = \frac{\partial u}{\partial t} = -\omega^2 y_m \sin(kx - \omega t) = -\omega^2 y$$

이것은 단순 조화 운동의 가속도와 같은 형태다! 줄의 각 원소는 SHM을 한다.

---

## 16.3 줄 위의 파동 속력

### 파동 속력은 무엇에 의해 결정되는가?

파동 속력은 파동의 성질(진동수, 진폭)이 아니라 **매질의 성질** 에 의해 결정된다.

줄(string)의 경우, 관련 물리량:

- **장력(tension)** $\tau$: 차원 $MLT^{-2}$
- **선밀도(linear density)** $\mu = m/L$: 차원 $ML^{-1}$

차원 분석으로 속력($LT^{-1}$)을 만들면:

$$v = C\sqrt{\frac{\tau}{\mu}}$$

정밀한 유도로 $C = 1$을 보일 수 있다.

---

### 뉴턴 제2법칙을 이용한 유도

<img src="/img/ch16/wave-speed-string.svg" style="max-height:50vh">

대칭적인 펄스가 속력 $v$로 이동하는 기준계를 생각하자.

펄스 꼭대기의 작은 줄 원소 $\Delta l$은 반지름 $R$인 원호를 따라 움직인다.

- 복원력: $F = 2\tau\sin\theta \approx \tau \frac{\Delta l}{R}$ (작은 각도 근사)
- 질량: $\Delta m = \mu \Delta l$
- 구심 가속도: $a = \frac{v^2}{R}$

뉴턴 제2법칙 $F = \Delta m \cdot a$:

$$\tau \frac{\Delta l}{R} = \mu \Delta l \cdot \frac{v^2}{R}$$

$$\boxed{v = \sqrt{\frac{\tau}{\mu}}}$$

핵심: 줄 위의 파동 속력은 **장력과 선밀도에만** 의존하며, 진동수나 진폭에는 무관하다.

---

### 주의: 파동 속력 vs 횡속도

혼동하지 말 것!

| | 파동 속력 $v$ | 횡속도 $u$ |
|---|---|---|
| 방향 | 파동 전파 방향 ($x$축) | 매질 진동 방향 ($y$축) |
| 크기 | $v = \omega/k = \lambda f$ | $u_\text{max} = \omega y_m$ |
| 특징 | 일정 (매질에 의해 결정) | 시간에 따라 변함 |

---

## 16.4 파동이 전달하는 에너지

### 에너지 전달률 (파워)

줄 위의 사인파는 운동에너지와 탄성 퍼텐셜에너지를 전달한다.

질량 $dm$인 줄 원소의 운동에너지:

$$dK = \frac{1}{2}dm \cdot u^2 = \frac{1}{2}\mu\,dx \cdot \omega^2 y_m^2 \cos^2(kx - \omega t)$$

운동에너지의 시간 전달률:

$$\frac{dK}{dt} = \frac{1}{2}\mu v \omega^2 y_m^2 \cos^2(kx - \omega t)$$

---

### 평균 파워

$\cos^2$의 평균값은 $\frac{1}{2}$이므로, 운동에너지의 평균 전달률:

$$\left(\frac{dK}{dt}\right)_\text{avg} = \frac{1}{4}\mu v \omega^2 y_m^2$$

탄성 퍼텐셜에너지도 같은 비율로 전달되므로, **총 평균 파워** :

$$\boxed{P_\text{avg} = \frac{1}{2}\mu v \omega^2 y_m^2}$$

- $\mu$, $v$: 매질의 성질
- $\omega$, $y_m$: 파동의 성질
- 파워는 **진폭의 제곱** 과 **진동수의 제곱** 에 비례한다. 모든 파동에 공통된 결과

---

## 16.5 파동 방정식

### 줄 원소에 대한 뉴턴 제2법칙

횡파가 지나가는 줄의 작은 원소 $dx$를 생각하자.

원소의 양 끝에 작용하는 장력의 $y$ 성분의 차이가 알짜력을 만든다:

$$F_{2y} - F_{1y} = dm \cdot a_y$$

장력의 $y$ 성분은 줄의 기울기 $S = \partial y/\partial x$에 비례하므로:

$$\tau S_2 - \tau S_1 = \mu\,dx \cdot \frac{\partial^2 y}{\partial t^2}$$

양변을 정리하면:

$$\frac{S_2 - S_1}{dx} = \frac{\mu}{\tau}\frac{\partial^2 y}{\partial t^2}$$

---

### 파동 방정식

좌변은 기울기의 변화율, 즉 $\partial^2 y/\partial x^2$이므로:

$$\frac{\partial^2 y}{\partial x^2} = \frac{\mu}{\tau}\frac{\partial^2 y}{\partial t^2}$$

$v = \sqrt{\tau/\mu}$를 대입하면:

$$\boxed{\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}} \quad \text{(파동 방정식)}$$

이것은 모든 종류의 파동을 지배하는 일반적인 미분 방정식이다.

$y(x, t) = y_m \sin(kx - \omega t)$가 이 방정식의 해임을 확인할 수 있다:

- 좌변: $-k^2 y_m \sin(kx - \omega t)$
- 우변: $\frac{1}{v^2}(-\omega^2) y_m \sin(kx - \omega t) = -\frac{\omega^2}{v^2} y_m \sin(kx - \omega t)$
- $k^2 = \omega^2/v^2$ $\checkmark$ ($v = \omega/k$이므로 성립)

---

<!-- sim:wave-propagation.html -->
파동 전파 시뮬레이션

---

## 16.6 중첩 원리

### 파동의 중첩

같은 매질을 동시에 통과하는 두 파동이 있을 때:

$$y'(x, t) = y_1(x, t) + y_2(x, t)$$

**중첩 원리(principle of superposition)** : 겹치는 파동들의 합성 변위는 개별 변위의 **대수적 합** 이다.

핵심 성질:

- 겹치는 파동들은 서로의 진행을 방해하지 않는다
- 관찰되는 것은 합성파(resultant wave)이다

---

## 16.7 파동의 간섭

### 같은 방향 진행파의 간섭

같은 진폭, 같은 파장, 같은 방향의 두 사인파가 위상차 $\phi$만큼 어긋나 있을 때:

$$y_1 = y_m \sin(kx - \omega t)$$

$$y_2 = y_m \sin(kx - \omega t + \phi)$$

삼각함수 합공식 $\sin\alpha + \sin\beta = 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$를 적용하면:

$$\boxed{y'(x, t) = \left[2y_m \cos\frac{\phi}{2}\right] \sin\left(kx - \omega t + \frac{\phi}{2}\right)}$$

---

### 합성파의 진폭

$$y'_m = \left|2y_m \cos\frac{\phi}{2}\right|$$

<img src="/img/ch16/wave-superposition.svg" style="max-height:50vh">

---

### 간섭의 종류

| 위상차 $\phi$ | 파장 단위 | 합성 진폭 $y'_m$ | 간섭 종류 |
|---|---|---|---|
| $0$ | 0 | $2y_m$ | **완전 보강(fully constructive)** |
| $\frac{2}{3}\pi$ | 0.33 | $y_m$ | 중간(intermediate) |
| $\pi$ | 0.50 | $0$ | **완전 상쇄(fully destructive)** |
| $\frac{4}{3}\pi$ | 0.67 | $y_m$ | 중간 |
| $2\pi$ | 1.00 | $2y_m$ | 완전 보강 |

- $\phi = 0$: 두 파가 같은 위상 → 진폭이 두 배
- $\phi = \pi$ (반파장 차이): 두 파가 반대 위상 → 완전 상쇄
- 위상차의 정수 부분($2\pi$의 배수)은 무시해도 된다 → **소수 부분** 만 본다

---

## 16.8 위상자

### 위상자란?

**위상자(phasor)** : 파동을 나타내는 회전 벡터

- 크기 = 파동의 진폭 $y_m$
- 원점 주위로 각속도 $\omega$로 회전
- $y$축 위의 정사영이 해당 시각의 변위

<img src="/img/ch16/phasor-addition.svg" style="max-height:50vh">

---

### 위상자를 이용한 파동 합성

두 파동의 합성을 벡터 덧셈으로 구할 수 있다:

- 위상자 1: 크기 $y_{m1}$
- 위상자 2: 크기 $y_{m2}$, 위상자 1과 $\phi$만큼 각도 차이

합성 위상자:

- 크기 $y'_m$: 두 위상자의 벡터합의 크기
- 위상 $\beta$: 합성 위상자의 각도

같은 진폭($y_{m1} = y_{m2} = y_m$)일 때:

$$y'_m = \left|2y_m \cos\frac{\phi}{2}\right|$$

위상자 방법은 진폭이 다른 파동의 합성에도 사용할 수 있다. 삼각함수보다 훨씬 편리하다.

---

## 16.9 정상파

### 반대 방향으로 진행하는 두 파의 중첩

같은 진폭, 파장, 진동수를 가진 두 파가 **반대 방향** 으로 진행하면:

$$y_1 = y_m \sin(kx - \omega t), \quad y_2 = y_m \sin(kx + \omega t)$$

중첩하면:

$$y' = y_1 + y_2 = y_m[\sin(kx - \omega t) + \sin(kx + \omega t)]$$

합공식 적용:

$$\boxed{y'(x, t) = [2y_m \sin kx]\cos\omega t}$$

---

### 정상파의 특징

$$y'(x, t) = [2y_m \sin kx]\cos\omega t$$

이것은 **진행파가 아니다**. $kx \pm \omega t$ 형태가 아니기 때문이다.

- $2y_m \sin kx$: **진폭** 이 위치 $x$에 따라 변한다
- $\cos\omega t$: 모든 점이 **같은 위상** 으로 진동한다

**마디(node)** : 진폭이 항상 0인 점

$$\sin kx = 0 \implies kx = n\pi \quad (n = 0, 1, 2, \ldots)$$

$$x = n\frac{\lambda}{2} \quad (n = 0, 1, 2, \ldots)$$

**배(antinode)** : 진폭이 최대인 점

$$|\sin kx| = 1 \implies kx = \left(n + \frac{1}{2}\right)\pi$$

$$x = \left(n + \frac{1}{2}\right)\frac{\lambda}{2} \quad (n = 0, 1, 2, \ldots)$$

---

### 마디와 배의 간격

인접한 마디 사이의 거리:

$$\Delta x_\text{node} = \frac{\lambda}{2}$$

인접한 배 사이의 거리:

$$\Delta x_\text{antinode} = \frac{\lambda}{2}$$

마디와 인접한 배 사이의 거리:

$$\frac{\lambda}{4}$$

---

### 경계에서의 반사

줄의 끝이 고정된 벽에 연결되어 있으면 (**고정 끝**):

- 입사 펄스가 **반전** 되어 돌아온다 (위상 $\pi$ 변화)
- 고정점은 항상 마디가 된다

줄의 끝이 자유롭게 움직일 수 있으면 (**자유 끝**):

- 입사 펄스가 **같은 방향** 으로 돌아온다 (위상 변화 없음)
- 자유 끝은 항상 배가 된다

고정 끝에서 반사된 파동과 입사 파동이 중첩되어 정상파를 형성한다.

---

## 16.10 정상파와 공명

### 양 끝이 고정된 줄

<img src="/img/ch16/standing-wave-modes.svg" style="max-height:50vh">

---

### 공명 조건

양 끝이 고정된 줄(길이 $L$)에서 정상파가 존재하려면, 양 끝이 모두 마디여야 한다.

마디 사이 간격이 $\lambda/2$이므로:

$$L = n\frac{\lambda}{2} \quad (n = 1, 2, 3, \ldots)$$

따라서 허용되는 파장:

$$\boxed{\lambda_n = \frac{2L}{n}} \quad (n = 1, 2, 3, \ldots)$$

대응하는 **공명 진동수(resonance frequency)** :

$$f_n = \frac{v}{\lambda_n} = n\frac{v}{2L}$$

$$\boxed{f_n = \frac{n}{2L}\sqrt{\frac{\tau}{\mu}}} \quad (n = 1, 2, 3, \ldots)$$

---

### 배음과 배음렬

- $n = 1$: **기본 진동수(fundamental frequency)** $f_1 = \frac{v}{2L}$. 1차 조화파
- $n = 2$: **2차 조화파(2nd harmonic)** $f_2 = 2f_1$. 1차 배음(overtone)
- $n = 3$: **3차 조화파(3rd harmonic)** $f_3 = 3f_1$. 2차 배음
- 일반: $n$차 조화파 $f_n = nf_1$

기타줄을 예로 들면:

- 줄의 장력을 높이면 → $v$ 증가 → 모든 $f_n$ 증가 (음이 높아진다)
- 줄의 길이를 짧게 하면(프렛을 누르면) → $L$ 감소 → $f_n$ 증가
- 굵은 줄($\mu$ 큼) → $v$ 감소 → $f_n$ 감소 (낮은 음)

---

### 예제: 기타줄의 공명

기타줄의 길이 $L = 0.65$ m, 선밀도 $\mu = 1.0 \times 10^{-3}$ kg/m, 장력 $\tau = 80$ N

파동 속력:

$$v = \sqrt{\frac{\tau}{\mu}} = \sqrt{\frac{80}{1.0 \times 10^{-3}}} = \sqrt{80000} = 283\;\text{m/s}$$

기본 진동수:

$$f_1 = \frac{v}{2L} = \frac{283}{2 \times 0.65} = 218\;\text{Hz}$$

2차 조화파: $f_2 = 2 \times 218 = 436$ Hz

3차 조화파: $f_3 = 3 \times 218 = 653$ Hz

---

<!-- sim:standing-wave.html -->
정상파와 공명 시뮬레이션

---

## Review & Summary

### 핵심 개념

| 개념 | 공식 |
|---|---|
| 사인파 | $y(x, t) = y_m \sin(kx - \omega t + \phi)$ |
| 각파수 | $k = 2\pi/\lambda$ |
| 각진동수 | $\omega = 2\pi/T = 2\pi f$ |
| 파동 속력 | $v = \omega/k = \lambda f$ |
| 줄 위의 파동 속력 | $v = \sqrt{\tau/\mu}$ |
| 평균 파워 | $P_\text{avg} = \frac{1}{2}\mu v \omega^2 y_m^2$ |

---

### 핵심 개념 (계속)

| 개념 | 공식 |
|---|---|
| 파동 방정식 | $\dfrac{\partial^2 y}{\partial x^2} = \dfrac{1}{v^2}\dfrac{\partial^2 y}{\partial t^2}$ |
| 간섭 (같은 진폭) | $y'_m = \|2y_m \cos(\phi/2)\|$ |
| 정상파 | $y' = [2y_m \sin kx]\cos\omega t$ |
| 공명 진동수 | $f_n = n\dfrac{v}{2L} = \dfrac{n}{2L}\sqrt{\dfrac{\tau}{\mu}}$ |

**기억할 것:**

- 파동 속력은 **매질** 에 의해 결정된다 (줄: 장력과 선밀도)
- 파워는 **진폭의 제곱** 과 **진동수의 제곱** 에 비례한다
- 중첩 원리: 파동은 **대수적으로 더해진다**
- 정상파의 **마디** 에서는 항상 변위 = 0, **배** 에서 진폭 최대
- 양 끝 고정 줄의 공명: $f_n = nf_1$ (정수배 진동수만 허용)
