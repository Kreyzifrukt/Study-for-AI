package lib;

import java.util.Random;

public class Helper {
    
    public int[] genRandArray(int N, int a, int b) {
        int[] X = new int[N];
        Random rand = new Random();
        
        for (int i = 0; i < N; i++) {
            X[i] = rand.nextInt((b - a) + 1) + a;
        }
        
        return X;
    }
    
    public void displayArray(int[] X) {
        for (int x : X) {
            System.out.printf("  %d", x);
        }
        System.out.println();
    }

    // Виведення масиву рядків (для студентів і товарів)
    public void displayStringArray(String[] X) {
        for (String x : X) {
            System.out.println("  " + x);
        }
        System.out.println();
    }
}