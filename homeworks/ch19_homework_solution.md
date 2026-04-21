# Chapter 19: The Kinetic Theory of Gases — 풀이

---

## 문제 1 풀이

$V = 0.050\;\text{m}^3$, $M = 0.032\;\text{kg/mol}$, $T = 300\;\text{K}$, $p = 2.0 \times 10^5\;\text{Pa}$

**(a)** 이상기체 법칙 $pV = nRT$에서:

$$n = \frac{pV}{RT} = \frac{(2.0 \times 10^5)(0.050)}{(8.31)(300)} = \frac{10000}{2493} = \boxed{4.01\;\text{mol}}$$

**(b)** rms 속력:

$$v_\text{rms} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3(8.31)(300)}{0.032}} = \sqrt{2.33 \times 10^5} = \boxed{483\;\text{m/s}}$$

**(c)** 평균 병진 운동에너지:

$$K_\text{avg} = \frac{3}{2}kT = \frac{3}{2}(1.38 \times 10^{-23})(300) = \boxed{6.21 \times 10^{-21}\;\text{J}}$$

---

## 문제 2 풀이

$M = 0.028\;\text{kg/mol}$, $d = 3.0 \times 10^{-10}\;\text{m}$, $T = 400\;\text{K}$, $p = 1.01 \times 10^5\;\text{Pa}$

**(a)** 평균 자유 경로:

$$\lambda = \frac{kT}{\sqrt{2}\,\pi d^2\, p}$$

$$= \frac{(1.38 \times 10^{-23})(400)}{\sqrt{2}\,\pi (3.0 \times 10^{-10})^2 (1.01 \times 10^5)}$$

분모:

$$\sqrt{2}\,\pi (9.0 \times 10^{-20})(1.01 \times 10^5) = 1.414 \times 3.1416 \times 9.09 \times 10^{-15} = 4.04 \times 10^{-14}$$

분자: $5.52 \times 10^{-21}$

$$\lambda = \frac{5.52 \times 10^{-21}}{4.04 \times 10^{-14}} = \boxed{1.37 \times 10^{-7}\;\text{m} \approx 0.14\;\mu\text{m}}$$

**(b)** 평균 속력:

$$v_\text{avg} = \sqrt{\frac{8RT}{\pi M}} = \sqrt{\frac{8(8.31)(400)}{\pi(0.028)}} = \sqrt{\frac{26592}{0.08796}} = \sqrt{3.02 \times 10^5} = \boxed{550\;\text{m/s}}$$

**(c)** 충돌 빈도:

$$f = \frac{v_\text{avg}}{\lambda} = \frac{550}{1.37 \times 10^{-7}} = \boxed{4.0 \times 10^{9}\;\text{s}^{-1}}$$

초당 약 40억 번 충돌한다.

---

## 문제 3 풀이

$n = 2.0\;\text{mol}$, $\gamma = 7/5 = 1.4$, $T_i = 300\;\text{K}$, $V_i = 0.040\;\text{m}^3$, $V_f = 0.080\;\text{m}^3$

이원자 기체: $C_V = \frac{5}{2}R = 20.8\;\text{J/(mol·K)}$

**(a)** 단열 과정에서 $TV^{\gamma-1} = \text{const}$:

$$T_i V_i^{\gamma-1} = T_f V_f^{\gamma-1}$$

$$T_f = T_i \left(\frac{V_i}{V_f}\right)^{\gamma-1} = 300 \left(\frac{0.040}{0.080}\right)^{0.4} = 300 \left(\frac{1}{2}\right)^{0.4}$$

$$\left(\frac{1}{2}\right)^{0.4} = 2^{-0.4} = e^{-0.4\ln 2} = e^{-0.2773} = 0.758$$

$$T_f = 300 \times 0.758 = \boxed{227\;\text{K}}$$

**(b)** 내부 에너지 변화:

$$\Delta E_\text{int} = nC_V\Delta T = nC_V(T_f - T_i)$$

$$= (2.0)(20.8)(227 - 300) = (2.0)(20.8)(-73)$$

$$= \boxed{-3037\;\text{J} \approx -3.0\;\text{kJ}}$$

온도가 내려갔으므로 내부 에너지가 감소했다.

