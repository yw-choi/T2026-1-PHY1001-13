# Chapter 20: Entropy and the Second Law of Thermodynamics — 풀이

---

## 문제 1 풀이

$n = 2.00$ mol, $T = 400$ K, $V_i = 10.0$ L $= 0.0100$ m$^3$, $V_f = 30.0$ L $= 0.0300$ m$^3$

**(a)** 등온 과정에서 엔트로피 변화:

$$\Delta S = nR \ln \frac{V_f}{V_i} = (2.00)(8.314) \ln \frac{30.0}{10.0} = 16.63 \times \ln 3 = 16.63 \times 1.099$$

$$\boxed{\Delta S = +18.3 \text{ J/K}}$$

**(b)** 등온 과정에서 $\Delta E_\text{int} = 0$이므로 $Q = W$:

$$Q = nRT \ln \frac{V_f}{V_i} = (2.00)(8.314)(400) \ln 3 = 6651 \times 1.099$$

$$\boxed{Q = +7310 \text{ J} \approx 7.31 \text{ kJ}}$$

검증: $\Delta S = Q/T = 7310/400 = 18.3$ J/K ✓

**(c)** 자유 팽창의 엔트로피 변화도 $\Delta S = +18.3$ J/K로 같다.

이유: 엔트로피는 **상태 함수** 이므로 경로에 무관하고 초기 상태와 최종 상태에만 의존한다. 자유 팽창과 등온 팽창은 같은 $(V_i, T) \to (V_f, T)$를 연결하므로 엔트로피 변화가 같다.

$\boxed{\text{같다. 엔트로피는 상태 함수이므로 경로에 무관하다.}}$

---

## 문제 2 풀이

$T_H = 620$ K, $T_L = 300$ K, $|Q_H| = 2400$ J

**(a)** 카르노 효율:

$$\varepsilon_C = 1 - \frac{T_L}{T_H} = 1 - \frac{300}{620} = 1 - 0.4839 = \boxed{0.516 \approx 51.6\%}$$

**(b)** 매 순환당 일:

$$W = \varepsilon_C |Q_H| = 0.516 \times 2400 = \boxed{1239 \text{ J} \approx 1240 \text{ J}}$$

**(c)** 저온 열원에 방출하는 열:

$$|Q_L| = |Q_H| - W = 2400 - 1239 = \boxed{1161 \text{ J} \approx 1160 \text{ J}}$$

**(d)** 전체 엔트로피 변화:

$$\Delta S_\text{total} = -\frac{|Q_H|}{T_H} + \frac{|Q_L|}{T_L} = -\frac{2400}{620} + \frac{1161}{300} = -3.871 + 3.870$$

$$\boxed{\Delta S_\text{total} = 0 \text{ J/K}}$$

카르노 기관은 가역 과정으로 작동하므로, 전체 엔트로피 변화가 0이다. 이것은 열역학 제2법칙 $\Delta S \geq 0$에서 등호에 해당하며, 카르노 기관이 이상적(가역)임을 확인해 준다.

---

## 문제 3 풀이

$m = 0.50$ kg, $c = 4186$ J/(kg·K), $T_i = 25°$C $= 298$ K, $T_f = 100°$C $= 373$ K

열원 온도: $T_\text{res} = 373$ K

**(a)** 물의 엔트로피 변화:

$$\Delta S_\text{water} = \int_{T_i}^{T_f} \frac{mc\,dT}{T} = mc \ln \frac{T_f}{T_i}$$

$$= (0.50)(4186) \ln \frac{373}{298} = 2093 \times \ln(1.2517) = 2093 \times 0.2245$$

$$\boxed{\Delta S_\text{water} = +470 \text{ J/K}}$$

**(b)** 열원이 잃는 열:

$$Q = mc(T_f - T_i) = (0.50)(4186)(75) = 156\,975 \text{ J}$$

열원의 엔트로피 변화 (일정 온도 $T_\text{res} = 373$ K):

$$\Delta S_\text{reservoir} = -\frac{Q}{T_\text{res}} = -\frac{156\,975}{373}$$

$$\boxed{\Delta S_\text{reservoir} = -421 \text{ J/K}}$$

**(c)** 전체 엔트로피 변화:

