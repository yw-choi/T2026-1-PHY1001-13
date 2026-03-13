# Chapter 2: Motion Along a Straight Line — 풀이

---

## 문제 1 풀이

**(a) $v(t) = v_0 + at$ 유도**

등가속도이므로 $a = \text{const}$. 양변을 $t$에 대해 적분:

$$\int_{v_0}^{v} dv' = \int_{0}^{t} a\, dt' \implies v - v_0 = a\,t$$

$$\boxed{v(t) = v_0 + a\,t} \tag{1}$$

**(b) $x(t) = x_0 + v_0 t + \frac{1}{2}at^2$ 유도**

$v = \frac{dx}{dt}$이므로, (1)을 대입하여 적분:

$$\int_{x_0}^{x} dx' = \int_{0}^{t} (v_0 + a\,t')\, dt' = v_0\,t + \frac{1}{2}a\,t^2$$

$$\boxed{x(t) = x_0 + v_0\,t + \frac{1}{2}a\,t^2} \tag{2}$$

**(c) $v^2 = v_0^2 + 2a(x - x_0)$ 유도**

식 (1)에서 $t = \frac{v - v_0}{a}$. 이를 식 (2)에 대입:

$$x - x_0 = v_0 \cdot \frac{v - v_0}{a} + \frac{1}{2}a\left(\frac{v - v_0}{a}\right)^2 = \frac{2v_0(v - v_0) + (v - v_0)^2}{2a} = \frac{v^2 - v_0^2}{2a}$$

$$\boxed{v^2 = v_0^2 + 2a(x - x_0)} \tag{3}$$

---

## 문제 2 풀이

자동차: $x_{\text{car}} = \frac{1}{2}a\,t^2 = 2.50\,t^2$, 트럭: $x_{\text{truck}} = 45.0\,t$

**(a)**

$$2.50\,t^2 = 45.0\,t \implies t(2.50\,t - 45.0) = 0 \implies \boxed{t = 18.0\;\text{s}}$$

**(b)**

$$x = 2.50 \times (18.0)^2 = 2.50 \times 324 = \boxed{810\;\text{m}}$$

**(c)**

$$v = v_0 + at = 0 + 5.00 \times 18.0 = \boxed{90.0\;\text{m/s}}$$

(참고: 따라잡는 순간 자동차의 속도는 트럭 속도의 2배이다.)

---

## 문제 3 풀이

옥상을 원점, 아래 방향을 양의 방향: $v_0 = 0$, $a = g = 9.80\;\text{m/s}^2$

**(a)**

$$x = \frac{1}{2}g\,t^2 \implies t = \sqrt{\frac{2x}{g}} = \sqrt{\frac{2 \times 80.0}{9.80}} = \sqrt{16.33} = \boxed{4.04\;\text{s}}$$

**(b)**

$$v = g\,t = 9.80 \times 4.04 = \boxed{39.6\;\text{m/s}}$$

검증: $v^2 = 2g\,x = 2 \times 9.80 \times 80.0 = 1568 \implies v = 39.6\;\text{m/s}$ $\checkmark$

**(c)**

낙하 거리 $20.0\;\text{m}$: $t_1 = \sqrt{\frac{2 \times 20.0}{9.80}} = \sqrt{4.082} = 2.020\;\text{s}$

낙하 거리 $70.0\;\text{m}$: $t_2 = \sqrt{\frac{2 \times 70.0}{9.80}} = \sqrt{14.29} = 3.780\;\text{s}$

$$\Delta t = t_2 - t_1 = 3.780 - 2.020 = \boxed{1.76\;\text{s}}$$

---

## 문제 4 풀이

**(a) 가속 구간:** $v_0 = 0$, $v = 30.0\;\text{m/s}$, $a_1 = 3.00\;\text{m/s}^2$

$$t_1 = \frac{v}{a_1} = \frac{30.0}{3.00} = 10.0\;\text{s}, \quad d_1 = \frac{v^2}{2a_1} = \frac{900}{6.00} = 150\;\text{m}$$

