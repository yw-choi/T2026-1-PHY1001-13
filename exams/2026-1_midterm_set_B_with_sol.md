# 일반물리 I 중간시험 — Set B

**2026학년도 1학기 · 서강대학교 물리학과**
**시험 시간: 1시간 15분 · 계산기 사용 불가 · 모든 답은 주어진 문자로 표현할 것**

---

## 문제 1 (20점)

벡터의 외적(cross product)에 대해 답하시오.

**(a)** (6점) 단위벡터 $\hat{i}$, $\hat{j}$, $\hat{k}$에 대해 $\hat{i} \times \hat{j} = \hat{k}$, $\hat{j} \times \hat{k} = \hat{i}$, $\hat{k} \times \hat{i} = \hat{j}$임을 외적의 정의(크기와 오른손법칙)를 이용하여 보이시오.

**풀이:**

외적의 정의에 의하면, 두 벡터 $\vec{A}$와 $\vec{B}$의 외적의 **크기** 는

$$|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$$

이고, **방향** 은 오른손법칙에 의해 $\vec{A}$에서 $\vec{B}$로 감아쥘 때 엄지가 가리키는 방향이다.

**$\hat{i} \times \hat{j}$의 경우:**

- 크기: $|\hat{i}||\hat{j}|\sin 90° = (1)(1)(1) = 1$
- 방향: 오른손으로 $\hat{i}$ ($x$축)에서 $\hat{j}$ ($y$축)으로 감아쥐면 엄지가 $+z$ 방향, 즉 $\hat{k}$ 방향을 가리킨다.
- 따라서 $\hat{i} \times \hat{j} = \hat{k}$ $\quad\square$

**$\hat{j} \times \hat{k}$의 경우:**

- 크기: $|\hat{j}||\hat{k}|\sin 90° = 1$
- 방향: 오른손으로 $\hat{j}$ ($y$축)에서 $\hat{k}$ ($z$축)으로 감아쥐면 엄지가 $+x$ 방향, 즉 $\hat{i}$ 방향을 가리킨다.
- 따라서 $\hat{j} \times \hat{k} = \hat{i}$ $\quad\square$

**$\hat{k} \times \hat{i}$의 경우:**

- 크기: $|\hat{k}||\hat{i}|\sin 90° = 1$
- 방향: 오른손으로 $\hat{k}$ ($z$축)에서 $\hat{i}$ ($x$축)으로 감아쥐면 엄지가 $+y$ 방향, 즉 $\hat{j}$ 방향을 가리킨다.
- 따라서 $\hat{k} \times \hat{i} = \hat{j}$ $\quad\square$

---

**(b)** (6점) 같은 단위벡터끼리의 외적이 영벡터임을 보이시오. 즉 $\hat{i} \times \hat{i} = \hat{j} \times \hat{j} = \hat{k} \times \hat{k} = \vec{0}$.

**풀이:**

같은 벡터끼리의 외적에서는 두 벡터 사이의 각도가 $\theta = 0°$이다.

$$|\hat{i} \times \hat{i}| = |\hat{i}||\hat{i}|\sin 0° = (1)(1)(0) = 0$$

크기가 0이므로 $\hat{i} \times \hat{i} = \vec{0}$이다.

동일한 논리로:

$$|\hat{j} \times \hat{j}| = |\hat{j}||\hat{j}|\sin 0° = 0 \implies \hat{j} \times \hat{j} = \vec{0}$$

$$|\hat{k} \times \hat{k}| = |\hat{k}||\hat{k}|\sin 0° = 0 \implies \hat{k} \times \hat{k} = \vec{0}$$

일반적으로, 임의의 벡터 $\vec{A}$에 대해 $\vec{A} \times \vec{A} = \vec{0}$이다. 이는 평행한 두 벡터의 외적은 항상 영벡터이기 때문이다. $\quad\square$

---

**(c)** (8점) (a)와 (b)의 결과를 이용하여 $\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$와 $\vec{b} = b_x\hat{i} + b_y\hat{j} + b_z\hat{k}$의 외적을 성분별로 전개하여 일반 공식을 유도하시오.

**풀이:**

외적의 분배법칙을 이용하여 전개한다:

