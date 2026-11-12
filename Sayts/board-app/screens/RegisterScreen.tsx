import {useState} from 'react';
import { View, Text, TextInput, Pressable, StyleSheet } from 'react-native';
import { register } from '../services/authService';

interface Props {
  onRegistered: () => void ;
  onBack: () => void;
}

export default function RegisterScreen({ onRegistered, onBack }: Props) {
  //Data Hooks:
  const [username, setusername] = useState<string>('');
  const [password, setpassword] = useState<string>('');

  // Register Function:
  async function handleRegister() {
    // 1 Валідація данних: 
    //==============
    if (!username || !password){
      alert('Помилка введення: не заповнені поля данних!')
    return;
    }
    //1.2
    if (password.length < 6) {
      alert('Помилка введення: пароль меньше 6 літер!')
    }
    //2 Рєстрація:
    //======================
    try{
        await register(username, password);
        alert('Реєстрація успішно завершена !');
        onRegistered();
    } catch (error: any){
        alert('Помилка реєстрації: ' + error.message);
    }
  }

  //GUI
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Реєстрація</Text>

      <TextInput
        style={styles.input}
        placeholder='Username...'
        value={username}
        onChangeText={setusername}
      />

      <TextInput
        style={styles.input}
        placeholder='Password...'
        value={password}
        onChangeText={setpassword}
        //HIDE PASSWORD
        secureTextEntry
      />

      <Pressable style={styles.button} onPress={handleRegister}>
          <Text style={styles.buttonText}>Зареєструватись</Text>
      </Pressable>

      <Pressable onPress={onBack}>
          <Text style={styles.link}>Вже є аккаунт ? Увійти</Text>
      </Pressable>
    </View>
  );
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