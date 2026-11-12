package app;

import javax.swing.*;
import java.awt.*;
import lib.Helper;

public class Main {

    public static void main(String[] args) {
        // 1
        var frame = new JFrame();
        frame.setLayout(new BorderLayout());
        
        //2
        frame.add(new JButton("Bropi"), BorderLayout.NORTH);
        frame.add(new JButton("Внизу"), BorderLayout.SOUTH);
        frame.add(new JButton("Ліворуч"), BorderLayout.WEST);
        frame.add(new JButton("Праворуч"), BorderLayout.EAST);
        frame.add(new JButton("Центр"), BorderLayout.CENTER);
        
        //3
        var helper = new Helper();
        helper.config(frame, 600, 500, "Приклад BorderLayout");
    }
}
