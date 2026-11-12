package ap;

import java.awt.FlowLayout;
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // 1 - Initialization
        var frame = new JFrame("Діалогові вікна");
        var textField = new JTextField(20);
        var button = new JButton("Показати текст");

        // 2 - Events
        button.addActionListener(event -> {
        	// -> 2.1.
            var text = textField.getText();
            JOptionPane.showMessageDialog(frame, "Ви ввели: " + text);
            // -> 2.2.
            var answer = JOptionPane.showInputDialog(frame, "Яка сьогодні погода?");
            JOptionpane.showMessageDialog(frame,"Я тєж так думаю що погода = " + answer);
            // -> 2.3.
            var choice = JOptionPane.showConfirmDialog(frame, "Ви підтвєржуєтє свою аперацію");
            if (choice == JOptionPane.YES_OPTION) {
            	JOptionpane.showMessageDialog(frame,"Дія буде виконана");
            } else {
            	JOptionpane.showMessageDialog(frame,"Дія не буде виконана");
            }
        });

        // 3 - Layout
        frame.setLayout(new FlowLayout());
        frame.add(textField);
        frame.add(button);

        // 4 - Configure or Geometigy 
        frame.setSize(500, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 5 - Show
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