$$\vec{a} \times \vec{b} = (a_x\hat{i} + a_y\hat{j} + a_z\hat{k}) \times (b_x\hat{i} + b_y\hat{j} + b_z\hat{k})$$

9개의 항을 모두 전개하면:

$$= a_x b_x (\hat{i} \times \hat{i}) + a_x b_y (\hat{i} \times \hat{j}) + a_x b_z (\hat{i} \times \hat{k})$$

$$+ a_y b_x (\hat{j} \times \hat{i}) + a_y b_y (\hat{j} \times \hat{j}) + a_y b_z (\hat{j} \times \hat{k})$$

$$+ a_z b_x (\hat{k} \times \hat{i}) + a_z b_y (\hat{k} \times \hat{j}) + a_z b_z (\hat{k} \times \hat{k})$$

(b)의 결과에 의해 같은 단위벡터끼리의 외적은 $\vec{0}$이므로 대각항은 사라진다. (a)의 결과와 외적의 반교환성 $\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$를 이용하면:

- $\hat{i} \times \hat{j} = \hat{k}$, $\quad \hat{j} \times \hat{i} = -\hat{k}$
- $\hat{j} \times \hat{k} = \hat{i}$, $\quad \hat{k} \times \hat{j} = -\hat{i}$
- $\hat{k} \times \hat{i} = \hat{j}$, $\quad \hat{i} \times \hat{k} = -\hat{j}$

대입하면:

$$\vec{a} \times \vec{b} = a_x b_y \hat{k} + a_x b_z (-\hat{j}) + a_y b_x (-\hat{k}) + a_y b_z \hat{i} + a_z b_x \hat{j} + a_z b_y (-\hat{i})$$

같은 단위벡터끼리 묶으면:

$$\boxed{\vec{a} \times \vec{b} = (a_y b_z - a_z b_y)\hat{i} + (a_z b_x - a_x b_z)\hat{j} + (a_x b_y - a_y b_x)\hat{k}}$$

이는 행렬식 표현으로 쓸 수도 있다:

$$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}$$

---

## 문제 2 (20점)

포물선 운동(projectile motion)에 대해 답하시오. 공기 저항은 무시한다.

**(a)** (10점) 지면에서 초기속력 $v_0$, 발사각 $\theta_0$로 던진 물체의 수평도달거리(range)가

$$R = \frac{v_0^2 \sin 2\theta_0}{g}$$

임을 유도하시오.

**풀이:**

초기 속도의 성분을 분해한다:

$$v_{0x} = v_0 \cos\theta_0, \quad v_{0y} = v_0 \sin\theta_0$$

**체공 시간 구하기:** 물체가 지면에서 출발하여 다시 지면으로 돌아오는 조건은 $y = 0$이다.

$$y = v_{0y} t - \frac{1}{2}g t^2 = 0$$

$$t\left(v_{0y} - \frac{1}{2}g t\right) = 0$$

$t = 0$ (출발)을 제외하면:

$$t_{\text{flight}} = \frac{2 v_{0y}}{g} = \frac{2 v_0 \sin\theta_0}{g}$$

**수평도달거리:** 수평 방향은 등속 운동이므로:

$$R = v_{0x} \cdot t_{\text{flight}} = (v_0 \cos\theta_0)\left(\frac{2 v_0 \sin\theta_0}{g}\right)$$

$$R = \frac{2 v_0^2 \sin\theta_0 \cos\theta_0}{g}$$

이중각 공식 $\sin 2\theta_0 = 2\sin\theta_0\cos\theta_0$을 적용하면:

$$\boxed{R = \frac{v_0^2 \sin 2\theta_0}{g}} \quad\square$$

---

**(b)** (5점) $R$이 최대가 되는 발사각 $\theta_0$를 구하시오.

**풀이:**

$R = \frac{v_0^2 \sin 2\theta_0}{g}$에서 $v_0$와 $g$는 상수이므로, $R$이 최대가 되려면 $\sin 2\theta_0$이 최대가 되어야 한다.

$\sin$ 함수의 최댓값은 1이고, 이는 인수가 $90°$일 때 달성된다:

$$\sin 2\theta_0 = 1 \implies 2\theta_0 = 90°$$

