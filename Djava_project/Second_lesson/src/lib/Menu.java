package lib;

import java.util.Scanner;
public class Menu {

	public static void display() {
		System.out.println("========================");
		System.out.println("Обчислення електричного опору");
		System.out.println("========================");
	}
	
	public static void showItems() {
		System.out.println("   1. Послідовне з'єднання");
		System.out.println("   2. Паралельне з'єднання");
		System.out.println("   3. Завершення роботи");
	}
	
	public static int getChoice() {
		Scanner scan = new Scanner(System.in);
		System.out.print("> Виберіть номер операції: ");
		int k = scan.nextInt();
		scan.nextLine();
		scan.close();
		return k;
	}
	
	public static boolean allowContinue() {
		Scanner scan = new Scanner(System.in);
		System.out.print("\n> Продовжити (y/n)? - ");
		String answer = scan.nextLine();
		scan.close();
		return (answer.equals("y"));
	}
	
	public static void finish() {
		System.out.print("\nПрограму завершено");
	}
}
