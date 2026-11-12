import Parse from "../back4app";
import { Announcement } from "../types/Announcement";

export async function getAnnoAnnouncement(
    search = '', category = 'Всі'): Promise<Announcement[]>{
    //1
    const query = new Parse.Query('Announcement');
    query.include('author');
    query.descending('createdAt');

    //2
    if (category !== 'Всі'){
        query.equalTo('category', category);
    }

    //3
    const objects = await query.find();
    let result = objects.map((item) => {
        const author = item.get('author');
        return{
            id: item.id!,
            title: item.get('title') || '',
            description: item.get('description') || '',
            price: item.get('price') || 0,
            category: item.get('category') || '',
            city: item.get("city") || '',
            phone: item.get("phone") || '',
            imageUrl: item.get("imageUrl") || '',
            authorId: author?.id || '',
            authorName: author?.get('username') || 'Користувач',
            createdAt: item.createdAt

        }
    });

    //4
    if (search.trim()) {
        const text = search.toLowerCase();
        result = result.filter((item) => 
            item.title.toLowerCase().include(text) ||
            item.description.toLowerCase().includes(text) ||
            item.city.toLowerCase().includes(text)
        );
    }

    //5
    return result;
}

//...