$$\boxed{\theta_0 = 45°}$$

이때 최대 수평도달거리는 $R_{\max} = \frac{v_0^2}{g}$이다.

---

**(c)** (5점) 발사각이 $\theta_0$일 때와 $90° - \theta_0$일 때 수평도달거리가 같음을 보이시오.

**풀이:**

발사각 $\theta_0$일 때의 수평도달거리:

$$R(\theta_0) = \frac{v_0^2 \sin 2\theta_0}{g}$$

발사각 $90° - \theta_0$일 때의 수평도달거리:

$$R(90° - \theta_0) = \frac{v_0^2 \sin[2(90° - \theta_0)]}{g} = \frac{v_0^2 \sin(180° - 2\theta_0)}{g}$$

삼각함수의 성질 $\sin(180° - \alpha) = \sin\alpha$를 이용하면:

$$R(90° - \theta_0) = \frac{v_0^2 \sin 2\theta_0}{g} = R(\theta_0)$$

따라서 두 발사각에서의 수평도달거리가 같다. $\quad\square$

이는 $45°$를 기준으로 대칭인 두 각도(예: $30°$와 $60°$, $20°$와 $70°$)가 같은 수평도달거리를 준다는 것을 의미한다.

---

**(d)** (5점) 같은 물체를 지면이 아니라 높이 $H$인 절벽 위에서 수평으로 ($\theta_0 = 0$) 던졌을 때, 수평도달거리를 $v_0$, $H$, $g$로 나타내시오.

**풀이:**

$\theta_0 = 0$이므로 초기 속도 성분은:

$$v_{0x} = v_0, \quad v_{0y} = 0$$

**낙하 시간 구하기:** 높이 $H$에서 출발하여 지면($y = 0$)에 도달하는 시간을 구한다. 위쪽을 양의 방향으로 잡으면:

$$y = H + v_{0y}t - \frac{1}{2}g t^2 = H - \frac{1}{2}g t^2$$

$y = 0$ (지면)으로 놓으면:

$$0 = H - \frac{1}{2}g t^2$$

$$t = \sqrt{\frac{2H}{g}}$$

(양의 근만 물리적으로 의미가 있다.)

**수평도달거리:**

$$R = v_{0x} \cdot t = v_0 \sqrt{\frac{2H}{g}}$$

$$\boxed{R = v_0 \sqrt{\frac{2H}{g}}}$$

---

## 문제 3 (25점)

마찰이 있는 경사면과 원운동에 대해 답하시오.

**(a)** (10점) 질량 $m$인 물체가 정지마찰계수 $\mu_s$인 경사면(경사각 $\theta$) 위에 놓여 있다. 자유물체도를 그리고, 물체가 미끄러지지 않기 위한 조건 $\tan\theta \le \mu_s$를 유도하시오.

**풀이:**

**자유물체도(Free Body Diagram):**

경사면 위의 물체에 작용하는 힘은 세 가지이다:
- 중력 $m\vec{g}$: 수직 아래 방향
- 수직항력 $\vec{N}$: 경사면에 수직인 방향 (면에서 물체 쪽)
- 정지마찰력 $\vec{f}_s$: 경사면을 따라 위쪽 방향 (미끄러짐을 방지)

경사면에 평행한 축($x$, 아래쪽이 양)과 수직인 축($y$, 면에서 바깥쪽이 양)을 설정한다.

**$y$방향 (경사면에 수직):** 가속도가 없으므로:

$$N - mg\cos\theta = 0$$

$$N = mg\cos\theta \quad \cdots (1)$$

**$x$방향 (경사면에 평행):** 가속도가 없으므로:

$$mg\sin\theta - f_s = 0$$

$$f_s = mg\sin\theta \quad \cdots (2)$$

**미끄러지지 않는 조건:** 정지마찰력은 최대 정지마찰력을 넘을 수 없다:

$$f_s \le \mu_s N$$

(1)과 (2)를 대입하면:

$$mg\sin\theta \le \mu_s \cdot mg\cos\theta$$

양변을 $mg\cos\theta > 0$으로 나누면:

$$\boxed{\tan\theta \le \mu_s} \quad\square$$

