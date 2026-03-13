# Chapter 3: Vectors — 풀이

---

## 문제 1 풀이

$\vec{a} = 3.0\,\hat{i} + 4.0\,\hat{j}$, $\vec{b} = -2.0\,\hat{i} + 5.0\,\hat{j}$

**(a)**

$$\vec{a} + \vec{b} = (3.0 - 2.0)\hat{i} + (4.0 + 5.0)\hat{j} = \boxed{1.0\,\hat{i} + 9.0\,\hat{j}}$$

$$\vec{a} - \vec{b} = (3.0 + 2.0)\hat{i} + (4.0 - 5.0)\hat{j} = \boxed{5.0\,\hat{i} - 1.0\,\hat{j}}$$

**(b)**

$$|\vec{a} + \vec{b}| = \sqrt{1.0^2 + 9.0^2} = \sqrt{82.0} = \boxed{9.06}$$

$$\theta = \arctan\frac{9.0}{1.0} = \boxed{83.7°}$$

**(c)**

$$|\vec{a} - \vec{b}| = \sqrt{5.0^2 + (-1.0)^2} = \sqrt{26.0} = \boxed{5.10}$$

$$\theta = \arctan\frac{-1.0}{5.0} = \boxed{-11.3°}$$

---

## 문제 2 풀이

**(a) 내적**

$\vec{a} \cdot \vec{b} = ab\cos\phi$

- 수직 ($\phi = 90°$): $\cos 90° = 0$ $\implies$ $\vec{a} \cdot \vec{b} = 0$
- 평행 ($\phi = 0°$): $\cos 0° = 1$ $\implies$ $\vec{a} \cdot \vec{b} = ab$
- 반평행 ($\phi = 180°$): $\cos 180° = -1$ $\implies$ $\vec{a} \cdot \vec{b} = -ab$

**(b) 외적**

$|\vec{a} \times \vec{b}| = ab\sin\phi$

- 수직 ($\phi = 90°$): $\sin 90° = 1$ $\implies$ $|\vec{a} \times \vec{b}| = ab$
- 평행/반평행 ($\phi = 0°, 180°$): $\sin\phi = 0$ $\implies$ $|\vec{a} \times \vec{b}| = 0$

**(c)** $\vec{a} \cdot \vec{b} = 0$ $\implies$ $\cos\phi = 0$ ($\phi = 90°$), $|\vec{a} \times \vec{b}| = 0$ $\implies$ $\sin\phi = 0$ ($\phi = 0°, 180°$)

동시에 성립하는 $\phi$는 없으므로, $\boxed{a = 0 \text{ 또는 } b = 0}$ (영벡터)이어야 한다.

---

## 문제 3 풀이

$\vec{a} = 2.0\,\hat{i} - 3.0\,\hat{j} + 1.0\,\hat{k}$, $\vec{b} = -1.0\,\hat{i} + 2.0\,\hat{j} + 4.0\,\hat{k}$

**(a)**

$$\vec{a} \cdot \vec{b} = (2.0)(-1.0) + (-3.0)(2.0) + (1.0)(4.0) = -2.0 - 6.0 + 4.0 = \boxed{-4.0}$$

**(b)**

$$|\vec{a}\,| = \sqrt{4.0 + 9.0 + 1.0} = \sqrt{14.0} = 3.742$$

$$|\vec{b}\,| = \sqrt{1.0 + 4.0 + 16.0} = \sqrt{21.0} = 4.583$$

$$\cos\phi = \frac{-4.0}{3.742 \times 4.583} = \frac{-4.0}{17.15} = -0.2332 \implies \boxed{\phi \approx 103.5°}$$

**(c)**

$$\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2.0 & -3.0 & 1.0 \\ -1.0 & 2.0 & 4.0 \end{vmatrix}$$

$$= \hat{i}[(-3.0)(4.0) - (1.0)(2.0)] - \hat{j}[(2.0)(4.0) - (1.0)(-1.0)] + \hat{k}[(2.0)(2.0) - (-3.0)(-1.0)]$$

$$= \hat{i}(-14.0) - \hat{j}(9.0) + \hat{k}(1.0) = \boxed{-14.0\,\hat{i} - 9.0\,\hat{j} + 1.0\,\hat{k}}$$

---

## 문제 4 풀이

$|\vec{c}\,| = 10.0$, $\theta_c = 120°$

**(a)**

