# Chapter 11: Rolling, Torque, and Angular Momentum — 풀이

---

## 문제 1 풀이

속이 찬 구: $R = 0.20\;\text{m}$, $M = 5.0\;\text{kg}$, $I_\text{com} = \frac{2}{5}MR^2$, $h = 3.0\;\text{m}$

**(a)** 에너지 보존:

$$Mgh = \frac{1}{2}Mv_\text{com}^2 + \frac{1}{2}I_\text{com}\omega^2$$

미끄러짐 없는 조건 $\omega = v_\text{com}/R$을 대입:

$$Mgh = \frac{1}{2}Mv_\text{com}^2 + \frac{1}{2}\left(\frac{2}{5}MR^2\right)\frac{v_\text{com}^2}{R^2} = \frac{1}{2}Mv_\text{com}^2 + \frac{1}{5}Mv_\text{com}^2 = \frac{7}{10}Mv_\text{com}^2$$

$$v_\text{com} = \sqrt{\frac{10gh}{7}} = \sqrt{\frac{10 \times 9.80 \times 3.0}{7}} = \sqrt{42.0} = \boxed{6.48\;\text{m/s}}$$

**(b)**

$$K_\text{trans} = \frac{1}{2}Mv_\text{com}^2, \quad K_\text{rot} = \frac{1}{2}I_\text{com}\omega^2 = \frac{1}{5}Mv_\text{com}^2$$

$$\frac{K_\text{trans}}{K_\text{rot}} = \frac{\frac{1}{2}Mv_\text{com}^2}{\frac{1}{5}Mv_\text{com}^2} = \frac{5}{2} = \boxed{2.5}$$

**(c)** 속이 빈 원통: $c = I_\text{com}/MR^2 = 1$

$$v_\text{com,cylinder} = \sqrt{\frac{2gh}{1 + c}} = \sqrt{\frac{2 \times 9.80 \times 3.0}{1 + 1}} = \sqrt{29.4} = 5.42\;\text{m/s}$$

속이 찬 구($v = 6.48\;\text{m/s}$)가 속이 빈 원통($v = 5.42\;\text{m/s}$)보다 빠르므로, $\boxed{\text{속이 찬 구가 먼저 도착한다.}}$

이유: 속이 찬 구는 관성모멘트 비율 $c$가 작아 같은 에너지에서 회전에 쓰이는 비율이 적고, 병진에 더 많은 에너지가 배분된다.

---

## 문제 2 풀이

**(a)** 경사면 아래 방향을 양의 방향, 경사면에 수직인 방향을 양의 법선 방향으로 잡는다.

병진 운동 방정식 (경사면 방향):

$$Mg\sin\theta - f = Ma_\text{com} \quad \cdots\;(1)$$

여기서 $f$는 정지마찰력 (경사면 위 방향).

회전 운동 방정식 (질량중심에 대해):

$$fR = I_\text{com}\alpha = cMR^2 \cdot \alpha \quad \cdots\;(2)$$

미끄러짐 없는 구름 조건: $a_\text{com} = \alpha R$ $\implies$ $\alpha = a_\text{com}/R$

식 (2)에 대입:

$$fR = cMR^2 \cdot \frac{a_\text{com}}{R} = cMRa_\text{com}$$

$$f = cMa_\text{com} \quad \cdots\;(3)$$

식 (3)을 식 (1)에 대입:

$$Mg\sin\theta - cMa_\text{com} = Ma_\text{com}$$

$$Mg\sin\theta = Ma_\text{com}(1 + c)$$

$$\boxed{a_\text{com} = \frac{g\sin\theta}{1 + c}}$$

**(b)** 에너지 보존: $Mgh = \frac{1}{2}Mv_\text{com}^2 + \frac{1}{2}I_\text{com}\omega^2$

$\omega = v_\text{com}/R$, $I_\text{com} = cMR^2$을 대입:

