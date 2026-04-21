# Chapter 16: Waves — I 풀이

---

## 문제 1 풀이

$y(x, t) = (0.12\;\text{m})\sin(4.0\pi x - 12\pi t)$

표준 형태 $y = y_m \sin(kx - \omega t)$와 비교:

**(a)**

- 진폭: $y_m = \boxed{0.12\;\text{m}}$
- 각파수: $k = 4.0\pi\;\text{rad/m}$ → 파장: $\lambda = \frac{2\pi}{k} = \frac{2\pi}{4.0\pi} = \boxed{0.50\;\text{m}}$
- 각진동수: $\omega = 12\pi\;\text{rad/s}$ → 진동수: $f = \frac{\omega}{2\pi} = \frac{12\pi}{2\pi} = \boxed{6.0\;\text{Hz}}$
- 주기: $T = \frac{1}{f} = \frac{1}{6.0} = \boxed{0.167\;\text{s}}$

**(b)**

$$v = \frac{\omega}{k} = \frac{12\pi}{4.0\pi} = \boxed{3.0\;\text{m/s}}$$

검산: $v = \lambda f = 0.50 \times 6.0 = 3.0\;\text{m/s}$ $\checkmark$

**(c)** $t = 0.025$ s, $x = 0.30$ m:

$$y = 0.12 \sin(4.0\pi \times 0.30 - 12\pi \times 0.025)$$

$$= 0.12 \sin(1.2\pi - 0.3\pi) = 0.12 \sin(0.9\pi)$$

$$\sin(0.9\pi) = \sin(162°) = \sin(18°) = 0.3090$$

$$y = 0.12 \times 0.3090 = \boxed{0.037\;\text{m} \approx 3.7\;\text{cm}}$$

---

## 문제 2 풀이

$M = 0.060$ kg, $L = 2.0$ m, $\tau = 500$ N

**(a)**

$$\mu = \frac{M}{L} = \frac{0.060}{2.0} = \boxed{0.030\;\text{kg/m}}$$

**(b)**

$$v = \sqrt{\frac{\tau}{\mu}} = \sqrt{\frac{500}{0.030}} = \sqrt{16667} = \boxed{129\;\text{m/s}}$$

**(c)**

$$\lambda = \frac{v}{f} = \frac{129}{200} = \boxed{0.645\;\text{m} \approx 0.65\;\text{m}}$$

---

## 문제 3 풀이

$y(x,t) = y_m \sin(kx - \omega t)$

**(a)** 횡속도:

$$u = \frac{\partial y}{\partial t} = -\omega y_m \cos(kx - \omega t)$$

$$\boxed{u = -\omega y_m \cos(kx - \omega t)}$$

횡가속도:

$$a_y = \frac{\partial^2 y}{\partial t^2} = -\omega^2 y_m \sin(kx - \omega t) = -\omega^2 y$$

$$\boxed{a_y = -\omega^2 y_m \sin(kx - \omega t)}$$

- 횡속도가 최대인 위치: $\cos(kx - \omega t) = \pm 1$, 즉 $y = 0$인 평형 위치를 지날 때. 변위가 0인 곳에서 속도가 최대이다 (SHM과 동일).
- 횡가속도가 최대인 위치: $\sin(kx - \omega t) = \pm 1$, 즉 $y = \pm y_m$인 최대 변위 위치. 마루나 골에서 가속도가 최대이다.

**(b)** 좌변:

$$\frac{\partial^2 y}{\partial x^2} = \frac{\partial}{\partial x}[ky_m \cos(kx - \omega t)] = -k^2 y_m \sin(kx - \omega t)$$

우변:

$$\frac{1}{v^2}\frac{\partial^2 y}{\partial t^2} = \frac{1}{v^2}[-\omega^2 y_m \sin(kx - \omega t)] = -\frac{\omega^2}{v^2}y_m \sin(kx - \omega t)$$

$v = \omega/k$이므로 $\frac{\omega^2}{v^2} = \frac{\omega^2}{\omega^2/k^2} = k^2$

따라서 좌변 = 우변 = $-k^2 y_m \sin(kx - \omega t)$ $\boxed{\checkmark}$

---

## 문제 4 풀이

$\mu = 0.40$ kg/m, $\tau = 90$ N, $y_m = 5.0$ mm $= 0.0050$ m, $f = 150$ Hz

**(a)**

$$v = \sqrt{\frac{\tau}{\mu}} = \sqrt{\frac{90}{0.40}} = \sqrt{225} = \boxed{15\;\text{m/s}}$$

**(b)** $\omega = 2\pi f = 2\pi \times 150 = 300\pi\;\text{rad/s}$

$$P_\text{avg} = \frac{1}{2}\mu v \omega^2 y_m^2$$

$$= \frac{1}{2}(0.40)(15)(300\pi)^2(0.0050)^2$$

$$= \frac{1}{2}(0.40)(15)(9.0 \times 10^4 \pi^2)(2.5 \times 10^{-5})$$

$$= \frac{1}{2}(0.40)(15)(9.0 \times 10^4)(9.8696)(2.5 \times 10^{-5})$$

$$= \frac{1}{2}(0.40)(15)(22.2)$$

$$= \frac{1}{2} \times 133.2 = \boxed{66.6\;\text{W} \approx 67\;\text{W}}$$

