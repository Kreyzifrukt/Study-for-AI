package app;

import java.awt.FlowLayout;
import javax.swing.*;

public class main_show {
    public static void main(String[] args) {
    	// 1 - Initialization
    	JFrame frame = new JFrame("Пенсійний калькулятор");
    	JButton button = new JButton("Перевірити вік");

    	// 2 - Events
    	button.addActionListener(event -> {
    	    // -> 2.1.
    	    String name = JOptionPane.showInputDialog(frame, "Як вас звати?");
    	    String answer = JOptionPane.showInputDialog(frame, "Скільки вам років?");

    	    // -> 2.2.
    	    if (name == null || answer == null) {
    	        return;
    	    }

    	    try {
    	        int age = Integer.parseInt(answer);
    	        int pension = 65;

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