---

**(b)** (8점) 질량 $m$인 자동차가 반지름 $r$인 수평 원형 트랙을 돈다. 도로와 타이어 사이의 정지마찰계수가 $\mu_s$일 때, 미끄러지지 않는 최대 속력 $v_\text{max}$를 구하시오.

**풀이:**

수평 원형 트랙에서 자동차에 작용하는 힘:
- 중력 $mg$: 아래 방향
- 수직항력 $N$: 위 방향
- 정지마찰력 $f_s$: 원의 중심 방향 (구심력 역할)

**수직 방향** (가속도 없음):

$$N = mg \quad \cdots (1)$$

**수평 방향** (구심 방향): 구심 가속도 $a_c = v^2/r$이 필요하므로:

$$f_s = \frac{mv^2}{r} \quad \cdots (2)$$

미끄러지지 않으려면:

$$f_s \le \mu_s N$$

$$\frac{mv^2}{r} \le \mu_s mg$$

$$v^2 \le \mu_s g r$$

따라서 최대 속력은:

$$\boxed{v_{\max} = \sqrt{\mu_s g r}}$$

---

**(c)** (7점) 같은 원형 트랙이 경사각 $\phi$로 **뱅크** 되어 있고 마찰이 없다면, 일정 속력으로 원운동이 가능한 속력 $v$를 $r$, $g$, $\phi$로 나타내시오.

**풀이:**

뱅크된 트랙에서 마찰이 없으므로 작용하는 힘은 중력 $mg$와 수직항력 $N$뿐이다. 수직항력은 뱅크된 면에 수직이므로, 수평 성분이 구심력을 제공한다.

**수직 방향** (가속도 없음):

$$N\cos\phi = mg \quad \cdots (1)$$

**수평 방향** (구심 방향):

$$N\sin\phi = \frac{mv^2}{r} \quad \cdots (2)$$

(2)를 (1)로 나누면:

$$\frac{N\sin\phi}{N\cos\phi} = \frac{v^2/r}{g}$$

$$\tan\phi = \frac{v^2}{rg}$$

따라서:

$$\boxed{v = \sqrt{rg\tan\phi}}$$

이 속력은 질량에 무관하며, 이 특정 속력에서만 마찰 없이 원운동이 가능하다. 이보다 빠르면 바깥으로, 느리면 안쪽으로 미끄러진다.

---

## 문제 4 (20점)

퍼텐셜에너지 함수가 $U(x) = \alpha x^2 - \beta x^3$으로 주어져 있다 ($\alpha, \beta > 0$, 적절한 단위).

**(a)** (5점) 이 계에 작용하는 힘 $F(x)$를 구하시오.

**풀이:**

보존력은 퍼텐셜에너지의 음의 미분으로 주어진다:

$$F(x) = -\frac{dU}{dx}$$

$$U(x) = \alpha x^2 - \beta x^3$$

미분하면:

$$\frac{dU}{dx} = 2\alpha x - 3\beta x^2$$

따라서:

$$\boxed{F(x) = -2\alpha x + 3\beta x^2}$$

---

**(b)** (7점) 평형점(equilibrium point)을 모두 구하고, 각각이 안정 평형인지 불안정 평형인지 판별하시오.

**풀이:**

평형점은 $F(x) = 0$인 점이다:

$$-2\alpha x + 3\beta x^2 = 0$$

$$x(-2\alpha + 3\beta x) = 0$$

따라서 두 평형점이 존재한다:

$$x_1 = 0, \quad x_2 = \frac{2\alpha}{3\beta}$$

**안정성 판별:** $\frac{d^2U}{dx^2}$의 부호로 판별한다.

$$\frac{d^2U}{dx^2} = 2\alpha - 6\beta x$$

**$x_1 = 0$에서:**

$$\left.\frac{d^2U}{dx^2}\right|_{x=0} = 2\alpha > 0$$

$\frac{d^2U}{dx^2} > 0$이므로 $U(x)$가 아래로 볼록(극소)이다. 따라서 $x_1 = 0$은 **안정 평형점** 이다.

**$x_2 = \frac{2\alpha}{3\beta}$에서:**

