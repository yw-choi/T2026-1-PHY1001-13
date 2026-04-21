# Chapter 12: Equilibrium and Elasticity — 풀이

---

## 문제 1 풀이

$L = 4.0\;\text{m}$, $M = 50\;\text{kg}$, A는 왼쪽 끝($x = 0$), B는 $x = 3.0\;\text{m}$, 물체($m = 20\;\text{kg}$)는 오른쪽 끝($x = 4.0\;\text{m}$)

**(a)** 힘의 평형 (수직 방향):

$$F_A + F_B = Mg + mg = (50 + 20) \times 9.80 = 686\;\text{N} \quad \cdots\;(1)$$

토크의 평형 (A 점 기준, 반시계 방향을 양으로):

$$F_B \times 3.0 - Mg \times 2.0 - mg \times 4.0 = 0$$

$$F_B = \frac{Mg \times 2.0 + mg \times 4.0}{3.0} = \frac{50 \times 9.80 \times 2.0 + 20 \times 9.80 \times 4.0}{3.0}$$

$$F_B = \frac{980 + 784}{3.0} = \frac{1764}{3.0} = \boxed{588\;\text{N}}$$

식 (1)에서:

$$F_A = 686 - 588 = \boxed{98\;\text{N}}$$

**(b)** 보가 B를 기준으로 기울어지기 시작하는 조건: $F_A = 0$ (A가 받침대에서 떨어짐)

B 점 기준 토크의 평형:

$$-F_A \times 3.0 + Mg \times (2.0 - 3.0) \times (-1) + mg \times (4.0 - 3.0) = 0$$

A 점 기준으로 다시 정리하면 $F_A = 0$이므로:

$$F_B \times 3.0 = Mg \times 2.0 + m_c g \times 4.0$$

이때 $F_B = Mg + m_c g$ (힘의 평형에서 $F_A = 0$)이므로:

$$(M + m_c)g \times 3.0 = Mg \times 2.0 + m_c g \times 4.0$$

$$3.0M + 3.0m_c = 2.0M + 4.0m_c$$

$$M = m_c$$

$$\boxed{m_c = 50\;\text{kg}}$$

검증: $m = 50\;\text{kg}$일 때 A 기준 토크: $F_B \times 3.0 = 50 \times 9.80 \times 2.0 + 50 \times 9.80 \times 4.0 = 2940$, $F_B = 980\;\text{N}$, $F_A = (50+50)(9.80) - 980 = 0$ $\checkmark$

**(c)** 보는 $\boxed{\text{받침대 B를 기준으로}}$ 기울어진다. 물체가 오른쪽 끝에 매달려 있으므로, $m$이 증가하면 오른쪽에 작용하는 토크가 커져 보가 B를 지렛점으로 시계 방향으로 회전하려 한다. B는 A보다 물체에 가까우므로, B가 회전의 받침점 역할을 하게 된다.

---

## 문제 2 풀이

$L = 5.0\;\text{m}$, $M = 12\;\text{kg}$, $\theta = 60°$, $m = 70\;\text{kg}$

매끄러운 벽 → 벽이 사다리에 수평 힘 $F_w$만 작용 (마찰 없음)

바닥 → 수직 항력 $N$과 수평 마찰력 $f$

**(a)** $d = L/2 = 2.5\;\text{m}$

힘의 평형:

수평: $f = F_w$ $\cdots$ (1)

수직: $N = (M + m)g = (12 + 70) \times 9.80 = 803.6\;\text{N}$ $\cdots$ (2)

토크의 평형 (바닥 접점 기준):

사다리의 질량중심은 사다리 중간 ($L/2$), 바닥에서의 수평 거리: $(L/2)\cos\theta$

사람의 위치 $d = L/2$, 바닥에서의 수평 거리: $(L/2)\cos\theta$

벽의 힘 $F_w$가 작용하는 높이: $L\sin\theta$

$$Mg \cdot \frac{L}{2}\cos\theta + mg \cdot \frac{L}{2}\cos\theta - F_w \cdot L\sin\theta = 0$$

$$F_w = \frac{(M + m)g \cdot \frac{L}{2}\cos\theta}{L\sin\theta} = \frac{(M + m)g\cos\theta}{2\sin\theta} = \frac{(M + m)g}{2\tan\theta}$$

$$F_w = \frac{(82)(9.80)}{2\tan 60°} = \frac{803.6}{2 \times 1.732} = \frac{803.6}{3.464} = \boxed{232\;\text{N}}$$