$$\Delta S_\text{total} = \Delta S_\text{water} + \Delta S_\text{reservoir} = 470 + (-421)$$

$$\boxed{\Delta S_\text{total} = +49 \text{ J/K} > 0 \;\checkmark}$$

전체 엔트로피가 증가하므로 열역학 제2법칙과 일치한다. 이것은 열원(373 K)과 물(298 K) 사이의 유한한 온도 차이로 인해 비가역 과정이기 때문이다.

---

## 문제 4 풀이

**(a)** 이상기체의 내부에너지 변화: $dE_\text{int} = nC_V\,dT$

열역학 제1법칙: $dQ = dE_\text{int} + dW = nC_V\,dT + p\,dV$

이상기체 법칙 $p = nRT/V$를 대입:

$$dQ = nC_V\,dT + \frac{nRT}{V}\,dV$$

양변을 $T$로 나누면:

$$\boxed{\frac{dQ}{T} = nC_V\frac{dT}{T} + nR\frac{dV}{V}}$$

**(b)** 임의의 초기 상태 $(T_i, V_i)$에서 최종 상태 $(T_f, V_f)$까지 적분:

$$\int_i^f \frac{dQ}{T} = \int_{T_i}^{T_f} nC_V \frac{dT}{T} + \int_{V_i}^{V_f} nR \frac{dV}{V}$$

좌변은 엔트로피 변화 $\Delta S$:

$$\boxed{\Delta S = nC_V \ln \frac{T_f}{T_i} + nR \ln \frac{V_f}{V_i}}$$

**(c)** 단열 가역 과정에서 $TV^{\gamma-1} = \text{const}$이므로:

$$T_i V_i^{\gamma-1} = T_f V_f^{\gamma-1}$$

$$\frac{T_f}{T_i} = \left(\frac{V_i}{V_f}\right)^{\gamma-1}$$

엔트로피 변화 공식에 대입:

$$\Delta S = nC_V \ln \left(\frac{V_i}{V_f}\right)^{\gamma-1} + nR \ln \frac{V_f}{V_i}$$

$$= -nC_V(\gamma - 1) \ln \frac{V_f}{V_i} + nR \ln \frac{V_f}{V_i}$$

$\gamma = C_p/C_V$이고 $C_p - C_V = R$이므로 $C_V(\gamma - 1) = C_V(C_p/C_V - 1) = C_p - C_V = R$:

$$\Delta S = -nR \ln \frac{V_f}{V_i} + nR \ln \frac{V_f}{V_i} = \boxed{0}$$

단열 가역 과정에서는 엔트로피가 변하지 않는다. ✓

---

## 문제 5 풀이

**(a)** 등온팽창(a→b)에서 $T = T_H$이고 $\Delta E_\text{int} = 0$이므로:

$$Q_H = W_{a \to b} = \int_{V_a}^{V_b} p\,dV = \int_{V_a}^{V_b} \frac{nRT_H}{V}\,dV = nRT_H \ln \frac{V_b}{V_a}$$

$$\boxed{|Q_H| = nRT_H \ln \frac{V_b}{V_a}}$$

마찬가지로 등온압축(c→d)에서:

$$|Q_L| = nRT_L \ln \frac{V_c}{V_d}$$

**(b)** 단열팽창(b→c): $T_H V_b^{\gamma-1} = T_L V_c^{\gamma-1}$ ... (1)

단열압축(d→a): $T_L V_d^{\gamma-1} = T_H V_a^{\gamma-1}$ ... (2)

(1)을 (2)로 나누면:

$$\frac{V_b^{\gamma-1}}{V_a^{\gamma-1}} = \frac{V_c^{\gamma-1}}{V_d^{\gamma-1}}$$

$$\left(\frac{V_b}{V_a}\right)^{\gamma-1} = \left(\frac{V_c}{V_d}\right)^{\gamma-1}$$

$$\boxed{\frac{V_b}{V_a} = \frac{V_c}{V_d}}$$

**(c)** 효율:

$$\varepsilon = 1 - \frac{|Q_L|}{|Q_H|} = 1 - \frac{nRT_L \ln(V_c/V_d)}{nRT_H \ln(V_b/V_a)}$$

