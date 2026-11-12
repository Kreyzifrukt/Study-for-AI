import React, { useState, useEffect } from 'react';
import { StyleSheet, View, ActivityIndicator } from 'react-native';
import Parse from './back4app';

import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import HomeScreen from './screens/HomeScreen';

import CreateScreen from './screens/CreateScreen';
import DisplayScreen from './screens/DisplayScreen';
import ProfileScreen from './screens/ProfileScreen';

import BottomNav from './components/BottomNav';
type AuthScreen = 'login' | 'register';
type AppScreen = 'home' | 'create' | 'display' | 'profile';

export default function App() {
  // Data:
  const [user, setUser] = useState<Parse.User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // Screens:
  const [authScreen, setAuthScreen] = useState<AuthScreen>('login');
  const [appScreen, setAppScreen] = useState<AppScreen>('home');

  // OnStart:
  useEffect(() => {
    async function checkUser() {
      const currentUser = await Parse.User.currentAsync();
      setUser(currentUser);
      setLoading(false);
    }
    checkUser();
  }, []);

  // Indicator
  if (loading) {
    return (
      <View style={styles.loading}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  // Auth:
  if (!user) {
    if (authScreen === 'register'){
      return(
          <RegisterScreen
              onRegistered={() => setAuthScreen('login')}
              onBack={() => setAuthScreen('register')}
          />
      );
    }

    
    return (
      <LoginScreen
          onLogin={async() => {
              const currentUser = await Parse.User.currentAsync();
              setUser(currentUser);
          }}
          onRegister={() => setAuthScreen('register')}
      />
    );
  }

  // General Render*
  function renderScreen(){
      switch (appScreen) {
        case 'home':
          return <HomeScreen onCreate={() => setAppScreen('create')} />
        case 'create':
          return <CreateScreen onCreated={() => setAppScreen('home')} />
        case 'display':
          return <DisplayScreen/>
        case 'profile':   
          return <ProfileScreen onLogout={() => {
              setUser(null);
              setAuthScreen('login');
          }} />
        default:
          return null;  
      }
  }

  // UI
  return (
    <View style={styles.container}>
        <View style={styles.content}>
            {renderScreen()}
        </View>
        <BottomNav 
            screen={appScreen}
            setScreen={(value) => setAppScreen(value as AppScreen)}
        />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'flex-start',
    paddingTop: 15,
  },
  content:{
      flex: 1
  },
  loading: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});