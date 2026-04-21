# Chapter 14: Fluids — 풀이

---

## 문제 1 풀이

$h = 4.5\;\text{m}$, $p_0 = 1.01 \times 10^5\;\text{Pa}$, $\rho = 1000\;\text{kg/m}^3$

**(a)** 게이지 압력:

$$p_g = \rho g h = (1000)(9.80)(4.5) = 4.41 \times 10^4\;\text{Pa}$$

$$\boxed{p_g = 4.41 \times 10^4\;\text{Pa} \approx 44.1\;\text{kPa}}$$

**(b)** 절대 압력:

$$p = p_0 + \rho g h = 1.01 \times 10^5 + 4.41 \times 10^4 = 1.451 \times 10^5\;\text{Pa}$$

$$\boxed{p = 1.45 \times 10^5\;\text{Pa} \approx 145\;\text{kPa}}$$

**(c)** 물에 의한 순 힘은 게이지 압력에 의한 것이다 (대기압은 뚜껑 양쪽에서 상쇄):

$$F = p_g \cdot A = (4.41 \times 10^4)(0.040) = 1764\;\text{N}$$

$$\boxed{F \approx 1760\;\text{N} \approx 1.76\;\text{kN}}$$

---

## 문제 2 풀이

$d_i = 5.0\;\text{cm}$, $d_o = 30\;\text{cm}$, $M = 1800\;\text{kg}$

면적비:

$$\frac{A_o}{A_i} = \frac{\pi d_o^2/4}{\pi d_i^2/4} = \frac{d_o^2}{d_i^2} = \frac{(30)^2}{(5.0)^2} = \frac{900}{25} = 36$$

**(a)** 파스칼의 원리에 의해:

$$F_o = F_i \cdot \frac{A_o}{A_i} \quad \Rightarrow \quad F_i = \frac{F_o}{A_o/A_i} = \frac{Mg}{36} = \frac{(1800)(9.80)}{36} = \frac{17640}{36} = 490\;\text{N}$$

$$\boxed{F_i = 490\;\text{N}}$$

약 50 kgf — 한 손으로 펌프질 가능한 수준!

**(b)** 비압축성이므로 이동한 유체의 부피가 같다:

$$A_i d_i = A_o d_o = A_o \cdot \Delta h$$

$$d_i = \frac{A_o}{A_i} \cdot \Delta h = 36 \times 2.0 = 72\;\text{m}$$

$$\boxed{d_i = 72\;\text{m}}$$

실제로는 펌프를 여러 번 반복하여 이 거리를 누적한다.

**(c)** 작은 피스톤에서 한 일:

$$W_i = F_i \cdot d_i = (490)(72) = 35{,}280\;\text{J}$$

큰 피스톤에서 한 일:

$$W_o = F_o \cdot \Delta h = (17{,}640)(2.0) = 35{,}280\;\text{J}$$

$$\boxed{W_i = W_o = 35{,}280\;\text{J} \approx 35.3\;\text{kJ}}$$

힘은 36배 증폭되지만, 이동 거리는 1/36로 줄어 일은 동일하다. 에너지 보존 법칙이 성립한다.

---

## 문제 3 풀이

$\rho_{\text{ice}} = 917\;\text{kg/m}^3$, $\rho_{\text{sw}} = 1025\;\text{kg/m}^3$, $V = 0.50\;\text{m}^3$

**(a)** 떠 있는 조건 ($F_b = F_g$):

$$\rho_{\text{sw}} V_{\text{sub}} g = \rho_{\text{ice}} V g$$

$$\frac{V_{\text{sub}}}{V} = \frac{\rho_{\text{ice}}}{\rho_{\text{sw}}} = \frac{917}{1025} = 0.8946$$

수면 위로 나와 있는 비율:

$$\frac{V_{\text{above}}}{V} = 1 - 0.8946 = 0.1054$$

$$\boxed{V_{\text{above}}/V \approx 10.5\%}$$

**(b)** 얼음의 질량: $m = \rho_{\text{ice}} V = 917 \times 0.50 = 458.5\;\text{kg}$

떠 있을 때 배제한 소금물의 부피: $V_{\text{sub}} = m/\rho_{\text{sw}} = 458.5/1025 = 0.4473\;\text{m}^3$

얼음이 녹으면 물이 된다. 녹은 물의 부피 (순수한 물이 아닌 소금물이 된다고 가정하면 약간 다르지만, 얼음이 녹은 물의 질량은 $m$으로 같고 이 물이 차지하는 부피는 $V_{\text{melt}} = m/\rho_w$이다. 그러나 문제를 단순화하여 녹은 물이 소금물과 같은 밀도가 된다고 하면 $V_{\text{melt}} = m/\rho_{\text{sw}} = V_{\text{sub}}$):

더 정확한 풀이: 순수 얼음이 녹으면 순수한 물($\rho_w = 1000\;\text{kg/m}^3$)이 된다.