$$\boxed{d_1 = 150\;\text{m},\; t_1 = 10.0\;\text{s}}$$

**(b) 감속 구간:** $v_0 = 30.0\;\text{m/s}$, $v = 0$, $a_2 = 2.00\;\text{m/s}^2$

$$t_2 = \frac{v_0}{a_2} = \frac{30.0}{2.00} = 15.0\;\text{s}, \quad d_2 = \frac{v_0^2}{2a_2} = \frac{900}{4.00} = 225\;\text{m}$$

$$\boxed{d_2 = 225\;\text{m},\; t_2 = 15.0\;\text{s}}$$

**(c) 총합**

$$d = d_1 + d_2 = 150 + 225 = \boxed{375\;\text{m}}, \quad t = t_1 + t_2 = 10.0 + 15.0 = \boxed{25.0\;\text{s}}$$

---

## 문제 5 풀이

$x(t) = 4.0\,t^2 - 2.0\,t + 1.0$

**(a)** $x(0) = 1.0\;\text{m}$, $x(2.0) = 4.0(4.0) - 2.0(2.0) + 1.0 = 13.0\;\text{m}$

$$v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{13.0 - 1.0}{2.0} = \boxed{6.0\;\text{m/s}}$$

**(b)**

$$v(t) = \frac{dx}{dt} = 8.0\,t - 2.0\;\text{(m/s)}, \quad v(2.0) = 8.0(2.0) - 2.0 = \boxed{14.0\;\text{m/s}}$$

**(c)**

$$a(t) = \frac{dv}{dt} = 8.0\;\text{m/s}^2 = \text{const} \implies \text{등가속도 운동}$$

순간 정지: $v(t) = 0 \implies 8.0\,t - 2.0 = 0 \implies \boxed{t = 0.25\;\text{s}}$

---

## 문제 6 풀이

$v_0 = 30.0\;\text{m/s}$, $v = 0$, $t = 6.00\;\text{s}$

**(a)**

$$a = \frac{v - v_0}{t} = \frac{0 - 30.0}{6.00} = -5.00\;\text{m/s}^2 \implies \boxed{|a| = 5.00\;\text{m/s}^2}$$

**(b)**

$$d = \frac{v_0 + v}{2} \times t = \frac{30.0 + 0}{2} \times 6.00 = \boxed{90.0\;\text{m}}$$

**(c)** $v = 15.0\;\text{m/s}$까지:

$$t' = \frac{v - v_0}{a} = \frac{15.0 - 30.0}{-5.00} = \boxed{3.00\;\text{s}}$$

$$d' = v_0\,t' + \frac{1}{2}a\,t'^2 = 30.0(3.00) + \frac{1}{2}(-5.00)(3.00)^2 = 90.0 - 22.5 = \boxed{67.5\;\text{m}}$$

---

## 문제 7 풀이

위 방향 양, $a = -g$, $y_0 = 0$

**(a)** 최고점에서 $v = 0$:

$$v = v_0 - g\,t_{\max} = 0 \implies \boxed{t_{\max} = \frac{v_0}{g}}$$

**(b)**

$$h_{\max} = v_0\,t_{\max} - \frac{1}{2}g\,t_{\max}^2 = v_0 \cdot \frac{v_0}{g} - \frac{1}{2}g\left(\frac{v_0}{g}\right)^2 = \frac{v_0^2}{g} - \frac{v_0^2}{2g} = \boxed{\frac{v_0^2}{2g}}$$

**(c)** 지면 복귀 $y = 0$:

$$0 = v_0\,t - \frac{1}{2}g\,t^2 = t\left(v_0 - \frac{1}{2}g\,t\right) \implies t = 0 \;\text{또는}\; t_{\text{total}} = \frac{2v_0}{g}$$

$$\frac{t_{\text{total}}}{t_{\max}} = \frac{2v_0/g}{v_0/g} = 2 \implies \boxed{t_{\text{total}} = 2\,t_{\max} = \frac{2v_0}{g}}$$