$$\left.\frac{d^2U}{dx^2}\right|_{x=2\alpha/3\beta} = 2\alpha - 6\beta \cdot \frac{2\alpha}{3\beta} = 2\alpha - 4\alpha = -2\alpha < 0$$

$\frac{d^2U}{dx^2} < 0$이므로 $U(x)$가 위로 볼록(극대)이다. 따라서 $x_2 = \frac{2\alpha}{3\beta}$는 **불안정 평형점** 이다.

---

**(c)** (8점) 안정 평형점 근처에서의 퍼텐셜에너지 곡선의 개형을 정성적으로 스케치하시오. 이 평형점에서 입자가 작은 진폭으로 진동한다면, 총 역학적 에너지 $E$와 되돌이점(turning points)의 관계를 설명하시오.

**풀이:**

**퍼텐셜에너지 곡선의 특징:**

- $U(0) = 0$ (안정 평형점, 극소)
- $U\left(\frac{2\alpha}{3\beta}\right) = \alpha\left(\frac{2\alpha}{3\beta}\right)^2 - \beta\left(\frac{2\alpha}{3\beta}\right)^3 = \frac{4\alpha^3}{9\beta^2} - \frac{8\alpha^3}{27\beta^2} = \frac{4\alpha^3}{27\beta^2}$ (불안정 평형점, 극대)
- $x \to -\infty$이면 $-\beta x^3 \to +\infty$이므로 $U \to +\infty$
- $x \to +\infty$이면 $-\beta x^3 \to -\infty$이므로 $U \to -\infty$

따라서 $x = 0$ 부근에서 아래로 볼록한 우물 형태를 이루고, $x = \frac{2\alpha}{3\beta}$에서 극대(언덕)를 형성한 후 $x$가 더 커지면 $U$는 $-\infty$로 발산한다.

**되돌이점과 역학적 에너지의 관계:**

총 역학적 에너지 $E = K + U$에서 운동에너지 $K \ge 0$이므로, 입자는 $U(x) \le E$인 영역에서만 운동할 수 있다.

되돌이점(turning point)은 $K = 0$, 즉 $U(x) = E$인 점이다. 이 점에서 입자의 속도가 0이 되고 방향이 반전된다.

안정 평형점 $x = 0$ 근처에서 작은 진폭의 진동을 하는 경우:

- 총 에너지 $E$가 $0 < E < \frac{4\alpha^3}{27\beta^2}$인 범위에 있다면, $U(x) = E$를 만족하는 두 되돌이점 $x_a$와 $x_b$ ($x_a < 0 < x_b$) 사이에서 입자가 왕복 진동한다.
- 에너지가 작을수록 두 되돌이점 사이의 간격이 좁아지고, $E \to 0$이면 진동 진폭이 0으로 줄어든다.
- $E = \frac{4\alpha^3}{27\beta^2}$ (극대점의 퍼텐셜에너지)에 도달하면, 입자는 불안정 평형점을 넘어서 탈출할 수 있다. 이 에너지를 초과하면 입자는 $x > \frac{2\alpha}{3\beta}$ 영역으로 빠져나가 돌아오지 않는다 (비속박 상태).
- 안정 평형점 근처에서 $U(x) \approx \alpha x^2$ (이차항이 지배)이므로, 작은 진폭에서 진동은 근사적으로 단순 조화 진동에 해당한다.

---

## 문제 5 (25점) — 각운동량 보존

질량을 무시할 수 있는 반지름 $R$의 원판이 수직 축에 대해 자유롭게 회전할 수 있다. 원판 가장자리에 질량 $M$인 물체가 부착되어 있고, 계는 정지해 있다. 질량 $m$인 작은 공이 속력 $v_0$로 원판의 가장자리에 접선 방향으로 날아와 물체와 완전비탄성 충돌을 한다.

**(a)** (5점) 충돌 직전에 공의 축에 대한 각운동량을 구하시오.

**풀이:**

각운동량은 $\vec{L} = \vec{r} \times \vec{p}$로 정의된다.

공이 원판 가장자리에 접선 방향으로 날아오므로, 위치벡터 $\vec{r}$ (회전축에서 공까지)의 크기는 $R$이고, 운동량 $\vec{p} = m\vec{v}_0$의 방향은 접선 방향이다. 접선 방향이므로 $\vec{r}$과 $\vec{p}$는 수직이다 ($\theta = 90°$).