$$V_{\text{melt}} = \frac{m}{\rho_w} = \frac{458.5}{1000} = 0.4585\;\text{m}^3$$

배제했던 부피: $V_{\text{sub}} = 0.4473\;\text{m}^3$

$V_{\text{melt}} > V_{\text{sub}}$이므로 녹은 물이 배제했던 공간보다 많다.

$$\boxed{\text{수면이 약간 올라간다.}}$$

순수한 물에 떠 있는 순수 얼음의 경우에는 $V_{\text{melt}} = m/\rho_w = V_{\text{sub}}$로 정확히 같아서 수면이 변하지 않는다.

**(c)** 얼음 속의 돌맹이는 떠 있는 동안 자기 질량만큼의 소금물을 배제한다 ($V_{\text{displaced}} = m_{\text{rock}}/\rho_{\text{sw}}$). 얼음이 녹으면 돌은 가라앉고, 가라앉은 돌은 자기 부피($V_{\text{rock}} = m_{\text{rock}}/\rho_{\text{rock}}$)만큼의 물을 배제한다. $\rho_{\text{rock}} > \rho_{\text{sw}}$이므로 $V_{\text{rock}} < m_{\text{rock}}/\rho_{\text{sw}}$이다.

$$\boxed{\text{수면이 내려간다.}}$$

돌이 떠 있을 때는 무게 기준으로 물을 밀어내고, 가라앉으면 부피 기준으로 밀어내므로, 밀도가 큰 돌의 경우 가라앉을 때 배제하는 부피가 줄어든다.

---

## 문제 4 풀이

$\rho_{\text{obj}} = 600\;\text{kg/m}^3$, $H = 0.10\;\text{m}$, $\rho_w = 1000\;\text{kg/m}^3$

블록의 밑면적을 $A$라 하면, 부피 $V = AH$, 질량 $m = \rho_{\text{obj}} A H$.

**(a)** 떠 있는 조건:

$$F_b = F_g$$

$$\rho_w (Ah) g = \rho_{\text{obj}} (AH) g$$

$$h = \frac{\rho_{\text{obj}}}{\rho_w} H = \frac{600}{1000} \times 0.10 = 0.060\;\text{m}$$

$$\boxed{h = 6.0\;\text{cm}}$$

**(b)** 완전히 잠겼을 때:

부력: $F_b = \rho_w V g = \rho_w A H g$

무게: $F_g = \rho_{\text{obj}} A H g$

뉴턴의 제2법칙 (위쪽 양의 방향):

$$F_b - F_g = ma$$

$$\rho_w A H g - \rho_{\text{obj}} A H g = \rho_{\text{obj}} A H \cdot a$$

$$a = \frac{(\rho_w - \rho_{\text{obj}})}{\rho_{\text{obj}}} g = \frac{(1000 - 600)}{600} \times 9.80 = \frac{400}{600} \times 9.80 = 6.53\;\text{m/s}^2$$

$$\boxed{a = 6.5\;\text{m/s}^2 \text{ (위 방향)}}$$

---

## 문제 5 풀이

수평 관: $y_1 = y_2$, 단면적 $A_1 \to A_2$ ($A_2 < A_1$), 유체 밀도 $\rho$

**(a)** 연속 방정식:

$$A_1 v_1 = A_2 v_2$$

$$\boxed{v_2 = v_1 \frac{A_1}{A_2}}$$

**(b)** 수평 베르누이 방정식:

$$p_1 + \frac{1}{2}\rho v_1^2 = p_2 + \frac{1}{2}\rho v_2^2$$

$$p_1 - p_2 = \frac{1}{2}\rho(v_2^2 - v_1^2) = \frac{1}{2}\rho\left[\left(\frac{A_1}{A_2}\right)^2 v_1^2 - v_1^2\right]$$

$$\boxed{p_1 - p_2 = \frac{1}{2}\rho v_1^2\left[\left(\frac{A_1}{A_2}\right)^2 - 1\right]}$$

**(c)** 위 결과에서 $v_1$에 대해 풀면:

$$v_1^2 = \frac{2(p_1 - p_2)}{\rho\left[\left(\frac{A_1}{A_2}\right)^2 - 1\right]}$$

$$v_1 = \sqrt{\frac{2\Delta p}{\rho\left[\left(\frac{A_1}{A_2}\right)^2 - 1\right]}}$$

체적 유량:

$$R_V = A_1 v_1 = A_1 \sqrt{\frac{2\Delta p}{\rho\left[\left(\frac{A_1}{A_2}\right)^2 - 1\right]}}$$

분모를 정리하면 $\left(\frac{A_1}{A_2}\right)^2 - 1 = \frac{A_1^2 - A_2^2}{A_2^2}$이므로:

$$\boxed{R_V = A_1 A_2 \sqrt{\frac{2\Delta p}{\rho(A_1^2 - A_2^2)}}}$$

이것이 벤투리 유량계의 원리이다. 두 지점의 압력 차만 측정하면 유량을 알 수 있다.

---

## 문제 6 풀이

