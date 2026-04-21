---
title: "17장: 파동 II"
week: 17
chapters: "17장"
topics: "음파, 음속, 세기와 음압 수준, 간섭, 맥놀이, 도플러 효과, 초음속과 충격파"
---

# 17장: 파동 II

Waves — II

---

## 이번 장에서 배울 내용

- **음파(sound wave)**: 종파, 변위와 압력 변화의 관계
- **음속(speed of sound)**: $v = \sqrt{B/\rho}$
- **세기(intensity)** 와 **데시벨(decibel)** 스케일
- **간섭(interference)**: 경로차와 보강/상쇄 간섭
- **맥놀이(beats)**: 진동수가 약간 다른 두 파동의 중첩
- **도플러 효과(Doppler effect)**: 음원/관측자의 운동에 따른 진동수 변화
- **초음속(supersonic)** 과 **충격파(shock wave)**

---

## 17.1 음속

### 음파란?

16장에서 배운 파동은 횡파(transverse wave)가 중심이었다. 이번 장의 주인공은 **종파(longitudinal wave)** 인 **음파(sound wave)** 다.

- **횡파**: 매질의 진동 방향이 파동 진행 방향에 **수직** (예: 줄의 파동)
- **종파**: 매질의 진동 방향이 파동 진행 방향에 **평행** (예: 음파, 지진의 P파)

음파는 공기, 물, 금속 등 **매질** 이 있어야 전파된다. 진공에서는 소리가 전달되지 않는다. 우주에서는 폭발 소리가 들리지 않는다!

---

### 음속 공식

16장에서 횡파의 속력이 $v = \sqrt{\tau/\mu}$ (탄성적 성질/관성적 성질)임을 배웠다. 종파에서도 같은 구조:

$$v = \sqrt{\frac{\text{탄성적 성질}}{\text{관성적 성질}}} = \sqrt{\frac{B}{\rho}}$$

- $B$: **체적 탄성률(bulk modulus)** — 매질이 압축에 저항하는 정도
- $\rho$: 매질의 **밀도(density)**

$$B = -\frac{\Delta p}{\Delta V / V}$$

압력 변화 $\Delta p$에 대한 부피 변화의 비율이다. 부호 규약: $\Delta p > 0$이면 $\Delta V < 0$ (압축)이므로 $B > 0$.

---

### 음속의 유도

공기 기둥 속을 진행하는 압축 펄스를 생각하자. 펄스와 함께 움직이는 기준계에서, 공기가 속력 $v$로 펄스를 통과한다.

두께 $\Delta x$, 단면적 $A$인 공기 요소에 뉴턴 제2법칙을 적용하면:

알짜힘: $F = pA - (p + \Delta p)A = -\Delta p \cdot A$

질량: $\Delta m = \rho A \Delta x = \rho A v \Delta t$

가속도: $a = \Delta v / \Delta t$

$F = ma$에서:

$$-\Delta p \cdot A = (\rho A v \Delta t) \frac{\Delta v}{\Delta t}$$

$$\rho v^2 = -\frac{\Delta p}{\Delta v / v}$$

여기서 $\Delta V / V = A\Delta v\Delta t / (Av\Delta t) = \Delta v / v$이므로:

$$\rho v^2 = -\frac{\Delta p}{\Delta V / V} = B$$

따라서:

$$\boxed{v = \sqrt{\frac{B}{\rho}}}$$

---

### 여러 매질에서의 음속

| 매질 | 음속 (m/s) |
|---|---|
| 공기 (0°C) | 331 |
| 공기 (20°C) | 343 |
| 헬륨 | 965 |
| 물 (20°C) | 1482 |
| 알루미늄 | 6420 |
| 강철 | 5941 |

공기 중 음속은 약 **343 m/s** (20°C). 빛의 속도(3×10⁸ m/s)보다 약 백만 배 느리다.

번개가 치면 빛은 즉시 보이지만, 천둥 소리는 나중에 들린다: $d = v \times t$.

3초 후 천둥이 들리면 거리는 약 $343 \times 3 \approx 1.0$ km.

---

## 17.2 진행하는 음파

### 변위 함수

음파에서 공기 요소의 **변위(displacement)** 는 평형 위치로부터의 종방향 이동:

$$s(x, t) = s_m \cos(kx - \omega t)$$

- $s_m$: **변위 진폭(displacement amplitude)** — 평형 위치에서 최대 변위
- $k = 2\pi/\lambda$: 파수(wave number)
- $\omega = 2\pi f$: 각진동수

횡파의 $y(x,t)$와 형태가 동일하다. 다만 진동 방향이 $x$축과 같다는 점이 다르다.