**(c)** 단열 과정에서 $Q = 0$이므로:

$$W = Q - \Delta E_\text{int} = 0 - (-3037) = \boxed{+3037\;\text{J} \approx +3.0\;\text{kJ}}$$

기체가 팽창하면서 외부에 양의 일을 했고, 그 에너지는 내부 에너지 감소(온도 하강)에서 왔다.

---

## 문제 4 풀이

**(a)** $pV = nRT$ ... (1), $p = \frac{nMv_\text{rms}^2}{3V}$ ... (2)

(2)를 (1)에 대입:

$$\frac{nMv_\text{rms}^2}{3V} \cdot V = nRT$$

$$\frac{nMv_\text{rms}^2}{3} = nRT$$

$$v_\text{rms}^2 = \frac{3RT}{M}$$

$$\boxed{v_\text{rms} = \sqrt{\frac{3RT}{M}}}$$

**(b)** 분자 1개의 평균 병진 운동에너지:

$$K_\text{avg} = \frac{1}{2}mv_\text{rms}^2 = \frac{1}{2}m \cdot \frac{3RT}{M}$$

$M = mN_A$이므로 $m = M/N_A$:

$$K_\text{avg} = \frac{1}{2}\frac{M}{N_A} \cdot \frac{3RT}{M} = \frac{3RT}{2N_A} = \frac{3}{2}\frac{R}{N_A}T$$

$k = R/N_A$이므로:

$$\boxed{K_\text{avg} = \frac{3}{2}kT}$$

**(c)** $K_\text{avg} = \frac{3}{2}kT$에는 분자 질량 $m$이 나타나지 않는다. 이는 무거운 분자가 가벼운 분자보다 느리게 움직이지만 ($v_\text{rms} \propto 1/\sqrt{M}$), 질량이 큰 만큼 운동에너지가 보상되기 때문이다. 열평형 상태에서 분자 간 충돌이 끊임없이 일어나면서, 가벼운 분자는 빠르게, 무거운 분자는 느리게 움직이되 **평균 운동에너지는 같아지도록** 에너지가 재분배된다. 이것이 등분배 정리의 핵심이다.

---

## 문제 5 풀이

**(a)** 단열 과정: $Q = 0$. 열역학 제1법칙:

$$dE_\text{int} = Q - p\,dV = -p\,dV$$

이상기체: $dE_\text{int} = nC_V\,dT$, $p = nRT/V$:

$$nC_V\,dT = -\frac{nRT}{V}\,dV$$

양변을 $nT$로 나누면:

$$C_V\,\frac{dT}{T} = -R\,\frac{dV}{V}$$

양변을 적분:

$$C_V \ln T = -R \ln V + \text{const}$$

$$C_V \ln T + R \ln V = \text{const}$$

$$\ln(T^{C_V} V^R) = \text{const}$$

$$T^{C_V} V^R = \text{const}$$

양변을 $1/C_V$ 제곱:

$$T V^{R/C_V} = \text{const}$$

$R/C_V = (C_p - C_V)/C_V = \gamma - 1$이므로:

$$\boxed{TV^{\gamma-1} = \text{const}}$$

**(b)** 이상기체 법칙에서 $T = pV/(nR)$을 대입:

$$\frac{pV}{nR} \cdot V^{\gamma-1} = \text{const}$$

$$pV^{\gamma} = \text{const} \times nR$$

$nR$은 상수이므로:

$$\boxed{pV^\gamma = \text{const}}$$

**(c)** $C_V = \frac{f}{2}R$이므로:

$$C_p = C_V + R = \frac{f}{2}R + R = \frac{f+2}{2}R$$

$$\gamma = \frac{C_p}{C_V} = \frac{(f+2)/2 \cdot R}{f/2 \cdot R} = \frac{f+2}{f} = \boxed{1 + \frac{2}{f}}$$

---

## 문제 6 풀이

**(a)** Maxwell 속력 분포는 $v^2 e^{-v^2}$ 형태로, 오른쪽으로 긴 꼬리(high-speed tail)를 갖는 비대칭 분포이다.

