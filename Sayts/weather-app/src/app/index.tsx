import CurrectWeather from "@/components/CurrectWeather";
import SearchBar from "../components/searchBar";
import { useEffect, useState } from "react";
import { StyleSheet, View } from "react-native";
import { getWeather } from "@/services/weather";
import { WeatherResponse } from "@/types/models";

import EveningWeather from '../components/EveningWeather';

export default function Index() {
  // Data:
  const [value, setValue] = useState<string>('Kyiv');
  const [weather, setWeather] = useState<WeatherResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  // F1:
  function onChangeText(value: string) {
    // ...
  }

  // F2:
  function onSearch() {
    // ...
  }

  //F3:
  async function loadWeather(cityName: string = value) {
    if (!cityName.trim()){
        setError('Ви не ввели назву міста');
        return;
    }
    try {
          setLoading(true);
          setError(null);
          const result = await getWeather(cityName.trim());
          setWeather(result);
          console.log(result);
    } catch (err: any){
      setWeather(null);
      setError(err.message);
    } finally{
      setLoading(false);
    }
  }

  // OnStart:
  useEffect(() => {
    loadWeather('Kyiv');
  }, []);

  // GUI:
  return (
    <View style={styles.container}>
      <SearchBar 
        value={value} 
        onChangeText={onChangeText} 
        onSearch={onSearch} 
      />
      {weather && (
         <>
        <CurrectWeather weather={weather} />
        <EveningWeather city={value} />
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "flex-start",
  },
});
