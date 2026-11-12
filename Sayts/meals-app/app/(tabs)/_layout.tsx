import { Tabs } from 'expo-router';

import { MaterialCommunityIcons } from '@expo/vector-icons';

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: '#e65100',
        headerShown: false
      }}>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Tab One',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name='food' size={size} color={color} />
          ),
        }}
      />

      <Tabs.Screen
        name="meals"
        options={{
          title: 'Пошук страв',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name='magnify' size={size} color={color} />
          ),
        }}
      />

      <Tabs.Screen
        name="random"
        options={{
          title: 'Випадкова',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name='dice-multiple' size={size} color={color} />
          ),
        }}
      />
    </Tabs>
  );
}
