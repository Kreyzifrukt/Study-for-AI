export interface WeatherLocation {
    name: string;
    region: string;
    country: string;
    lat: number;
    lon: number;
    localtime: string;
}

export interface WeatherCondition {
    text: string;
    icon: string;
    code: number;
}

export interface CurrentWeather {
    last_updated: string;
    temp_c: number;
    feelslike_c: number;
    humidity: number;
    wind_kph: number;
    wind_dir: string;
    pressure_mb: number;
    vis_km: number;
    uv: number;
    cloud: number;
    condition: WeatherCondition;
    is_day: number;
}

export interface WeatherResponse {
    location: WeatherLocation;
    current: CurrentWeather;
}
