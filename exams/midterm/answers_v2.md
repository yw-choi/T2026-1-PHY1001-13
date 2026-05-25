# 중간고사 답안 v2 (워드 수식 + 채점 기준)

각 소문항의 답. 부분점수 기준이 각 핵심 단계마다 부기됨. LaTeX 수식 → pandoc → OMML.

---

## 1(a) [5점]
**제1법칙 서술 [2점]:** 물체에 작용하는 알짜힘이 0이면, 정지한 물체는 계속 정지, 운동하는 물체는 등속직선운동을 유지한다 ($\vec{F}_\text{net} = 0 \Rightarrow \vec{v} = $ 일정).
**관성 기준틀 [3점]:** 제1법칙이 성립하는 기준틀. 즉, 가속하지 않고 등속으로 움직이거나 정지한 기준틀. (가속·회전 기준틀은 $\vec{F}_\text{net}=0$ 인데도 가속하는 것처럼 보이므로 제1법칙이 그대로 성립하지 않음.)

## 1(b) [5점]
$\vec{F}_\text{net} = m\vec{a} \Rightarrow a = F_\text{net}/m$.
**[2.5점]** 질량 일정, $F \to 2F$: $a' = \dfrac{2F}{m} = 2a$ → 가속도 **2배**.
**[2.5점]** 힘 일정, $m \to 3m$: $a' = \dfrac{F}{3m} = \dfrac{a}{3}$ → 가속도 **1/3배**.

## 1(c) [5점]
**제3법칙 [1점]:** A가 B에 $\vec{F}_{AB}$를 가하면 B도 A에 $\vec{F}_{BA} = -\vec{F}_{AB}$를 가한다 (서로 다른 두 물체에 작용).
**쌍 ① 책–지구 (중력) [2점]:** 지구→책 $= m\vec{g}$ (아래) ↔ 책→지구 $= -m\vec{g}$ (위).
**쌍 ② 책–테이블 (수직항력) [2점]:** 테이블→책 $= \vec{N}$ (위) ↔ 책→테이블 $= -\vec{N}$ (아래).
(참고: 책에 작용하는 $m\vec{g}$와 $\vec{N}$은 둘 다 책에 작용하므로 작용-반작용 쌍이 아니라 힘의 평형.)

## 2(a) [5점]
$y(t) = v_0\sin\theta_0 \cdot t - \tfrac{1}{2}gt^2$, $y=0 \Rightarrow$ **[비행시간 3점]** $t_f = \dfrac{2v_0\sin\theta_0}{g}$.
**[사거리 2점]** $R = v_0\cos\theta_0 \cdot t_f = \dfrac{v_0^2 \sin(2\theta_0)}{g}$.

## 2(b) [5점]
(a)에서 바로: $t(\theta_0) = \dfrac{2v_0\sin\theta_0}{g}$. **[5점]**

## 2(c) [5점]
**[$t_\text{max}$ 2점]** $t(\theta_0) \propto \sin\theta_0$이므로 $\theta_0 = 90°$에서 $t_\text{max} = \dfrac{2v_0}{g}$.
**[방정식 2점]** $t(\theta_0) = 0.5\, t_\text{max} \Rightarrow \sin\theta_0 = \tfrac{1}{2}$.
**[해 1점]** 발사각 범위 $0° < \theta_0 \le 90°$에서 $\theta_0 = 30°$.

## 2(d) [10점]
$v^2 = v_x^2 + v_y^2$, $v_x = v_0\cos\theta_0$ (일정), $v_y(t) = v_0\sin\theta_0 - gt$.
**[최소 조건 3점]** $v_x$가 일정하므로 $v^2$은 $v_y=0$일 때 최소 → **궤적의 최고점**.
**[물리적 해석 3점]** 중력은 연직 방향으로만 작용 → $v_x$ 보존, $v_y$만 감속(상승)→0→증가(하강). 최고점에서는 수평 성분만 남음.
**[$v_\text{min}$ 4점]** $\theta_0 = 30°$: $v_\text{min} = v_0\cos 30° = \dfrac{\sqrt{3}}{2}v_0$.

