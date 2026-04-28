---
title: "11장: 구름 운동, 돌림힘, 각운동량"
week: 11
chapters: "11장"
topics: "구름 운동, 돌림힘 벡터, 각운동량, 각운동량 보존, 세차운동"
---

# 11장: 구름 운동, 돌림힘, 각운동량

Rolling, Torque, and Angular Momentum

---

## 이번 장에서 배울 내용

- **구름 운동(rolling)**: 병진 + 회전의 결합
- **구름 운동의 에너지** 와 빗면 위의 구름 운동
- **돌림힘 벡터(torque vector)**: $\vec{\tau} = \vec{r} \times \vec{F}$
- **각운동량(angular momentum)**: $\vec{\ell} = \vec{r} \times \vec{p}$, $\vec{L} = I\vec{\omega}$
- **각운동량 보존**: 피겨 스케이팅, 다이빙
- **세차운동(precession)**: 자이로스코프

---

## 11.1 구름 운동

### 구름 = 병진 + 회전

자전거 바퀴, 볼링공, 축구공 — 일상에서 흔히 보는 운동이다.

**구름 운동(rolling)** 은 **순수 병진(translation)** 과 **순수 회전(rotation)** 의 결합이다.

<img src="/img/ch11/rolling-combination.svg" style="max-height:50vh">

---

### 구름 조건

미끄러짐 없는 구름 운동의 핵심 조건:

$$v_\text{com} = \omega R$$

여기서 $v_\text{com}$은 질량 중심의 속력, $\omega$는 각속력, $R$은 반지름이다.

**물리적 의미:** 접촉점의 속도가 0이다!

- 접촉점 (바닥): $v_\text{com} - \omega R = 0$
- 꼭대기: $v_\text{com} + \omega R = 2v_\text{com}$

양변을 시간 미분하면 가속도 관계도 얻는다:

$$a_\text{com} = \alpha R$$

---

### 구름 운동의 운동에너지

구름 운동의 전체 운동에너지:

$$K = \frac{1}{2}I_\text{com}\omega^2 + \frac{1}{2}Mv_\text{com}^2$$

- 첫째 항: **회전 운동에너지** (질량 중심 둘레의 회전)
- 둘째 항: **병진 운동에너지** (질량 중심의 이동)

$v_\text{com} = \omega R$을 대입하면:

$$K = \frac{1}{2}I_\text{com}\frac{v_\text{com}^2}{R^2} + \frac{1}{2}Mv_\text{com}^2 = \frac{1}{2}\left(\frac{I_\text{com}}{R^2} + M\right)v_\text{com}^2$$

---

## 11.2 빗면 위의 구름 운동

### 자유 물체 다이어그램

<img src="/img/ch11/rolling-ramp-fbd.svg" style="max-height:50vh">

빗면 아래로 구르는 물체에 작용하는 힘: 중력 $Mg$, 수직항력 $N$, 정지 마찰력 $f_s$

---

### 운동 방정식

빗면 방향 ($x$축):

$$Mg\sin\theta - f_s = Ma_\text{com}$$

회전 (질량 중심에 대한 돌림힘):

$$Rf_s = I_\text{com}\alpha$$

구름 조건 $a_\text{com} = \alpha R$을 사용하면:

$$f_s = \frac{I_\text{com} a_\text{com}}{R^2}$$

대입하면:

$$Mg\sin\theta - \frac{I_\text{com} a_\text{com}}{R^2} = Ma_\text{com}$$

---

### 빗면 가속도

$$a_\text{com} = \frac{g\sin\theta}{1 + I_\text{com}/MR^2}$$

$c = I_\text{com}/MR^2$으로 놓으면:

$$a_\text{com} = \frac{g\sin\theta}{1 + c}$$

| 물체 | $I_\text{com}$ | $c$ | $a_\text{com}$ |
|---|---|---|---|
| 속이 빈 원통 (링) | $MR^2$ | 1 | $\frac{1}{2}g\sin\theta$ |
| 속이 찬 원판 | $\frac{1}{2}MR^2$ | $\frac{1}{2}$ | $\frac{2}{3}g\sin\theta$ |
| 속이 찬 구 | $\frac{2}{5}MR^2$ | $\frac{2}{5}$ | $\frac{5}{7}g\sin\theta$ |

---

### 누가 먼저 도착할까?

$c$가 작을수록 (관성 모멘트가 작을수록) 가속도가 크다.

**순서: 구 > 원판 > 링** (구가 가장 빨리 도착!)

핵심: **질량과 반지름에 무관** — 오직 질량 분포(관성 모멘트의 형태)만 중요하다.

구가 가장 빠른 이유: 회전에 소비하는 에너지 비율이 가장 작기 때문이다.

---