$$Mgh = \frac{1}{2}Mv_\text{com}^2 + \frac{1}{2}cMR^2 \cdot \frac{v_\text{com}^2}{R^2} = \frac{1}{2}Mv_\text{com}^2(1 + c)$$

$$v_\text{com}^2 = \frac{2gh}{1 + c}$$

$$\boxed{v_\text{com} = \sqrt{\frac{2gh}{1 + c}}}$$

**(c)** $a_\text{com}$과 $v_\text{com}$ 모두 $M$과 $R$에 의존하지 않는다. 이는 관성모멘트가 $I_\text{com} = cMR^2$ 형태이기 때문이다. 운동 방정식과 에너지 보존식에서 $M$은 양변에서 약분되고, 미끄러짐 없는 구름 조건 $v_\text{com} = \omega R$에 의해 $R$도 약분된다. 따라서 같은 형태($c$ 값이 같은)의 물체는 질량이나 크기에 관계없이 동일한 가속도와 속력을 갖는다.

---

## 문제 3 풀이

$\vec{r} = 3.0\,\hat{i} - 2.0\,\hat{j} + 1.0\,\hat{k}\;\text{m}$, $\vec{F} = 4.0\,\hat{i} + 5.0\,\hat{j} - 3.0\,\hat{k}\;\text{N}$

**(a)**

$$\vec{\tau} = \vec{r} \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 3.0 & -2.0 & 1.0 \\ 4.0 & 5.0 & -3.0 \end{vmatrix}$$

$$\tau_x = (-2.0)(-3.0) - (1.0)(5.0) = 6.0 - 5.0 = 1.0$$

$$\tau_y = (1.0)(4.0) - (3.0)(-3.0) = 4.0 + 9.0 = 13.0$$

$$\tau_z = (3.0)(5.0) - (-2.0)(4.0) = 15.0 + 8.0 = 23.0$$

$$\boxed{\vec{\tau} = 1.0\,\hat{i} + 13.0\,\hat{j} + 23.0\,\hat{k}\;\text{N·m}}$$

**(b)**

$$|\vec{\tau}\,| = \sqrt{1.0^2 + 13.0^2 + 23.0^2} = \sqrt{1.0 + 169.0 + 529.0} = \sqrt{699.0} = \boxed{26.44\;\text{N·m}}$$

**(c)** 내적:

$$\vec{r} \cdot \vec{F} = (3.0)(4.0) + (-2.0)(5.0) + (1.0)(-3.0) = 12.0 - 10.0 - 3.0 = -1.0$$

크기:

$$|\vec{r}\,| = \sqrt{9.0 + 4.0 + 1.0} = \sqrt{14.0} = 3.742\;\text{m}$$

$$|\vec{F}\,| = \sqrt{16.0 + 25.0 + 9.0} = \sqrt{50.0} = 7.071\;\text{N}$$

외적으로부터 $\sin\phi$:

$$\sin\phi = \frac{|\vec{\tau}\,|}{|\vec{r}\,||\vec{F}\,|} = \frac{26.44}{3.742 \times 7.071} = \frac{26.44}{26.46} = 0.9992$$

내적으로부터 $\cos\phi$:

$$\cos\phi = \frac{\vec{r} \cdot \vec{F}}{|\vec{r}\,||\vec{F}\,|} = \frac{-1.0}{26.46} = -0.0378$$

$$\phi = \arccos(-0.0378) = \boxed{92.2°}$$

검증: $\sin(92.2°) = 0.9993 \approx 0.999$ $\checkmark$

---

## 문제 4 풀이

$m = 2.0\;\text{kg}$, $\vec{r} = 4.0\,\hat{i} + 3.0\,\hat{j}\;\text{m}$, $\vec{v} = -5.0\,\hat{i} + 2.0\,\hat{j}\;\text{m/s}$

**(a)**

$$\vec{r} \times \vec{v} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 4.0 & 3.0 & 0 \\ -5.0 & 2.0 & 0 \end{vmatrix}$$

