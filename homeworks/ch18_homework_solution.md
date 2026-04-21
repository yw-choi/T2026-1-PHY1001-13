# Chapter 18: Temperature, Heat, and the First Law of Thermodynamics — 풀이

---

## 문제 1 풀이

**(a)** $T_C = -15°$C

$$T_F = \frac{9}{5}(-15) + 32 = -27 + 32 = \boxed{5°\text{F}}$$

$$T = T_C + 273.15 = -15 + 273.15 = \boxed{258 \text{ K}}$$

**(b)** $T_F = 95°$F

$$T_C = \frac{5}{9}(T_F - 32) = \frac{5}{9}(95 - 32) = \frac{5}{9}(63) = \boxed{35°\text{C}}$$

**(c)** $T_C = T_F$로 놓으면:

$$T = \frac{9}{5}T + 32$$

$$T - \frac{9}{5}T = 32 \implies -\frac{4}{5}T = 32$$

$$\boxed{T = -40°}$$

섭씨와 화씨가 같아지는 유일한 온도는 $-40°$이다.

---

## 문제 2 풀이

**(a)** 온도 변화: $\Delta T = 40 - (-20) = 60°$C

$$\Delta L = L\alpha\Delta T = (12.000)(11 \times 10^{-6})(60)$$

$$\boxed{\Delta L = 7.92 \times 10^{-3} \text{ m} = 7.92 \text{ mm}}$$

**(b)** 가솔린의 체적 변화:

$$\Delta T = 45 - 15 = 30°\text{C}$$

$$\Delta V = V\beta\Delta T = (60.0)(9.5 \times 10^{-4})(30) = \boxed{1.71 \text{ L}}$$

약 1.7 L의 가솔린이 넘친다.

---

## 문제 3 풀이

**(a)** 물이 $50°$C에서 $0°$C로 내려갈 때 방출하는 최대 열량:

$$Q_\text{avail} = m_w c_w \Delta T = (0.300)(4187)(50) = \boxed{62\,805 \text{ J} \approx 62.8 \text{ kJ}}$$

**(b)** 얼음을 전부 녹이는 데 필요한 열량:

1단계 — 얼음을 $-5°$C에서 $0°$C로:

$$Q_1 = m_\text{ice} c_\text{ice} \Delta T = (0.200)(2220)(5) = 2220 \text{ J}$$

2단계 — $0°$C에서 전부 녹이기:

$$Q_2 = m_\text{ice} L_F = (0.200)(333\,000) = 66\,600 \text{ J}$$

$$Q_\text{needed} = Q_1 + Q_2 = 2220 + 66\,600 = \boxed{68\,820 \text{ J} \approx 68.8 \text{ kJ}}$$

**(c)** $Q_\text{avail} = 62.8$ kJ $< Q_\text{needed} = 68.8$ kJ이므로, 얼음을 전부 녹이기에 열이 **부족** 하다.

얼음을 $0°$C로 올린 후 녹이기에 사용할 수 있는 열:

$$Q_\text{melt} = Q_\text{avail} - Q_1 = 62\,805 - 2220 = 60\,585 \text{ J}$$

녹는 얼음의 질량:

$$m_\text{melted} = \frac{Q_\text{melt}}{L_F} = \frac{60\,585}{333\,000} = 0.182 \text{ kg} = 182 \text{ g}$$

녹지 않은 얼음: $200 - 182 = 18$ g

$$\boxed{T_f = 0°\text{C}, \quad \text{물 482 g + 얼음 18 g 혼합 상태}}$$

---

## 문제 4 풀이

**(a)** 한 변의 길이가 $L' = L(1 + \alpha\Delta T)$이므로:

$$V' = (L')^3 = L^3(1 + \alpha\Delta T)^3$$

이항 전개:

$$V' = L^3\left[1 + 3\alpha\Delta T + 3(\alpha\Delta T)^2 + (\alpha\Delta T)^3\right]$$