- $v_p$는 분포의 **최대값** 위치이다 — 가장 많은 분자가 갖는 속력.
- $v_\text{avg}$는 $v$를 가중 평균하므로, 고속 꼬리의 영향을 받아 $v_p$보다 크다.
- $v_\text{rms}$는 $v^2$를 가중 평균한 뒤 제곱근을 취하므로, 고속 분자의 기여가 $v_\text{avg}$보다 **더 크게** 반영된다.

따라서 항상 $\boxed{v_p < v_\text{avg} < v_\text{rms}}$이다.

**(b)** $M = 0.032\;\text{kg/mol}$, $T = 300\;\text{K}$:

최빈 속력:

$$v_p = \sqrt{\frac{2RT}{M}} = \sqrt{\frac{2(8.31)(300)}{0.032}} = \sqrt{1.556 \times 10^5} = \boxed{395\;\text{m/s}}$$

평균 속력:

$$v_\text{avg} = \sqrt{\frac{8RT}{\pi M}} = \sqrt{\frac{8(8.31)(300)}{\pi(0.032)}} = \sqrt{\frac{19944}{0.1005}} = \sqrt{1.984 \times 10^5} = \boxed{445\;\text{m/s}}$$

rms 속력:

$$v_\text{rms} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3(8.31)(300)}{0.032}} = \sqrt{2.334 \times 10^5} = \boxed{483\;\text{m/s}}$$

검증: $v_p < v_\text{avg} < v_\text{rms}$: 395 < 445 < 483 $\checkmark$

**(c)** $v_\text{rms} \propto \sqrt{T}$이므로:

$$\frac{v_\text{rms}(600)}{v_\text{rms}(300)} = \sqrt{\frac{600}{300}} = \sqrt{2} \approx 1.414$$

$$\boxed{v_\text{rms}\text{는 약 } \sqrt{2} \approx 1.41\text{배가 된다.}}$$

---

## 문제 7 풀이

$n = 3.0\;\text{mol}$, He (단원자): $C_V = \frac{3}{2}R = 12.47\;\text{J/(mol·K)}$, $C_p = \frac{5}{2}R = 20.78\;\text{J/(mol·K)}$

$T_i = 400\;\text{K}$, $T_f = 600\;\text{K}$, $\Delta T = 200\;\text{K}$

**(a)** 이상기체의 내부 에너지 변화는 경로에 무관하고 온도 변화에만 의존한다:

$$\Delta E_\text{int} = nC_V\Delta T = (3.0)(12.47)(200) = \boxed{7479\;\text{J} \approx 7.5\;\text{kJ}}$$

두 과정 모두 동일하다. 이유: 이상기체의 내부 에너지는 온도에만 의존하므로 ($E_\text{int} = nC_VT$), 같은 $\Delta T$이면 경로에 관계없이 $\Delta E_\text{int}$이 같다.

**(b)**

**과정 A (등적)**: $W_A = 0$ (부피 불변)이므로

$$Q_A = \Delta E_\text{int} + W_A = 7479 + 0 = \boxed{7479\;\text{J} \approx 7.5\;\text{kJ}}$$

**과정 B (등압)**:

$$Q_B = nC_p\Delta T = (3.0)(20.78)(200) = \boxed{12465\;\text{J} \approx 12.5\;\text{kJ}}$$

**(c)**

**과정 A**: $\boxed{W_A = 0}$ (등적이므로)

**과정 B**: 열역학 제1법칙 $W_B = Q_B - \Delta E_\text{int}$:

$$W_B = 12465 - 7479 = \boxed{4986\;\text{J} \approx 5.0\;\text{kJ}}$$

검증: $W_B = nR\Delta T = (3.0)(8.31)(200) = 4986\;\text{J}$ $\checkmark$

과정 B에서 $Q$가 더 큰 이유: 등압 과정에서는 온도를 올리는 데 필요한 내부 에너지 증가분 $\Delta E_\text{int}$ 외에, 기체가 팽창하면서 외부에 한 일 $W = nR\Delta T$만큼의 에너지도 추가로 공급해야 한다. 등적 과정에서는 일이 0이므로, 열은 전부 내부 에너지 증가에만 사용된다. 따라서 $Q_B = Q_A + nR\Delta T$이다.
