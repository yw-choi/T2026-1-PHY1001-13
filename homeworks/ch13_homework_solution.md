# Chapter 13: Gravitation — 풀이

---

## 문제 1 풀이

$m_1 = 50\;\text{kg}$, $m_2 = 70\;\text{kg}$, $r = 1.0\;\text{m}$

**(a)**

$$F = G\frac{m_1 m_2}{r^2} = (6.674 \times 10^{-11})\frac{(50)(70)}{(1.0)^2}$$

$$= 6.674 \times 10^{-11} \times 3500 = \boxed{2.34 \times 10^{-7}\;\text{N}}$$

**(b)** 지구가 $m_1$에 작용하는 중력:

$$F_g = m_1 g = 50 \times 9.8 = 490\;\text{N}$$

비율:

$$\frac{F}{F_g} = \frac{2.34 \times 10^{-7}}{490} = \boxed{4.8 \times 10^{-10}}$$

**(c)** 두 사람 사이의 만유인력은 지구 중력의 약 $5 \times 10^{-10}$ 배, 즉 약 $0.00000005\%$에 불과하다. 이처럼 극도로 작은 힘이므로, 일상생활에서 사람들 사이의 만유인력은 감지할 수 없다. 만유인력이 의미 있는 크기가 되려면 적어도 하나의 질량이 행성 규모여야 한다.

---

## 문제 2 풀이

$M_E = 5.98 \times 10^{24}\;\text{kg}$, $R_E = 6.37 \times 10^6\;\text{m}$

**(a)**

$$a_g = \frac{GM_E}{R_E^2} = \frac{(6.674 \times 10^{-11})(5.98 \times 10^{24})}{(6.37 \times 10^6)^2}$$

$$= \frac{3.99 \times 10^{14}}{4.06 \times 10^{13}} = \boxed{9.83\;\text{m/s}^2}$$

**(b)** ISS 궤도: $r = R_E + h = 6.37 \times 10^6 + 4.00 \times 10^5 = 6.77 \times 10^6\;\text{m}$

$$a_g = \frac{GM_E}{r^2} = \frac{3.99 \times 10^{14}}{(6.77 \times 10^6)^2} = \frac{3.99 \times 10^{14}}{4.58 \times 10^{13}} = \boxed{8.70\;\text{m/s}^2}$$

**(c)**

$$\frac{a_g(h)}{a_g(0)} = \frac{8.70}{9.83} = 0.885 = \boxed{88.5\%}$$

ISS 궤도 높이에서도 중력은 지표면의 약 89%나 된다. ISS의 우주인이 "무중력"처럼 보이는 것은 중력이 없어서가 아니라, ISS와 우주인이 함께 **자유낙하** (원운동)하고 있기 때문이다. 체중계가 없는 자유낙하 상태에서는 "무중량(weightlessness)"을 경험하지만, 중력 자체는 존재한다.

---

## 문제 3 풀이

$M = 5.98 \times 10^{24}\;\text{kg}$, $R = 6.37 \times 10^6\;\text{m}$

**(a)** 탈출 속력:

$$v_\text{esc} = \sqrt{\frac{2GM}{R}} = \sqrt{\frac{2(6.674 \times 10^{-11})(5.98 \times 10^{24})}{6.37 \times 10^6}}$$

$$= \sqrt{\frac{7.98 \times 10^{14}}{6.37 \times 10^6}} = \sqrt{1.253 \times 10^8} = \boxed{1.12 \times 10^4\;\text{m/s} = 11.2\;\text{km/s}}$$

**(b)** 필요한 운동에너지:

$$K = \frac{1}{2}mv_\text{esc}^2 = \frac{1}{2}(1000)(1.12 \times 10^4)^2 = \frac{1}{2}(1000)(1.253 \times 10^8)$$

$$= \boxed{6.26 \times 10^{10}\;\text{J} \approx 62.6\;\text{GJ}}$$

**(c)** 반지름이 $R' = R/2$이면:

$$v'_\text{esc} = \sqrt{\frac{2GM}{R/2}} = \sqrt{\frac{4GM}{R}} = \sqrt{2}\, v_\text{esc}$$