## 3(a) [10점]
**[$\Delta p$ 3점]** 충격량-운동량 정리: $\Delta p = F\Delta t$.
**[$v$ 3점]** 초기 정지, $\Delta p = mv \Rightarrow v = \dfrac{F\Delta t}{m}$.
**[$W$ 4점]** 일-운동에너지 정리: $W = \Delta K = \tfrac{1}{2}mv^2 = \dfrac{F^2(\Delta t)^2}{2m}$.

## 3(b) [10점]
운동량 성분 보존 ⇔ 그 방향의 알짜힘 $=0$.
**[수평면, 수평 1점]** 알짜힘 $= F \neq 0 \Rightarrow$ 보존 ✗.
**[수평면, 연직 1점]** 중력 $+$ 수직항력 $= 0 \Rightarrow$ 보존 ✓.
**[경사면 수직항력 2점]** $N = mg\cos\theta$ (경사면에 수직한 방향으로 가속 없음).
**[경사면, 수평 2점]** 알짜힘 $= -N\sin\theta = -mg\sin\theta\cos\theta \neq 0 \Rightarrow$ 보존 ✗.
**[경사면, 연직 2점]** 알짜힘 $= N\cos\theta - mg = -mg\sin^2\theta \neq 0 \Rightarrow$ 보존 ✗.
**[이유 설명 2점]** 경사면의 수직항력이 수평·연직 두 방향 모두에 성분을 가지므로 두 성분 모두 보존되지 않는다.

## 3(c) [10점]
**[진입 직후 2점]** $K_i = \tfrac{1}{2}mv^2 = \dfrac{F^2(\Delta t)^2}{2m}$, $U_i = 0$ (수평면 기준).
**[정지 순간 2점]** 거리 $d$, 높이 $h = d\sin\theta$: $K_f = 0$, $U_f = mgd\sin\theta$.
**[에너지 보존 3점]** 마찰 없음, 수직항력은 일을 하지 않음: $\tfrac{1}{2}mv^2 = mgd\sin\theta$.
**[$d$ 계산 3점]** $d = \dfrac{v^2}{2g\sin\theta} = \dfrac{F^2(\Delta t)^2}{2m^2 g\sin\theta}$. ($U_f = \dfrac{F^2(\Delta t)^2}{2m}$).

## 4(a) [10점]
**[보존법칙 3점]** 축에 대한 외부 토크 0 (중력·축 수직항력은 축을 지남, 충돌 내력은 상쇄) → **각운동량 보존**.
**[$L_i$ 2점]** 충돌 전: $L_i = mvR$ (충격 매개변수 $R$).
**[$I_f$ 3점]** 충돌 후: $I_f = \tfrac{1}{2}MR^2 + mR^2 = \dfrac{(M+2m)R^2}{2}$.
**[$\omega$ 2점]** $mvR = I_f\omega \Rightarrow \omega = \dfrac{2mv}{(M+2m)R}$.

## 4(b) [10점]
**[$K_i$ 1점]** $K_i = \tfrac{1}{2}mv^2$.
**[$K_f$ 계산 4점]** $K_f = \tfrac{1}{2}I_f\omega^2 = \tfrac{1}{2}\cdot\dfrac{(M+2m)R^2}{2}\cdot\dfrac{4m^2v^2}{(M+2m)^2R^2} = \dfrac{m^2v^2}{M+2m}$.
**[비율·부등식 3점]** $\dfrac{K_f}{K_i} = \dfrac{2m}{M+2m} < 1$ ($M>0$이므로 $M+2m > 2m$).
**[판정 2점]** $K$ 감소 → **비탄성 충돌**. 입자가 원판에 붙으므로 **완전비탄성 충돌**.

## 4(c) [10점]
**[보존량 3점]** 미는 힘은 반지름 방향 → 축에 대한 토크 0 → **각운동량 보존** ($L = mvR$ 유지).
**[$I(r)$ 3점]** $I(r) = \tfrac{1}{2}MR^2 + mr^2$.
**[$\omega_f$ 유도 4점]** $L = I(r)\omega_f \Rightarrow \omega_f = \dfrac{mvR}{\tfrac{1}{2}MR^2 + mr^2} = \dfrac{2mvR}{MR^2 + 2mr^2}$.
