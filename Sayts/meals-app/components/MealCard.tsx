import { MealPreview } from '@/types/meal';
import { View } from 'react-native';
import { Button, Card, Text } from 'react-native-paper';

interface MealCardProps {
    meal: MealPreview;
    onPress: () => void;
}

export default function MealCard(props: MealCardProps) {
    // 1
    const { meal, onPress } = props;

    // 2 - GUI:
    return (
        <Card mode='elevated' style={{ marginBottom: 16 }}>
            <Card.Cover source={{ uri: meal.strMealThumb }} />
            <Card.Content style={{ paddingTop: 12 }}>
                <Text variant='titleMedium'>
                    {meal.strMeal}
                </Text>
            </Card.Content>
            <Card.Actions>
                <Button icon='book-open-page-variant' onPress={onPress}>
                    Рецепт
                </Button>
            </Card.Actions>
        </Card>
    );
}
