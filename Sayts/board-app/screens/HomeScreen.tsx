import { View, Text, TextInput, FlatList, StyleSheet, ActivityIndicator } from 'react-native'
import {useState, useEffect} from 'react'

import { getAnnoAnnouncement } from '../services/boardService';
import { Announcement } from '../types/Announcement';
import { categories } from '../Constants/categories';
import { PostCard } from '../components/PostCard';


interface Props {
    onCreate: () => void
}

export default function HomeScreen({ onCreate }: Props) {
  // Date Hooks:
  const [items, setItems] = useState<Announcement[]>([]);
  const [category, setCategory] = useState<string>('Всі');
  const [search, setSearch] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);

  //load Function:
  async function loadDate(){
    try{
        setLoading(true);
        const data = await getAnnoAnnouncement(search, category);
        setItems(data);
    }catch(error: any){
        alert('Помилка завантаження оголошень' + error.message);
    } finally{
      setLoading(false);
    }
  }
   
  //
  useEffect(() => {
      const delay = 3000;
      const timer = setTimeout(loadDate, delay);
      return () => clearTimeout(timer);
  }, [search, category]);
  
  // GUI: 
  return (
    <View style = {styles.container}>
      <View style={styles.top}>
          <Text style={styles.title}>оголошення</Text>

        <TextInput
        style={styles.search}
        placeholder='Пошук'
        value={search}
        onChangeText={setSearch}
        />

        <FlatList
            horizontal
            data={['Всі', ...categories]}
            keyExtractor={(item) => item}
            showsHorizontalScrollIndicator={false}
            renderItem={({item}) => (
                <Text 
                style={[
                  styles.category,
                  category === item && styles.selectedCategory
                ]} 
                onPress={() => setCategory(item)}
                >
                    {item}
                </Text>
            )}
        />

      </View>

      {loading ? (
        <>
            <ActivityIndicator size='large' style={{ marginTop: 15}}/>
            <Text 
                style={{
                    textAlign:'center',
                    fontSize: 16,
                    marginTop: 15
            }}
          >
              Триває завантаження данних....
            </Text>
        </>
      ): (
        <FlatList
            data={items}
            keyExtractor={(item) => item.id}
            contentContainerStyle={styles.list}
            renderItem={({ item }) => (
                <PostCard />
            )}
            ListEmptyComponent={
                <Text style={styles.empty}>
                  Оголошень не знайдено
                </Text> 
            }
        />
      )}
    </View>
  )
}

const styles = StyleSheet.create({
container: {
      flex: 1,
      backgroundColor: "#f5f7fa",
  },
  top: {
      padding: 16,
      backgroundColor: "#fff",
  },
  title: {
      fontSize: 26,
      fontWeight: "600",
      marginBottom: 15,
      color:'navy',
      fontFamily:'Trebuchet MS',
      fontStyle: 'italic'
  },
  search: {
      borderWidth: 1,
      borderColor: "#ddd",
      borderRadius: 8,
      padding: 12,
      fontSize: 16,
      marginBottom: 12,
  },
  category: {
      paddingVertical: 8,
      paddingHorizontal: 14,
      marginRight: 8,
      borderRadius: 20,
      backgroundColor: "#eee",
  },
  selectedCategory: {
      backgroundColor: "#1976d2",
      color: "#fff",
  },
  list: {
      width: "100%",
      maxWidth: 900,
      alignSelf: "center",
      padding: 16,
  },
  empty: {
      textAlign: "center",
      marginTop: 40,
      color: "#777",
  },
});