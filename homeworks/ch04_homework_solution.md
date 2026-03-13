# Chapter 4: Motion in Two and Three Dimensions — 풀이

---

## 문제 1 풀이

$\vec{r}(t) = (3.0t^2 - 2.0t)\,\hat{i} + (4.0 - 1.5t^3)\,\hat{j}$ (m)

**(a)** $t = 2.0$ s:

$$x = 3.0(2.0)^2 - 2.0(2.0) = 12.0 - 4.0 = 8.0 \text{ m}$$

$$y = 4.0 - 1.5(2.0)^3 = 4.0 - 12.0 = -8.0 \text{ m}$$

$$\boxed{\vec{r} = 8.0\,\hat{i} - 8.0\,\hat{j} \text{ (m)}}$$

**(b)** 속도: $\vec{v} = \dfrac{d\vec{r}}{dt}$

$$v_x = \frac{dx}{dt} = 6.0t - 2.0, \quad v_y = \frac{dy}{dt} = -4.5t^2$$

$t = 2.0$ s:

$$v_x = 6.0(2.0) - 2.0 = 10.0 \text{ m/s}, \quad v_y = -4.5(2.0)^2 = -18.0 \text{ m/s}$$

$$\boxed{\vec{v} = 10.0\,\hat{i} - 18.0\,\hat{j} \text{ (m/s)}}$$

**(c)** 가속도: $\vec{a} = \dfrac{d\vec{v}}{dt}$

$$a_x = \frac{dv_x}{dt} = 6.0, \quad a_y = \frac{dv_y}{dt} = -9.0t$$

$t = 2.0$ s:

$$a_x = 6.0 \text{ m/s}^2, \quad a_y = -9.0(2.0) = -18.0 \text{ m/s}^2$$

$$\boxed{\vec{a} = 6.0\,\hat{i} - 18.0\,\hat{j} \text{ (m/s}^2\text{)}}$$

**(d)**

$$v = \sqrt{v_x^2 + v_y^2} = \sqrt{(10.0)^2 + (-18.0)^2} = \sqrt{424} = \boxed{20.6 \text{ m/s}}$$

$$\theta = \arctan\frac{v_y}{v_x} = \arctan\frac{-18.0}{10.0} = \boxed{-60.9°}$$

(속도 벡터가 $+x$축 아래 $60.9°$ 방향)

---

## 문제 2 풀이

$v_0 = 25.0$ m/s, $\theta_0 = 53.0°$, $g = 9.80$ m/s$^2$

초기 속도 성분:

$$v_{0x} = v_0\cos 53.0° = 25.0 \times 0.6018 = 15.05 \text{ m/s}$$

$$v_{0y} = v_0\sin 53.0° = 25.0 \times 0.7986 = 19.97 \text{ m/s}$$

**(a)** 최대 높이에서 $v_y = 0$:

$$v_y = v_{0y} - gt = 0 \implies t_{\text{top}} = \frac{v_{0y}}{g} = \frac{19.97}{9.80} = 2.038 \text{ s}$$

$$H = v_{0y}\,t_{\text{top}} - \frac{1}{2}g\,t_{\text{top}}^2 = 19.97(2.038) - \frac{1}{2}(9.80)(2.038)^2$$

$$= 40.70 - 20.35 = \boxed{20.3 \text{ m}}$$

**(b)** 체공 시간: $y - y_0 = 0$일 때

$$0 = v_{0y}\,t - \frac{1}{2}g\,t^2 = t\left(v_{0y} - \frac{1}{2}g\,t\right)$$

$t \neq 0$이므로:

$$t_f = \frac{2v_{0y}}{g} = \frac{2(19.97)}{9.80} = \boxed{4.08 \text{ s}}$$

**(c)** 수평 도달 거리:

$$R = v_{0x} \times t_f = 15.05 \times 4.08 = \boxed{61.4 \text{ m}}$$

검산: $R = \dfrac{v_0^2}{g}\sin 2\theta_0 = \dfrac{(25.0)^2}{9.80}\sin 106° = 63.78 \times 0.9613 = 61.3$ m $\checkmark$

**(d)** 지면 도달 순간:

$$v_x = v_{0x} = 15.05 \text{ m/s}$$

$$v_y = v_{0y} - g\,t_f = 19.97 - 9.80(4.08) = 19.97 - 39.98 = -20.0 \text{ m/s}$$

$$v = \sqrt{v_x^2 + v_y^2} = \sqrt{(15.05)^2 + (-20.0)^2} = \sqrt{226.5 + 400.0} = \boxed{25.0 \text{ m/s}}$$

