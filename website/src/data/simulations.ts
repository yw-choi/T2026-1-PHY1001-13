export interface Simulation {
  id: string;
  file: string;
  title: string;
  chapter: number;
  description: string;
}

export const simulations: Simulation[] = [
  {
    id: 'kinematics-graphs',
    file: 'kinematics-graphs.html',
    title: '등가속도 직선 운동',
    chapter: 2,
    description: '초기 위치($x_0$), 초기 속도($v_0$), 가속도($a$)를 조절하며 $x(t)$, $v(t)$, $a(t)$ 그래프를 실시간으로 관찰합니다. 등가속도 공식 $x = x_0 + v_0 t + \\tfrac{1}{2}at^2$를 시각적으로 확인합니다.',
  },
  {
    id: 'free-fall',
    file: 'free-fall.html',
    title: '자유 낙하',
    chapter: 2,
    description: '초기 높이($y_0$)와 초기 속도($v_0$)를 조절하며 자유 낙하 운동을 관찰합니다. 최고점에서 $v=0$, 지면 충돌 속도, $y(t)$와 $v(t)$ 그래프를 확인합니다.',
  },
  {
    id: 'scale-explorer',
    file: 'scale-explorer.html',
    title: '스케일 탐험기',
    chapter: 1,
    description: '길이($10^{-18}$~$10^{27}$ m), 시간($10^{-24}$~$10^{17}$ s), 질량($10^{-30}$~$10^{53}$ kg)의 다양한 스케일을 탐험하며 SI 접두어와 대표 물체를 확인합니다.',
  },
  {
    id: 'newton2nd',
    file: 'newton2nd.html',
    title: '뉴턴의 제2법칙',
    chapter: 5,
    description: '알짜힘 $F$와 질량 $m$을 조절하여 $\\vec{F}_{\\text{net}} = m\\vec{a}$를 확인합니다. 힘의 방향(양/음)에 따른 가속도 변화를 실시간으로 관찰합니다.',
  },
  {
    id: 'atwood-machine',
    file: 'atwood-machine.html',
    title: '앳우드 기계',
    chapter: 5,
    description: '두 질량 $m_1$, $m_2$를 조절하여 앳우드 기계의 가속도 $a = (m_1 - m_2)g/(m_1 + m_2)$와 장력 $T = 2m_1 m_2 g/(m_1 + m_2)$를 실시간으로 확인합니다.',
  },
  {
    id: 'incline-friction',
    file: 'incline-friction.html',
    title: '빗면 위의 마찰력',
    chapter: 6,
    description: '빗면 각도와 마찰 계수를 조절하며 정지 마찰과 운동 마찰의 차이를 확인합니다. 임계각($\\theta_c = \\tan^{-1}\\mu_s$) 이상에서 물체가 미끄러지기 시작하며, 가속도 $a = g(\\sin\\theta - \\mu_k\\cos\\theta)$를 실시간으로 검증합니다.',
  },
  {
    id: 'centripetal-force',
    file: 'centripetal-force.html',
    title: '등속 원운동과 구심력',
    chapter: 6,
    description: '등속 원운동에서 속도 벡터(접선)와 구심 가속도(중심 방향)를 시각화합니다. 구심력 $F = mv^2/R$과 주기 $T = 2\\pi R/v$를 실시간으로 확인할 수 있습니다.',
  },
  {
    id: 'work-energy',
    file: 'work-energy.html',
    title: '일과 운동에너지',
    chapter: 7,
    description: '일정한 힘에 의한 일($W = Fd\\cos\\varphi$)과 운동에너지 변화($\\Delta K$)를 실시간으로 비교하여 일-운동에너지 정리($\\Delta K = W$)를 검증합니다.',
  },
  {
    id: 'spring-work',
    file: 'spring-work.html',
    title: '용수철 힘이 하는 일',
    chapter: 7,
    description: '훅 법칙($F = -kx$)과 용수철이 한 일($W_s = \\tfrac{1}{2}kx_i^2 - \\tfrac{1}{2}kx_f^2$)을 시각화. $F(x)$ 그래프의 면적으로 일을 확인하고, 일-에너지 정리를 수치적으로 검증합니다.',
  },
  {
    id: 'vector-addition',
    file: 'vector-addition.html',
    title: '벡터 덧셈과 성분 분해',
    chapter: 3,
    description: '두 벡터 $\\vec{a}$, $\\vec{b}$의 덧셈을 머리-꼬리(head-to-tail) 방법과 성분 분해($s_x = a_x + b_x$, $s_y = a_y + b_y$)로 시각화합니다.',
  },
  {
    id: 'dot-cross-product',
    file: 'dot-cross-product.html',
    title: '내적과 외적 시각화',
    chapter: 3,
    description: '내적($\\vec{a}\\cdot\\vec{b} = ab\\cos\\phi$)의 정사영 의미와 외적($|\\vec{a}\\times\\vec{b}| = ab\\sin\\phi$)의 평행사변형 넓이를 시각적으로 이해합니다.',
  },
  {
    id: 'projectile-motion',
    file: 'projectile-motion.html',
    title: '포물체 운동',
    chapter: 4,
    description: '수평·수직 운동의 독립성과 포물선 궤적을 시각화합니다. 속도 벡터 분해($v_x$ 일정, $v_y$ 변화)와 수평 도달 거리 $R = v_0^2\\sin 2\\theta_0/g$를 확인합니다.',
  },
  {
    id: 'circular-motion',
    file: 'circular-motion.html',
    title: '등속 원운동',
    chapter: 4,
    description: '등속 원운동에서 구심 가속도 $a = v^2/r$이 항상 중심을 향하고 속도 벡터에 수직($\\vec{v} \\perp \\vec{a}$)임을 시각적으로 확인합니다.',
  },
  {
    id: 'relative-motion-2d',
    file: 'relative-motion-2d.html',
    title: '2차원 상대 운동',
    chapter: 4,
    description: '강을 건너는 보트 시나리오로 상대 속도($\\vec{v}_{PG} = \\vec{v}_{PR} + \\vec{v}_{RG}$)를 이해합니다. 강물 기준과 지면 기준의 궤적을 비교합니다.',
  },
  {
    id: 'rotation-kinematics',
    file: 'rotation-kinematics.html',
    title: '회전 운동학',
    chapter: 10,
    description: '등각가속도 회전 운동을 시각화합니다. 회전하는 원판 위의 점 P에서 $v = \\omega r$, $a_r = \\omega^2 r$ 등 선형-각 관계를 실시간으로 확인하고, $\\theta(t)$와 $\\omega(t)$ 그래프를 관찰합니다.',
  },
  {
    id: 'moment-of-inertia',
    file: 'moment-of-inertia.html',
    title: '관성모멘트와 토크',
    chapter: 10,
    description: '다양한 형태(고리, 원판, 구, 막대)의 관성모멘트 $I$를 비교하고, 토크 $\\tau$에 의한 각가속도 $\\alpha = \\tau/I$를 확인합니다. 회전 운동에너지 $K = \\tfrac{1}{2}I\\omega^2$와 토크가 한 일 $W = \\tau\\theta$의 일치를 검증합니다.',
  },
  {
    id: 'collision-1d',
    file: 'collision-1d.html',
    title: '1차원 충돌',
    chapter: 9,
    description: '탄성·비탄성·완전 비탄성 충돌을 시뮬레이션합니다. 운동량 보존($\\vec{p}_i = \\vec{p}_f$)과 운동에너지 변화($\\Delta K$)를 바 차트로 실시간 확인합니다.',
  },
  {
    id: 'collision-2d',
    file: 'collision-2d.html',
    title: '2차원 탄성 충돌',
    chapter: 9,
    description: '충돌 변수(impact parameter)를 조절하여 2차원 탄성 충돌의 산란 각도를 관찰합니다. 같은 질량일 때 $\\theta_1 + \\theta_2 = 90°$를 확인합니다.',
  },
  {
    id: 'energy-conservation',
    file: 'energy-conservation.html',
    title: '역학적 에너지 보존',
    chapter: 8,
    description: '빗면을 내려오는 물체의 운동에너지($K$)와 퍼텐셜에너지($U$)의 실시간 변환을 관찰합니다. 마찰을 켜면 $\\Delta E_{\\text{mec}} = -f_k d$를 확인할 수 있습니다.',
  },
  {
    id: 'potential-energy-curve',
    file: 'potential-energy-curve.html',
    title: '퍼텐셜에너지 곡선 탐색기',
    chapter: 8,
    description: '$U(x)$ 곡선 위에서 $E_{\\text{mec}}$ 수준을 조절하여 반환점, 안정/불안정 평형점을 탐색합니다. $F(x) = -dU/dx$ 관계를 시각적으로 확인합니다.',
  },
  {
    id: 'rolling-race',
    file: 'rolling-race.html',
    title: '구름 운동 경주',
    chapter: 11,
    description: '링($I = MR^2$), 원판($I = \\tfrac{1}{2}MR^2$), 구($I = \\tfrac{2}{5}MR^2$)가 빗면을 굴러 내려오는 경주. 관성 모멘트에 따른 가속도 차이($a_{com} = g\\sin\\theta/(1+c)$)와 에너지 분배를 실시간으로 비교합니다.',
  },
  {
    id: 'angular-momentum',
    file: 'angular-momentum.html',
    title: '각운동량 보존',
    chapter: 11,
    description: '회전 원판 위에서 추의 거리를 조절하여 각운동량 보존($I_i\\omega_i = I_f\\omega_f$)을 검증합니다. 관성 모멘트가 줄면 각속도가 증가하는 피겨 스케이팅 원리를 체험합니다.',
  },
  {
    id: 'ladder-equilibrium',
    file: 'ladder-equilibrium.html',
    title: '사다리 평형',
    chapter: 12,
    description: '마찰 없는 벽에 기댄 사다리의 정적 평형을 시각화합니다. 각도, 질량, 마찰계수를 조절하며 $\\sum\\vec{F}=0$, $\\sum\\vec{\\tau}=0$ 조건과 미끄러짐 한계를 확인합니다.',
  },
  {
    id: 'stress-strain',
    file: 'stress-strain.html',
    title: '응력-변형률 곡선',
    chapter: 12,
    description: '다양한 재료(강철, 알루미늄, 구리, 고무 등)의 응력-변형률 곡선을 탐색하고, 가상 인장 시험으로 탄성 영역, 소성 변형, 파단 과정을 관찰합니다. $\\sigma = E\\varepsilon$.',
  },
];

