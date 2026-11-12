package app;

import lib.Menu;

public class main {
	
	public static void Main() {
		// ->
		do {
			Menu.display();
			Menu.showItems();
			switch (Menu.getChoice()) {
			case 1:
				break;
			case 2:
				break;
			case 3:
				break;
			default:
				System.out.println(" Ви обрали неіснуючий формат");
				break;
			}
		} while(Menu.allowContinue());
		// ->
		Menu.finish();
	}
}
