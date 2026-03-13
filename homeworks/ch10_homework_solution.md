# Chapter 10: Rotation — 풀이

---

## 문제 1 풀이

$\theta(t) = 3.0 - 2.0t + 4.0t^2 - 0.50t^3$

**(a)** 각속도는 $\omega = d\theta/dt$:

$$\omega(t) = -2.0 + 8.0t - 1.5t^2$$

$t = 2.0$ s 대입:

$$\omega(2.0) = -2.0 + 8.0(2.0) - 1.5(2.0)^2 = -2.0 + 16.0 - 6.0 = \boxed{8.0\;\text{rad/s}}$$

**(b)** 각가속도는 $\alpha = d\omega/dt$:

$$\alpha(t) = 8.0 - 3.0t$$

$t = 2.0$ s 대입:

$$\alpha(2.0) = 8.0 - 3.0(2.0) = \boxed{2.0\;\text{rad/s}^2}$$

**(c)** 순간 정지: $\omega = 0$

$$-2.0 + 8.0t - 1.5t^2 = 0$$

$$1.5t^2 - 8.0t + 2.0 = 0$$

근의 공식:

$$t = \frac{8.0 \pm \sqrt{64.0 - 12.0}}{3.0} = \frac{8.0 \pm 7.211}{3.0}$$

$$t = 5.07\;\text{s} \quad \text{또는} \quad t = 0.26\;\text{s}$$

$t > 0$인 두 시각 모두 유효: $\boxed{t \approx 0.26\;\text{s} \;\text{또는}\; t \approx 5.07\;\text{s}}$

---

## 문제 2 풀이

$\alpha = 0.40\;\text{rad/s}^2$, $\omega_0 = 0$

**(a)** $\omega = \omega_0 + \alpha t$에서:

$$t = \frac{\omega - \omega_0}{\alpha} = \frac{6.0 - 0}{0.40} = \boxed{15\;\text{s}}$$

**(b)** $\theta - \theta_0 = \omega_0 t + \frac{1}{2}\alpha t^2$에서:

$$\Delta\theta = 0 + \frac{1}{2}(0.40)(15)^2 = \boxed{45\;\text{rad}}$$

**(c)** 감속 시: $\omega_0' = 6.0$ rad/s, $\omega' = 0$, $\alpha' = -0.20\;\text{rad/s}^2$

$\omega'^2 = \omega_0'^2 + 2\alpha'(\Delta\theta')$에서:

$$\Delta\theta' = \frac{\omega'^2 - \omega_0'^2}{2\alpha'} = \frac{0 - 36.0}{2(-0.20)} = \boxed{90\;\text{rad}}$$

---

## 문제 3 풀이

**(a)**

$$\boxed{v = \omega r}, \quad \boxed{a_t = \alpha r}, \quad \boxed{a_r = \omega^2 r = \frac{v^2}{r}}$$

**(b)** $R = 0.30$ m, $\omega = 10$ rad/s, $\alpha = 5.0\;\text{rad/s}^2$

$$a_t = \alpha R = (5.0)(0.30) = \boxed{1.5\;\text{m/s}^2}$$

$$a_r = \omega^2 R = (10)^2(0.30) = \boxed{30\;\text{m/s}^2}$$

$$a = \sqrt{a_t^2 + a_r^2} = \sqrt{1.5^2 + 30^2} = \sqrt{2.25 + 900} = \boxed{30.04\;\text{m/s}^2}$$

**(c)** 총 가속도와 반지름 방향 사이의 각도:

$$\phi = \arctan\frac{a_t}{a_r} = \arctan\frac{1.5}{30} = \boxed{2.9°}$$

---

## 문제 4 풀이

$M = 5.0$ kg, $R = 0.20$ m

**(a)** 균일한 원판의 중심축에 대한 관성모멘트:

$$I_{\text{com}} = \frac{1}{2}MR^2 = \frac{1}{2}(5.0)(0.20)^2 = \boxed{0.10\;\text{kg·m}^2}$$

**(b)** 평행축 정리: $I = I_{\text{com}} + Mh^2$, 여기서 $h = R$ (중심에서 가장자리까지 거리):

$$I = \frac{1}{2}MR^2 + MR^2 = \frac{3}{2}MR^2 = \frac{3}{2}(5.0)(0.20)^2 = \boxed{0.30\;\text{kg·m}^2}$$

**(c)** 회전 운동에너지:

$$K = \frac{1}{2}I_{\text{com}}\omega^2 = \frac{1}{2}(0.10)(12)^2 = \boxed{7.2\;\text{J}}$$

