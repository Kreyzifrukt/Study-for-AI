package lib;

import javax.swing.*;

public class Helper {

    public void config(JFrame frame, int width, int height, String title) {
    	frame.setTitle(title);
        frame.setSize(width, height);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