<!-- sim:rolling-race.html -->
구름 운동 경주 시뮬레이션

---

### 요요(Yo-yo)

요요는 빗면 위의 구름 운동의 특수한 경우로 이해할 수 있다.

<img src="/img/ch11/yoyo-fbd.svg" style="max-height:50vh">

요요에 작용하는 힘: 중력 $Mg$ (아래)와 실의 장력 $T$ (위)

핵심: 실이 감긴 **축의 반지름 $R_0$** 이 구름 조건에서 $R$ 역할을 한다.

---

### 요요의 운동 방정식

**1단계: 병진 운동** (아래 방향을 양의 방향으로)

$$Mg - T = Ma_\text{com}$$

**2단계: 회전 운동** (질량 중심 축에 대해)

실이 축 반지름 $R_0$에 감겨 있으므로, 장력 $T$가 만드는 돌림힘:

$$TR_0 = I_\text{com}\alpha$$

**3단계: 구름 조건**

실이 풀리면서 요요가 회전하므로:

$$a_\text{com} = \alpha R_0$$

---

### 요요의 가속도 유도

회전 방정식과 구름 조건에서 $T$를 구하면:

$$T = \frac{I_\text{com}\alpha}{R_0} = \frac{I_\text{com} a_\text{com}}{R_0^2}$$

이것을 병진 방정식에 대입:

$$Mg - \frac{I_\text{com} a_\text{com}}{R_0^2} = Ma_\text{com}$$

$$Mg = a_\text{com}\left(M + \frac{I_\text{com}}{R_0^2}\right)$$

$$\boxed{a_\text{com} = \frac{g}{1 + I_\text{com}/MR_0^2}}$$

빗면 공식에서 $\theta = 90°$ ($\sin 90° = 1$), $R \to R_0$으로 놓은 것과 정확히 같다!

---

### 요요의 장력과 물리적 의미

실의 장력:

$$T = Mg - Ma_\text{com} = Mg\left(1 - \frac{1}{1 + I_\text{com}/MR_0^2}\right) = \frac{Mg}{1 + MR_0^2/I_\text{com}}$$

균일한 원판 요요 ($I_\text{com} = \frac{1}{2}MR^2$)의 경우:

$$a_\text{com} = \frac{g}{1 + R^2/2R_0^2} = \frac{2gR_0^2}{2R_0^2 + R^2}$$

축 반지름 $R_0$이 외반지름 $R$보다 훨씬 작으면 ($R_0 \ll R$):

$$a_\text{com} \approx \frac{2gR_0^2}{R^2} \ll g$$

요요가 천천히 내려오는 이유: 작은 $R_0$로 인해 $I_\text{com}/MR_0^2$이 매우 커지기 때문이다. 회전 관성이 병진 운동을 크게 저항한다!

---

## 11.3 돌림힘 벡터

### 벡터곱 복습

돌림힘을 벡터로 정의하려면 **벡터곱(cross product)** 이 필요하다.

$$\vec{c} = \vec{a} \times \vec{b}$$

- 크기: $|\vec{c}| = ab\sin\phi$ ($\phi$는 $\vec{a}$와 $\vec{b}$ 사이의 각)
- 방향: **오른손 법칙** — $\vec{a}$에서 $\vec{b}$로 감아쥐면 엄지 방향

성질:

- $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$ (교환 불가!)
- $\vec{a} \times \vec{a} = \vec{0}$

---

### 돌림힘의 벡터 정의

<img src="/img/ch11/torque-cross-product.svg" style="max-height:50vh">

원점 O에서 힘의 작용점까지의 위치 벡터가 $\vec{r}$이고, 힘이 $\vec{F}$일 때:

$$\vec{\tau} = \vec{r} \times \vec{F}$$

크기: $|\vec{\tau}| = rF\sin\phi$

---

### 돌림힘의 의미

$$\tau = rF\sin\phi = r_\perp F = rF_\perp$$

- $r_\perp = r\sin\phi$: **모멘트 팔(moment arm)** — 회전축에서 힘의 작용선까지의 수직 거리
- $F_\perp = F\sin\phi$: 회전을 일으키는 힘의 **접선 성분**

돌림힘은 **회전 운동의 원인** 이다 — 힘이 병진 운동의 원인인 것처럼.

---

## 11.4 각운동량

### 입자의 각운동량

<img src="/img/ch11/angular-momentum-definition.svg" style="max-height:50vh">

원점 O에 대한 입자의 **각운동량(angular momentum)** :

$$\vec{\ell} = \vec{r} \times \vec{p} = \vec{r} \times m\vec{v}$$

---

### 각운동량의 크기

$$\ell = rmv\sin\phi = r_\perp mv = rmv_\perp$$

