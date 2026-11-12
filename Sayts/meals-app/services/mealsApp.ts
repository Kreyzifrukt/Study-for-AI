import { CategoriesResponse, Category, Meal, MealPreview, MealsResponse } from "@/types/meal";

const BASE_URL = 'https://www.themealdb.com/api/json/v1/1'

async function request<T>(url: string): Promise<T> {
    const response = await fetch(url)
    if (!response.ok) throw new Error(`HTTP error: ${response.status}`)
    return response.json()
}

export async function getCategories(): Promise<Category[]> {
    const data = await request<CategoriesResponse>(`${BASE_URL}/categories.php`)
    return data.categories
}

export async function getMealsByCategory(category: string): Promise<MealPreview[]> {
    const data = await request<MealsResponse<MealPreview>>(`${BASE_URL}/filter.php?c=${encodeURIComponent(category)}`)
    return data.meals ?? []
}

export async function searchMeals(query: string): Promise<Meal[]> {
    const data = await request<MealsResponse<Meal>>(`${BASE_URL}/search.php?s=${encodeURIComponent(query)}`)
    return data.meals ?? []
}

export async function getMealById(id: string): Promise<Meal | null> {
    const data = await request<MealsResponse<Meal>>(`${BASE_URL}/lookup.php?i=${id}`)
    return data.meals?.[0] ?? null
}

export async function getRandomMeal(): Promise<Meal | null> {
    const data = await request<MealsResponse<Meal>>(`${BASE_URL}/random.php`)
    return data.meals?.[0] ?? null
}