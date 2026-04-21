# Chapter 15: Oscillations — 풀이

---

## 문제 1 풀이

$k = 150\;\text{N/m}$, $m = 0.60\;\text{kg}$, $x_m = 0.12\;\text{m}$

**(a)**

$$\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{150}{0.60}} = \sqrt{250} = \boxed{15.8\;\text{rad/s}}$$

$$T = \frac{2\pi}{\omega} = \frac{2\pi}{15.8} = \boxed{0.398\;\text{s}}$$

$$f = \frac{1}{T} = \frac{1}{0.398} = \boxed{2.51\;\text{Hz}}$$

**(b)**

$$v_m = \omega x_m = 15.8 \times 0.12 = \boxed{1.90\;\text{m/s}}$$

$$a_m = \omega^2 x_m = 250 \times 0.12 = \boxed{30.0\;\text{m/s}^2}$$

**(c)** 에너지 보존을 이용:

$$v = \omega\sqrt{x_m^2 - x^2} = 15.8\sqrt{(0.12)^2 - (0.080)^2} = 15.8\sqrt{0.0144 - 0.0064}$$

$$= 15.8\sqrt{0.0080} = 15.8 \times 0.0894 = \boxed{1.41\;\text{m/s}}$$

---

## 문제 2 풀이

$m = 0.50\;\text{kg}$, $k = 200\;\text{N/m}$, $x(0) = -0.040\;\text{m}$, $v(0) = +1.2\;\text{m/s}$

**(a)**

$$\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{200}{0.50}} = \sqrt{400} = \boxed{20\;\text{rad/s}}$$

**(b)** 진폭:

$$x_m = \sqrt{x_0^2 + \left(\frac{v_0}{\omega}\right)^2} = \sqrt{(-0.040)^2 + \left(\frac{1.2}{20}\right)^2}$$

$$= \sqrt{0.0016 + 0.0036} = \sqrt{0.0052} = \boxed{0.072\;\text{m}}$$

**(c)** 위상 상수:

$$\tan\phi = -\frac{v_0}{\omega x_0} = -\frac{1.2}{20 \times (-0.040)} = -\frac{1.2}{-0.80} = 1.5$$

$\phi$의 후보: $\phi = \arctan(1.5) = 56.3°$ 또는 $\phi = 180° + 56.3° = 236.3°$

초기 조건 확인: $x(0) = x_m\cos\phi < 0$이므로 $\cos\phi < 0$이어야 한다.

$\phi = 56.3°$이면 $\cos(56.3°) = 0.555 > 0$ → 부적합

$\phi = 236.3°$이면 $\cos(236.3°) = -0.555 < 0$ → 적합

$$\boxed{\phi = 236° \approx 4.12\;\text{rad}}$$

검증: $x(0) = 0.072 \times \cos(236.3°) = 0.072 \times (-0.555) = -0.040\;\text{m}$ ✓

$v(0) = -20 \times 0.072 \times \sin(236.3°) = -1.44 \times (-0.832) = +1.2\;\text{m/s}$ ✓

---

## 문제 3 풀이

**(a)**

$$U = \frac{1}{2}kx^2 = \frac{1}{2}k[x_m\cos(\omega t + \phi)]^2 = \frac{1}{2}kx_m^2\cos^2(\omega t + \phi)$$

$$K = \frac{1}{2}mv^2 = \frac{1}{2}m[-\omega x_m\sin(\omega t + \phi)]^2 = \frac{1}{2}m\omega^2 x_m^2\sin^2(\omega t + \phi)$$

$m\omega^2 = m \cdot \frac{k}{m} = k$이므로:

$$\boxed{K = \frac{1}{2}kx_m^2\sin^2(\omega t + \phi)}$$

**(b)**

$$E = K + U = \frac{1}{2}kx_m^2\sin^2(\omega t + \phi) + \frac{1}{2}kx_m^2\cos^2(\omega t + \phi)$$

$$= \frac{1}{2}kx_m^2[\sin^2(\omega t + \phi) + \cos^2(\omega t + \phi)]$$

$$\boxed{E = \frac{1}{2}kx_m^2 = \text{const}}$$

시간 $t$에 의존하지 않으므로 역학적 에너지는 보존된다.

**(c)** 에너지 보존에서:

$$\frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \frac{1}{2}kx_m^2$$

$$mv^2 = k(x_m^2 - x^2)$$

$$v^2 = \frac{k}{m}(x_m^2 - x^2) = \omega^2(x_m^2 - x^2)$$

$$\boxed{v = \pm\omega\sqrt{x_m^2 - x^2}}$$

---

## 문제 4 풀이

**(a)** $L = 2.0\;\text{m}$, $g = 9.80\;\text{m/s}^2$

$$T = 2\pi\sqrt{\frac{L}{g}} = 2\pi\sqrt{\frac{2.0}{9.80}} = 2\pi\sqrt{0.2041} = 2\pi \times 0.4518 = \boxed{2.84\;\text{s}}$$

**(b)** $T = 1.00\;\text{s}$일 때:

$$T = 2\pi\sqrt{\frac{L}{g}} \implies L = \frac{gT^2}{4\pi^2} = \frac{9.80 \times (1.00)^2}{4\pi^2} = \frac{9.80}{39.48} = \boxed{0.248\;\text{m}}$$

**(c)** 달 표면에서 ($L = 2.0\;\text{m}$, $g_\text{moon} = 1.63\;\text{m/s}^2$):

$$T_\text{moon} = 2\pi\sqrt{\frac{L}{g_\text{moon}}} = 2\pi\sqrt{\frac{2.0}{1.63}} = 2\pi\sqrt{1.227} = 2\pi \times 1.108 = \boxed{6.96\;\text{s}}$$