$$\boxed{V' = V\left[1 + 3\alpha\Delta T + 3\alpha^2(\Delta T)^2 + \alpha^3(\Delta T)^3\right]}$$

**(b)** $\alpha\Delta T \ll 1$이면 $(\alpha\Delta T)^2$과 $(\alpha\Delta T)^3$ 항은 무시할 수 있다:

$$V' \approx V(1 + 3\alpha\Delta T)$$

$$\Delta V = V' - V \approx 3\alpha V\Delta T$$

부피 팽창 공식 $\Delta V = \beta V\Delta T$와 비교하면:

$$\boxed{\beta = 3\alpha}$$

**(c)** 구리의 경우:

$$\beta = 3\alpha = 3 \times 17 \times 10^{-6} = \boxed{51 \times 10^{-6}/°\text{C}}$$

---

## 문제 5 풀이

**(a)** 이상기체 상태방정식으로부터 $p = nRT/V$이다. 등온 과정에서 $T = \text{const}$이므로:

$$W = \int_{V_i}^{V_f} p\,dV = \int_{V_i}^{V_f} \frac{nRT}{V}\,dV$$

$nRT$는 상수이므로 적분 밖으로 뺄 수 있다:

$$W = nRT \int_{V_i}^{V_f} \frac{dV}{V} = nRT \left[\ln V\right]_{V_i}^{V_f}$$

$$\boxed{W = nRT\ln\frac{V_f}{V_i}}$$

**(b)** 이상기체의 내부 에너지는 온도에만 의존한다: $E_\text{int} = nC_VT$ (단원자: $C_V = \frac{3}{2}R$). 등온 과정에서 $T$가 변하지 않으므로:

$$\Delta E_\text{int} = nC_V\Delta T = 0$$

열역학 제1법칙 $\Delta E_\text{int} = Q - W$에서:

$$0 = Q - W \implies \boxed{Q = W}$$

등온 팽창에서 기체가 한 일만큼의 열을 환경으로부터 흡수한다.

**(c)** $n = 2$ mol, $T = 300$ K, $V_f/V_i = 2$:

$$W = nRT\ln\frac{V_f}{V_i} = (2)(8.314)(300)\ln 2 = 4988.4 \times 0.6931$$

$$\boxed{W = Q = 3456 \text{ J} \approx 3.46 \text{ kJ}}$$

---

## 문제 6 풀이

단위: $1$ atm·L $= 1.013 \times 10^5 \times 10^{-3} = 101.3$ J

**(a) 경로 A:** 등압($p = p_i = 3$ atm) + 등적

$$W_A = p_i(V_f - V_i) + 0 = 3 \times (3 - 1) = 6 \text{ atm·L}$$

$$\boxed{W_A = 6 \text{ atm·L} = 607.8 \text{ J}}$$

**경로 B:** 등적 + 등압($p = p_f = 1$ atm)

$$W_B = 0 + p_f(V_f - V_i) = 1 \times (3 - 1) = 2 \text{ atm·L}$$

$$\boxed{W_B = 2 \text{ atm·L} = 202.6 \text{ J}}$$

**(b)** $\Delta E_\text{int}$는 **상태 함수** 이므로, 시작 상태 $i$와 끝 상태 $f$가 같으면 경로에 관계없이 값이 같다:

$$\boxed{\Delta E_\text{int,A} = \Delta E_\text{int,B}}$$

이유: 내부 에너지는 온도(와 상태)에만 의존하는 상태 함수이다. $Q$와 $W$는 경로 의존적이지만, $Q - W = \Delta E_\text{int}$는 항상 같다.

**(c)** 열역학 제1법칙 $Q = \Delta E_\text{int} + W$에서, $\Delta E_\text{int}$가 두 경로에서 동일하므로:

$$Q_A - Q_B = (\Delta E_\text{int} + W_A) - (\Delta E_\text{int} + W_B) = W_A - W_B$$

$$\boxed{Q_A - Q_B = 607.8 - 202.6 = 405.2 \text{ J}}$$

경로 A에서 기체가 더 많은 일을 하므로, 외부로부터 더 많은 열을 흡수해야 한다.

---

## 문제 7 풀이

**(a)** 단일 유리창:

$$P_\text{cond} = kA\frac{T_H - T_C}{L} = (1.0)(2.0)\frac{20 - (-10)}{0.050} = \frac{(1.0)(2.0)(30)}{0.050}$$

$$\boxed{P_\text{cond} = 1200 \text{ W}}$$

**(b)** 이중 유리 (유리-공기-유리 복합벽):

$$P_\text{cond} = \frac{A(T_H - T_C)}{\dfrac{L_1}{k_1} + \dfrac{L_2}{k_2} + \dfrac{L_3}{k_3}} = \frac{(2.0)(30)}{\dfrac{0.025}{1.0} + \dfrac{0.010}{0.026} + \dfrac{0.025}{1.0}}$$

$$= \frac{60}{0.025 + 0.3846 + 0.025} = \frac{60}{0.4346}$$

$$\boxed{P_\text{cond} = 138 \text{ W}}$$

**(c)** 감소율:

$$\frac{1200 - 138}{1200} \times 100\% = \boxed{88.5\%}$$

공기층이 단열 효과를 크게 높이는 이유: 공기의 열전도율($k = 0.026$ W/(m·K))이 유리($k = 1.0$ W/(m·K))보다 약 40배 작다. 따라서 얇은 공기층이라도 매우 큰 열저항($R = L/kA$)을 제공한다. 복합벽의 총 열저항에서 공기층이 $0.3846/(0.025 + 0.3846 + 0.025) = 88.5\%$를 차지한다. 이것이 이중창, 삼중창 유리의 단열 원리이다.