---

### 압력 변화

음파가 지나가면 공기의 압력도 주기적으로 변한다:

$$\Delta p(x, t) = \Delta p_m \sin(kx - \omega t)$$

여기서 **압력 진폭(pressure amplitude)** 은:

$$\Delta p_m = (v\rho\omega) s_m$$

**핵심: 변위와 압력은 90° 위상차가 있다!**

- 변위가 최대인 곳 → 압력 변화 = 0
- 변위가 0인 곳 → 압력 변화 최대 (압축 또는 팽창)

<img src="/img/ch17/sound-wave-pressure.svg" style="max-height:50vh">

---

### 압력-변위 관계의 유도

변위 $s$에 의해 공기 요소의 부피가 변한다. 두께 $\Delta x$, 단면적 $A$인 요소에서:

원래 부피: $V = A\Delta x$

부피 변화: $\Delta V = A\Delta s$ ($\Delta s$는 양쪽 면의 변위 차)

미분 극한에서: $\frac{\Delta V}{V} = \frac{\Delta s}{\Delta x} \to \frac{\partial s}{\partial x}$

체적 탄성률의 정의 $\Delta p = -B \frac{\Delta V}{V}$에서:

$$\Delta p = -B \frac{\partial s}{\partial x}$$

$s = s_m \cos(kx - \omega t)$를 대입하면:

$$\Delta p = -B \cdot (-k s_m) \sin(kx - \omega t) = Bk s_m \sin(kx - \omega t)$$

$v = \omega / k$와 $v^2 = B/\rho$를 사용하면 $Bk = v^2\rho k = v\rho\omega$이므로:

$$\boxed{\Delta p_m = v\rho\omega s_m}$$

---

## 17.3 간섭

### 두 음파의 간섭

같은 진동수, 같은 진폭의 두 음파가 같은 방향으로 진행하되 위상차 $\phi$가 있는 경우:

$$s_1 = s_m \cos(kx - \omega t), \quad s_2 = s_m \cos(kx - \omega t + \phi)$$

중첩 원리에 의한 합성파:

$$s' = \left[2s_m \cos\frac{\phi}{2}\right] \cos\left(kx - \omega t + \frac{\phi}{2}\right)$$

합성파의 진폭:

$$s'_m = \left|2s_m \cos\frac{\phi}{2}\right|$$

---

### 보강 간섭과 상쇄 간섭

**보강 간섭(constructive interference):** $\phi = 0, 2\pi, 4\pi, \ldots$ → $s'_m = 2s_m$ (최대)

**상쇄 간섭(destructive interference):** $\phi = \pi, 3\pi, 5\pi, \ldots$ → $s'_m = 0$ (소멸)

위상차 $\phi$는 **경로차(path length difference)** $\Delta L$과 관련된다:

$$\phi = \frac{\Delta L}{\lambda} \cdot 2\pi$$

---

### 경로차에 의한 간섭 조건

<img src="/img/ch17/interference-two-sources.svg" style="max-height:50vh">

두 점 음원 $S_1$, $S_2$에서 같은 위상으로 방출된 음파가 점 $P$에 도달할 때, 경로차 $\Delta L = |L_2 - L_1|$에 따라:

**보강 간섭:**

$$\frac{\Delta L}{\lambda} = 0, 1, 2, 3, \ldots$$

**상쇄 간섭:**

$$\frac{\Delta L}{\lambda} = 0.5, 1.5, 2.5, \ldots$$

---

## 17.4 세기와 음압 수준

### 세기(Intensity)

음파의 **세기(intensity)** 는 단위 면적당 전달되는 평균 에너지 비율(일률):

$$I = \frac{P}{A}$$

변위 진폭 $s_m$으로 표현하면:

$$I = \frac{1}{2}\rho v \omega^2 s_m^2$$

**단위:** W/m²

---

### 역제곱 법칙

등방성 점 음원(isotropic point source)에서 출력 $P_s$로 음파를 방출하면, 거리 $r$에서의 세기:

$$I = \frac{P_s}{4\pi r^2}$$

구의 표면적 $4\pi r^2$에 에너지가 균일하게 분배되기 때문이다.

핵심: **세기는 거리의 제곱에 반비례한다.**

거리가 2배 → 세기가 1/4로 감소. 거리가 10배 → 세기가 1/100로 감소.

---

### 데시벨 스케일

인간의 귀는 세기 범위가 $10^{12}$배나 된다. 이 거대한 범위를 다루기 위해 로그 스케일을 사용한다.

**음압 수준(sound level)** $\beta$:

$$\beta = (10 \text{ dB}) \log \frac{I}{I_0}$$

