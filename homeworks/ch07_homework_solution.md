# Chapter 7: Kinetic Energy and Work — 풀이

---

## 문제 1 풀이

$m = 1500\,\text{kg}$, $v_i = 0$, $F_{\text{net}} = 4000\,\text{N}$, $d = 200\,\text{m}$

**(a)** 알짜힘과 변위가 같은 방향이므로 ($\phi = 0°$):

$$W = F_{\text{net}} d \cos 0° = (4000\,\text{N})(200\,\text{m}) = \boxed{8.0 \times 10^5\,\text{J}}$$

**(b)** 일-운동에너지 정리: $W = K_f - K_i = \frac{1}{2}mv_f^2 - 0$

$$v_f = \sqrt{\frac{2W}{m}} = \sqrt{\frac{2(8.0 \times 10^5)}{1500}} = \sqrt{1066.7} = \boxed{32.7\,\text{m/s}}$$

**(c)** $K = W = F_{\text{net}} d$ 이므로:

$$d = \frac{K}{F_{\text{net}}} = \frac{6.0 \times 10^5}{4000} = \boxed{150\,\text{m}}$$

---

## 문제 2 풀이

**(a)** 일-운동에너지 정리:

$$\boxed{\Delta K = K_f - K_i = W}$$

- $K_i = \frac{1}{2}mv_i^2$: 초기 운동에너지
- $K_f = \frac{1}{2}mv_f^2$: 최종 운동에너지
- $W$: 물체에 한 알짜 일(net work)

운동에너지의 변화량은 물체에 한 알짜 일과 같다.

**(b)**

$$W = K_f - K_i = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2 = \boxed{\frac{1}{2}m(v_f^2 - v_i^2)}$$

**(c)** $W = Fd\cos\phi$에서:

- $0° \leq \phi < 90°$: $\cos\phi > 0$ $\implies$ $W > 0$ (양의 일). 힘의 변위 방향 성분이 변위와 같은 방향. 물체의 운동에너지 증가.
- $\phi = 90°$: $\cos\phi = 0$ $\implies$ $W = 0$ (일 없음). 힘이 변위에 수직. 운동에너지 변화 없음.
- $90° < \phi \leq 180°$: $\cos\phi < 0$ $\implies$ $W < 0$ (음의 일). 힘의 변위 방향 성분이 변위와 반대 방향. 물체의 운동에너지 감소.

---

## 문제 3 풀이

$\vec{F} = (3.0)\hat{i} + (-2.0)\hat{j}\;\text{N}$, $\vec{d} = (4.0)\hat{i} + (5.0)\hat{j}\;\text{m}$

**(a)** 내적으로 일을 계산:

$$W = \vec{F} \cdot \vec{d} = (3.0)(4.0) + (-2.0)(5.0) = 12.0 - 10.0 = \boxed{2.0\,\text{J}}$$

**(b)** 일-운동에너지 정리:

$$K_f = K_i + W = 20\,\text{J} + 2.0\,\text{J} = \boxed{22\,\text{J}}$$

**(c)** $K_f = \frac{1}{2}mv_f^2$이므로:

$$v_f = \sqrt{\frac{2K_f}{m}} = \sqrt{\frac{2(22)}{2.0}} = \sqrt{22} = \boxed{4.69\,\text{m/s}}$$

---

## 문제 4 풀이

$m = 5.0\,\text{kg}$, $d = 10\,\text{m}$, $T = 50\,\text{N}$, $\theta = 30°$

**(a)** 장력과 변위 사이의 각도가 $30°$:

$$W_T = Td\cos\theta = (50)(10)\cos 30° = 500 \times 0.866 = \boxed{433\,\text{J}}$$

**(b)** 중력은 변위(수평)에 수직 ($\phi = 90°$):

$$W_g = mgd\cos 90° = \boxed{0\,\text{J}}$$

**(c)** 수직항력도 변위에 수직 ($\phi = 90°$):

$$W_N = F_N d\cos 90° = \boxed{0\,\text{J}}$$

**(d)** 마찰이 없으므로 알짜 일 $W = W_T + W_g + W_N = 433\,\text{J}$.

일-운동에너지 정리 ($K_i = 0$):

$$W = \frac{1}{2}mv_f^2 \implies v_f = \sqrt{\frac{2W}{m}} = \sqrt{\frac{2(433)}{5.0}} = \sqrt{173.2} = \boxed{13.2\,\text{m/s}}$$

