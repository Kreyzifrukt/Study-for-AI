

import java.awt.FlowLayout;
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // 1 - Initialization
        var frame = new JFrame("Пенсійний калькулятор");
        var button = new JButton("Перевірити вік");

        // 2 - Events
        button.addActionListener(event -> {
            // -> 2.1.
            var name = JOptionPane.showInputDialog(frame, "Як вас звати?");
            var answer = JOptionPane.showInputDialog(frame, "Скільки вам років?");

            // -> 2.2.
            if (name == null || answer == null) {
                return;
            }

            try {
                var age = Integer.parseInt(answer);
                var pension = 60;

                // -> 2.3.
                if (age < 0) {
                    JOptionPane.showMessageDialog(frame, "Вік не може бути від'ємним!");
                } else if (age < pension) {
                    JOptionPane.showMessageDialog(frame,
                        name + ", до пенсії залишилось " + (pension - age) + " років");
                } else {
                    JOptionPane.showMessageDialog(frame,
                        name + ", ви вже досягли пенсійного віку!");
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(frame, "Введи вік числом!");
            }
        });

        // 3 - Layout
        frame.setLayout(new FlowLayout());
        frame.add(button);

        // 4 - Configure or Geometry
        frame.setSize(300, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 5 - Show
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}