- $I_0 = 10^{-12}$ W/m²: 기준 세기 (청각 역치)
- **dB(decibel):** 음압 수준의 단위

| 환경 | 음압 수준 (dB) |
|---|---|
| 청각 역치 | 0 |
| 나뭇잎 스치는 소리 | 10 |
| 일상 대화 | 60 |
| 록 콘서트 | 110 |
| 통증 역치 | 120 |
| 제트 엔진 (근거리) | 130 |

---

### 데시벨 계산 예시

세기가 10배 증가하면 $\beta$는 **10 dB** 증가:

$$\beta_2 - \beta_1 = 10 \log \frac{I_2}{I_0} - 10\log\frac{I_1}{I_0} = 10\log\frac{I_2}{I_1}$$

$I_2 = 10 I_1$이면 $\Delta\beta = 10\log 10 = 10$ dB.

$I_2 = 100 I_1$이면 $\Delta\beta = 10\log 100 = 20$ dB.

$I_2 = 2 I_1$이면 $\Delta\beta = 10\log 2 \approx 3$ dB.

**"3 dB 증가 = 세기 2배"** 는 기억해 둘 가치가 있다.

---

### 세기 공식 유도

단면적 $A$, 두께 $dx$인 공기 요소의 운동에너지:

$$dK = \frac{1}{2}dm \cdot v_s^2$$

여기서 $v_s = \partial s / \partial t = \omega s_m \sin(kx - \omega t)$는 공기 요소의 속도이고, $dm = \rho A\,dx$.

$$\frac{dK}{dt} = \frac{1}{2}\rho A v \omega^2 s_m^2 \sin^2(kx - \omega t)$$

시간 평균: $\langle \sin^2 \rangle = 1/2$

$$\left\langle\frac{dK}{dt}\right\rangle = \frac{1}{4}\rho A v \omega^2 s_m^2$$

---

### 세기 공식 유도 (계속)

퍼텐셜에너지도 동일한 기여를 하므로, 전체 에너지 전달률:

$$P = 2 \times \frac{1}{4}\rho A v \omega^2 s_m^2 = \frac{1}{2}\rho A v \omega^2 s_m^2$$

세기 $I = P/A$:

$$\boxed{I = \frac{1}{2}\rho v \omega^2 s_m^2}$$

---

## 17.5 악기의 음원: 관에서의 정상파

### 열린관과 닫힌관

관악기(플루트, 클라리넷, 파이프 오르간 등)의 원리는 관 속에서 형성되는 **정상파(standing wave)** 다.

- **열린 끝(open end)**: 배(antinode) — 공기가 자유롭게 진동
- **닫힌 끝(closed end)**: 마디(node) — 공기가 움직이지 못함

이것은 줄의 정상파에서 고정단(마디)과 자유단(배)에 해당한다.

---

### 양쪽 열린 관 (Two Open Ends)

양 끝이 배이므로, 가장 단순한 정상파의 파장:

$$L = \frac{\lambda}{2} \quad \Rightarrow \quad \lambda = 2L$$

일반적으로, $n$번째 배음(harmonic)의 파장과 진동수:

$$\lambda = \frac{2L}{n}, \quad f = \frac{v}{\lambda} = \frac{nv}{2L}, \quad n = 1, 2, 3, \ldots$$

**모든 정수 배음** 이 가능하다. $n = 1$이 기본 진동(fundamental), $n = 2$가 2차 배음, ...

---

### 한쪽 닫힌 관 (One Open End)

열린 끝은 배, 닫힌 끝은 마디. 가장 단순한 정상파:

$$L = \frac{\lambda}{4} \quad \Rightarrow \quad \lambda = 4L$$

일반적으로:

$$\lambda = \frac{4L}{n}, \quad f = \frac{nv}{4L}, \quad n = 1, 3, 5, \ldots$$

**홀수 배음만** 가능하다! $n = 2, 4, 6, \ldots$는 존재하지 않는다.

이것이 클라리넷(한쪽 닫힌 관)과 플루트(양쪽 열린 관)의 음색 차이를 만든다.

---

<!-- sim:sound-waves.html -->
음파 시뮬레이션: 관의 정상파, 맥놀이, 도플러 효과

---

## 17.6 맥놀이

### 맥놀이 현상

진동수가 약간 다른 두 음파가 동시에 들리면, 소리의 세기가 주기적으로 커졌다 작아졌다 한다. 이것이 **맥놀이(beats)** 다.

예: 440 Hz와 444 Hz 음을 동시에 들으면, 1초에 4번 소리가 커졌다 작아진다.