$$= \hat{k}[(4.0)(2.0) - (3.0)(-5.0)] = \hat{k}(8.0 + 15.0) = 23.0\,\hat{k}\;\text{m}^2/\text{s}$$

$$\vec{\ell} = m(\vec{r} \times \vec{v}) = 2.0 \times 23.0\,\hat{k} = \boxed{46.0\,\hat{k}\;\text{kg·m}^2/\text{s}}$$

**(b)** $\vec{F} = 6.0\,\hat{i}\;\text{N}$

$$\vec{\tau} = \vec{r} \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 4.0 & 3.0 & 0 \\ 6.0 & 0 & 0 \end{vmatrix}$$

$$= \hat{k}[(4.0)(0) - (3.0)(6.0)] = -18.0\,\hat{k}$$

$$\boxed{\vec{\tau} = -18.0\,\hat{k}\;\text{N·m}}$$

**(c)** $\vec{\ell} = 46.0\,\hat{k}$ ($+z$ 방향)이고 $\vec{\tau} = -18.0\,\hat{k}$ ($-z$ 방향)이다. $\vec{\tau} = d\vec{\ell}/dt$이므로, 각운동량이 시간에 따라 감소하는 방향으로 변한다. 즉 토크가 각운동량과 반대 방향이므로, 각운동량의 크기가 줄어든다. 이는 힘 $\vec{F}$가 입자의 회전을 감속시키는 방향으로 작용함을 의미한다.

---

## 문제 5 풀이

원판: $M = 120\;\text{kg}$, $R_1 = 0.80\;\text{m}$, $I_\text{disk} = \frac{1}{2}MR_1^2$

사람: $m = 60\;\text{kg}$ (질점), 처음 위치 $r = R_1$

$\omega_1 = 2.0\;\text{rad/s}$

**(a)**

$$I_\text{disk} = \frac{1}{2}(120)(0.80)^2 = \frac{1}{2}(120)(0.64) = 38.4\;\text{kg·m}^2$$

$$I_\text{person,1} = m R_1^2 = (60)(0.80)^2 = (60)(0.64) = 38.4\;\text{kg·m}^2$$

$$I_1 = I_\text{disk} + I_\text{person,1} = 38.4 + 38.4 = 76.8\;\text{kg·m}^2$$

$$L = I_1 \omega_1 = 76.8 \times 2.0 = \boxed{153.6\;\text{kg·m}^2/\text{s}}$$

**(b)** 사람이 중심으로 이동: $r = 0$ $\implies$ $I_\text{person,2} = 0$

$$I_2 = I_\text{disk} + I_\text{person,2} = 38.4 + 0 = 38.4\;\text{kg·m}^2$$

각운동량 보존 ($L = I_1\omega_1 = I_2\omega_2$):

$$\omega_2 = \frac{I_1}{I_2}\omega_1 = \frac{76.8}{38.4} \times 2.0 = \boxed{4.0\;\text{rad/s}}$$

**(c)**

$$K_1 = \frac{1}{2}I_1\omega_1^2 = \frac{1}{2}(76.8)(2.0)^2 = \frac{1}{2}(76.8)(4.0) = 153.6\;\text{J}$$

$$K_2 = \frac{1}{2}I_2\omega_2^2 = \frac{1}{2}(38.4)(4.0)^2 = \frac{1}{2}(38.4)(16.0) = 307.2\;\text{J}$$

$$\boxed{K_1 = 153.6\;\text{J}, \quad K_2 = 307.2\;\text{J}}$$

운동에너지가 $307.2 - 153.6 = 153.6\;\text{J}$ 증가했다. 이 에너지는 사람이 중심을 향해 걸어갈 때 한 내부 일(internal work)에서 온 것이다. 사람은 원심 방향의 관성력에 대항하여 중심 방향으로 이동하므로 양의 일을 하며, 이 일이 계의 운동에너지 증가로 나타난다.

---

## 문제 6 풀이

$R = 3.0\;\text{cm} = 0.030\;\text{m}$, $R_0 = 0.50\;\text{cm} = 0.0050\;\text{m}$