따라서:

$$L = rp\sin 90° = R \cdot mv_0 \cdot 1$$

$$\boxed{L = mRv_0}$$

방향은 오른손법칙에 의해 회전축 방향(위쪽)이다.

---

**(b)** (8점) 충돌 직후 계의 각속도 $\omega$를 $m$, $M$, $v_0$, $R$로 나타내시오.

**풀이:**

외부 토크가 없으므로 **각운동량이 보존** 된다.

**충돌 전 각운동량:**

- 공: $L_{\text{공}} = mRv_0$ (위에서 구함)
- 원판 + 물체: 정지해 있으므로 $L_{\text{판}} = 0$
- 총 각운동량: $L_i = mRv_0$

**충돌 후 각운동량:**

완전비탄성 충돌이므로 공과 물체가 합쳐진다. 합쳐진 질량 $(m + M)$이 반지름 $R$에서 회전한다. 원판의 질량은 무시하므로:

$$I = (m + M)R^2$$

충돌 직후 각속도가 $\omega$이면:

$$L_f = I\omega = (m + M)R^2 \omega$$

**각운동량 보존:**

$$mRv_0 = (m + M)R^2 \omega$$

$$\boxed{\omega = \frac{mv_0}{(m + M)R}}$$

---

**(c)** (5점) 충돌 전후의 운동에너지를 비교하고, 에너지 손실 비율을 $m$, $M$으로 나타내시오.

**풀이:**

**충돌 전 운동에너지:**

$$K_i = \frac{1}{2}mv_0^2$$

(물체와 원판은 정지해 있으므로 기여 없음)

**충돌 후 운동에너지:**

$$K_f = \frac{1}{2}I\omega^2 = \frac{1}{2}(m + M)R^2 \left(\frac{mv_0}{(m+M)R}\right)^2$$

$$= \frac{1}{2}(m + M)R^2 \cdot \frac{m^2 v_0^2}{(m+M)^2 R^2}$$

$$= \frac{m^2 v_0^2}{2(m + M)}$$

**에너지 손실:**

$$\Delta K = K_i - K_f = \frac{1}{2}mv_0^2 - \frac{m^2 v_0^2}{2(m+M)}$$

$$= \frac{mv_0^2}{2}\left(1 - \frac{m}{m+M}\right) = \frac{mv_0^2}{2} \cdot \frac{M}{m+M}$$

**에너지 손실 비율:**

$$\frac{\Delta K}{K_i} = \frac{\frac{mv_0^2}{2} \cdot \frac{M}{m+M}}{\frac{1}{2}mv_0^2}$$

$$\boxed{\frac{\Delta K}{K_i} = \frac{M}{m + M}}$$

이는 선운동에서의 완전비탄성 충돌의 에너지 손실 비율과 동일한 형태이다. $M \gg m$이면 거의 모든 에너지가 손실되고, $m \gg M$이면 손실이 작다.

---

**(d)** (7점) 충돌 후 물체와 공이 합쳐진 덩어리가 줄을 잡아당겨 반지름 $r_f = R/2$인 위치까지 이동한다. 각운동량 보존을 이용하여 새로운 각속도 $\omega_f$를 구하고, 회전 운동에너지의 변화를 논하시오.

**풀이:**

줄을 잡아당기는 힘은 회전축을 지나므로 토크를 만들지 않는다. 따라서 **각운동량이 보존** 된다.

**반지름 변화 전 (반지름 $R$):**

$$L_i = (m + M)R^2 \omega$$

여기서 $\omega = \frac{mv_0}{(m+M)R}$이므로:

$$L_i = (m + M)R^2 \cdot \frac{mv_0}{(m+M)R} = mRv_0$$

**반지름 변화 후 (반지름 $r_f = R/2$):**

$$L_f = (m + M)r_f^2 \omega_f = (m+M)\frac{R^2}{4}\omega_f$$

**각운동량 보존** $L_i = L_f$:

$$mRv_0 = (m+M)\frac{R^2}{4}\omega_f$$