또는 비율로: $T_\text{moon} = T_\text{earth}\sqrt{g_\text{earth}/g_\text{moon}} = 2.84\sqrt{9.80/1.63} = 2.84 \times 2.452 = 6.96\;\text{s}$

---

## 문제 5 풀이

**(a)** 평행축 정리: $I = I_\text{com} + Mh^2$

질량 중심은 막대 중앙에 있으므로 피벗에서 $h = L/2$:

$$I = \frac{1}{12}ML^2 + M\left(\frac{L}{2}\right)^2 = \frac{1}{12}ML^2 + \frac{1}{4}ML^2 = \frac{1 + 3}{12}ML^2 = \boxed{\frac{1}{3}ML^2}$$

**(b)** 물리 진자 주기 공식에 대입 ($h = L/2$):

$$T = 2\pi\sqrt{\frac{I}{Mgh}} = 2\pi\sqrt{\frac{\frac{1}{3}ML^2}{Mg\cdot\frac{L}{2}}} = 2\pi\sqrt{\frac{\frac{1}{3}L^2}{\frac{1}{2}gL}} = 2\pi\sqrt{\frac{2L}{3g}}$$

$$\boxed{T = 2\pi\sqrt{\frac{2L}{3g}}}$$

**(c)** 같은 주기를 갖는 단진자의 길이 $L_0$:

$$2\pi\sqrt{\frac{L_0}{g}} = 2\pi\sqrt{\frac{2L}{3g}}$$

양변을 제곱하면:

$$\frac{L_0}{g} = \frac{2L}{3g}$$

$$\boxed{L_0 = \frac{2}{3}L}$$

이것이 진동 중심(center of oscillation)까지의 거리이다. 피벗에서 $\frac{2}{3}L$ 지점에 해당한다.

---

## 문제 6 풀이

$m = 0.25\;\text{kg}$, $k = 85\;\text{N/m}$, $b = 0.070\;\text{kg/s}$

**(a)** 임계 감쇠 조건:

$$2\sqrt{km} = 2\sqrt{85 \times 0.25} = 2\sqrt{21.25} = 2 \times 4.610 = 9.22\;\text{kg/s}$$

$b = 0.070 \ll 9.22$이므로 $\boxed{\text{약감쇠(underdamped)}}$

**(b)** 비감쇠 각진동수:

$$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{85}{0.25}} = \sqrt{340} = 18.44\;\text{rad/s}$$

감쇠 각진동수:

$$\omega' = \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}} = \sqrt{340 - \frac{(0.070)^2}{4(0.25)^2}} = \sqrt{340 - \frac{0.0049}{0.25}}$$

$$= \sqrt{340 - 0.0196} = \sqrt{339.98} = \boxed{18.44\;\text{rad/s}}$$

감쇠가 매우 작으므로 $\omega' \approx \omega_0$. 실질적인 차이가 없다.

**(c)** 진폭: $x_m(t) = x_m(0)\,e^{-bt/2m}$

진폭이 절반: $e^{-bt/2m} = \frac{1}{2}$

$$-\frac{bt}{2m} = \ln\frac{1}{2} = -\ln 2$$

$$t = \frac{2m\ln 2}{b} = \frac{2 \times 0.25 \times 0.693}{0.070} = \frac{0.347}{0.070} = \boxed{4.95\;\text{s}}$$

**(d)** 에너지: $E(t) = E(0)\,e^{-bt/m}$ (에너지는 진폭의 제곱에 비례하므로 시정수가 절반)

$e^{-bt/m} = \frac{1}{2}$:

$$t = \frac{m\ln 2}{b} = \frac{0.25 \times 0.693}{0.070} = \frac{0.173}{0.070} = \boxed{2.48\;\text{s}}$$

에너지가 절반이 되는 시간은 진폭이 절반이 되는 시간의 절반이다. 이는 $E \propto x_m^2 \propto e^{-bt/m}$이기 때문이다.

---

## 문제 7 풀이

**(a)** 공명 조건: $\omega_d = \omega_0 = 2\pi f_0$

$$\omega_d = 2\pi \times 5.0 = \boxed{31.4\;\text{rad/s}}$$

**(b)** 감쇠가 없는 이상적인 경우, 공명 시 진폭은 이론적으로 $\boxed{\text{무한대로 발산}}$ 한다.

물리적 설명: 외부 구동력이 항상 운동 방향으로 에너지를 전달하므로(양의 일), 에너지가 계속 축적되어 진폭이 끝없이 커진다. 실제로는 비선형 효과나 재료의 파괴로 제한된다.

**(c)** 감쇠 상수 $b$가 커지면:
- 공명 peak의 **높이가 낮아진다** (최대 진폭 감소)
- 공명 peak의 **폭이 넓어진다** (더 넓은 진동수 범위에서 응답)
- 공명 진동수가 $\omega_0$에서 약간 아래로 이동한다 ($\omega_\text{res} = \sqrt{\omega_0^2 - b^2/(2m^2)}$)

$\boxed{\text{감쇠가 클수록 공명 곡선이 낮고 넓어진다.}}$

**(d)** 타코마 내로우즈 다리는 바람이 일정한 속도로 불 때, 와류(vortex)가 다리의 비틀림 진동에 주기적인 힘을 가했다. 이 **와류의 진동수** 가 다리의 **비틀림 고유 진동수** 와 일치하면서 공명이 발생했고, 감쇠가 작아서 진폭이 점점 커져 결국 구조적 한계를 초과하여 $\boxed{\text{붕괴에 이르렀다.}}$