- $\phi$는 $\vec{r}$과 $\vec{v}$ 사이의 각도
- $r_\perp = r\sin\phi$: 직선 운동 경로까지의 수직 거리

**단위:** $\text{kg}\cdot\text{m}^2/\text{s}$

원운동하는 입자의 경우 ($\phi = 90°$):

$$\ell = rmv = mr^2\omega$$

---

### 회전의 뉴턴 제2법칙

**병진:** $\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$

이와 유사하게, **회전** 에서:

$$\vec{\tau}_\text{net} = \frac{d\vec{\ell}}{dt}$$

입자에 작용하는 알짜 돌림힘 = 각운동량의 시간 변화율

증명: $\vec{\ell} = \vec{r} \times \vec{p}$를 시간 미분하면

$$\frac{d\vec{\ell}}{dt} = \frac{d\vec{r}}{dt} \times \vec{p} + \vec{r} \times \frac{d\vec{p}}{dt} = \vec{v} \times m\vec{v} + \vec{r} \times \vec{F} = \vec{0} + \vec{\tau} = \vec{\tau}$$

---

### 강체의 각운동량

고정축을 중심으로 회전하는 강체의 각운동량:

$$L = \sum_i \ell_i = \sum_i m_i r_i^2 \omega = I\omega$$

$$\boxed{L = I\omega}$$

회전의 뉴턴 제2법칙 (강체):

$$\tau_\text{net} = \frac{dL}{dt} = I\alpha$$

이것은 10장에서 배운 $\tau_\text{net} = I\alpha$와 같다!

---

## 11.5 각운동량 보존

### 보존 법칙

만약 계에 작용하는 **알짜 외부 돌림힘이 0** 이면:

$$\tau_\text{net, ext} = \frac{dL}{dt} = 0$$

따라서:

$$\boxed{L = I\omega = \text{일정}}$$

$$I_i\omega_i = I_f\omega_f$$

이것은 선운동량 보존 ($\vec{F}_\text{net} = 0 \Rightarrow \vec{p} = \text{const}$)의 회전 버전이다.

---

### 피겨 스케이팅: 각운동량 보존의 대표적 예

<img src="/img/ch11/angular-momentum-conservation.svg" style="max-height:50vh">

김연아 선수의 스핀을 떠올려 보자:

- 팔을 벌린 상태: $I$ 크고 → $\omega$ 작음 (느린 회전)
- 팔을 모은 상태: $I$ 작고 → $\omega$ 큼 (빠른 회전)

외부 돌림힘이 거의 없으므로 $L = I\omega$가 보존된다!

---

### 다이빙과 체조

다이빙 선수가 공중에서 몸을 웅크리면:

- 관성 모멘트 $I$가 감소
- 각속력 $\omega$가 증가 → 빠르게 회전
- 입수 전에 몸을 펴면 → $I$ 증가, $\omega$ 감소 → 안정적 입수

**핵심:** 외부 돌림힘 없이도 자신의 몸 형태를 바꿔서 회전 속도를 조절할 수 있다.

같은 원리가 우주 공간에서 위성의 자세 제어에도 사용된다 (반작용 바퀴, reaction wheel).

---

<!-- sim:angular-momentum.html -->
각운동량 보존 시뮬레이션

---

### 예제: 회전하는 학생

질량 $M = 5.0$ kg, 반지름 $R = 0.50$ m인 회전 원판 위에 학생이 서 있다. 양손에 각각 $m = 2.0$ kg의 아령을 들고 $r_i = 0.80$ m에서 팔을 벌린 채 $\omega_i = 3.0$ rad/s로 회전 중이다.

팔을 모아 $r_f = 0.20$ m으로 줄이면 $\omega_f$는?

$$I_i = \frac{1}{2}MR^2 + 2mr_i^2 = \frac{1}{2}(5.0)(0.50)^2 + 2(2.0)(0.80)^2 = 3.185 \;\text{kg}\cdot\text{m}^2$$

$$I_f = \frac{1}{2}MR^2 + 2mr_f^2 = \frac{1}{2}(5.0)(0.50)^2 + 2(2.0)(0.20)^2 = 0.785 \;\text{kg}\cdot\text{m}^2$$

$$\omega_f = \frac{I_i}{I_f}\omega_i = \frac{3.185}{0.785}(3.0) = 12.2 \text{ rad/s}$$

관성 모멘트가 약 4배 줄면, 각속력은 약 4배 증가!

---

## 11.6 세차운동

### 자이로스코프의 세차운동

<img src="/img/ch11/gyroscope-precession.svg" style="max-height:50vh">

빠르게 회전하는 팽이가 쓰러지지 않고 빙글빙글 도는 현상 — **세차운동(precession)** 이다.

회전하지 않는 팽이는 즉시 쓰러진다. 빠르게 회전하면 왜 쓰러지지 않을까?

