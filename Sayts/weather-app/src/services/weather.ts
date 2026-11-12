import {
  WEATHER_API_KEY,
  WEATHER_API_URL
} from '../constants/config';

import { WeatherResponse } from '../types/models';

export async function getWeather(city: string): Promise<WeatherResponse> {
  // 1
  if (!WEATHER_API_KEY) {
    throw new Error('Ключ доступу не знайдений або недійсний');
  }
  // 2
  const serverUrl = 
    `${WEATHER_API_URL}/current.json` + 
    `?key=${WEATHER_API_KEY}` +
    `&q=${city}`;
    // 3
  const response = await fetch(serverUrl);
  const data = await response.json();
  //4
  if (!response.ok){
    throw new Error(
        data?.error?.message || 
        'Помилка WeatherAPI'
    );
  }
  //5
  return data;
}
