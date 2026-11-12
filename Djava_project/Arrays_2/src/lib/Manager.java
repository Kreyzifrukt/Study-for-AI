package lib;

public class Manager {

    // Реалізація створення масиву, заповнення та виведення на екран
    public void Task1() {
        Helper helper = new Helper();
        
        int[] userArray = helper.createIntArray();
        helper.fillArrayFromConsole(userArray);
        helper.displayIntArray(userArray);
    }
}