$$\boxed{v'_\text{esc} = \sqrt{2}\, v_\text{esc} \approx 1.414\, v_\text{esc}}$$

탈출 속력이 $\sqrt{2} \approx 1.41$ 배로 증가한다. 같은 질량이 더 작은 부피에 집중되면 표면에서의 중력이 강해지기 때문이다.

---

## 문제 4 풀이

$m = 200\;\text{kg}$, $r = R_E + 600\;\text{km} = 6.37 \times 10^6 + 6.00 \times 10^5 = 6.97 \times 10^6\;\text{m}$

**(a)** 원궤도 속력 (중력 = 구심력):

$$\frac{GM_E m}{r^2} = \frac{mv^2}{r} \quad \Rightarrow \quad v = \sqrt{\frac{GM_E}{r}}$$

$$v = \sqrt{\frac{(6.674 \times 10^{-11})(5.98 \times 10^{24})}{6.97 \times 10^6}} = \sqrt{\frac{3.99 \times 10^{14}}{6.97 \times 10^6}}$$

$$= \sqrt{5.73 \times 10^7} = \boxed{7.57 \times 10^3\;\text{m/s} = 7.57\;\text{km/s}}$$

**(b)** 궤도 주기:

$$T = \frac{2\pi r}{v} = \frac{2\pi (6.97 \times 10^6)}{7.57 \times 10^3} = \frac{4.38 \times 10^7}{7.57 \times 10^3} = 5784\;\text{s} = \boxed{96.4\;\text{min}}$$

검증 (케플러 제3법칙):

$$T = 2\pi\sqrt{\frac{r^3}{GM_E}} = 2\pi\sqrt{\frac{(6.97 \times 10^6)^3}{3.99 \times 10^{14}}} = 2\pi\sqrt{8.48 \times 10^8} = 2\pi(2.91 \times 10^4) = 5780\;\text{s}\;\checkmark$$

**(c)**

$$K = \frac{1}{2}mv^2 = \frac{GM_E m}{2r} = \frac{(3.99 \times 10^{14})(200)}{2(6.97 \times 10^6)} = \boxed{5.73 \times 10^9\;\text{J}}$$

$$U = -\frac{GM_E m}{r} = -\frac{(3.99 \times 10^{14})(200)}{6.97 \times 10^6} = \boxed{-1.145 \times 10^{10}\;\text{J}}$$

$$E = K + U = 5.73 \times 10^9 - 1.145 \times 10^{10} = \boxed{-5.73 \times 10^9\;\text{J}}$$

확인:
- $E = -K$: $-5.73 \times 10^9 = -(5.73 \times 10^9)$ $\checkmark$
- $E = U/2$: $-5.73 \times 10^9 = (-1.145 \times 10^{10})/2 = -5.73 \times 10^9$ $\checkmark$

---

## 문제 5 풀이

**(a)** 중심에서 거리 $r$에서, 반지름 $r$ 안쪽의 질량만 기여한다 (껍질 정리).

균일 밀도이므로:

$$M_\text{ins} = M \frac{\frac{4}{3}\pi r^3}{\frac{4}{3}\pi R^3} = \frac{M r^3}{R^3}$$

중력:

$$\boxed{F = G\frac{m M_\text{ins}}{r^2} = \frac{GmM}{R^3}r}$$

**(b)** 힘을 벡터로 쓰면 (중심을 원점, 바깥 방향을 양의 $r$):

$$F = -\frac{GmM}{R^3}r$$

이것은 $F = -kr$ 형태이다. 따라서:

$$\boxed{k = \frac{GmM}{R^3}}$$

이는 SHM의 복원력과 동일한 형태이다. 물체는 지구 중심을 기준으로 단순조화운동을 한다.

**(c)** SHM 주기:

$$T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{m}{\frac{GmM}{R^3}}} = 2\pi\sqrt{\frac{R^3}{GM}}$$

$$\boxed{T = 2\pi\sqrt{\frac{R^3}{GM}}}$$

$g = GM/R^2$를 이용하면:

$$T = 2\pi\sqrt{\frac{R}{g}} = 2\pi\sqrt{\frac{6.37 \times 10^6}{9.8}} = 2\pi \times 806 = \boxed{5065\;\text{s} \approx 84.4\;\text{min}}$$

