package app;

import javax.swing.*;
import java.awt.*;

public class Main extends JFrame {

    public Main() {
        // 1
        setTitle("Messanger Interface");
        setSize(700, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // 2
        setLayout(new BorderLayout(10, 10));

        // 3
        var contactsPanel = new JPanel();
        contactsPanel.setLayout(new BoxLayout(contactsPanel, BoxLayout.Y_AXIS));

        // 4
        contactsPanel.setBorder(
                BorderFactory.createTitledBorder("Контакти")
        );

        // 5
        contactsPanel.add(new JButton("C++"));
        contactsPanel.add(new JButton("Java"));
        contactsPanel.add(new JButton("C#"));
        contactsPanel.add(new JButton("Assembler"));

        // 6
        contactsPanel.setPreferredSize(
                new Dimension(150, 100)
        );
        add(contactsPanel, BorderLayout.WEST);

        // 7
        var messagesArea = new JTextArea();
        messagesArea.setEditable(false);
        var scrollPane = new JScrollPane(messagesArea);
        add(scrollPane, BorderLayout.CENTER);

        // 8
        var inputPanel = new JPanel(new BorderLayout(5, 5));
        var messageField = new JTextField();
        var sendButton = new JButton("Надіслати");

        // 9
        inputPanel.add(messageField, BorderLayout.CENTER);
        inputPanel.add(sendButton, BorderLayout.EAST);
        add(inputPanel, BorderLayout.SOUTH);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Main().setVisible(true);
        });
    }
}