악기 조율에 활용: 기준 음과 맞추려는 악기를 동시에 울리고, 맥놀이가 사라질 때까지 조율한다.

<img src="/img/ch17/beat-pattern.svg" style="max-height:50vh">

---

### 맥놀이의 수학적 분석

같은 진폭 $s_m$, 약간 다른 각진동수 $\omega_1$, $\omega_2$ ($\omega_1 > \omega_2$)인 두 파동:

$$s_1 = s_m \cos \omega_1 t, \quad s_2 = s_m \cos \omega_2 t$$

중첩: $s = s_1 + s_2 = s_m(\cos\omega_1 t + \cos\omega_2 t)$

삼각함수 덧셈 공식 $\cos\alpha + \cos\beta = 2\cos\frac{\alpha-\beta}{2}\cos\frac{\alpha+\beta}{2}$을 적용:

$$s = \left[2s_m \cos\left(\frac{\omega_1 - \omega_2}{2}t\right)\right] \cos\left(\frac{\omega_1 + \omega_2}{2}t\right)$$

---

### 맥놀이 진동수

$$s(t) = \underbrace{\left[2s_m \cos\omega' t\right]}_{\text{천천히 변하는 진폭}} \cos\omega t$$

여기서 $\omega' = \frac{1}{2}(\omega_1 - \omega_2)$, $\omega = \frac{1}{2}(\omega_1 + \omega_2)$.

<img src="/img/ch17/beats-waveform.svg" style="max-height:50vh">

맥놀이의 세기가 최대가 되는 것은 $\cos\omega' t = \pm 1$일 때, 즉 한 주기 동안 **2번** 이므로:

$$\omega_\text{beat} = 2\omega' = \omega_1 - \omega_2$$

진동수로 표현하면:

$$\boxed{f_\text{beat} = |f_1 - f_2|}$$

맥놀이 진동수 = 두 진동수의 차이(절댓값).

---

### 맥놀이 예시

피아노 조율사가 440 Hz 소리굽쇠와 함께 피아노 건반을 쳤더니 1초에 3번 맥놀이가 들렸다.

피아노 건반의 진동수는?

$$f_\text{beat} = |f_1 - f_2| = 3 \text{ Hz}$$

따라서 $f_\text{piano} = 440 \pm 3$ Hz, 즉 437 Hz 또는 443 Hz.

어느 쪽인지 알려면? 건반의 음을 약간 높이면(줄을 조이면):
- 맥놀이가 빨라지면 → 440에서 멀어지는 중 → 원래 443 Hz였다
- 맥놀이가 느려지면 → 440에 가까워지는 중 → 원래 437 Hz였다

<!-- sim:beats-interference.html -->
맥놀이와 간섭 시뮬레이션

---

## 17.7 도플러 효과

### 도플러 효과란?

구급차가 다가올 때 사이렌 소리가 높게 들리고, 멀어질 때 낮게 들린다. 이것이 **도플러 효과(Doppler effect)** 다.

<img src="/img/ch17/doppler-effect.svg" style="max-height:50vh">

음원이나 관측자가 움직이면, 관측되는 진동수가 원래 진동수와 달라진다.

---

### 도플러 효과 일반 공식

$$f' = f \frac{v \pm v_O}{v \mp v_S}$$

- $f$: 음원의 고유 진동수
- $f'$: 관측되는 진동수
- $v$: 음속
- $v_O$: 관측자의 속력
- $v_S$: 음원의 속력

**부호 규칙**: "접근하면 진동수 증가" 방향이 양

- 분자($v \pm v_O$): 관측자가 **음원 쪽으로** 이동하면 **+**
- 분모($v \mp v_S$): 음원이 **관측자 쪽으로** 이동하면 **−**

---

### 경우 1: 관측자가 움직이는 경우

음원 정지($v_S = 0$), 관측자가 속력 $v_O$로 움직이는 경우.

관측자가 음원에 접근하면, 파면을 더 자주 만난다:

$$f' = f \frac{v + v_O}{v}$$

관측자가 음원에서 멀어지면:

$$f' = f \frac{v - v_O}{v}$$

물리적 이해: 관측자 기준에서 파동의 상대 속도가 $v + v_O$ (접근) 또는 $v - v_O$ (멀어짐)로 바뀐다. 파장은 그대로이므로, 진동수가 변한다.

---

### 경우 2: 음원이 움직이는 경우

관측자 정지($v_O = 0$), 음원이 속력 $v_S$로 움직이는 경우.

<img src="/img/ch17/doppler-source-moving.svg" style="max-height:50vh">

음원이 관측자에 접근하면, 파면이 앞쪽으로 압축된다:

$$\lambda' = \lambda - v_S T = \lambda\left(1 - \frac{v_S}{v}\right) = \frac{v - v_S}{f}$$

$$f' = \frac{v}{\lambda'} = f\frac{v}{v - v_S}$$

음원이 멀어지면:

$$f' = f\frac{v}{v + v_S}$$

---

### 도플러 효과 예제

구급차의 사이렌 진동수: $f = 1000$ Hz. 구급차 속도: $v_S = 30$ m/s. 음속: $v = 343$ m/s.

**다가올 때:**

$$f' = 1000 \times \frac{343}{343 - 30} = 1000 \times \frac{343}{313} = 1096 \text{ Hz}$$

**멀어질 때:**

$$f' = 1000 \times \frac{343}{343 + 30} = 1000 \times \frac{343}{373} = 920 \text{ Hz}$$

진동수 변화: $1096 - 920 = 176$ Hz. 이것이 우리가 흔히 듣는 "삐~이이" 소리의 원인이다.

---

## 17.8 초음속과 충격파

### 음원이 음속을 넘으면?

도플러 공식에서 $v_S > v$이면 분모가 음수 — 공식이 더 이상 성립하지 않는다.

음원이 음속보다 빠르면, 음파의 파면을 앞지른다. 이때 발생하는 것이 **충격파(shock wave)** 다.

<img src="/img/ch17/mach-cone.svg" style="max-height:50vh">

---

### 마하 원뿔

음원이 $v_S > v$로 이동하면, 각 순간 방출된 구면파의 공통접선이 **원뿔면** 을 이룬다.

이 원뿔의 반각 $\theta$:

$$\sin\theta = \frac{v}{v_S} = \frac{1}{\text{Ma}}$$

여기서 **마하 수(Mach number)** 는:

$$\text{Ma} = \frac{v_S}{v}$$

- Ma = 1: 음속 (소닉 붐의 시작)
- Ma > 1: 초음속(supersonic) — 전투기, 총알 등
- Ma > 5: 극초음속(hypersonic)

---

### 충격파의 물리

충격파는 매우 큰 압력 변화를 수반한다. 이것이 **소닉 붐(sonic boom)** 의 원인이다.

- 총알이 지나가면 "탁!" 하는 소리 — 이것이 미니 소닉 붐
- 번개의 열 팽창이 충격파를 만들어 천둥 소리가 된다
- 초음속 전투기가 지나가면 원뿔형 충격파가 지면을 쓸고 지나간다

마하 원뿔의 각도를 측정하면 물체의 속도를 알 수 있다:

$$v_S = \frac{v}{\sin\theta}$$

예: 총알의 사진에서 마하 원뿔 각도가 $\theta = 30°$이면:

$$\text{Ma} = \frac{1}{\sin 30°} = 2.0$$

총알은 음속의 2배로 날아간다.

<!-- sim:doppler-effect.html -->
도플러 효과 시뮬레이션

---

## Review & Summary

### 핵심 개념

| 개념 | 공식 |
|---|---|
| 음속 | $v = \sqrt{B/\rho}$ |
| 변위 | $s = s_m\cos(kx - \omega t)$ |
| 압력 변화 | $\Delta p = \Delta p_m \sin(kx - \omega t)$ |
| 압력 진폭 | $\Delta p_m = v\rho\omega s_m$ |
| 세기 | $I = \frac{1}{2}\rho v\omega^2 s_m^2$ |
| 역제곱 법칙 | $I = P_s / (4\pi r^2)$ |

---

### 핵심 개념 (계속)

| 개념 | 공식 |
|---|---|
| 음압 수준 | $\beta = (10\text{ dB})\log(I/I_0)$ |
| 보강/상쇄 간섭 | $\Delta L / \lambda = 0, 1, 2, \ldots$ / $0.5, 1.5, \ldots$ |
| 열린관 공명 | $f = nv/(2L)$, $n = 1, 2, 3, \ldots$ |
| 닫힌관 공명 | $f = nv/(4L)$, $n = 1, 3, 5, \ldots$ |
| 맥놀이 | $f_\text{beat} = |f_1 - f_2|$ |
| 도플러 효과 | $f' = f(v \pm v_O)/(v \mp v_S)$ |

**기억할 것:**

- 음파는 **종파** 다. 변위와 압력은 90° 위상차
- 세기는 거리의 제곱에 반비례 (**역제곱 법칙**)
- 맥놀이 = 두 진동수의 **차이**
- 도플러: 접근 → 높은 진동수, 멀어짐 → 낮은 진동수
- $v_S > v$ → **마하 원뿔** 과 충격파