(에너지 보존에 의해 같은 높이로 되돌아오므로 발사 시 속력과 같다.)

---

## 문제 3 풀이

**(a)** 수평 방향: $x - x_0 = (v_0\cos\theta_0)\,t$ ... (1)

수직 방향: $y - y_0 = (v_0\sin\theta_0)\,t - \frac{1}{2}g\,t^2$ ... (2)

같은 높이 조건 $y - y_0 = 0$을 (2)에 대입:

$$0 = (v_0\sin\theta_0)\,t - \frac{1}{2}g\,t^2 = t\!\left(v_0\sin\theta_0 - \frac{1}{2}g\,t\right)$$

$t = 0$ (출발)을 제외하면:

$$t_f = \frac{2v_0\sin\theta_0}{g}$$

이를 (1)에 대입:

$$R = (v_0\cos\theta_0)\,t_f = (v_0\cos\theta_0)\frac{2v_0\sin\theta_0}{g} = \frac{2v_0^2\sin\theta_0\cos\theta_0}{g}$$

$2\sin\theta_0\cos\theta_0 = \sin 2\theta_0$을 적용하면:

$$\boxed{R = \frac{v_0^2}{g}\sin 2\theta_0}$$

**(b)** $R$이 최대가 되려면 $\sin 2\theta_0 = 1$이어야 한다.

$$2\theta_0 = 90° \implies \boxed{\theta_0 = 45°}$$

이유: $\sin$ 함수의 최댓값은 1이며, 이는 인수가 $90°$일 때 달성된다. 발사 각도 $45°$는 수평 방향과 수직 방향의 속도 성분을 최적으로 배분하여, 체공 시간과 수평 속도의 곱을 극대화한다.

**(c)** 각도 $\theta_0$일 때: $R(\theta_0) = \dfrac{v_0^2}{g}\sin 2\theta_0$

각도 $(90° - \theta_0)$일 때: $R(90° - \theta_0) = \dfrac{v_0^2}{g}\sin 2(90° - \theta_0) = \dfrac{v_0^2}{g}\sin(180° - 2\theta_0)$

$\sin(180° - \alpha) = \sin\alpha$이므로:

$$\boxed{R(90° - \theta_0) = \frac{v_0^2}{g}\sin 2\theta_0 = R(\theta_0)}$$

물리적 의미: 예를 들어 $30°$와 $60°$로 같은 속력으로 발사하면 수평 도달 거리가 같다. $30°$는 수평 속도가 크지만 체공 시간이 짧고, $60°$는 수평 속도가 작지만 체공 시간이 길어서 결과적으로 같은 거리를 이동한다. 이 두 각도를 보각(complementary angles)이라 한다.

---

## 문제 4 풀이

절벽 꼭대기를 원점으로 잡는다. $+x$: 수평 던진 방향, $+y$: 위쪽.

초기 조건: $v_{0x} = 18.0$ m/s, $v_{0y} = 0$, $y_0 = 0$, 지면의 $y$ 좌표: $y = -45.0$ m.

**(a)** 수직 방향:

$$y = v_{0y}\,t - \frac{1}{2}g\,t^2 = -\frac{1}{2}g\,t^2$$

$$-45.0 = -\frac{1}{2}(9.80)\,t^2$$

$$t^2 = \frac{2 \times 45.0}{9.80} = 9.184$$

$$\boxed{t = 3.03 \text{ s}}$$

**(b)** 수평 거리:

$$x = v_{0x}\,t = 18.0 \times 3.03 = \boxed{54.5 \text{ m}}$$

**(c)** 지면 도달 시 속도:

$$v_x = v_{0x} = 18.0 \text{ m/s}$$

$$v_y = 0 - g\,t = -9.80 \times 3.03 = -29.7 \text{ m/s}$$

$$\boxed{\vec{v} = 18.0\,\hat{i} - 29.7\,\hat{j} \text{ (m/s)}}$$

**(d)** 수평면과 이루는 각도:

$$\theta = \arctan\frac{|v_y|}{v_x} = \arctan\frac{29.7}{18.0} = \boxed{58.8°} \text{ (수평면 아래)}$$

---

## 문제 5 풀이

$r = 50.0$ m, $a = 2.0g = 2.0 \times 9.80 = 19.6$ m/s$^2$

**(a)** 구심 가속도 $a = v^2/r$에서:

$$v = \sqrt{a \cdot r} = \sqrt{19.6 \times 50.0} = \sqrt{980} = \boxed{31.3 \text{ m/s}}$$

(약 $113$ km/h)

**(b)** 주기:

$$T = \frac{2\pi r}{v} = \frac{2\pi(50.0)}{31.3} = \frac{314.2}{31.3} = \boxed{10.0 \text{ s}}$$

**(c)** 속력을 $2v$로 늘리면:

$$a' = \frac{(2v)^2}{r} = \frac{4v^2}{r} = 4a$$

$$\boxed{a' = 4a \text{ (구심 가속도는 4배)}}$$

구심 가속도는 속력의 제곱에 비례하므로, 속력이 2배가 되면 가속도는 $2^2 = 4$배가 된다.

---

## 문제 6 풀이

$\vec{r}(t) = r\cos(\omega t)\,\hat{i} + r\sin(\omega t)\,\hat{j}$, 여기서 $\omega = v/r$.

**(a)** 속도:

$$\vec{v}(t) = \frac{d\vec{r}}{dt} = -r\omega\sin(\omega t)\,\hat{i} + r\omega\cos(\omega t)\,\hat{j}$$

속력:

$$|\vec{v}| = \sqrt{(-r\omega\sin\omega t)^2 + (r\omega\cos\omega t)^2} = r\omega\sqrt{\sin^2\omega t + \cos^2\omega t} = r\omega$$

$\omega = v/r$이므로:

$$\boxed{|\vec{v}| = r \cdot \frac{v}{r} = v} \quad \checkmark$$

**(b)** 가속도:

$$\vec{a}(t) = \frac{d\vec{v}}{dt} = -r\omega^2\cos(\omega t)\,\hat{i} - r\omega^2\sin(\omega t)\,\hat{j}$$

$$\boxed{\vec{a}(t) = -\omega^2\left[r\cos(\omega t)\,\hat{i} + r\sin(\omega t)\,\hat{j}\right] = -\omega^2\,\vec{r}(t)}$$

**(c)** 크기:

$$|\vec{a}| = \sqrt{(r\omega^2\cos\omega t)^2 + (r\omega^2\sin\omega t)^2} = r\omega^2\sqrt{\cos^2\omega t + \sin^2\omega t} = r\omega^2$$

$\omega = v/r$을 대입:

$$\boxed{|\vec{a}| = r\left(\frac{v}{r}\right)^2 = \frac{v^2}{r}}$$

방향: $\vec{a} = -\omega^2\,\vec{r}$이므로, 가속도 벡터는 위치 벡터 $\vec{r}$의 **반대 방향**, 즉 항상 **원의 중심을 향한다** (구심 방향). $\square$

---

## 문제 7 풀이

좌표계: $+x$ = 동쪽, $+y$ = 북쪽.

비행기의 대기(바람)에 대한 속력: $v_{PW} = 250$ km/h.
바람의 지면에 대한 속도: $\vec{v}_{WG} = 60.0\,\hat{i}$ km/h (서쪽에서 동쪽).

비행기의 지면에 대한 속도: $\vec{v}_{PG} = \vec{v}_{PW} + \vec{v}_{WG}$

조종사가 정북 이동을 원하므로 $\vec{v}_{PG}$는 $+y$ 방향만 가져야 한다.

비행기 기수를 정북에서 서쪽으로 $\theta$만큼 틀면:

$$\vec{v}_{PW} = -v_{PW}\sin\theta\,\hat{i} + v_{PW}\cos\theta\,\hat{j}$$

**(a)** $\vec{v}_{PG}$의 $x$성분 = 0:

$$-v_{PW}\sin\theta + v_{WG} = 0$$

$$\sin\theta = \frac{v_{WG}}{v_{PW}} = \frac{60.0}{250} = 0.240$$

$$\boxed{\theta = 13.9°} \text{ (정북에서 서쪽으로)}$$

**(b)** $\vec{v}_{PG}$의 $y$성분 (= 실제 속력):

$$v_{PG} = v_{PW}\cos\theta = 250\cos 13.9° = 250 \times 0.9708 = \boxed{243 \text{ km/h}}$$

**(c)** 거리 500 km:

바람이 불 때:

$$t_{\text{wind}} = \frac{500}{243} = 2.06 \text{ h} = \boxed{2\text{시간}\;4\text{분}}$$

바람이 없을 때:

$$t_{\text{calm}} = \frac{500}{250} = 2.00 \text{ h} = \boxed{2\text{시간}\;0\text{분}}$$

시간 차이:

$$\Delta t = 2.06 - 2.00 = \boxed{0.06 \text{ h} \approx 3.6\text{분}}$$

바람으로 인해 기수를 틀어야 하므로 북쪽 성분 속도가 줄어들어, 약 3.6분 더 걸린다.