$$c_x = 10.0\cos 120° = -5.00, \quad c_y = 10.0\sin 120° = 8.66$$

$$\boxed{\vec{c} = -5.00\,\hat{i} + 8.66\,\hat{j}}$$

**(b)** $\vec{d} = 5.0\,\hat{i}$

$$\vec{c} + \vec{d} = (-5.00 + 5.0)\hat{i} + 8.66\,\hat{j} = \boxed{8.66\,\hat{j}}$$

**(c)**

$$|\vec{c} + \vec{d}\,| = \boxed{8.66}, \quad \theta = \boxed{90°}\;(+y\text{ 방향})$$

---

## 문제 5 풀이

**(a)**

$\hat{i} \times \hat{j}$: 크기 $= |\hat{i}\,||\hat{j}\,|\sin 90° = 1$. 오른손법칙: $\hat{i} \to \hat{j}$ 방향으로 감으면 $+z$ $\implies$ $\boxed{\hat{i} \times \hat{j} = \hat{k}}$

같은 방법으로: $\boxed{\hat{j} \times \hat{k} = \hat{i}}$, $\boxed{\hat{k} \times \hat{i} = \hat{j}}$

**(b)**

$$|\hat{i} \times \hat{i}\,| = |\hat{i}\,|^2 \sin 0° = 0 \implies \boxed{\hat{i} \times \hat{i} = \vec{0}}$$

마찬가지로 $\hat{j} \times \hat{j} = \vec{0}$, $\hat{k} \times \hat{k} = \vec{0}$

**(c)** 분배법칙으로 전개 (9개 항):

$$\vec{a} \times \vec{b} = a_x b_x(\hat{i} \times \hat{i}) + a_x b_y(\hat{i} \times \hat{j}) + a_x b_z(\hat{i} \times \hat{k}) + \cdots$$

(b)에 의해 같은 벡터끼리의 외적 $= \vec{0}$, (a)의 결과와 반교환성을 적용:

$$\boxed{\vec{a} \times \vec{b} = (a_y b_z - a_z b_y)\,\hat{i} + (a_z b_x - a_x b_z)\,\hat{j} + (a_x b_y - a_y b_x)\,\hat{k}}$$

---

## 문제 6 풀이

$\vec{A} = 4.0\,\hat{i} - 2.0\,\hat{j}$, $\vec{B} = -3.0\,\hat{i} + 6.0\,\hat{j}$

**(a)**

$$\vec{C} = \vec{A} + \vec{B} = (4.0 - 3.0)\hat{i} + (-2.0 + 6.0)\hat{j} = \boxed{1.0\,\hat{i} + 4.0\,\hat{j}}$$

**(b)**

$$\vec{A} \cdot \vec{C} = (4.0)(1.0) + (-2.0)(4.0) = 4.0 - 8.0 = \boxed{-4.0}$$

**(c)** 2차원 외적 ($z$성분만):

$$\vec{A} \times \vec{C} = (A_x C_y - A_y C_x)\,\hat{k} = [(4.0)(4.0) - (-2.0)(1.0)]\,\hat{k} = (16.0 + 2.0)\,\hat{k} = \boxed{18.0\,\hat{k}}$$

---

## 문제 7 풀이

**(a)**

문제 5에서 $\hat{j} \times \hat{k} = \hat{i}$. 반교환성에 의해:

$$\hat{k} \times \hat{j} = -(\hat{j} \times \hat{k}) = \boxed{-\hat{i}}$$

**(b)**

$$\hat{j} \times \hat{k} = \hat{i}\;(+x), \quad \hat{k} \times \hat{j} = -\hat{i}\;(-x)$$

외적은 교환법칙이 성립하지 않고, 반교환법칙이 성립한다:

$$\boxed{\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})}$$

**(c)** $\vec{v} = 3.0\,\hat{j} + 4.0\,\hat{k}$, $\vec{w} = 1.0\,\hat{j} + 2.0\,\hat{k}$ (즉 $v_x = w_x = 0$)

$$\vec{v} \times \vec{w} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0 & 3.0 & 4.0 \\ 0 & 1.0 & 2.0 \end{vmatrix}$$

$$= \hat{i}[(3.0)(2.0) - (4.0)(1.0)] - \hat{j}[(0)(2.0) - (4.0)(0)] + \hat{k}[(0)(1.0) - (3.0)(0)]$$

$$= \hat{i}(6.0 - 4.0) = \boxed{2.0\,\hat{i}}$$
