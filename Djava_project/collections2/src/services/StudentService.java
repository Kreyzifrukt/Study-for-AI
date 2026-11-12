package services;

import models.Student;
import reposetories.StudentsRepository;
import java.util.Scanner;

public class StudentService {

    private StudentsRepository repo = new StudentsRepository();
    private Scanner scanner = new Scanner(System.in);

    public void addStudent() {
        // 1. Діалог введення ID студента:
        System.out.print("Введіть ID студента: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        // 2. Діалог введення імені студента:
        System.out.print("Введіть ім'я студента: ");
        String name = scanner.nextLine();

        // 3. Діалог введення віку студента:
        System.out.print("Введіть вік студента: ");
        int age = scanner.nextInt();

        // 4. Діалог введення рейтингу студента:
        System.out.print("Введіть рейтинг студента");
        double rating = scanner.nextDouble();
        scanner.nextLine(); // Очищення буфера

        // 5. Створення екземпляру студента:
        Student student = new Student(id, name, age, rating);

        // 6. Збереження студента у файлі:
        repo.add(student);
        repo.saveToFile("students.dat");
    }
}
