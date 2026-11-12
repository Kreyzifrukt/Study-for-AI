import {
    Category,
    CategoriesResponse,
    Meal,
    MealPreview,
    MealsResponse
} from '@/types/meal';

const BASE_URL = 'https://www.themealdb.com/api/json/v1/1';
//1. reqest
async function request<T>(url: string): Promise<T>{
    const responce = await fetch(url);
    if (!responce.ok){
        throw new Error(`HTTP error: ${responce.status}`);
    }
    return responce.json();
}

//2. categories:
export async function getCategories(): Promise<Category[]>{
    const data = await request<CategoriesResponse>(
        `${BASE_URL}/categories.php`
    );
    return data.categories;
}

//3. meals by category:
export async function getMealsByCategory(
    category: string
): Promise<MealPreview[]>{
    const data = await request<MealsResponse<MealPreview>>(
        `${BASE_URL}/filter.php?c=${encodeURIComponent(category)}`
    );
    return data.meals ?? [];
}

//4. meals by name:
export async function searchMeals(
    query: string
): Promise<Meal[]>{
    const data = await request<MealsResponse<Meal>>(
         `${BASE_URL}/search.php?s=${encodeURIComponent(query)}`
    );
    return data.meals ?? [];
}

//5. single meal:
export async function getMealsById(
    id: string
): Promise<Meal | null> {
    const data = await request<MealsResponse<Meal>>(
        `${BASE_URL}/lookup.php?i=${id}`
    )
    return data.meals?.[0] ?? null;
}

// 6. random meal:
export async function getRandomMeal(): Promise<Meal | null> {
    const data = await request<MealsResponse<Meal>>(
        `${BASE_URL}/random.php`
    );
    return data.meals?.[0] ?? null;
}


//7. ...