---

### 1단계: 자전하는 바퀴의 각운동량

바퀴가 각속도 $\omega$로 자전하고 있으면:

$$\vec{L} = I\vec{\omega}$$

$\vec{L}$은 회전축 방향(수평)을 가리킨다. 크기는 $L = I\omega$.

지지점에서 질량 중심까지의 거리를 $r$이라 하자.

---

### 2단계: 중력에 의한 돌림힘

지지점을 기준으로 한 중력의 돌림힘:

$$\vec{\tau} = \vec{r} \times M\vec{g}$$

- $\vec{r}$: 수평 방향 (지지점 → 질량 중심)
- $M\vec{g}$: 아래 방향

오른손 법칙 적용:

- 크기: $\tau = Mgr$
- 방향: **수평면 위에서 $\vec{L}$에 수직**

핵심: $\vec{\tau} \perp \vec{L}$ — 돌림힘과 각운동량이 서로 수직이다!

---

### 3단계: 각운동량의 방향 변화

뉴턴 제2법칙의 회전 버전:

$$d\vec{L} = \vec{\tau}\,dt$$

$\vec{\tau}$가 $\vec{L}$에 수직이므로, $d\vec{L}$도 $\vec{L}$에 수직이다.

벡터에 수직인 미소 변화를 더하면 → **크기는 변하지 않고 방향만 변한다**

이것은 원운동에서 구심 가속도가 속력은 유지하면서 방향만 바꾸는 것과 같은 원리!

결과: $\vec{L}$의 끝이 수평면 위에서 원을 그리며 회전한다 → 이것이 세차운동이다.

---

### 4단계: 세차 각속도 유도

<img src="/img/ch11/precession-vectors.svg" style="max-height:40vh">

시간 $dt$ 동안 $\vec{L}$이 수평면에서 $d\phi$만큼 회전했다고 하자.

$\vec{L}$의 끝이 그리는 원호의 길이 (작은 각도 근사):

$$|d\vec{L}| = L\,d\phi$$

한편 $|d\vec{L}| = \tau\,dt = Mgr\,dt$이므로:

$$L\,d\phi = Mgr\,dt$$

세차 각속도 $\Omega = \frac{d\phi}{dt}$를 구하면:

$$\boxed{\Omega = \frac{Mgr}{L} = \frac{Mgr}{I\omega}}$$

---

### 세차운동의 의미

$$\Omega = \frac{Mgr}{I\omega}$$

- $\omega$ 증가 → $\Omega$ 감소: **빠르게 돌수록** 세차가 느려진다
- $\omega$ 감소 → $\Omega$ 증가: 느려지면 세차가 빨라지다가 결국 쓰러진다
- $M$ 또는 $r$ 증가 → 돌림힘 증가 → 세차가 빨라진다

**팽이:** 마찰로 $\omega$가 줄면 $\Omega$가 커지다가 결국 쓰러진다

**자전거 바퀴:** 빠르게 돌 때 세차 효과로 안정적 — 넘어지기 어렵다

**주의:** 위 공식은 $\omega \gg \Omega$ (자전이 세차보다 훨씬 빠를 때)의 근사이다. 이 조건이 깨지면 **장동(nutation)** 등 더 복잡한 운동이 나타난다.

---

## Review & Summary

### 핵심 개념

| 개념 | 공식 |
|---|---|
| 구름 조건 | $v_\text{com} = \omega R$ |
| 구름 운동에너지 | $K = \frac{1}{2}I_\text{com}\omega^2 + \frac{1}{2}Mv_\text{com}^2$ |
| 빗면 가속도 | $a_\text{com} = \frac{g\sin\theta}{1 + I_\text{com}/MR^2}$ |
| 돌림힘 벡터 | $\vec{\tau} = \vec{r} \times \vec{F}$ |
| 각운동량 (입자) | $\vec{\ell} = \vec{r} \times \vec{p}$ |
| 각운동량 (강체) | $L = I\omega$ |

---

### 핵심 개념 (계속)

| 개념 | 공식 |
|---|---|
| 회전의 뉴턴 2법칙 | $\vec{\tau}_\text{net} = \frac{d\vec{L}}{dt}$ |
| 각운동량 보존 | $I_i\omega_i = I_f\omega_f$ (외부 돌림힘 = 0) |
| 세차 각속도 | $\Omega = \frac{Mgr}{I\omega}$ |

**기억할 것:**

- 구름 운동은 **병진 + 회전** 의 조합이다
- 빗면 경주에서 **질량 분포** 가 중요하다 (질량·반지름은 무관)
- **각운동량은 보존량** 이다 (외부 돌림힘이 없을 때)
- 돌림힘은 $\vec{L}$의 **방향** 을 바꿀 수 있다 (세차운동)
