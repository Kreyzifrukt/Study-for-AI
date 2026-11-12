package lib;

import java.util.Scanner;

public class Helper {

    // Виведення елементів масиву на екран
    public void displayIntArray(int[] array) {
        System.out.print("Елементи масиву: ");
        for (int element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    // Створення масиву, розмір якого вводиться з консолі
    public int[] createIntArray() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введіть розмір масиву: ");
        int size = scanner.nextInt();
        return new int[size];
    }

    // Заповнення масиву числами, введеними з консолі
    public void fillArrayFromConsole(int[] array) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введіть " + array.length + " елементів масиву:");
        for (int i = 0; i < array.length; i++) {
            System.out.print("Елемент " + i + ": ");
            array[i] = scanner.nextInt();
        }
    }
}