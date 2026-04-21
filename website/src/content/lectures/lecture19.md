---
title: "19장: 기체 분자 운동론"
week: 19
chapters: "19장"
topics: "이상기체, 압력과 온도의 미시적 해석, 평균 자유 경로, 에너지 등분배 정리, 이상기체의 비열, 단열 팽창, 맥스웰 속력 분포"
---

# 19장: 기체 분자 운동론

The Kinetic Theory of Gases

---

## 이번 장에서 배울 내용

- **이상기체 법칙(ideal gas law)** : $pV = nRT = NkT$
- **압력과 온도의 미시적 해석** : 벽 충돌 → 압력, $K_\text{avg} = \frac{3}{2}kT$
- **평균 자유 경로(mean free path)** : 분자 간 충돌 사이의 평균 거리
- **에너지 등분배 정리(equipartition theorem)** : 자유도와 비열의 관계
- **이상기체의 몰비열과 단열 팽창** : $C_V$, $C_p = C_V + R$, $pV^\gamma = \text{const}$
- **맥스웰 속력 분포(Maxwell speed distribution)** : $v_p$, $v_\text{avg}$, $v_\text{rms}$

---

## 19.1 아보가드로 수와 이상기체

### 기체 분자 운동론이란?

기체의 **거시적 성질** (압력, 온도, 부피)을 **미시적 성질** (분자의 속력, 운동에너지, 충돌)로 설명하는 이론이다.

자동차 엔진의 연소 가스, 제빵 시 발생하는 발효 가스, 잠수부의 감압병(질소 기포) — 모두 기체 분자 운동론의 응용이다.

---

### 아보가드로 수

**몰(mole)** 은 SI 기본 단위 중 하나이다. 1몰은 탄소-12의 12 g에 들어 있는 원자 수와 같다.