주기가 물체의 질량 $m$에 무관한 것은, 복원력과 관성 모두 $m$에 비례하기 때문이다 ($k$에 $m$이 포함되어 있고, $T = 2\pi\sqrt{m/k}$에서 $m$이 상쇄됨). 이는 자유낙하에서 가속도가 질량에 무관한 것과 같은 원리이다.

---

## 문제 6 풀이

**(a)** 중력이 구심력을 제공:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

$$\boxed{\frac{GM}{r^2} = \frac{v^2}{r}}$$

**(b)** (a)에서 $v$에 대해 풀면:

$$v^2 = \frac{GM}{r}$$

$$\boxed{v = \sqrt{\frac{GM}{r}}}$$

**(c)** 궤도 주기 $T = 2\pi r / v$에서:

$$T = \frac{2\pi r}{\sqrt{GM/r}} = 2\pi r \sqrt{\frac{r}{GM}} = 2\pi \sqrt{\frac{r^3}{GM}}$$

양변을 제곱하면:

$$\boxed{T^2 = \frac{4\pi^2}{GM}r^3}$$

이 결과에서 행성의 질량 $m$은 나타나지 않는다. 이는 (a)에서 뉴턴의 제2법칙을 적용할 때 양변에서 $m$이 소거되었기 때문이다. 즉, 같은 중심 천체($M$) 주위를 도는 모든 물체는 질량에 관계없이 같은 $T^2/r^3$ 비를 갖는다. 이것이 케플러 제3법칙이다.

---

## 문제 7 풀이

$m = 2.0\;\text{kg}$, $a = 0.50\;\text{m}$

**(a)** 한 입자(꼭짓점 A)에 대해, 다른 두 입자(B, C)가 각각 거리 $a$에서 힘을 작용한다.

각 힘의 크기:

$$F = G\frac{m^2}{a^2} = (6.674 \times 10^{-11})\frac{(2.0)^2}{(0.50)^2} = (6.674 \times 10^{-11})\frac{4.0}{0.25}$$

$$= 1.07 \times 10^{-9}\;\text{N}$$

정삼각형에서, B와 C에 의한 두 힘은 크기가 같고 사잇각이 $60°$이다. 합력:

$$F_\text{net} = \sqrt{F^2 + F^2 + 2F^2\cos 60°} = F\sqrt{2 + 2\cos 60°} = F\sqrt{2 + 1} = F\sqrt{3}$$

$$F_\text{net} = 1.07 \times 10^{-9} \times \sqrt{3} = \boxed{1.85 \times 10^{-9}\;\text{N}}$$

**(b)** 대칭에 의해, 알짜 중력의 방향은 A에서 BC의 중점을 향한다, 즉 **삼각형의 중심** 을 향한다.

**(c)** 정삼각형의 중심에서 각 꼭짓점까지의 거리:

$$d = \frac{a}{\sqrt{3}} = \frac{0.50}{\sqrt{3}} = 0.289\;\text{m}$$

대칭에 의해, 세 꼭짓점의 질량이 중심의 입자에 작용하는 세 힘은 크기가 같고 $120°$ 간격이므로 벡터합이 $\vec{0}$이다.

$$\boxed{F_\text{net} = 0}$$

---

## 문제 8 풀이

**(a)** 타원에서:

$$\boxed{R_p = a(1-e), \quad R_a = a(1+e)}$$

검증: $R_p + R_a = 2a$ $\checkmark$ (장축의 길이)

**(b)** 각운동량 보존: $L = mv_p R_p = mv_a R_a$

$$\frac{v_p}{v_a} = \frac{R_a}{R_p} = \frac{a(1+e)}{a(1-e)} = \boxed{\frac{1+e}{1-e}}$$

**(c)** 에너지 보존: 근일점에서의 에너지 = 원일점에서의 에너지

$$\frac{1}{2}mv_p^2 - \frac{GMm}{R_p} = \frac{1}{2}mv_a^2 - \frac{GMm}{R_a}$$

또한, 타원 궤도의 역학적 에너지:

$$E = -\frac{GMm}{2a}$$

근일점에서:

$$-\frac{GMm}{2a} = \frac{1}{2}mv_p^2 - \frac{GMm}{R_p}$$

