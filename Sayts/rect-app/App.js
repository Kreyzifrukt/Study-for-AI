import React, {useState} from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';

export default function App() {
    // Input Data:
    const [sideA, setSideA] = useState('');
    const [sideB, setSideB] = useState('');
    const [sideC, setSideC] = useState('');

    //Results:
    const [error, setError] = useState('');
    const [length, setLength] = useState(null);
    const [area, setArea] = useState(null);

    // calc():
    function calc(){
        setError('');
        
        const a = parseFloat(sideA);
        const b = parseFloat(sideB);
        const c = parseFloat(sideC);

        if(isNaN(a) || isNaN(b) || isNaN(c)){
            setError('Wrong input data');
            return;
        }
        
        if (a <= 0 || b <= 0 || c <= 0){
            setError('Довжини сторін повинні бути додатні');
            return;
        }

        if (a + b <= c || a + c <= b || b + c <= a) {
            setError('Сума двох сторін повинна бути більшою за третю');
            return;
        }

        setLength(a + b + c);
        const p = (a + b + c) / 2;
        const s = Math.sqrt(p * (p - a) * (p - b) * (p - c));
        setArea(s.toFixed(2));
    }

    //reset():
    function reset(){
        setSideA('');
        setSideB('');
        setSideC('');
    }

    //GUI
  return (
    <View style={styles.container}>
        {/** Заголовки */}
        <View style={{ alignItems: 'center', marginBottom: 15 }}>
            <Text style={{ fontSize: 24, fontWeight: 'bold', color: 'purple' }}>
                Triangle calculate without commertial and SMS
            </Text>
            <Text style={{ fontSize: 16, fontWeight: 'bold', color: 'teal', fontStyle: 'italic' }}>
                calculate Площі (методом Герона) та периметру
            </Text>
        </View>
        {/** Форма введення даних */}
        <View style={{}}>
            <Text style={{ fontSize: 16, fontWeight: 'bold', color: 'navy'}}>
                Довжина 1 сторони:
            </Text>
            <TextInput
                placeholder='input First size'
                style={{ marginTop: 5, borderWidth: 1, height: 32,
                borderRadius:10, paddingHorizontal: 10,  
            }}
            value={sideA}
            onChangeText={setSideA}
            keyboardType="numeric"
            />
        </View>
            {/**-> */}
        <View style={{}}>
            <Text style={{ fontSize: 16, fontWeight: 'bold', color: 'navy',
                marginTop: 10
            }}>
                Довжина 2 сторони:
            </Text>
            <TextInput
                placeholder='input Second size'
                style={{ marginTop: 5, borderWidth: 1, height: 32,
                borderRadius:10, paddingHorizontal: 10,  
            }}
            value={sideB}
            onChangeText={setSideB}
            keyboardType="numeric"
            />
        </View>
        <View style={{}}>
            <Text style={{ fontSize: 16, fontWeight: 'bold', color: 'navy',
                marginTop: 10
            }}>
                Довжина 3 сторони:
            </Text>
            <TextInput
                placeholder='input Third size'
                style={{ marginTop: 5, borderWidth: 1, height: 32,
                borderRadius:10, paddingHorizontal: 10,  
            }}
            value={sideC}
            onChangeText={sideC}
            keyboardType="numeric"
            />
            {/**-> */}
            <TouchableOpacity 
                style={{
                    backgroundColor: 'lightgreen', borderRadius: 10,
                    alignItems: 'center', borderWidth: 2,
                    paddingVertical: 14, marginTop: 15, marginHorizontal: 20
                }}
                onPress={calc}>

                <Text>Обчислити</Text>
            </TouchableOpacity>
        </View>
                    
        {/** Панель відображення результатів */}
        {area !== null &&(
            <View>
                <Text>
                    Результати обчислень:
                </Text>
                <Text>
                    Периметр: P = {length} од.
                </Text>
                <Text>
                    Площа: S = {area} кв.од.
                </Text>
            </View>
        )}
        <View>
            
        </View>

        {/** Панель відображення помилок */}
        <View>
            {error !== '' && (
                <Text style={{ color: 'red', marginTop: 10 }}>{error}</Text>
            )}
        </View>        
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'flex-start',
    paddingTop: 15
  },
});