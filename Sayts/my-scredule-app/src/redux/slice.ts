import { createSlice, PayloadAction } from '@reduxjs/toolkit'; 
import { Lesson } from '@/types/Lesson'; 

interface LessonsState { 
  items: Lesson[]; 
  loading: boolean; 
} 

const initialState: LessonsState = { 
  items: [], 
  loading: false 
}; 

export const lessonsSlice = createSlice({ 
  name: 'lessons', 
  initialState, 
  reducers: { 
    setLessons(state, action: PayloadAction<Lesson[]>) { 
      state.items = action.payload; 
    },
    addLessonToStore(state, action: PayloadAction<Lesson>) {
      state.items.push(action.payload);
      state.items.sort((a, b) => {
        if (a.dayOfWeek !== b.dayOfWeek) {
          return a.dayOfWeek - b.dayOfWeek;
        }
        return 0;
      });
    },
    removeLessonFromStore(state, action: PayloadAction<number | string>) {
      state.items = state.items.filter(item => item.id !== action.payload);
    },
    setLoading(state, action: PayloadAction<boolean>) {
      state.loading = action.payload;
    }
  } 
});

export const { setLessons, addLessonToStore, removeLessonFromStore, setLoading } = lessonsSlice.actions;
export default lessonsSlice.reducer;
