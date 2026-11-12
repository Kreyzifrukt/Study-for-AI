import React, { useEffect, useState } from 'react';
import { View, Text } from 'react-native';
import { getWeather } from '../services/weather';

export default function EveningWeather({ city }: { city: string }) {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    getWeather(city).then(setData);
  }, [city]);

  if (!data) return null;

  const evening = data.forecast?.find((f: any) => f.time.includes("18:00")) || data.current;

  return (
    <View style={{ padding: 15, backgroundColor: '#f0f4f8', borderRadius: 10 }}>
      <Text style={{ fontSize: 16, fontWeight: 'bold' }}>Прогноз на вечір</Text>
      <Text style={{ fontSize: 24, fontWeight: 'bold' }}>{Math.round(evening.temp_c)}°C</Text>
      <Text style={{ fontSize: 14, color: '#555' }}>{evening.condition?.text || 'Ясно'}</Text>
    </View>
  );
}