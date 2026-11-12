import { 
    StyleSheet,
    View,
    Text,
    TextInput,
    Pressable
 } from 'react-native';

interface SearchBarProps {
    value: string;
    onChangeText: (value: string) => void;
    onSearch: () => void;   
}

export default function searchBar(props: SearchBarProps) {
  return (
    <View style={styles.container}>
        <TextInput
            style={styles.input}
            placeholder='Введіть назву міста...'
            value={props.value}
            onChangeText={props.onChangeText}
            onSubmitEditing={props.onSearch}
        />
        <Pressable
            style={styles.button}
            onPress={props.onSearch}
        >
            <Text style={styles.buttonText}>
                ?
            </Text>
        </Pressable>
    </View>
  )
}
const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 20,
    marginTop: 30,
  },
  input: {
    flex: 1,
    height: 50,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 12,
    paddingHorizontal: 16,
    fontSize: 16,
    backgroundColor: '#fff',
  },
  button: {
    width: 50,
    height: 50,
    borderRadius: 12,
    backgroundColor: '#2563eb',
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonText: {
    fontSize: 22,
    color: 'white'
  },
});