$$f = F_w = \boxed{232\;\text{N}}$$

**(b)** 사람이 거리 $d$에 있을 때 토크의 평형 (바닥 접점 기준):

$$Mg \cdot \frac{L}{2}\cos\theta + mg \cdot d\cos\theta - F_w \cdot L\sin\theta = 0$$

$$F_w = \frac{Mg\frac{L}{2}\cos\theta + mgd\cos\theta}{L\sin\theta} = \frac{\cos\theta}{L\sin\theta}\left(\frac{ML}{2} + md\right)g$$

사다리가 미끄러지는 조건: $f = F_w = \mu_s N = \mu_s(M+m)g$

$$\frac{\cos\theta}{L\sin\theta}\left(\frac{ML}{2} + md\right)g = \mu_s(M+m)g$$

$$\frac{ML}{2} + md = \mu_s(M+m)L\tan\theta$$

$$d = \frac{\mu_s(M+m)L\tan\theta - ML/2}{m}$$

$$d_\text{max} = \frac{0.40 \times 82 \times 5.0 \times 1.732 - 12 \times 5.0/2}{70}$$

$$= \frac{0.40 \times 82 \times 8.660 - 30.0}{70} = \frac{284.0 - 30.0}{70} = \frac{254.0}{70} = \boxed{3.63\;\text{m}}$$

검증: $d_\text{max}/L = 3.63/5.0 = 0.73$, 사다리의 $73\%$ 지점까지 올라갈 수 있다.

**(c)** $d_\text{max}$의 식에서 $\tan\theta$가 커지면 ($\theta$ 증가) $d_\text{max}$도 증가한다. 사다리를 더 가파르게 세우면 벽에 수평으로 미는 힘($F_w$)이 줄어들고, 따라서 필요한 마찰력도 줄어든다. 극한적으로 $\theta = 90°$이면 벽에 힘이 전혀 필요 없으므로 사다리가 미끄러지지 않는다.

---

## 문제 3 풀이

**(a)** 질량중심의 운동 방정식:

$$\vec{F}_\text{net} = M\vec{a}_\text{com}$$

정적 평형에서는 물체가 정지해 있으므로 $\vec{a}_\text{com} = \vec{0}$. 따라서:

$$\boxed{\sum \vec{F} = \vec{0}}$$

성분별로: $\sum F_x = 0$, $\sum F_y = 0$, $\sum F_z = 0$

**(b)** 회전 운동 방정식:

$$\vec{\tau}_\text{net} = I\vec{\alpha}$$

정적 평형에서는 물체가 회전하지 않으므로 $\vec{\alpha} = \vec{0}$. 따라서:

$$\boxed{\sum \vec{\tau} = \vec{0}}$$

**(c)** 점 O에 대한 힘 $\vec{F}_i$의 토크: $\vec{\tau}_{i,O} = \vec{r}_{i,O} \times \vec{F}_i$

