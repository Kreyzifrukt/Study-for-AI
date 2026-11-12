package app;

import lib.Helper;
import lib.Sorter;

public class Main {

    public static void main(String[] args) {
        Helper h = new Helper();
        Sorter s = new Sorter();
        
        // 1 половина за зростанням, 2 за спаданням
        System.out.println("Половинне сортування");
        int[] A = h.genRandArray(10, 10, 99);
        h.displayArray(A);
        s.sortHalfArray(A);
        h.displayArray(A);
        System.out.println();
        
        // Студенти та їх рейтинги
        System.out.println("Завдання 2: Студенти за рейтингом");
        String[] students = {"Олег (рейтинг: 60)", "Марія (рейтинг: 95)", "Андрій (рейтинг: 75)"};
        int[] studentRatings = {60, 95, 75};
        
        h.displayStringArray(students);
        s.sortByNumber(students, studentRatings);
        h.displayStringArray(students);
        
        // Товари та їх ціни
        System.out.println("Завдання 3: Товари за ціною");
        String[] products = {"Ноутбук (ціна: 25000)", "Мишка (ціна: 450)", "Килимок (ціна: 200)"};
        int[] productPrices = {25000, 450, 200};
        
        h.displayStringArray(products);
        s.sortByNumber(products, productPrices);
        h.displayStringArray(products);
    }
}