**(c)** $P_\text{avg} = \frac{1}{2}\mu v \omega^2 y_m^2 \propto \omega^2 y_m^2 \propto f^2 y_m^2$

진폭 2배, 진동수 절반:

$$P'_\text{avg} \propto (f/2)^2 (2y_m)^2 = \frac{f^2}{4} \times 4y_m^2 = f^2 y_m^2$$

$$\boxed{P'_\text{avg} = P_\text{avg}} \quad \text{(평균 파워는 변하지 않는다)}$$

진폭 증가 효과와 진동수 감소 효과가 정확히 상쇄된다.

---

## 문제 5 풀이

**(a)** $\alpha = kx - \omega t$, $\beta = kx - \omega t + \phi$로 놓으면:

$$y' = y_m(\sin\alpha + \sin\beta) = 2y_m \sin\frac{\alpha + \beta}{2}\cos\frac{\alpha - \beta}{2}$$

$$\frac{\alpha + \beta}{2} = \frac{(kx - \omega t) + (kx - \omega t + \phi)}{2} = kx - \omega t + \frac{\phi}{2}$$

$$\frac{\alpha - \beta}{2} = \frac{(kx - \omega t) - (kx - \omega t + \phi)}{2} = -\frac{\phi}{2}$$

$\cos(-\phi/2) = \cos(\phi/2)$이므로:

$$\boxed{y' = \left[2y_m \cos\frac{\phi}{2}\right]\sin\left(kx - \omega t + \frac{\phi}{2}\right)}$$

**(b)**

$\phi = 0$:

$$y'_m = |2y_m \cos 0| = \boxed{2y_m} \quad \text{(완전 보강 간섭)}$$

$\phi = \pi$:

$$y'_m = |2y_m \cos(\pi/2)| = |2y_m \times 0| = \boxed{0} \quad \text{(완전 상쇄 간섭)}$$

$\phi = 2\pi/3$:

$$y'_m = |2y_m \cos(\pi/3)| = |2y_m \times 0.5| = \boxed{y_m} \quad \text{(중간 간섭)}$$

---

## 문제 6 풀이

$L = 1.2$ m, $\mu = 2.0 \times 10^{-3}$ kg/m, $\tau = 50$ N

**(a)**

$$v = \sqrt{\frac{\tau}{\mu}} = \sqrt{\frac{50}{2.0 \times 10^{-3}}} = \sqrt{25000} = \boxed{158\;\text{m/s}}$$

**(b)** 기본 진동수:

$$f_1 = \frac{v}{2L} = \frac{158}{2 \times 1.2} = \frac{158}{2.4} = \boxed{65.8\;\text{Hz}}$$

**(c)** 3차 조화파:

$$f_3 = 3f_1 = 3 \times 65.8 = \boxed{197\;\text{Hz}}$$

$$\lambda_3 = \frac{2L}{3} = \frac{2 \times 1.2}{3} = \boxed{0.80\;\text{m}}$$

**(d)** 3차 조화파에서 마디는 $x = n\frac{\lambda_3}{2}$ ($n = 0, 1, 2, 3$)에 위치한다:

$$x = 0 \times 0.40 = 0\;\text{m}$$
$$x = 1 \times 0.40 = 0.40\;\text{m}$$
$$x = 2 \times 0.40 = 0.80\;\text{m}$$
$$x = 3 \times 0.40 = 1.20\;\text{m}$$

$$\boxed{x = 0,\; 0.40,\; 0.80,\; 1.20\;\text{m}}$$

(양 끝 포함 4개의 마디)

---

## 문제 7 풀이

양 끝 고정, 길이 $L$

**(a)** 2차 조화파 ($n = 2$): $\lambda_2 = 2L/2 = L$

마디: $x = 0, \frac{L}{2}, L$ (3개)

배: $x = \frac{L}{4}, \frac{3L}{4}$ (2개)

$$\boxed{\text{마디: } x = 0, \frac{L}{2}, L \quad |\quad \text{배: } x = \frac{L}{4}, \frac{3L}{4}}$$

**(b)** 5차 조화파 ($n = 5$): $\lambda_5 = 2L/5$

마디 간격: $\frac{\lambda_5}{2} = \frac{L}{5}$

마디: $x = 0, \frac{L}{5}, \frac{2L}{5}, \frac{3L}{5}, \frac{4L}{5}, L$ (6개)

$$\boxed{x = 0, \frac{L}{5}, \frac{2L}{5}, \frac{3L}{5}, \frac{4L}{5}, L}$$

**(c)** $f_1 = 440$ Hz일 때:

$$f_2 = 2f_1 = 2 \times 440 = \boxed{880\;\text{Hz}}$$

$$f_5 = 5f_1 = 5 \times 440 = \boxed{2200\;\text{Hz}}$$

**(d)** $f_1 = \frac{1}{2L}\sqrt{\frac{\tau}{\mu}}$이므로, 장력을 4배로 하면:

$$f_1' = \frac{1}{2L}\sqrt{\frac{4\tau}{\mu}} = \frac{2}{2L}\sqrt{\frac{\tau}{\mu}} = 2f_1$$

$$\boxed{\text{기본 진동수가 2배로 증가한다.}}$$

장력의 제곱근에 비례하므로 장력을 4배로 하면 진동수는 2배가 된다.
