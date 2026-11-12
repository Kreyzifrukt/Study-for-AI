import { configureStore } from '@reduxjs/toolkit';
import lessonsReducer from './slice'; 

export const store = configureStore({
    reducer: {
        lessons: lessonsReducer
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