$M = 0.10\;\text{kg}$, $I = 4.5 \times 10^{-5}\;\text{kg·m}^2$

요요는 축에서 실이 풀리며 내려간다. 실은 축 반지름 $R_0$에서 접선 방향으로 풀린다.

**(a)** 병진 운동 방정식 (아래 방향 양):

$$Mg - T = Ma_\text{com} \quad \cdots\;(1)$$

회전 운동 방정식 (질량중심에 대해):

$$TR_0 = I\alpha \quad \cdots\;(2)$$

미끄러짐 없는 조건: $a_\text{com} = \alpha R_0$ $\implies$ $\alpha = a_\text{com}/R_0$

식 (2)에서:

$$T = \frac{I\alpha}{R_0} = \frac{Ia_\text{com}}{R_0^2} \quad \cdots\;(3)$$

식 (3)을 식 (1)에 대입:

$$Mg - \frac{Ia_\text{com}}{R_0^2} = Ma_\text{com}$$

$$Mg = a_\text{com}\left(M + \frac{I}{R_0^2}\right)$$

$$a_\text{com} = \frac{Mg}{M + I/R_0^2} = \frac{0.10 \times 9.80}{0.10 + \frac{4.5 \times 10^{-5}}{(0.0050)^2}} = \frac{0.980}{0.10 + 1.80} = \frac{0.980}{1.90} = 0.516\;\text{m/s}^2$$

식 (3)에서:

$$T = \frac{Ia_\text{com}}{R_0^2} = \frac{4.5 \times 10^{-5} \times 0.516}{(0.0050)^2} = \frac{2.322 \times 10^{-5}}{2.5 \times 10^{-5}} = 0.929\;\text{N}$$

$$\boxed{T = 0.929\;\text{N} \approx 0.93\;\text{N}}$$

**(b)**

$$\boxed{a_\text{com} = 0.516\;\text{m/s}^2 \approx 0.52\;\text{m/s}^2}$$

**(c)** 요요의 가속도 $a_\text{com} = 0.52\;\text{m/s}^2$은 $g = 9.80\;\text{m/s}^2$의 약 $5.3\%$에 불과하다. 이는 요요의 관성모멘트 $I$가 축 반지름 $R_0$에 비해 매우 크기 때문이다. $I/R_0^2 \gg M$이므로 실에 걸리는 장력 $T$가 중력 $Mg$에 거의 가까워지고, 순가속력이 매우 작아진다. 물리적으로, 중력이 한 일의 대부분이 회전 운동에너지로 전환되고 병진 운동에너지로 가는 비율이 매우 작기 때문이다.

---

## 문제 7 풀이

$M = 0.50\;\text{kg}$, $r = 5.0\;\text{cm} = 0.050\;\text{m}$, $\omega = 40\;\text{rad/s}$, $I = 4.0 \times 10^{-4}\;\text{kg·m}^2$

**(a)** 중력에 의한 토크:

$$\tau = Mgr = 0.50 \times 9.80 \times 0.050 = \boxed{0.245\;\text{N·m}}$$

**(b)** 세차 각속도:

$$\Omega = \frac{Mgr}{I\omega} = \frac{\tau}{I\omega} = \frac{0.245}{4.0 \times 10^{-4} \times 40} = \frac{0.245}{0.016} = \boxed{15.3\;\text{rad/s}}$$

**(c)** 세차 각속도 $\Omega = \frac{Mgr}{I\omega}$이므로, $\omega$를 두 배로 증가시키면:

$$\Omega' = \frac{Mgr}{I(2\omega)} = \frac{\Omega}{2}$$

$\boxed{\text{세차 각속도는 절반으로 감소한다.}}$ 팽이가 더 빠르게 회전할수록 각운동량 $L = I\omega$가 커지고, 같은 크기의 토크로는 $L$의 방향을 천천히 변화시킬 수밖에 없기 때문이다.
