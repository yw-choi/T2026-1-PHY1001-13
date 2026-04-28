# Chapter 17: Waves II — 풀이

---

## 문제 1 풀이

$\rho = 1.21\;\text{kg/m}^3$, $v = 343\;\text{m/s}$, $f = 1000\;\text{Hz}$, $\Delta p_m = 28\;\text{Pa}$

**(a)** 압력 진폭과 변위 진폭의 관계:

$$\Delta p_m = v\rho\omega s_m = v\rho(2\pi f) s_m$$

$$s_m = \frac{\Delta p_m}{v\rho(2\pi f)} = \frac{28}{343 \times 1.21 \times 2\pi \times 1000}$$

$$s_m = \frac{28}{2\,609\,000} = \boxed{1.07 \times 10^{-5}\;\text{m} \approx 11\;\mu\text{m}}$$

**(b)** 세기:

$$I = \frac{(\Delta p_m)^2}{2\rho v}$$

이 공식은 $\Delta p_m = v\rho\omega s_m$을 $I = \frac{1}{2}\rho v\omega^2 s_m^2$에 대입하면 얻는다:

$$I = \frac{28^2}{2 \times 1.21 \times 343} = \frac{784}{830.1} = \boxed{0.944\;\text{W/m}^2}$$

**(c)** 음압 수준:

$$\beta = 10 \log\frac{I}{I_0} = 10\log\frac{0.944}{10^{-12}} = 10\log(9.44 \times 10^{11})$$

$$= 10 \times (11 + \log 9.44) = 10 \times (11 + 0.975) = \boxed{119.8\;\text{dB} \approx 120\;\text{dB}}$$

이것은 통증 역치에 해당한다.

---

## 문제 2 풀이

$P_s = 100\;\text{W}$, $I_0 = 10^{-12}\;\text{W/m}^2$

**(a)** 거리 $r_1 = 5.0\;\text{m}$에서:

$$I_1 = \frac{P_s}{4\pi r_1^2} = \frac{100}{4\pi(5.0)^2} = \frac{100}{314.2} = \boxed{0.318\;\text{W/m}^2}$$

$$\beta_1 = 10\log\frac{I_1}{I_0} = 10\log\frac{0.318}{10^{-12}} = 10\log(3.18 \times 10^{11})$$

$$= 10(11 + \log 3.18) = 10(11 + 0.502) = \boxed{115.0\;\text{dB}}$$

**(b)** $\beta_2 = 60\;\text{dB}$이면:

$$60 = 10\log\frac{I_2}{10^{-12}} \implies \log\frac{I_2}{10^{-12}} = 6 \implies I_2 = 10^{-6}\;\text{W/m}^2$$

$$I_2 = \frac{P_s}{4\pi r_2^2} \implies r_2 = \sqrt{\frac{P_s}{4\pi I_2}} = \sqrt{\frac{100}{4\pi \times 10^{-6}}}$$

$$r_2 = \sqrt{\frac{10^8}{4\pi}} = \sqrt{7.96 \times 10^6} = \boxed{2820\;\text{m} \approx 2.8\;\text{km}}$$

**(c)** 거리가 2배가 되면 세기는 $1/4$배:

$$\Delta\beta = 10\log\frac{I_2}{I_1} = 10\log\frac{1}{4} = 10 \times (-0.602) = \boxed{-6.0\;\text{dB}}$$

음압 수준이 6 dB 감소한다. 이것은 역제곱 법칙의 직접적 결과이다.

---

## 문제 3 풀이

$\lambda = 0.50\;\text{m}$, $L_1 = 4.20\;\text{m}$, $L_2 = 4.95\;\text{m}$

**(a)** 경로차:

$$\Delta L = |L_2 - L_1| = |4.95 - 4.20| = \boxed{0.75\;\text{m}}$$

**(b)** 

$$\frac{\Delta L}{\lambda} = \frac{0.75}{0.50} = 1.5$$

$\Delta L / \lambda = 1.5$는 상쇄 간섭 조건 $0.5, 1.5, 2.5, \ldots$에 해당하므로, $\boxed{\text{완전한 상쇄 간섭(fully destructive interference)}}$ 이 일어난다. 점 $P$에서 두 파동은 정확히 반파장 차이로 도착하여 서로 상쇄된다.

**(c)** $\lambda' = 0.60\;\text{m}$이면:

$$\frac{\Delta L}{\lambda'} = \frac{0.75}{0.60} = 1.25$$

$\Delta L / \lambda' = 1.25$는 정수(보강)도 아니고 반정수(상쇄)도 아니다. 따라서 $\boxed{\text{불완전 간섭(intermediate interference)}}$ 이 일어난다. 합성 진폭은 0과 $2s_m$ 사이의 중간값이다. $1.25$는 $1.0$ (보강)보다 $1.5$ (상쇄)에 더 가까우므로, 상쇄에 가까운 불완전 간섭이다.

---

## 문제 4 풀이

**(a)** 닫힌 끝에서 공기는 벽에 의해 움직일 수 없으므로 **변위가 0** 이다 → 마디(node). 열린 끝에서 공기는 외부와 자유롭게 소통하여 **변위가 최대** → 배(antinode). 이것은 줄의 정상파에서 고정단이 마디, 자유단이 배인 것과 같은 원리이다.

**(b)** 가장 단순한 정상파: 닫힌 끝에 마디, 열린 끝에 배 → 마디와 배 사이의 거리는 $\lambda/4$:

$$L = \frac{\lambda}{4} \implies \lambda = 4L$$

$$\boxed{f_1 = \frac{v}{\lambda} = \frac{v}{4L}}$$

**(c)** 닫힌 끝(마디)에서 열린 끝(배)까지의 거리 $L$에는 마디-배 간격 $\lambda/4$의 **홀수 배** 만 들어갈 수 있다:

$$L = n \times \frac{\lambda}{4}, \quad n = 1, 3, 5, \ldots$$

$$\lambda = \frac{4L}{n}, \quad f = \frac{v}{\lambda} = \frac{nv}{4L}, \quad n = 1, 3, 5, \ldots$$

짝수 $n$의 경우, 양 끝이 모두 마디이거나 모두 배가 되어 경계 조건(한쪽 마디, 한쪽 배)을 만족하지 않는다. 따라서 $\boxed{\text{홀수 배음만 가능하다.}}$

---

## 문제 5 풀이

**(a)** 두 파동의 중첩:

$$s = s_m\cos\omega_1 t + s_m\cos\omega_2 t = s_m(\cos\omega_1 t + \cos\omega_2 t)$$

삼각함수 항등식 $\cos\alpha + \cos\beta = 2\cos\frac{\alpha-\beta}{2}\cos\frac{\alpha+\beta}{2}$에서 $\alpha = \omega_1 t$, $\beta = \omega_2 t$를 대입:

$$s = s_m \cdot 2\cos\left(\frac{\omega_1 t - \omega_2 t}{2}\right)\cos\left(\frac{\omega_1 t + \omega_2 t}{2}\right)$$

$$\boxed{s(t) = \left[2s_m\cos\left(\frac{\omega_1 - \omega_2}{2}t\right)\right]\cos\left(\frac{\omega_1 + \omega_2}{2}t\right)}$$

**(b)** $\omega' = \frac{1}{2}(\omega_1 - \omega_2)$로 놓으면, 대괄호 안의 항 $2s_m\cos\omega' t$가 천천히 변하는 진폭이다.

진폭의 절댓값 $|2s_m\cos\omega' t|$가 최대가 되는 것은 $\cos\omega' t = \pm 1$일 때이다.

$\cos\omega' t$의 한 주기($T' = 2\pi/\omega'$) 동안 $\cos\omega' t = +1$ 한 번, $\cos\omega' t = -1$ 한 번 → 맥놀이 최대가 **2번** 발생한다.

따라서 맥놀이 각진동수:

$$\omega_\text{beat} = 2\omega' = 2 \times \frac{\omega_1 - \omega_2}{2} = \omega_1 - \omega_2$$

$\omega = 2\pi f$이고 일반적으로 $f_1, f_2$ 대소가 정해지지 않으므로 절댓값으로:

$$\boxed{f_\text{beat} = |f_1 - f_2|}$$

**(c)** $f_1 = 262\;\text{Hz}$, $f_2 = 266\;\text{Hz}$:

$$f_\text{beat} = |f_1 - f_2| = |262 - 266| = 4\;\text{Hz}$$

$$\boxed{\text{1초 동안 맥놀이가 4회 발생한다.}}$$

---

## 문제 6 풀이

$v_S = 40\;\text{m/s}$, $f = 500\;\text{Hz}$, $v = 343\;\text{m/s}$

**(a)** 기차가 접근할 때 (음원이 관측자에 접근, $v_O = 0$):

$$f' = f\frac{v}{v - v_S} = 500 \times \frac{343}{343 - 40} = 500 \times \frac{343}{303} = \boxed{566\;\text{Hz}}$$

**(b)** 기차가 멀어질 때:

$$f'' = f\frac{v}{v + v_S} = 500 \times \frac{343}{343 + 40} = 500 \times \frac{343}{383} = \boxed{448\;\text{Hz}}$$

**(c)** 진동수 변화량:

$$|f' - f''| = 566 - 448 = \boxed{118\;\text{Hz}}$$

물리적 설명: 기차가 접근할 때는 연속적으로 방출되는 파면이 앞쪽으로 압축되어 관측자가 더 짧은 파장(높은 진동수)을 감지한다. 기차가 멀어질 때는 파면이 뒤쪽으로 늘어나 더 긴 파장(낮은 진동수)이 된다. 접근 시 분모가 $v - v_S$ (작아짐 → 진동수 증가), 멀어질 시 분모가 $v + v_S$ (커짐 → 진동수 감소)인 것이 이를 수학적으로 반영한다.

---

## 문제 7 풀이

Ma = 2.5, $v = 343\;\text{m/s}$

**(a)** 총알의 속력:

$$v_S = \text{Ma} \times v = 2.5 \times 343 = \boxed{857.5\;\text{m/s}}$$

**(b)** 마하 원뿔의 반각:

$$\sin\theta = \frac{v}{v_S} = \frac{1}{\text{Ma}} = \frac{1}{2.5} = 0.400$$

$$\theta = \arcsin(0.400) = \boxed{23.6°}$$

**(c)** 총알이 음속보다 빠르므로, 총알은 자신이 만든 음파보다 **앞서 나간다**. 충격파(마하 원뿔)는 총알의 현재 위치가 아닌 **뒤쪽** 으로 펼쳐진다.

관측자 바로 위를 총알이 지나가는 순간, 마하 원뿔의 표면(충격파)은 아직 관측자에게 도달하지 않았다. 충격파는 총알의 경로 뒤쪽으로 비스듬히 퍼지므로, 총알이 관측자를 지나간 후에야 원뿔 면이 관측자 위치에 도달한다.

기하학적으로, 반각 $\theta = 23.6°$인 원뿔의 표면은 총알의 진행 방향과 $90° - 23.6° = 66.4°$의 각도를 이룬다. 총알이 관측자 위를 지날 때, 충격파 면은 아직 관측자보다 뒤에 있으며, 총알이 더 진행한 후에야 원뿔 면이 관측자에 닿는다. 따라서 $\boxed{\text{관측자는 총알이 지나간 후에 소닉 붐을 듣는다.}}$
