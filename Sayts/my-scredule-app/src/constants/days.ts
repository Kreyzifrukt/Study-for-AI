export const DAYS = [
  { id: 1, name: 'Понеділок', shortName: 'Пн' },
  { id: 2, name: 'Вівторок', shortName: 'Вт' },
  { id: 3, name: 'Середа', shortName: 'Ср' },
  { id: 4, name: 'Четвер', shortName: 'Чт' },
  { id: 5, name: 'П`ятниця', shortName: 'Пт' },
  { id: 6, name: 'Субота', shortName: 'Сб' },
  { id: 7, name: 'Неділя', shortName: 'Нд' },
];

export function getDayName(id: number): string {
    return DAYS.find((item) => item.id === id)?.name ?? '';
}