$$\omega_f = \frac{4mv_0}{(m+M)R}$$

(b)의 결과와 비교하면:

$$\boxed{\omega_f = 4\omega = \frac{4mv_0}{(m+M)R}}$$

반지름이 절반으로 줄었으므로 각속도는 4배 증가한다 ($I \propto r^2$이므로 관성모멘트가 $1/4$이 되고, $L = I\omega$ 보존에 의해 $\omega$가 4배).

**회전 운동에너지의 변화:**

변화 전:

$$K_i = \frac{1}{2}(m+M)R^2 \omega^2 = \frac{m^2 v_0^2}{2(m+M)}$$

변화 후:

$$K_f = \frac{1}{2}(m+M)\frac{R^2}{4}(4\omega)^2 = \frac{1}{2}(m+M)\frac{R^2}{4} \cdot 16\omega^2 = 4 \cdot \frac{1}{2}(m+M)R^2\omega^2$$

$$K_f = 4K_i = \frac{2m^2 v_0^2}{(m+M)}$$

따라서:

$$\Delta K = K_f - K_i = 3K_i = \frac{3m^2v_0^2}{2(m+M)}$$

회전 운동에너지가 **4배로 증가** 했다. 이 에너지 증가분은 줄을 잡아당기는 힘이 한 **일** 에서 비롯된다. 줄을 당기는 힘은 변위 방향과 같은 방향(안쪽)으로 작용하므로 양의 일을 하고, 그만큼 계의 운동에너지가 증가한 것이다. 각운동량은 보존되지만 에너지는 외부에서 일을 해준 만큼 증가하므로, 에너지 보존에도 모순이 없다.

---

## 채점 기준 요약

| 문항 | 배점 | 핵심 채점 요소 |
|------|------|---------------|
| **1(a)** | 6 | 크기 계산 ($\sin 90° = 1$) 3점 + 오른손법칙으로 방향 결정 3점 |
| **1(b)** | 6 | $\sin 0° = 0$ 적용하여 크기 = 0임을 보임 (각 2점) |
| **1(c)** | 8 | 9개 항 전개 3점 + (a)(b) 결과 대입 3점 + 최종 공식 정리 2점 |
| **2(a)** | 10 | 속도 성분 분해 2점 + 체공 시간 유도 4점 + 이중각 공식 적용하여 $R$ 유도 4점 |
| **2(b)** | 5 | $\sin 2\theta_0 = 1$ 조건으로 $\theta_0 = 45°$ 도출 |
| **2(c)** | 5 | $\sin(180° - 2\theta_0) = \sin 2\theta_0$ 이용하여 증명 |
| **2(d)** | 5 | 낙하 시간 $t = \sqrt{2H/g}$ 유도 3점 + $R = v_0 t$ 계산 2점 |
| **3(a)** | 10 | 자유물체도(3개 힘) 4점 + 수직·평행 방향 분해 3점 + $\tan\theta \le \mu_s$ 유도 3점 |
| **3(b)** | 8 | 구심력 = 마찰력 설정 4점 + $v_{\max}$ 유도 4점 |
| **3(c)** | 7 | 수직·수평 방향 힘 분해 4점 + 나누기로 $v$ 유도 3점 |
| **4(a)** | 5 | $F = -dU/dx$ 적용하여 올바른 미분 |
| **4(b)** | 7 | 평형점 2개 구하기 3점 + $d^2U/dx^2$ 부호로 안정성 판별 4점 |
| **4(c)** | 8 | 곡선 개형 스케치 3점 + 되돌이점 = $U(x) = E$ 설명 3점 + 탈출 에너지 조건 2점 |
| **5(a)** | 5 | $L = mRv_0$ (접선 방향이므로 $\sin 90°$) |
| **5(b)** | 8 | 각운동량 보존 적용 4점 + $\omega$ 도출 4점 |
| **5(c)** | 5 | $K_i$, $K_f$ 계산 3점 + 손실 비율 $M/(m+M)$ 도출 2점 |
| **5(d)** | 7 | 각운동량 보존으로 $\omega_f = 4\omega$ 유도 4점 + 에너지 4배 증가 및 줄의 일 설명 3점 |
