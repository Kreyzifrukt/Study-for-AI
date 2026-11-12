import { SQLiteDatabase } from "expo-sqlite";
import { Lesson, NewLesson } from '@/types/Lesson';

// 1
export async function getLessons(db: SQLiteDatabase): Promise<Lesson[]> {
  return await db.getAllAsync<Lesson>(`
    SELECT * FROM lessons ORDER BY dayOfWeek, startTime
  `);
}

// 2
export async function getLessonsByDay(db: SQLiteDatabase, id: number): Promise<Lesson[]> {
  return await db.getAllAsync<Lesson>(`
    SELECT * FROM lessons WHERE dayOfWeek = ? ORDER BY startTime
  `, id);
}

// 3
export async function addLesson(db: SQLiteDatabase, lesson: NewLesson): Promise<void> {
  const result = await db.runAsync(`
    INSERT INTO lessons (subject, teacher, room, dayOfWeek, startTime, endTime, note)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `, lesson.subject, lesson.teacher, lesson.room, lesson.dayOfWeek, lesson.startTime,
  lesson.endTime, lesson.note);
}

// 4
export async function deleteLesson(db: SQLiteDatabase, id: number): Promise<void> {
  await db.runAsync(`
    DELETE FROM lessons WHERE id = ?
  `, id);
}
