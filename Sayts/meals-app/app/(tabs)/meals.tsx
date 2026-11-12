import { useState, useEffect } from 'react';
import { View, FlatList } from 'react-native';
import MealCard from '@/components/MealCard';
import { MealPreview } from '@/types/meal';
import {
    ActivityIndicator,
    Searchbar,
    Appbar,
    Text
} from 'react-native-paper';
import {
    router,
    useLocalSearchParams
} from 'expo-router';
import {
    getMealsByCategory,
    searchMeals
} from '@/services/mealApi';

export default function MealsScreen() {
    // 1
    const params = useLocalSearchParams<{
        category?: string;
    }>();

    // 2
    const [query, setQuery] = useState<string>('');
    const [meals, setMeals] = useState<MealPreview[]>([]);
    const [loading, setLoading] = useState<boolean>(false);

    // 3
    useEffect(() => {
        if (params.category) {
            loadCategory(params.category);
        }
    }, [params.category]);

    // 4
    async function loadCategory(category: string) {
        try {
            setLoading(true);
            const data = await getMealsByCategory(category);
            setMeals(data);
        } finally {
            setLoading(false);
        }
    }

    // 5
    async function handleSearch() {
        if (!query.trim()) {
            return;
        }
        try {
            setLoading(true);
            const data = await searchMeals(query);
            setMeals(data);
        } finally {
            setLoading(false);
        }
    }

    // GUI:
    return (
        <View style={{ flex: 1 }}>
            <Appbar.Header>
                <Appbar.Content 
                    title={params.category ? params.category : 'Пошук страв'} 
                />
            </Appbar.Header>
            {/* ... */}
        </View>
    );
}
