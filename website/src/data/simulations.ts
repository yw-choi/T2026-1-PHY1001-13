export interface Simulation {
  id: string;
  file: string;
  title: string;
  chapter: number;
  description: string;
}

export const simulations: Simulation[] = [
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