$$\frac{1}{2}v_p^2 = \frac{GM}{R_p} - \frac{GM}{2a} = GM\left(\frac{1}{a(1-e)} - \frac{1}{2a}\right) = \frac{GM}{2a}\left(\frac{2}{1-e} - 1\right) = \frac{GM}{2a}\cdot\frac{1+e}{1-e}$$

$$\boxed{v_p = \sqrt{\frac{GM}{a}\cdot\frac{1+e}{1-e}}}$$

검증: $e = 0$ (원궤도)이면 $v_p = \sqrt{GM/a}$, 이는 원궤도 속력과 일치. $\checkmark$

---

## 문제 9 풀이

$M_E = 5.98 \times 10^{24}\;\text{kg}$, $T = 24.0\;\text{h} = 86400\;\text{s}$

**(a)** 케플러 제3법칙:

$$T^2 = \frac{4\pi^2}{GM_E}r^3$$

$$r^3 = \frac{GM_E T^2}{4\pi^2} = \frac{(6.674 \times 10^{-11})(5.98 \times 10^{24})(86400)^2}{4\pi^2}$$

$$= \frac{(3.99 \times 10^{14})(7.46 \times 10^9)}{39.48} = \frac{2.977 \times 10^{24}}{39.48} = 7.54 \times 10^{22}$$

$$r = (7.54 \times 10^{22})^{1/3} = \boxed{4.22 \times 10^7\;\text{m} = 42{,}200\;\text{km}}$$

**(b)**

$$\frac{r}{R_E} = \frac{4.22 \times 10^7}{6.37 \times 10^6} = \boxed{6.63}$$

지구 반지름의 약 6.6배.

**(c)** 궤도 속력:

$$v = \frac{2\pi r}{T} = \frac{2\pi (4.22 \times 10^7)}{86400} = \frac{2.65 \times 10^8}{86400} = \boxed{3.07 \times 10^3\;\text{m/s} = 3.07\;\text{km/s}}$$

---

## 문제 10 풀이

**(a)** 높이 $h$인 원궤도의 반지름: $r = R + h$

구심력 조건에서:

$$\frac{GMm}{(R+h)^2} = \frac{mv_\text{orb}^2}{R+h}$$

$$\boxed{v_\text{orb} = \sqrt{\frac{GM}{R+h}}}$$

**(b)** 지표면에서의 역학적 에너지 (정지 상태에서 출발):

$$E_i = K_i + U_i = 0 + \left(-\frac{GMm}{R}\right) = -\frac{GMm}{R}$$

원궤도에서의 역학적 에너지:

$$E_f = -\frac{GMm}{2(R+h)}$$

필요한 에너지:

$$\Delta E = E_f - E_i = -\frac{GMm}{2(R+h)} + \frac{GMm}{R}$$

$$\boxed{\Delta E = GMm\left(\frac{1}{R} - \frac{1}{2(R+h)}\right)}$$

정리하면:

$$\Delta E = \frac{GMm}{R}\left(1 - \frac{R}{2(R+h)}\right) = \frac{GMm}{R}\cdot\frac{2(R+h) - R}{2(R+h)} = \frac{GMm(R + 2h)}{2R(R+h)}$$

**(c)** $h \ll R$이면 $R + h \approx R$:

$$\Delta E \approx \frac{GMm(R + 2h)}{2R \cdot R} = \frac{GMm}{2R^2}(R + 2h) = \frac{GMm}{2R} + \frac{GMmh}{R^2}$$

$g = GM/R^2$를 이용하면:

$$\Delta E \approx \frac{1}{2}mgR + mgh$$

$h \ll R$이면 두 번째 항 $mgh$는 첫 번째 항에 비해 작으므로:

$$\boxed{\Delta E \approx \frac{1}{2}mgR + mgh}$$

여기서 $\frac{1}{2}mgR$ 항은 궤도 운동에너지에 해당하고, $mgh$ 항은 높이 상승에 따른 퍼텐셜에너지 증가분이다. 놀랍게도, 저궤도 위성의 경우 궤도 운동에너지($\frac{1}{2}mgR \approx 3.1 \times 10^7\;m$ J)가 위치에너지 증가($mgh$)보다 훨씬 크다.
