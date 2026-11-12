package app;

import javax.swing.*;
import java.awt.*;

public class Main extends JFrame {

    /**
     * Приклад форми реєстрації
     */
    private static final long serialVersionUID = 1L;

    public Main() {
        // 1
        setTitle("Реєстрація");
        setSize(450, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // 2
        setLayout(new BorderLayout(10, 10));

        // 3
        var formPanel = new JPanel(
            new GridLayout(4, 2, 10, 10)
        );

        // 4
        formPanel.add(new JLabel("Ім'я:"));
        formPanel.add(new JTextField());

        // 5
        formPanel.add(new JLabel("Email:"));
        formPanel.add(new JTextField());

        // 6
        formPanel.add(new JLabel("Пароль:"));
        formPanel.add(new JPasswordField());

        // 7
        formPanel.add(new JLabel("Місто:"));
        String[] cities = {
            "Київ", "Львів", "Одеса", "Харків"
        };
        formPanel.add(new JComboBox<String>(cities));

        // 8
        var buttonsPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        buttonsPanel.add(new JButton("Скасувати"));
        buttonsPanel.add(new JButton("Відправити"));

        // 9
        add(formPanel, BorderLayout.CENTER);
        add(buttonsPanel, BorderLayout.SOUTH);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Main().setVisible(true);
        });
    }
}
