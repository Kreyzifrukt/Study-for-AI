package app;

import java.awt.FlowLayout;
import javax.swing.*;

public class Main {

    public static void main(String[] args) {
        // 1
        var frame = new JFrame("Взаємодія компонентів");
        var label = new JLabel("Очікую натискання");
        var button = new JButton("Натисни");

        // 2
        button.addActionListener(event -> {
            label.setText("Кнопку натиснуто");
        });

        // 3
        frame.setLayout(new FlowLayout());
        frame.add(label);
        frame.add(button);

        // 4
        frame.setSize(450, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 5
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