---

## 문제 5 풀이

질량 $M$, 길이 $L$인 균일한 막대. 선밀도 $\lambda = M/L$.

**(a)** 중심에 원점을 놓으면 $x$는 $-L/2$에서 $+L/2$까지. $dm = \frac{M}{L}dx$.

$$I_{\text{com}} = \int_{-L/2}^{L/2} x^2 \frac{M}{L}\,dx = \frac{M}{L}\left[\frac{x^3}{3}\right]_{-L/2}^{L/2}$$

$$= \frac{M}{L} \cdot \frac{1}{3}\left[\left(\frac{L}{2}\right)^3 - \left(-\frac{L}{2}\right)^3\right] = \frac{M}{3L}\cdot 2\cdot\frac{L^3}{8} = \boxed{\frac{1}{12}ML^2}$$

**(b)** 평행축 정리 적용. 한쪽 끝은 중심에서 $h = L/2$ 만큼 떨어져 있다:

$$I_{\text{end}} = I_{\text{com}} + Mh^2 = \frac{1}{12}ML^2 + M\left(\frac{L}{2}\right)^2 = \frac{1}{12}ML^2 + \frac{1}{4}ML^2 = \boxed{\frac{1}{3}ML^2}$$

**(c)** 직접 적분으로 검증. 한쪽 끝에 원점을 놓으면 $x$는 $0$에서 $L$까지:

$$I_{\text{end}} = \int_0^L x^2 \frac{M}{L}\,dx = \frac{M}{L}\left[\frac{x^3}{3}\right]_0^L = \frac{M}{L}\cdot\frac{L^3}{3} = \boxed{\frac{1}{3}ML^2}$$

(b)의 결과와 일치한다.

---

## 문제 6 풀이

$R = 0.50$ m, $M = 20$ kg, $\tau = 8.0\;\text{N·m}$, $\omega_0 = 0$

원판의 관성모멘트: $I = \frac{1}{2}MR^2 = \frac{1}{2}(20)(0.50)^2 = 2.5\;\text{kg·m}^2$

**(a)** 뉴턴 제2법칙 (회전): $\tau = I\alpha$

$$\alpha = \frac{\tau}{I} = \frac{8.0}{2.5} = \boxed{3.2\;\text{rad/s}^2}$$

**(b)** $\omega = \omega_0 + \alpha t = 0 + (3.2)(5.0) = \boxed{16\;\text{rad/s}}$

**(c)** 먼저 각변위를 구한다:

$$\Delta\theta = \omega_0 t + \frac{1}{2}\alpha t^2 = 0 + \frac{1}{2}(3.2)(5.0)^2 = 40\;\text{rad}$$

일정한 토크가 한 일:

$$W = \tau \cdot \Delta\theta = (8.0)(40) = \boxed{320\;\text{J}}$$

검증: $W = \Delta K = \frac{1}{2}I\omega^2 - 0 = \frac{1}{2}(2.5)(16)^2 = 320$ J ✓

**(d)** 순간 일률:

$$P = \tau\omega = (8.0)(16) = \boxed{128\;\text{W}}$$

---

## 문제 7 풀이

질량 $m_1$, $m_2$가 길이 $L$인 막대 양 끝에 고정. 회전축은 $m_1$에서 거리 $d$.

**(a)** $m_1$은 축에서 거리 $d$, $m_2$는 축에서 거리 $(L - d)$:

$$\boxed{I = m_1 d^2 + m_2(L - d)^2}$$

**(b)** $I$를 최소화:

$$\frac{dI}{dd} = 2m_1 d - 2m_2(L - d) = 0$$

$$m_1 d = m_2(L - d)$$

$$m_1 d = m_2 L - m_2 d$$

$$d(m_1 + m_2) = m_2 L$$

$$\boxed{d = \frac{m_2 L}{m_1 + m_2}}$$

($d^2I/dd^2 = 2(m_1 + m_2) > 0$이므로 확실히 최솟값이다.)

**(c)** $m_1$을 원점에 놓으면 질량중심의 위치는:

$$x_{\text{com}} = \frac{m_1 \cdot 0 + m_2 \cdot L}{m_1 + m_2} = \frac{m_2 L}{m_1 + m_2}$$

이는 (b)의 결과 $d$와 정확히 같다. 따라서 $\boxed{I\text{가 최소가 되는 회전축의 위치는 질량중심을 지나는 축이다.}}$

이는 평행축 정리 $I = I_{\text{com}} + Mh^2$에서 $h = 0$일 때 $I$가 최소가 된다는 일반적 결론과 일치한다.
