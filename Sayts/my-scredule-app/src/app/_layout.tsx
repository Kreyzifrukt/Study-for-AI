import { Stack } from "expo-router";
import { Provider } from "react-redux";
import { SQLiteProvider } from "expo-sqlite";
import {
  MD3LightTheme,
  PaperProvider
} from 'react-native-paper';

import { store } from "@/redux/store";
import { initDatabase } from "@/db/database";

const theme = {
  ...MD3LightTheme,
  colors: {
    ...MD3LightTheme.colors,
    primary: '#4051b5',
    secondary: '#5c6bc0'
  }
};

export default function RootLayout() {
  return (
    <Provider store={store}>
      <SQLiteProvider
        databaseName="schedule.db"
        onInit={initDatabase}
      >
        <PaperProvider theme={theme}>
          <Stack>
            {/* -> ... */}
          </Stack>
        </PaperProvider>
      </SQLiteProvider>
    </Provider>
  );
}