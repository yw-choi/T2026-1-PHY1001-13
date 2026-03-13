# Chapter 6: Force and Motion—II — 풀이

---

## 문제 1 풀이

$m = 5.0\,\text{kg}$, $\mu_s = 0.50$, $\mu_k = 0.30$

**(a)** 상자를 움직이려면 가하는 수평력이 최대 정지마찰력을 넘어야 한다.

수평면 위에 놓인 물체이므로 수직항력은 $F_N = mg$이다.

$$f_{s,\max} = \mu_s F_N = \mu_s mg = (0.50)(5.0)(9.8) = \boxed{24.5\,\text{N}}$$

**(b)** 상자가 움직이면 운동마찰력이 작용한다:

$$f_k = \mu_k mg = (0.30)(5.0)(9.8) = 14.7\,\text{N}$$

뉴턴 제2법칙 ($x$ 방향):

$$F - f_k = ma$$

$$a = \frac{F - f_k}{m} = \frac{24.5 - 14.7}{5.0} = \boxed{1.96\,\text{m/s}^2}$$

**(c)** 등속도 운동이므로 $a = 0$:

$$F = f_k = \mu_k mg = \boxed{14.7\,\text{N}}$$

---

## 문제 2 풀이

$m = 8.0\,\text{kg}$, $\theta = 30°$, $\mu_s = 0.40$, $\mu_k = 0.25$

**(a)** 빗면을 따라 내려가는 중력 성분:

$$F_{\parallel} = mg\sin\theta = (8.0)(9.8)\sin 30° = 39.2\,\text{N}$$

빗면에 수직인 수직항력:

$$F_N = mg\cos\theta = (8.0)(9.8)\cos 30° = 67.9\,\text{N}$$

최대 정지마찰력:

$$f_{s,\max} = \mu_s F_N = (0.40)(67.9) = 27.2\,\text{N}$$

$F_{\parallel} = 39.2\,\text{N} > f_{s,\max} = 27.2\,\text{N}$이므로, $\boxed{\text{물체는 정지해 있을 수 없고 미끄러진다.}}$

**(b)** 빗면 아래 방향을 양의 방향으로 잡으면:

$$ma = mg\sin\theta - f_k = mg\sin\theta - \mu_k mg\cos\theta$$

$$a = g(\sin\theta - \mu_k\cos\theta) = 9.8(\sin 30° - 0.25\cos 30°)$$

$$= 9.8(0.500 - 0.217) = \boxed{2.78\,\text{m/s}^2}$$

**(c)** $v_0 = 0$에서 출발하여 거리 $L = 3.0\,\text{m}$를 이동:

$$v^2 = v_0^2 + 2aL = 0 + 2(2.78)(3.0) = 16.68$$

$$v = \sqrt{16.68} = \boxed{4.08\,\text{m/s}}$$

---

## 문제 3 풀이

수평 아래 $\theta$ 방향으로 힘 $F$를 가하고, 물체가 미끄러지고 있는 상황.

**(a)** 자유물체도에 작용하는 힘:
- 중력 $mg$ (아래 방향)
- 수직항력 $F_N$ (위 방향)
- 가해진 힘 $F$: 수평 성분 $F\cos\theta$ (진행 방향), 수직 성분 $F\sin\theta$ (아래 방향)
- 운동마찰력 $f_k = \mu_k F_N$ (진행 반대 방향)

**(b)** $y$ 방향 (연직, 가속도 없음):

$$F_N - mg - F\sin\theta = 0$$

$x$ 방향 (수평, 가속도 $a$):

$$F\cos\theta - f_k = ma$$

$$F\cos\theta - \mu_k F_N = ma$$

**(c)** $y$ 방향 식에서:

$$\boxed{F_N = mg + F\sin\theta}$$

**(d)** $x$ 방향 식에 $F_N$을 대입:

$$F\cos\theta - \mu_k(mg + F\sin\theta) = ma$$

$$a = \frac{F\cos\theta - \mu_k(mg + F\sin\theta)}{m}$$

$$\boxed{a = \frac{F(\cos\theta - \mu_k\sin\theta) - \mu_k mg}{m}}$$

---

## 문제 4 풀이

$m = 70\,\text{kg}$, $C = 0.70$, $\rho = 1.21\,\text{kg/m}^3$

종단속력 공식: $v_t = \sqrt{\dfrac{2F_g}{C\rho A}} = \sqrt{\dfrac{2mg}{C\rho A}}$

**(a)** $A_1 = 0.50\,\text{m}^2$:

$$v_{t1} = \sqrt{\frac{2(70)(9.8)}{(0.70)(1.21)(0.50)}} = \sqrt{\frac{1372}{0.4235}} = \sqrt{3240}$$

