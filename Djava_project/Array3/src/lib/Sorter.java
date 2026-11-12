package lib;

public class Sorter {

    // 1. Половина за зростанням, друга половина за спаданням
    public void sortHalfArray(int[] X) {
        int n = X.length;
        int mid = n / 2;
        int temp = 0;
        
        // Перша половина (зростання)
        for (int i = 0; i < mid - 1; i++) {
            for (int j = 0; j < mid - i - 1; j++) {
                if (X[j] > X[j + 1]) {
                    temp = X[j];
                    X[j] = X[j + 1];
                    X[j + 1] = temp;
                }
            }
        }
        
        // Друга половина (спадання)
        for (int i = mid; i < n - 1; i++) {
            for (int j = mid; j < n - (i - mid) - 1; j++) {
                if (X[j] < X[j + 1]) {
                    temp = X[j];
                    X[j] = X[j + 1];
                    X[j + 1] = temp;
                }
            }
        }
    }

    // 2 та 3. Сортування текстового масиву за числовим значенням у тексті
    public void sortByNumber(String[] X, int[] ratings) {
        int n = X.length;
        int tempRating = 0;
        String tempStr = "";
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (ratings[j] > ratings[j + 1]) {
                    // Міняємо місцями числа
                    tempRating = ratings[j];
                    ratings[j] = ratings[j + 1];
                    ratings[j + 1] = tempRating;
                    
                    // Міняємо місцями рядки
                    tempStr = X[j];
                    X[j] = X[j + 1];
                    X[j + 1] = tempStr;
                }
            }
        }
    }
}