(b)의 결과 $V_b/V_a = V_c/V_d$를 대입하면 $\ln$항이 약분된다:

$$\varepsilon = 1 - \frac{T_L}{T_H}$$

$$\boxed{\varepsilon_C = 1 - \frac{T_L}{T_H}}$$

---

## 문제 6 풀이

$T_L = -18°$C $= 255$ K, $T_H = 30°$C $= 303$ K

**(a)** 카르노 냉동기의 성능계수:

$$K_C = \frac{T_L}{T_H - T_L} = \frac{255}{303 - 255} = \frac{255}{48} = \boxed{5.31}$$

**(b)** $|Q_L| = 500$ J를 제거하기 위한 최소 일:

$$W_\text{min} = \frac{|Q_L|}{K_C} = \frac{500}{5.31} = \boxed{94.2 \text{ J}}$$

**(c)** 실제 냉동기 ($K = 3.0$):

$$W = \frac{|Q_L|}{K} = \frac{500}{3.0} = \boxed{167 \text{ J}}$$

**(d)** 실제 냉동기는 마찰, 열전도 등 비가역 과정을 포함하므로 전체 엔트로피가 증가한다. 열역학 제2법칙 $\Delta S \geq 0$에 의해, 비가역 과정이 있는 실제 냉동기는 카르노 냉동기보다 성능계수가 낮다 ($K < K_C$). 같은 양의 열을 이동시키려면 더 많은 일이 필요하다.

$\boxed{\text{비가역 과정(마찰, 열전도 등)으로 인해 엔트로피가 생성되어 } K < K_C \text{이다.}}$

---

## 문제 7 풀이

$N = 6$

**(a)** 각 배치의 다중도 $W = \frac{6!}{n_1!\,n_2!}$:

| $(n_1, n_2)$ | 계산 | $W$ |
|---|---|---|
| $(6, 0)$ | $6!/(6!\,0!) = 720/720$ | 1 |
| $(5, 1)$ | $6!/(5!\,1!) = 720/120$ | 6 |
| $(4, 2)$ | $6!/(4!\,2!) = 720/48$ | 15 |
| $(3, 3)$ | $6!/(3!\,3!) = 720/36$ | $\boxed{20}$ |
| $(2, 4)$ | $6!/(2!\,4!) = 720/48$ | 15 |
| $(1, 5)$ | $6!/(1!\,5!) = 720/120$ | 6 |
| $(0, 6)$ | $6!/(0!\,6!) = 720/720$ | 1 |

전체 미시상태: $1 + 6 + 15 + 20 + 15 + 6 + 1 = 64 = 2^6$ ✓

**(b)** 가장 확률 높은 배치: $\boxed{(3, 3)}$, $W = 20$

확률: $P_{3,3} = 20/64 = \boxed{0.3125 = 31.25\%}$

가장 확률 낮은 배치: $(6, 0)$ 또는 $(0, 6)$, $W = 1$

확률: $P_{6,0} = 1/64 = \boxed{0.0156 = 1.56\%}$

**(c)** 초기: $n_1 = 6$, $W_i = 1$, 최종: $n_1 = 3$, $W_f = 20$

$$\Delta S = k(\ln W_f - \ln W_i) = k \ln \frac{W_f}{W_i} = (1.38 \times 10^{-23}) \ln 20$$

$$= (1.38 \times 10^{-23})(3.00) = \boxed{4.13 \times 10^{-23} \text{ J/K}}$$

**(d)** $N = 100$일 때:

$W_{50,50} = \frac{100!}{50!\,50!} \approx 1.01 \times 10^{29}$

$W_{100,0} = 1$

비율: $\boxed{W_{50,50}/W_{100,0} \approx 10^{29}}$

50-50 분배가 100-0보다 약 $10^{29}$배 확률이 높다. 이것은 자유 팽창에서 기체가 전체 부피로 퍼지는 이유를 통계적으로 설명한다. 실제 기체($N \sim 10^{23}$)에서는 이 비율이 천문학적으로 커져, 모든 분자가 한쪽에 모이는 요동은 사실상 불가능하다. 비가역 과정은 **다중도가 작은 상태에서 큰 상태로** — 즉 엔트로피가 증가하는 방향으로 — 진행한다.