$$= \boxed{56.9\,\text{m/s} \approx 205\,\text{km/h}}$$

**(b)** $A_2 = 1.50\,\text{m}^2$:

$$v_{t2} = \sqrt{\frac{2(70)(9.8)}{(0.70)(1.21)(1.50)}} = \sqrt{\frac{1372}{1.2705}} = \sqrt{1080}$$

$$= \boxed{32.9\,\text{m/s} \approx 118\,\text{km/h}}$$

**(c)**

$$\frac{v_{t2}}{v_{t1}} = \frac{32.9}{56.9} = 0.578$$

종단속력 공식에서 $v_t \propto \dfrac{1}{\sqrt{A}}$이므로:

$$\frac{v_{t2}}{v_{t1}} = \sqrt{\frac{A_1}{A_2}} = \sqrt{\frac{0.50}{1.50}} = \sqrt{\frac{1}{3}} = \boxed{0.577}$$

종단속력의 비는 단면적 비의 제곱근의 역수이다.

---

## 문제 5 풀이

**(a)** 수평 원형 트랙에서 등속 원운동을 하려면 중심 방향의 구심력이 필요하다. 이 구심력의 역할을 하는 것은 $\boxed{\text{타이어와 도로 사이의 정지마찰력}}$이다. (자동차가 미끄러지지 않으므로 운동마찰력이 아닌 정지마찰력이다.)

**(b)** 구심력 = 정지마찰력:

$$\frac{mv^2}{R} \leq f_{s,\max} = \mu_s F_N = \mu_s mg$$

최대 속력일 때 등호가 성립:

$$\frac{mv_{\max}^2}{R} = \mu_s mg$$

$$\boxed{v_{\max} = \sqrt{\mu_s g R}}$$

**(c)** $\mu_s = 0.60$, $R = 50\,\text{m}$:

$$v_{\max} = \sqrt{(0.60)(9.8)(50)} = \sqrt{294} = 17.1\,\text{m/s}$$

$$= 17.1 \times 3.6 = \boxed{61.6\,\text{km/h}}$$

**(d)** $\mu_s' = \mu_s / 2$이면:

$$v_{\max}' = \sqrt{\mu_s' g R} = \sqrt{\frac{\mu_s}{2} g R} = \frac{1}{\sqrt{2}} \sqrt{\mu_s g R} = \frac{v_{\max}}{\sqrt{2}}$$

$$\boxed{\frac{v_{\max}'}{v_{\max}} = \frac{1}{\sqrt{2}} \approx 0.707}$$

최대 속력은 원래의 약 $70.7\%$, 즉 $\dfrac{1}{\sqrt{2}}$배가 된다.

---

## 문제 6 풀이

$m = 0.50\,\text{kg}$, $L = 1.2\,\text{m}$, $v_{\text{top}} = 5.0\,\text{m/s}$

**(a)** 꼭대기에서 중력과 장력이 모두 중심(아래) 방향:

$$T_{\text{top}} + mg = \frac{mv_{\text{top}}^2}{L}$$

$$T_{\text{top}} = \frac{mv_{\text{top}}^2}{L} - mg = m\left(\frac{v_{\text{top}}^2}{L} - g\right)$$

$$= 0.50\left(\frac{25}{1.2} - 9.8\right) = 0.50(20.83 - 9.8) = 0.50 \times 11.03$$

$$= \boxed{5.52\,\text{N}}$$

**(b)** 역학적 에너지 보존 (꼭대기를 기준점, 아래 지점은 높이 $-2L$):

$$\frac{1}{2}mv_{\text{top}}^2 + mg(2L) = \frac{1}{2}mv_{\text{bot}}^2$$

$$v_{\text{bot}}^2 = v_{\text{top}}^2 + 4gL = 25 + 4(9.8)(1.2) = 25 + 47.04 = 72.04$$

$$v_{\text{bot}} = \sqrt{72.04} = \boxed{8.49\,\text{m/s}}$$

**(c)** 아래 지점에서 장력은 위(중심) 방향, 중력은 아래 방향:

$$T_{\text{bot}} - mg = \frac{mv_{\text{bot}}^2}{L}$$

$$T_{\text{bot}} = \frac{mv_{\text{bot}}^2}{L} + mg = m\left(\frac{v_{\text{bot}}^2}{L} + g\right)$$

$$= 0.50\left(\frac{72.04}{1.2} + 9.8\right) = 0.50(60.03 + 9.8) = 0.50 \times 69.83$$

$$= \boxed{34.9\,\text{N}}$$
