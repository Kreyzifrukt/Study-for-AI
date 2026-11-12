package app;

import javax.swing.*;
import java.awt.*;

public class Main extends JFrame {

    public Main() {
        // 1. Базові налаштування вікна
        setTitle("To-Do List");
        setSize(500, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // 2. Встановлення основного менеджера компонування
        setLayout(new BorderLayout(10, 10));
        
        // Додаємо відступи навколо всього контенту всередині вікна
        ((JPanel) getContentPane()).setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // 3. Верхня панель: Створення нової задачі
        var topPanel = new JPanel(new BorderLayout(10, 0));
        
        var label = new JLabel("Нова задача: [");
        var textField = new JTextField();
        var endLabel = new JLabel("]");
        
        // Допоміжна панель для текстового поля з квадратними дужками, як на макеті
        var inputFieldPanel = new JPanel(new BorderLayout(5, 0));
        inputFieldPanel.add(label, BorderLayout.WEST);
        inputFieldPanel.add(textField, BorderLayout.CENTER);
        inputFieldPanel.add(endLabel, BorderLayout.EAST);

        var addButton = new JButton("Додати");

        topPanel.add(inputFieldPanel, BorderLayout.CENTER);
        topPanel.add(addButton, BorderLayout.EAST);
        add(topPanel, BorderLayout.NORTH);

        // 4. Центральна панель: Список задач (із чекбоксами)
        var todoPanel = new JPanel();
        todoPanel.setLayout(new BoxLayout(todoPanel, BoxLayout.Y_AXIS));
        todoPanel.setBorder(BorderFactory.createEmptyBorder(10, 0, 10, 0));

        // 5. Створення та додавання елементів списку задач
        var task1 = new JCheckBox("Вивчити Swing");
        var task2 = new JCheckBox("Виконати лабораторну");
        var task3 = new JCheckBox("Завантажити проєкт");

        // Встановлюємо галочку для другої задачі, як на скриншоті
        task2.setSelected(true);

        todoPanel.add(task1);
        todoPanel.add(task2);
        todoPanel.add(task3);

        // Огортаємо в скрол-панель на випадок, якщо задач стане багато
        var scrollPane = new JScrollPane(todoPanel);
        scrollPane.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1));
        add(scrollPane, BorderLayout.CENTER);

        // 6. Нижня панель: Керування (Кнопки "Видалити" та "Очистити")
        var bottomPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT, 10, 0));
        
        var deleteButton = new JButton("Видалити");
        var clearButton = new JButton("Очистити");

        bottomPanel.add(deleteButton);
        bottomPanel.add(clearButton);
        add(bottomPanel, BorderLayout.SOUTH);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Main().setVisible(true);
        });
    }
}