export const simulationGroups = [
  { label: '역학 I (1~6장)', filter: (s: Simulation) => s.chapter <= 6 },
  { label: '역학 II (7~11장)', filter: (s: Simulation) => s.chapter >= 7 && s.chapter <= 11 },
  { label: '역학 III (12~14장)', filter: (s: Simulation) => s.chapter >= 12 && s.chapter <= 14 },
  { label: '파동 & 열 (15~20장)', filter: (s: Simulation) => s.chapter >= 15 },
];

export interface LegacySimulation {
  id: string;
  file: string;
  title: string;
  category: string;
}

export const legacySimulations: LegacySimulation[] = [
  // 역학 I
  { id: '01-freefall', file: '01_freefall.html', title: '자유낙하', category: '역학 I' },
  { id: '02-projectile', file: '02_projectile.html', title: '포물체 운동', category: '역학 I' },
  { id: '03-circular-motion', file: '03_circular_motion.html', title: '원운동', category: '역학 I' },
  { id: '04-newton-second-law', file: '04_newton_second_law.html', title: '뉴턴의 제2법칙', category: '역학 I' },
  { id: '05-atwood', file: '05_atwood.html', title: '앳우드 기계', category: '역학 I' },
  { id: '06-inclined-plane', file: '06_inclined_plane.html', title: '빗면 운동', category: '역학 I' },
  { id: '07-vectors', file: '07_vectors.html', title: '벡터', category: '역학 I' },
  // 역학 II
  { id: '09-work-energy', file: '09_work_energy.html', title: '일과 에너지', category: '역학 II' },
  { id: '10-energy-conservation', file: '10_energy_conservation.html', title: '에너지 보존', category: '역학 II' },
  { id: '11-collision', file: '11_collision.html', title: '충돌', category: '역학 II' },
  { id: '12-rotation', file: '12_rotation.html', title: '회전 운동', category: '역학 II' },
  { id: '13-rolling', file: '13_rolling.html', title: '굴림 운동', category: '역학 II' },
  // 역학 III
  { id: '14-gravity-orbit', file: '14_gravity_orbit.html', title: '중력과 궤도', category: '역학 III' },
  { id: '15-fluids', file: '15_fluids.html', title: '유체', category: '역학 III' },
  // 진동 & 파동
  { id: '16-oscillation', file: '16_oscillation.html', title: '진동', category: '진동 & 파동' },
  { id: '17-wave', file: '17_wave.html', title: '파동', category: '진동 & 파동' },
  { id: '18-standing-wave', file: '18_standing_wave.html', title: '정상파', category: '진동 & 파동' },
  // 열역학
  { id: '19-heat', file: '19_heat.html', title: '열', category: '열역학' },
  { id: '20-ideal-gas', file: '20_ideal_gas.html', title: '이상기체', category: '열역학' },
  { id: '21-carnot', file: '21_carnot.html', title: '카르노 기관', category: '열역학' },
  // 전자기학
  { id: '22-coulomb', file: '22_coulomb.html', title: '쿨롱 법칙', category: '전자기학' },
  { id: '23-electric-field', file: '23_electric_field.html', title: '전기장', category: '전자기학' },
  { id: '24-gauss-law', file: '24_gauss_law.html', title: '가우스 법칙', category: '전자기학' },
  { id: '25-electric-potential', file: '25_electric_potential.html', title: '전기 퍼텐셜', category: '전자기학' },
  { id: '26-capacitor', file: '26_capacitor.html', title: '축전기', category: '전자기학' },
  { id: '27-ohm-law', file: '27_ohm_law.html', title: '옴의 법칙', category: '전자기학' },
  { id: '28-rc-circuit', file: '28_rc_circuit.html', title: 'RC 회로', category: '전자기학' },
  { id: '29-charged-particle-magnetic', file: '29_charged_particle_magnetic.html', title: '자기장 속 하전입자', category: '전자기학' },
  { id: '30-magnetic-field-wires', file: '30_magnetic_field_wires.html', title: '전류의 자기장', category: '전자기학' },
  { id: '31-faraday', file: '31_faraday.html', title: '패러데이 법칙', category: '전자기학' },
  { id: '32-rlc-circuit', file: '32_rlc_circuit.html', title: 'RLC 회로', category: '전자기학' },
  { id: '33-solenoid', file: '33_solenoid.html', title: '솔레노이드', category: '전자기학' },
  { id: '34-em-wave', file: '34_em_wave.html', title: '전자기파', category: '전자기학' },
  // 광학
  { id: '35-mirror-lens', file: '35_mirror_lens.html', title: '거울과 렌즈', category: '광학' },
  { id: '36-double-slit', file: '36_double_slit.html', title: '이중슬릿', category: '광학' },
  { id: '37-single-slit', file: '37_single_slit.html', title: '단일슬릿', category: '광학' },
  // 현대물리
  { id: '38-time-dilation', file: '38_time_dilation.html', title: '시간 지연', category: '현대물리' },
  { id: '39-photoelectric', file: '39_photoelectric.html', title: '광전효과', category: '현대물리' },
  { id: '40-infinite-well', file: '40_infinite_well.html', title: '무한 퍼텐셜 우물', category: '현대물리' },
  { id: '41-hydrogen-atom', file: '41_hydrogen_atom.html', title: '수소 원자', category: '현대물리' },
];
