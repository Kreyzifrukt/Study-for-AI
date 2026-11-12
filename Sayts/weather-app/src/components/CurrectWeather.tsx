import { 
    View, 
    Text,
    Image,
    StyleSheet 
} from 'react-native';

import { WeatherResponse } from '@/types/models';

interface CurrectWeatherProps {
    weather: WeatherResponse
}

export default function CurrectWeather(props: CurrectWeatherProps) {
    //Const:
    const {weather} = props; // розпаковка об'єкту props
    const icon = `https://${props.weather.current.condition.icon}`

    //GUI
    return (
    <View style={styles.card}>
      <View style={styles.location}>
          <Text style={styles.city}>
              {props.weather.location.name}
          </Text>
          <Text style={[styles.country, { fontSize: 18, color: 'navy'}]}>
              {weather.location.region ? `${props.weather.location.region}` : ``}
              {weather.location.country}
          </Text>
          <View style={styles.main}>
              <Image style={styles.icon} source={{uri: icon}} />
              <View>
                  <Text style={[styles.temperature, {color: 'navy'}]}>
                      {Math.round(weather.current.temp_c)}&deg;c
                  </Text>
                  <Text 
                      style={[styles.updated, 
                      {
                          color: 'gray', 
                          fontWeight: '500',
                          fontSize: 16
                      }
                    ]}
                  >
                      Updated: {weather.current.last_updated}
                  </Text>
              </View>
          </View>
      </View>
      
    </View>
  )
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    borderRadius: 20,
    padding: 24,
    marginBottom: 16,
 
    shadowColor: '#000',
    shadowOpacity: 0.08,
    shadowRadius: 10,
    elevation: 3,
  },
 
  location: {
    marginBottom: 15,
  },
 
  city: {
    fontSize: 28,
    fontWeight: '700',
  },
 
  country: {
    color: '#666',
    fontSize: 15,
    marginTop: 4,
  },
 
  main: {
    flexDirection: 'row',
    alignItems: 'center',
  },
 
  icon: {
    width: 90,
    height: 90,
    marginRight: 15,
  },
 
  temperature: {
    fontSize: 52,
    fontWeight: '700',
  },
 
  condition: {
    fontSize: 18,
    color: '#555',
  },
 
  updated: {
    marginTop: 15,
    color: '#888',
  },
});