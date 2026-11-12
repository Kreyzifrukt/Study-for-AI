import React, { use, useState } from 'react';
import { View, Text, TextInput, Pressable, StyleSheet } from 'react-native';
import { login } from '../services/authService';

interface Props {
  onLogin:() => void;
  onRegister: () => void ;
}

export default function LoginScreen({ onLogin, onRegister }: Props) {
    //Data
    const [username, setusername] = useState<string>("");
    const [password, setpassword] = useState<string>("");

    //Main Func:
    async function handleLogin() {
      if (!username || !password){
        alert('Ви не заповнили поля данних');
      }
      // -> 
      try {
          await login(username, password);
          onLogin();
      } catch (error:any) {
          alert('Помилка входу:' + error.message);
      }
    }

  //GUI:
  return (
    <View style = {styles.container}>
        <Text style={styles.logo}>Дошка огоголень</Text>
        <Text style={styles.title}>Вхід</Text>

        <TextInput
            style = {styles.input}
            placeholder='Введіть логін тут'
            value={username}
            onChangeText={setusername}
        />
        <TextInput
            style = {styles.input}
            placeholder='Введіть пароль тут'
            value={password}
            onChangeText={setpassword}
            //Hide pass
            secureTextEntry
        />

        <Pressable style={styles.button} onPress={handleLogin}>
            <Text style={styles.buttonText}>Увійти</Text>
        </Pressable>

        <Pressable onPress={onRegister}>
            <Text style={styles.link}>Немає аккаунта ? Зареєструватись</Text>
        </Pressable>
    </View>
  )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        padding: 25,
        backgroundColor: "#f5f7fa",
    },
    logo: {
        fontSize: 25,
        fontWeight: "700",
        marginBottom: 35,
    },
    title: {
        fontSize: 28,
        fontWeight: "700",
        marginBottom: 20,
        color: 'purple'
    },
    input: {
        width: "100%",
        maxWidth: 450,
        backgroundColor: "#fff",
        borderWidth: 1,
        borderColor: "#ddd",
        borderRadius: 8,
        padding: 14,
        marginBottom: 12,
        fontSize: 18,
        fontWeight: '600',
        color:'gray'
    },
    button: {
        width: "100%",
        maxWidth: 450,
        backgroundColor: "#1976d2",
        padding: 15,
        borderRadius: 8,
        alignItems: "center",
        marginTop: 8,
    },
    buttonText: {
        color: "#fff",
        fontSize: 18,
        fontWeight: "700",
    },
    link: {
        color: "#1976d2",
        marginTop: 20,
        fontSize: 26,
        fontWeight: '600'
    }
});