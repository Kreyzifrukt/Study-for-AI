package app;

import javax.swing.*;
import java.awt.*;

public class Main extends JFrame {

    private final JPanel todoPanel;

    public Main() {
        // Налаштування вікна
        setTitle("To-Do List");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Головне компонування
        setLayout(new BorderLayout(10, 10));
        ((JPanel) getContentPane()).setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Верхня панель
        var topPanel = new JPanel(new BorderLayout(10, 0));
        
        var label = new JLabel("Нова задача: [");
        var textField = new JTextField();
        var endLabel = new JLabel("]");
        
        var inputFieldPanel = new JPanel(new BorderLayout(5, 0));
        inputFieldPanel.add(label, BorderLayout.WEST);
        inputFieldPanel.add(textField, BorderLayout.CENTER);
        inputFieldPanel.add(endLabel, BorderLayout.EAST);

        var addButton = new JButton("Додати");

        topPanel.add(inputFieldPanel, BorderLayout.CENTER);
        topPanel.add(addButton, BorderLayout.EAST);
        add(topPanel, BorderLayout.NORTH);

        // Центральна панель
        todoPanel = new JPanel();
        todoPanel.setLayout(new BoxLayout(todoPanel, BoxLayout.Y_AXIS));
        todoPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Початкові задачі
        var task1 = new JCheckBox("Вивчити Swing");
        var task2 = new JCheckBox("Виконати лабораторну");
        var task3 = new JCheckBox("Завантажити проєкт");

        task2.setSelected(true);

        todoPanel.add(task1);
        todoPanel.add(task2);
        todoPanel.add(task3);

        var scrollPane = new JScrollPane(todoPanel);
        scrollPane.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1));
        add(scrollPane, BorderLayout.CENTER);

        // Нижня панель
        var bottomPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT, 10, 0));
        
        var deleteButton = new JButton("Видалити");
        var clearButton = new JButton("Очистити");

        bottomPanel.add(deleteButton);
        bottomPanel.add(clearButton);
        add(bottomPanel, BorderLayout.SOUTH);

        // Логіка кнопок
        addButton.addActionListener(e -> {
            var text = textField.getText().trim();
            if (!text.isEmpty()) {
                todoPanel.add(new JCheckBox(text));
                textField.setText("");
                refreshTodoPanel();
            }
        });

        // Додавання через Enter
        textField.addActionListener(e -> addButton.doClick());

        // Видалення вибраних
        deleteButton.addActionListener(e -> {
            var components = todoPanel.getComponents();
            for (var component : components) {
                if (component instanceof JCheckBox checkBox) {
                    if (checkBox.isSelected()) {
                        todoPanel.remove(checkBox);
                    }
                }
            }
            refreshTodoPanel();
        });

        // Повне очищення
        clearButton.addActionListener(e -> {
            todoPanel.removeAll();
            refreshTodoPanel();
        });
    }

    // Оновлення інтерфейсу
    private void refreshTodoPanel() {
        todoPanel.revalidate();
        todoPanel.repaint();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Main().setVisible(true);
        });
    }
}