다른 점 O$'$에 대한 토크: $\vec{\tau}_{i,O'} = \vec{r}_{i,O'} \times \vec{F}_i$

$\vec{r}_{i,O} = \vec{r}_{i,O'} + \vec{r}_{O'O}$이므로 ($\vec{r}_{O'O}$는 O$'$에서 O로의 벡터):

$$\sum_i \vec{\tau}_{i,O} = \sum_i (\vec{r}_{i,O'} + \vec{r}_{O'O}) \times \vec{F}_i = \sum_i \vec{r}_{i,O'} \times \vec{F}_i + \vec{r}_{O'O} \times \sum_i \vec{F}_i$$

힘의 평형 조건 $\sum_i \vec{F}_i = \vec{0}$에 의해 두 번째 항이 사라지므로:

$$\sum_i \vec{\tau}_{i,O} = \sum_i \vec{\tau}_{i,O'}$$

따라서 한 점에 대해 $\sum \vec{\tau} = \vec{0}$이면 다른 어떤 점에 대해서도 $\sum \vec{\tau} = \vec{0}$이다. $\blacksquare$

---

## 문제 4 풀이

$L = 2.0\;\text{m}$, $A = 4.0 \times 10^{-4}\;\text{m}^2$, $E = 200\;\text{GPa} = 2.0 \times 10^{11}\;\text{Pa}$, $F = 8.0 \times 10^{4}\;\text{N}$

**(a)**

$$\sigma = \frac{F}{A} = \frac{8.0 \times 10^{4}}{4.0 \times 10^{-4}} = \boxed{2.0 \times 10^{8}\;\text{Pa} = 200\;\text{MPa}}$$

$$\varepsilon = \frac{\sigma}{E} = \frac{2.0 \times 10^{8}}{2.0 \times 10^{11}} = \boxed{1.0 \times 10^{-3}}$$

**(b)**

$$\Delta L = \varepsilon \cdot L = 1.0 \times 10^{-3} \times 2.0 = \boxed{2.0 \times 10^{-3}\;\text{m} = 2.0\;\text{mm}}$$

**(c)** 알루미늄의 경우:

$$\Delta L_\text{Al} = \frac{FL}{A E_\text{Al}} = \frac{FL}{A} \cdot \frac{1}{E_\text{Al}}$$

$$\frac{\Delta L_\text{Al}}{\Delta L_\text{steel}} = \frac{E_\text{steel}}{E_\text{Al}} = \frac{200}{70} = \boxed{2.86\;\text{배}}$$

영률이 작을수록 같은 응력에 대해 더 많이 변형되므로, 알루미늄이 강철보다 약 2.9배 더 많이 줄어든다.

---

## 문제 5 풀이

$a = 10.0\;\text{cm} = 0.100\;\text{m}$, $B = 140\;\text{GPa} = 1.40 \times 10^{11}\;\text{Pa}$

$V = a^3 = (0.100)^3 = 1.00 \times 10^{-3}\;\text{m}^3 = 1000\;\text{cm}^3$

**(a)** 체적탄성률의 정의: $\Delta p = -B \frac{\Delta V}{V}$

$$\left|\frac{\Delta V}{V}\right| = \frac{\Delta p}{B} = \frac{1.0 \times 10^{8}}{1.40 \times 10^{11}} = \boxed{7.14 \times 10^{-4}}$$

**(b)**

$$|\Delta V| = 7.14 \times 10^{-4} \times 1.00 \times 10^{-3}\;\text{m}^3 = 7.14 \times 10^{-7}\;\text{m}^3$$

$$= 7.14 \times 10^{-7} \times 10^{6}\;\text{cm}^3 = \boxed{0.714\;\text{cm}^3}$$

**(c)** $|\Delta V/V| = 0.010$이 되려면:

$$\Delta p = B \times 0.010 = 1.40 \times 10^{11} \times 0.010 = \boxed{1.40 \times 10^{9}\;\text{Pa} = 1.40\;\text{GPa}}$$

이는 약 $1.4 \times 10^{4}$ 기압에 해당한다.

---

## 문제 6 풀이

**(a)**

- **인장/압축 변형** : 물체의 한 축 방향으로 잡아당기거나(인장) 누르는(압축) 힘에 의해 그 방향으로 길이가 변하는 변형이다.
- **전단 변형** : 물체의 한 면에 평행한 방향으로 힘이 작용하여 물체가 비틀리듯 형태가 변하는 변형이다.
- **체적 변형** : 물체 표면 전체에 균일한 압력이 작용하여 부피가 변하는 변형이다.

**(b)** 영률에 의한 인장 변형:

$$\Delta L = \frac{FL}{AE} = \frac{5.0 \times 10^{4} \times 1.5}{2.0 \times 10^{-4} \times 2.0 \times 10^{11}} = \frac{7.5 \times 10^{4}}{4.0 \times 10^{7}} = \boxed{1.875 \times 10^{-3}\;\text{m} \approx 1.9\;\text{mm}}$$

**(c)** 전단탄성률에 의한 전단 변형:

$$\Delta x = \frac{FL}{AG} = \frac{5.0 \times 10^{4} \times 1.5}{2.0 \times 10^{-4} \times 8.0 \times 10^{10}} = \frac{7.5 \times 10^{4}}{1.6 \times 10^{7}} = \boxed{4.69 \times 10^{-3}\;\text{m} \approx 4.7\;\text{mm}}$$

$$\frac{\Delta x}{\Delta L} = \frac{E}{G} = \frac{200}{80} = 2.5$$

$\boxed{\text{전단 변형이 인장 변형의 2.5배로 더 크다.}}$ 이는 $G < E$ (전단탄성률이 영률보다 작음)이기 때문이다. 일반적으로 고체는 축 방향 변형보다 전단 변형에 더 약하다.
