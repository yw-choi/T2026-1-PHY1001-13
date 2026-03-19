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
    description: '일정한 힘에 의한 일(W = Fd cos φ)과 운동에너지 변화(ΔK)를 실시간으로 비교하여 일-운동에너지 정리(ΔK = W)를 검증합니다.',
  },
  {
    id: 'spring-work',
    file: 'spring-work.html',
    title: '용수철 힘이 하는 일',
    chapter: 7,
    description: '훅 법칙(F = -kx)과 용수철이 한 일(W = ½kxi² - ½kxf²)을 시각화. F(x) 그래프의 면적으로 일을 확인하고, 일-에너지 정리를 수치적으로 검증합니다.',
  },
];

export const simulationGroups = [
  { label: '역학 I (1~6장)', filter: (s: Simulation) => s.chapter <= 6 },
  { label: '역학 II (7~11장)', filter: (s: Simulation) => s.chapter >= 7 && s.chapter <= 11 },
  { label: '역학 III (12~14장)', filter: (s: Simulation) => s.chapter >= 12 && s.chapter <= 14 },
  { label: '파동 & 열 (15~20장)', filter: (s: Simulation) => s.chapter >= 15 },
];