큰 물탱크, 구멍은 수면 아래 깊이 $h$.

**(a)** 수면(점 1)과 구멍(점 2)에 베르누이 방정식을 적용한다.

$$p_1 + \frac{1}{2}\rho v_1^2 + \rho g y_1 = p_2 + \frac{1}{2}\rho v_2^2 + \rho g y_2$$

- $p_1 = p_2 = p_0$ (수면과 구멍 모두 대기에 노출)
- $v_1 \approx 0$ (탱크가 충분히 크므로 수면 하강 속도 무시)
- $y_1 - y_2 = h$

$$p_0 + 0 + \rho g h = p_0 + \frac{1}{2}\rho v_2^2 + 0$$

$$\rho g h = \frac{1}{2}\rho v_2^2$$

$$\boxed{v_2 = v = \sqrt{2gh}}$$

이것이 토리첼리의 정리이다. 높이 $h$에서 자유낙하하는 물체의 속력과 동일하다!

**(b)** $A = 2.0\;\text{cm}^2 = 2.0 \times 10^{-4}\;\text{m}^2$, $h = 5.0\;\text{m}$

$$v = \sqrt{2(9.80)(5.0)} = \sqrt{98.0} = 9.90\;\text{m/s}$$

$$R_V = Av = (2.0 \times 10^{-4})(9.90) = 1.98 \times 10^{-3}\;\text{m}^3/\text{s}$$

$$\boxed{R_V \approx 2.0 \times 10^{-3}\;\text{m}^3/\text{s} = 2.0\;\text{L/s}}$$

**(c)** 연속 방정식에 의해:

$$A_{\text{tank}} v_{\text{surface}} = A v$$

$$v_{\text{surface}} = \frac{Av}{A_{\text{tank}}} = \frac{(2.0 \times 10^{-4})(9.90)}{1.0} = 1.98 \times 10^{-3}\;\text{m/s}$$

$$\boxed{v_{\text{surface}} \approx 2.0 \times 10^{-3}\;\text{m/s} = 2.0\;\text{mm/s}}$$

이는 매우 느리므로 앞서 $v_1 \approx 0$으로 놓은 근사가 정당화된다.

---

## 문제 7 풀이

$\rho = 1000\;\text{kg/m}^3$, $A_1 = 8.0\;\text{cm}^2$, $A_2 = 4.0\;\text{cm}^2$, $\Delta y = y_2 - y_1 = 2.0\;\text{m}$

$p_1 = 200\;\text{kPa} = 2.00 \times 10^5\;\text{Pa}$, $v_1 = 3.0\;\text{m/s}$

**(a)** 연속 방정식:

$$v_2 = v_1 \frac{A_1}{A_2} = 3.0 \times \frac{8.0}{4.0} = 6.0\;\text{m/s}$$

$$\boxed{v_2 = 6.0\;\text{m/s}}$$

**(b)** 베르누이 방정식:

$$p_1 + \frac{1}{2}\rho v_1^2 + \rho g y_1 = p_2 + \frac{1}{2}\rho v_2^2 + \rho g y_2$$

$$p_2 = p_1 + \frac{1}{2}\rho(v_1^2 - v_2^2) + \rho g(y_1 - y_2)$$

$$p_2 = 2.00 \times 10^5 + \frac{1}{2}(1000)(3.0^2 - 6.0^2) + (1000)(9.80)(-2.0)$$

$$p_2 = 2.00 \times 10^5 + \frac{1}{2}(1000)(9.0 - 36.0) + (-19{,}600)$$

$$p_2 = 2.00 \times 10^5 + (-13{,}500) + (-19{,}600)$$

$$p_2 = 2.00 \times 10^5 - 33{,}100 = 166{,}900\;\text{Pa}$$

$$\boxed{p_2 \approx 167\;\text{kPa}}$$

**(c)** 베르누이 방정식 $p + \frac{1}{2}\rho v^2 + \rho g y = \text{일정}$은 유체의 에너지 보존 법칙이다. 세 항은 각각 압력 에너지 밀도, 운동 에너지 밀도, 중력 퍼텐셜 에너지 밀도를 나타낸다.

단면적이 좁아지면 연속 방정식에 의해 유속이 빨라져 운동 에너지 밀도($\frac{1}{2}\rho v^2$)가 증가한다. 또한 높이가 올라가면 중력 퍼텐셜 에너지 밀도($\rho g y$)도 증가한다. 세 항의 합이 일정해야 하므로, 압력 에너지 밀도($p$)가 반드시 감소해야 한다.

수치적으로: 운동 에너지 증가분($13.5\;\text{kPa}$)과 중력 퍼텐셜 에너지 증가분($19.6\;\text{kPa}$)의 합 $33.1\;\text{kPa}$만큼 압력이 감소하여, $200\;\text{kPa}$에서 $167\;\text{kPa}$로 낮아진다. $\boxed{\text{에너지 보존에 의해, 운동에너지와 위치에너지가 증가하면 압력이 낮아진다.}}$