---

## 문제 5 풀이

**(a)** 용수철 힘: $F_x = -kx$. 블록이 $x = 0$에서 $x = x_f$까지 이동할 때:

$$W_s = \int_{0}^{x_f} (-kx)\,dx = -k\left[\frac{x^2}{2}\right]_0^{x_f} = \boxed{-\frac{1}{2}kx_f^2}$$

**(b)** $x_i$에서 $x_f$까지:

$$W_s = \int_{x_i}^{x_f} (-kx)\,dx = -\frac{1}{2}k\left[x^2\right]_{x_i}^{x_f} = \boxed{\frac{1}{2}kx_i^2 - \frac{1}{2}kx_f^2}$$

**(c)** $x_i = A$에서 정지 상태 ($v_i = 0$)로 놓아줌. $x = 0$에서의 속력을 구한다.

일-운동에너지 정리: $W_s = K_f - K_i$

$$\frac{1}{2}kA^2 - \frac{1}{2}k(0)^2 = \frac{1}{2}mv^2 - 0$$

$$\frac{1}{2}kA^2 = \frac{1}{2}mv^2$$

$$\boxed{v = A\sqrt{\frac{k}{m}}}$$

---

## 문제 6 풀이

$m = 3.0\,\text{kg}$, $F(x) = (6.0 - 2.0x)\,\text{N}$, $x_i = 0$, $v_i = 4.0\,\text{m/s}$

**(a)** 변력이 한 일:

$$W = \int_{0}^{3.0} (6.0 - 2.0x)\,dx = \left[6.0x - x^2\right]_0^{3.0}$$

$$= (18.0 - 9.0) - 0 = \boxed{9.0\,\text{J}}$$

**(b)** 초기 운동에너지:

$$K_i = \frac{1}{2}mv_i^2 = \frac{1}{2}(3.0)(4.0)^2 = 24\,\text{J}$$

일-운동에너지 정리:

$$K_f = K_i + W = 24 + 9.0 = 33\,\text{J}$$

$$v_f = \sqrt{\frac{2K_f}{m}} = \sqrt{\frac{2(33)}{3.0}} = \sqrt{22} = \boxed{4.69\,\text{m/s}}$$

**(c)** 운동에너지가 최대가 되려면 $\frac{dK}{dx} = 0$이어야 한다. 일-운동에너지 정리에서 $K(x) = K_i + W(x)$이고, $\frac{dK}{dx} = F(x)$이므로:

$$F(x) = 6.0 - 2.0x = 0 \implies \boxed{x = 3.0\,\text{m}}$$

$x < 3.0$에서 $F > 0$ (양의 일), $x > 3.0$에서 $F < 0$ (음의 일)이므로 $x = 3.0\,\text{m}$에서 운동에너지가 최대이다.

---

## 문제 7 풀이

$m = 800\,\text{kg}$, $h = 20\,\text{m}$, 일정한 속력, $g = 9.8\,\text{m/s}^2$

일정한 속력이므로 가속도 $a = 0$, 즉 장력 $T = mg$.

**(a)** 장력은 위쪽, 변위도 위쪽 ($\phi = 0°$):

$$W_T = Th\cos 0° = mgh = (800)(9.8)(20) = \boxed{1.568 \times 10^5\,\text{J} \approx 1.57 \times 10^5\,\text{J}}$$

**(b)** 중력은 아래쪽, 변위는 위쪽 ($\phi = 180°$):

$$W_g = mgh\cos 180° = -mgh = -(800)(9.8)(20) = \boxed{-1.57 \times 10^5\,\text{J}}$$

**(c)** 알짜 일:

$$W_{\text{net}} = W_T + W_g = 1.57 \times 10^5 + (-1.57 \times 10^5) = \boxed{0\,\text{J}}$$

일-운동에너지 정리에 의하면 $W_{\text{net}} = \Delta K$. 일정한 속력이므로 $\Delta K = 0$이고, 이는 $W_{\text{net}} = 0$과 일치한다.

**(d)** 평균 일률:

$$P_{\text{avg}} = \frac{W_T}{\Delta t} = \frac{1.568 \times 10^5}{40} = 3920\,\text{W} \approx \boxed{3.92\,\text{kW}}$$

마력(hp) 단위로:

$$P_{\text{avg}} = \frac{3920}{746} = \boxed{5.25\,\text{hp}}$$
