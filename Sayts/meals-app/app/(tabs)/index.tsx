import { useEffect, useState } from 'react';
import { FlatList, View } from 'react-native';

import { getCategories } from '@/services/mealApi';
import { Category } from '@/types/meal';
import { ActivityIndicator, Appbar, Text } from 'react-native-paper';
import { Item } from 'react-native-paper/lib/typescript/components/Drawer/Drawer';
import CategoryCard from '@/components/CategoryCard';
import { router } from 'expo-router';


export default function HomeScreen() {
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string>('')

  useEffect(() => {
    loadCategories()
  }, [])

  async function loadCategories() {
    try {
      setLoading(true)
      setError('')

      const data = await getCategories()
      setCategories(data)
      console.log(data)

    } catch (err: any) {
      setError('Помилка завантаження категорій: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center' }}>
        <ActivityIndicator size='large' />
      </View>
    )
  }

  return (
    <View>
      <Appbar.Header>
        <Appbar.Content title="Каталог страв" />
      </Appbar.Header>

      {error ? (
        <Text style={{ margin: 20, textAlign: 'center' }}>
          {error}
        </Text>
      ) : (
        <FlatList
         data={categories}
         keyExtractor={(item)=> item.idCategory}
         contentContainerStyle={{padding:16}}
         renderItem={({item}) => (
          <CategoryCard 
            category={item}
            onPress={() => 
              router.push({
                pathname: '/meals',
                params:{
                  categories: item.strCategory
                }
              })
            }
          />
         )}
         />
      )}
    </View>
  );
}
