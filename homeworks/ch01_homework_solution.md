# Chapter 1: Measurement — 풀이

---

## 문제 1 풀이

**(a) 지구의 부피**

구의 부피 공식: $V = \frac{4}{3}\pi R^3$

$$V = \frac{4}{3} \times \pi \times (6.37 \times 10^{6})^3 = \frac{4}{3} \times \pi \times (2.584 \times 10^{20}) = 1.082 \times 10^{21}\;\text{m}^3$$

$$\boxed{V \approx 1.08 \times 10^{21}\;\text{m}^3}$$

**(b) 지구의 평균 밀도**

$$\rho = \frac{M}{V} = \frac{5.97 \times 10^{24}\;\text{kg}}{1.082 \times 10^{21}\;\text{m}^3} = \boxed{5.52 \times 10^{3}\;\text{kg/m}^3}$$

**(c) $\text{g/cm}^3$으로 변환**

$1\;\text{kg} = 10^{3}\;\text{g}$, $1\;\text{m} = 10^{2}\;\text{cm}$ $\Rightarrow$ $1\;\text{m}^3 = 10^{6}\;\text{cm}^3$

$$\rho = 5.52 \times 10^{3}\;\frac{\text{kg}}{\text{m}^3} \times \frac{10^{3}\;\text{g}}{1\;\text{kg}} \times \frac{1\;\text{m}^3}{10^{6}\;\text{cm}^3} = \boxed{5.52\;\text{g/cm}^3}$$

---

## 문제 2 풀이

**(a) $\text{m}^2$ 단위 면적**

$$A = 12.0 \times 15.0 = 180\;\text{ft}^2$$

$1\;\text{ft} = 0.3048\;\text{m}$ $\Rightarrow$ $1\;\text{ft}^2 = (0.3048)^2 = 0.09290\;\text{m}^2$

$$A = 180 \times 0.09290 = \boxed{16.7\;\text{m}^2}$$

**(b) $\text{cm}^2$ 단위 면적**

$1\;\text{m}^2 = 10^{4}\;\text{cm}^2$

$$A = 16.7 \times 10^{4} = \boxed{1.67 \times 10^{5}\;\text{cm}^2}$$

**(c) 타일 개수**

타일 1장의 면적: $30 \times 30 = 900\;\text{cm}^2$

$$N = \frac{167{,}200}{900} = 185.8 \implies \boxed{186\text{장 (올림)}}$$

---

## 문제 3 풀이

**(a) $E$의 SI 단위**

$$[E] = [k][m][v^2] = (1)(\text{kg})\left(\frac{\text{m}}{\text{s}}\right)^2 = \text{kg} \cdot \text{m}^2 / \text{s}^2$$

$$\boxed{[E] = \text{kg} \cdot \text{m}^2 / \text{s}^2 \;(= \text{J})}$$

**(b) $E/F$의 차원**

$$[F] = [m][a] = \text{kg} \cdot \text{m}/\text{s}^2$$

$$\frac{[E]}{[F]} = \frac{\text{kg} \cdot \text{m}^2/\text{s}^2}{\text{kg} \cdot \text{m}/\text{s}^2} = \text{m}$$

$$\boxed{E/F\text{는 길이}[L]\text{의 차원을 갖는다.}}$$

**(c) $E = mv^3$ 주장 검증**

$$[mv^3] = \text{kg} \cdot \left(\frac{\text{m}}{\text{s}}\right)^3 = \text{kg} \cdot \text{m}^3/\text{s}^3$$

에너지의 차원 $\text{kg} \cdot \text{m}^2/\text{s}^2$와 다르므로, 차원분석만으로 틀렸음을 보일 수 있다.

---

## 문제 4 풀이

**(a) 1 광년을 km로**

$$1\;\text{year} = 365.25 \times 24 \times 3600 = 3.156 \times 10^{7}\;\text{s}$$

$$1\;\text{ly} = c \times t = (3.00 \times 10^{8})(3.156 \times 10^{7}) = 9.467 \times 10^{15}\;\text{m} = \boxed{9.47 \times 10^{12}\;\text{km}}$$

**(b) 프록시마 센타우리까지 거리**

$$d = 4.24 \times 9.467 \times 10^{15} = \boxed{4.01 \times 10^{16}\;\text{m}}$$

**(c) 우주선 도달 시간**

$v = 30\;\text{km/s} = 3.00 \times 10^{4}\;\text{m/s}$

$$t = \frac{d}{v} = \frac{4.01 \times 10^{16}}{3.00 \times 10^{4}} = 1.337 \times 10^{12}\;\text{s}$$

$$t = \frac{1.337 \times 10^{12}}{3.156 \times 10^{7}} = \boxed{4.24 \times 10^{4}\;\text{년}}$$

---

## 문제 5 풀이

**(a) 밀도 공식 유도**

원기둥의 부피: $V = \pi r^2 h = \pi \left(\frac{d}{2}\right)^2 h = \frac{\pi d^2 h}{4}$

$$\boxed{\rho = \frac{M}{V} = \frac{4M}{\pi d^2 h}}$$

**(b) 수치 계산**

$$\rho = \frac{4 \times 55.0}{\pi \times (2.50)^2 \times 5.00} = \frac{220.0}{\pi \times 31.25} = \frac{220.0}{98.17} = \boxed{2.24\;\text{g/cm}^3}$$

**(c) 물질 추정**

계산된 밀도 $2.24\;\text{g/cm}^3$은 알루미늄($2.70\;\text{g/cm}^3$)보다 작다. 흑연($\sim 2.2\;\text{g/cm}^3$)이나 실리콘($\sim 2.33\;\text{g/cm}^3$)의 밀도와 유사하다.
