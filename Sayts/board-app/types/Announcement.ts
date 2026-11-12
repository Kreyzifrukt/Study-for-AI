export interface Announcement {
    id: string;
    title: string;
    description: string;
    price: number;
    category: string;
    city: string;
    phone: string;
    imageUrl?: string; 
    authorId: string;
    authorName: string;
    createdAt?: Date;
}