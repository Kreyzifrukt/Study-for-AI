export interface Lesson {
  id: number;
  subject: string;
  teacher: string;
  room: string;
  dayOfWeek: number;
  startTime: string;
  endTime: string;
  note: string;
}

export type NewLesson = Omit<Lesson, 'id'>;