**아보가드로 수(Avogadro's number)** :

$$N_A = 6.02 \times 10^{23} \;\text{mol}^{-1}$$

시료의 몰 수 $n$과 분자 수 $N$의 관계:

$$n = \frac{N}{N_A} = \frac{M_\text{sam}}{M} = \frac{M_\text{sam}}{mN_A}$$

- $M_\text{sam}$: 시료의 질량
- $M$: 몰 질량 (1몰의 질량), $m$: 분자 1개의 질량

---

### 이상기체 법칙

충분히 밀도가 낮은 기체는 종류에 관계없이 다음 관계를 만족한다:

$$\boxed{pV = nRT}$$

- $p$: 압력 (Pa), $V$: 부피 (m$^3$), $T$: **절대 온도** (K)
- $n$: 몰 수
- $R = 8.31$ J/mol$\cdot$K (기체 상수)

**볼츠만 상수(Boltzmann constant)** :

$$k = \frac{R}{N_A} = 1.38 \times 10^{-23} \;\text{J/K}$$

분자 수 $N$으로 표현하면:

$$\boxed{pV = NkT}$$

> **주의** : $pV = nRT$는 몰수 $n$, $pV = NkT$는 분자 수 $N$을 사용한다. 혼동하지 않도록!

---

### 등온 과정에서 기체가 한 일

온도 $T$를 일정하게 유지하면서 부피를 $V_i$에서 $V_f$로 바꾸면:

$$W = \int_{V_i}^{V_f} p\,dV = \int_{V_i}^{V_f} \frac{nRT}{V}\,dV$$

$T$가 일정하므로:

$$\boxed{W = nRT \ln\frac{V_f}{V_i}} \quad \text{(등온 과정)}$$

- 팽창 ($V_f > V_i$): $W > 0$ — 기체가 외부에 일을 한다
- 압축 ($V_f < V_i$): $W < 0$ — 외부가 기체에 일을 한다

등적 과정에서는 $W = 0$, 등압 과정에서는 $W = p\Delta V = nR\Delta T$이다.

---

## 19.2 압력, 온도, rms 속력

### 압력의 미시적 기원

기체 분자가 용기 벽에 충돌하며 **운동량을 전달** 한다. 이것이 압력의 미시적 기원이다.

<img src="/img/ch19/gas-molecule-wall.svg" style="max-height:50vh">

---

### 압력 유도

<img src="/img/ch19/gas-molecule-box.svg" style="max-height:50vh">

한 변의 길이가 $L$인 정육면체 용기 안에 $N$개의 분자가 있다. 질량 $m$인 분자 하나가 $x$ 방향 속도 $v_x$로 오른쪽 벽에 탄성 충돌하면:

$$\Delta p_x = (-mv_x) - (mv_x) = -2mv_x$$

벽이 받는 운동량: $+2mv_x$

왕복 시간: $\Delta t = 2L/v_x$

단일 분자가 벽에 가하는 평균 힘:

$$F_1 = \frac{2mv_x}{2L/v_x} = \frac{mv_x^2}{L}$$

---

### 모든 분자의 기여

$N$개 분자 전체가 벽에 가하는 힘:

$$F = \frac{m}{L}\sum_{i=1}^{N} v_{xi}^2 = \frac{Nm}{L}(v_x^2)_\text{avg}$$

등방성 조건: 분자가 모든 방향으로 균등하게 움직이므로

$$(v_x^2)_\text{avg} = (v_y^2)_\text{avg} = (v_z^2)_\text{avg} = \frac{1}{3}(v^2)_\text{avg}$$

압력 $p = F/L^2$이고 $L^3 = V$이므로:

$$p = \frac{Nm(v^2)_\text{avg}}{3V} = \frac{nM v_\text{rms}^2}{3V}$$

여기서 **제곱평균제곱근 속력(root-mean-square speed)** :

$$v_\text{rms} = \sqrt{(v^2)_\text{avg}}$$

---

### rms 속력과 온도

$pV = nRT$와 $p = nMv_\text{rms}^2/(3V)$를 결합하면:

$$nRT = \frac{nMv_\text{rms}^2}{3}$$

$$\boxed{v_\text{rms} = \sqrt{\frac{3RT}{M}}}$$

실온(300 K)에서의 예:

| 기체 | 몰 질량 (g/mol) | $v_\text{rms}$ (m/s) |
|---|---|---|
| H$_2$ | 2.0 | 1920 |
| He | 4.0 | 1370 |
| N$_2$ | 28 | 517 |
| O$_2$ | 32 | 483 |

수소 분자의 rms 속력은 약 1920 m/s — 총알보다 빠르다!

---

## 19.3 병진 운동에너지

### 분자의 평균 운동에너지

분자 하나의 평균 병진 운동에너지:

$$K_\text{avg} = \frac{1}{2}m v_\text{rms}^2$$

$v_\text{rms}^2 = 3RT/M$이고 $M/m = N_A$, $R/N_A = k$이므로 $v_\text{rms}^2 = 3kT/m$:

$$K_\text{avg} = \frac{1}{2}m \cdot \frac{3kT}{m} = \frac{3}{2}kT$$

$$\boxed{K_\text{avg} = \frac{3}{2}kT}$$

놀라운 결과: **같은 온도에서 모든 이상기체 분자는 질량에 관계없이 같은 평균 병진 운동에너지를 갖는다.**

온도를 재는 것은 곧 분자의 평균 운동에너지를 재는 것이다!

---

## 19.4 평균 자유 경로

### 분자 사이의 충돌

분자들은 매우 빠르게 움직이지만, 향수병을 열어도 냄새가 방 건너편까지 도달하는 데 시간이 걸린다. 이유는 분자들이 서로 끊임없이 **충돌** 하기 때문이다.

<img src="/img/ch19/mean-free-path.svg" style="max-height:50vh">

---

### 평균 자유 경로 유도

**평균 자유 경로(mean free path)** $\lambda$: 분자가 연속 충돌 사이에 이동하는 평균 거리

분자 지름 $d$인 분자가 시간 $\Delta t$ 동안 이동하면, 단면적 $\pi d^2$, 길이 $v\Delta t$인 원통을 쓸고 지나간다.

이 원통 안의 분자 수 = 충돌 횟수:

$$\text{충돌 수} = \frac{N}{V}\pi d^2 v\Delta t$$

상대 속도를 보정하면 ($v_\text{rel} = \sqrt{2}\,v_\text{avg}$):

$$\boxed{\lambda = \frac{1}{\sqrt{2}\,\pi d^2 \;N/V}}$$

이상기체 법칙 $N/V = p/(kT)$를 대입하면:

$$\lambda = \frac{kT}{\sqrt{2}\,\pi d^2\, p}$$

---

### 평균 자유 경로의 의미

해수면($p = 1$ atm, $T = 300$ K)에서 산소 분자($d \approx 2.9 \times 10^{-10}$ m):

$$\lambda \approx 1.1 \times 10^{-7}\;\text{m} \approx 0.1\;\mu\text{m} \approx 380 \times d$$

충돌 사이 평균 시간: $t = \lambda/v_\text{avg} \approx 0.24$ ns

충돌 빈도: $f = 1/t \approx 4 \times 10^9\;\text{s}^{-1}$ — 초당 약 **40억 회** 충돌!

해발 100 km에서는 $\lambda \approx 16$ cm, 300 km에서는 $\lambda \approx 20$ km까지 증가한다.

---

## 19.5 에너지 등분배 정리

### 자유도와 에너지

<img src="/img/ch19/degrees-of-freedom.svg" style="max-height:50vh">

---

### 등분배 정리

**에너지 등분배 정리(equipartition theorem)** :

> 열평형 상태에서, 에너지의 각 **자유도(degree of freedom)** 에 평균 $\frac{1}{2}kT$의 에너지가 배분된다.

- **단원자 분자** (He, Ne, Ar): 병진 3개 자유도 → $K_\text{avg} = \frac{3}{2}kT$
- **이원자 분자** (N$_2$, O$_2$, H$_2$): 병진 3 + 회전 2 = 5개 자유도 → $E_\text{avg} = \frac{5}{2}kT$
- **다원자 분자** (CO$_2$, NH$_3$): 병진 3 + 회전 3 = 6개 자유도 → $E_\text{avg} = 3kT$

이원자 분자의 회전 자유도가 2인 이유: 결합축 방향 회전은 관성 모멘트가 거의 0이므로 양자역학적으로 여기되지 않는다.

---

### 자유도의 양자역학적 동결

실제로 이원자 분자의 $C_V$는 온도에 따라 변한다. 수소(H$_2$)의 경우:

- **극저온** ($T < 80$ K): 회전 에너지 준위 간격이 $kT$보다 크다 → 회전이 여기되지 않음 → $f = 3$, $C_V = \frac{3}{2}R$
- **상온** ($80 < T < 1000$ K): 회전은 여기되지만 진동은 아직 동결 → $f = 5$, $C_V = \frac{5}{2}R$
- **고온** ($T > 1000$ K): 진동 자유도(운동에너지 + 위치에너지)도 여기 → $f = 7$, $C_V = \frac{7}{2}R$

이것은 고전 물리학으로는 설명할 수 없으며, 에너지가 양자화되어 있기 때문에 나타나는 현상이다.

---

## 19.6 이상기체의 몰비열

### 내부 에너지

$n$몰의 이상기체의 내부 에너지:

$$E_\text{int} = nN_A \cdot \frac{f}{2}kT = \frac{f}{2}nRT$$

여기서 $f$는 자유도 수이다. 일반적으로:

$$\boxed{E_\text{int} = nC_VT}$$

> 이상기체의 내부 에너지는 **온도에만** 의존하고, 압력이나 부피에 의존하지 않는다.

---

### 정적 몰비열 ($C_V$)

부피를 일정하게 유지하면서 열 $Q$를 가하면 ($W = 0$):

$$Q = \Delta E_\text{int} = nC_V\Delta T$$

$$\boxed{C_V = \frac{f}{2}R}$$

| 분자 유형 | $f$ | $C_V$ | 예시 |
|---|---|---|---|
| 단원자 | 3 | $\frac{3}{2}R = 12.5$ J/mol$\cdot$K | He, Ar |
| 이원자 | 5 | $\frac{5}{2}R = 20.8$ J/mol$\cdot$K | N$_2$, O$_2$ |
| 다원자 | 6 | $3R = 24.9$ J/mol$\cdot$K | CO$_2$, NH$_3$ |

---

### 정압 몰비열 ($C_p$)

압력을 일정하게 유지하면서 열을 가하면, 기체가 팽창하며 외부에 일을 한다.

열역학 제1법칙:

$$Q = \Delta E_\text{int} + W$$

$$nC_p\Delta T = nC_V\Delta T + p\Delta V$$

이상기체이므로 $p\Delta V = nR\Delta T$:

$$nC_p\Delta T = nC_V\Delta T + nR\Delta T$$

$$\boxed{C_p = C_V + R}$$

$C_p > C_V$ 인 이유: 정압 과정에서는 온도를 올리는 데 필요한 에너지 외에 팽창 일까지 해야 하므로 더 많은 열이 필요하다.

---

### 비열비

비열비(ratio of specific heats):

$$\gamma = \frac{C_p}{C_V} = \frac{C_V + R}{C_V} = 1 + \frac{2}{f}$$

| 분자 유형 | $f$ | $C_V$ | $C_p$ | $\gamma$ |
|---|---|---|---|---|
| 단원자 | 3 | $\frac{3}{2}R$ | $\frac{5}{2}R$ | 5/3 = 1.67 |
| 이원자 | 5 | $\frac{5}{2}R$ | $\frac{7}{2}R$ | 7/5 = 1.40 |
| 다원자 | 6 | $3R$ | $4R$ | 4/3 = 1.33 |

핵심: $\Delta E_\text{int} = nC_V\Delta T$는 **모든 과정** 에서 성립한다 (이상기체의 경우). 경로에 관계없이 같은 $\Delta T$이면 같은 $\Delta E_\text{int}$이다.

---

## 19.7 이상기체의 단열 팽창

### 단열 과정

**단열 과정(adiabatic process)** : 열 교환이 없는 과정 ($Q = 0$)

열역학 제1법칙에서:

$$\Delta E_\text{int} = Q - W = -W$$

단열 팽창 → $W > 0$ → $\Delta E_\text{int} < 0$ → **온도가 내려간다**

단열 압축 → $W < 0$ → $\Delta E_\text{int} > 0$ → **온도가 올라간다**

디젤 엔진은 연료 혼합 기체를 단열 압축하여 온도를 올리고, 자연 발화시킨다.

---

### 단열 과정의 $p$-$V$ 관계 유도

$dE_\text{int} = -p\,dV$ 에서:

$$nC_V\,dT = -\frac{nRT}{V}\,dV$$

$$\frac{dT}{T} = -\frac{R}{C_V}\frac{dV}{V}$$

$R/C_V = \gamma - 1$이므로 양변을 적분하면:

$$\ln T + (\gamma-1)\ln V = \text{const}$$

---

### 단열 과정의 $p$-$V$ 관계

따라서:

$$\boxed{TV^{\gamma-1} = \text{const}}$$

$pV = nRT$를 이용하면:

$$\boxed{pV^\gamma = \text{const}}$$

등온선($pV = \text{const}$)보다 단열선이 $p$-$V$ 다이어그램에서 더 가파르다 ($\gamma > 1$).

<img src="/img/ch19/adiabatic-vs-isothermal.svg" style="max-height:50vh">

---

### 단열 과정에서의 일

$$W = \frac{p_iV_i - p_fV_f}{\gamma - 1} = nC_V(T_i - T_f)$$

### 자유 팽창

이상기체가 진공 속으로 자유 팽창하면:

- $Q = 0$ (단열벽), $W = 0$ (진공에 대한 팽창)
- $\Delta E_\text{int} = 0$ → $\Delta T = 0$

이상기체의 자유 팽창에서는 **온도가 변하지 않는다** .

> 자유 팽창은 $pV^\gamma = \text{const}$가 적용되지 **않는다** (비가역 과정).

---

## 19.8 맥스웰 속력 분포

### 속력 분포 함수

모든 분자가 같은 속력을 갖지 않는다. 1852년 James Clerk Maxwell이 속력의 분포를 이론적으로 유도했다.

**맥스웰의 속력 분포 법칙(Maxwell speed distribution law)** :

$$\boxed{P(v) = 4\pi\left(\frac{M}{2\pi RT}\right)^{3/2} v^2\, e^{-Mv^2/2RT}}$$

$P(v)\,dv$ = 속력 $v \sim v+dv$ 구간에 있는 분자의 비율

---

### 맥스웰 분포의 특성

<img src="/img/ch19/maxwell-distribution.svg" style="max-height:50vh">

---

### 세 가지 특성 속력

**최빈 속력(most probable speed)** — $P(v)$가 최대인 속력:

$$v_p = \sqrt{\frac{2RT}{M}}$$

**평균 속력(average speed)** :

$$v_\text{avg} = \sqrt{\frac{8RT}{\pi M}}$$

**rms 속력(root-mean-square speed)** :

$$v_\text{rms} = \sqrt{\frac{3RT}{M}}$$

항상 $v_p < v_\text{avg} < v_\text{rms}$ 순서이다.

산소 분자 ($M = 0.032$ kg/mol, $T = 300$ K):

| 속력 | 값 (m/s) |
|---|---|
| $v_p$ | 395 |
| $v_\text{avg}$ | 445 |
| $v_\text{rms}$ | 483 |

---

### 맥스웰 분포의 의미

온도가 높아지면:

- 분포 곡선이 오른쪽으로 이동 (평균 속력 증가)
- 곡선이 넓어지고 낮아진다 (속력 분산 증가)
- 전체 면적은 항상 1 (확률 보존)

질량이 작은 분자일수록 같은 온도에서 더 빠르다.

태양의 대기에서 가벼운 수소가 탈출하는 것, 지구 대기에서 헬륨이 드문 것 모두 맥스웰 분포의 고속 꼬리(high-speed tail) 때문이다.

---

<!-- sim:ideal-gas-kinetic.html -->
이상기체 분자 운동 시뮬레이션

<!-- sim:molecular-motion.html -->
분자 운동과 Maxwell 분포 시뮬레이션

---

## Review & Summary

### 핵심 공식 (1)

| 개념 | 공식 |
|---|---|
| 이상기체 법칙 | $pV = nRT = NkT$ |
| 등온 과정의 일 | $W = nRT\ln(V_f/V_i)$ |
| rms 속력 | $v_\text{rms} = \sqrt{3RT/M}$ |
| 평균 운동에너지 | $K_\text{avg} = \frac{3}{2}kT$ |
| 평균 자유 경로 | $\lambda = 1/(\sqrt{2}\,\pi d^2\, N/V)$ |

---

### 핵심 공식 (2)

| 개념 | 공식 |
|---|---|
| 정적 몰비열 | $C_V = \frac{f}{2}R$ |
| 정압 몰비열 | $C_p = C_V + R$ |
| 비열비 | $\gamma = C_p/C_V = 1 + 2/f$ |
| 단열 과정 | $pV^\gamma = \text{const}$, $TV^{\gamma-1} = \text{const}$ |
| 맥스웰 분포 | $P(v) = 4\pi(M/2\pi RT)^{3/2} v^2 e^{-Mv^2/2RT}$ |

**기억할 것:**

- **온도** 는 분자의 평균 병진 운동에너지의 척도이다
- 같은 온도에서 **모든 기체 분자는 같은 평균 $K$** 를 갖는다
- $C_p > C_V$: 정압 과정에서 팽창 일이 추가로 필요
- 단열 팽창 → 온도 하강, 단열 압축 → 온도 상승
- $v_p < v_\text{avg} < v_\text{rms}$
