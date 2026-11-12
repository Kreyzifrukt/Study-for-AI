package lib;

public class Demo {

	public void createExample() {
		//1
		String[] names = {
				"Оксана", "Петро", "Остап"
		};
//		Helper h = new Helper();
//		h.displayStringArray(names);
		
		//2
		double[] salaries = {
			1300.45, 2700.15, 1987.99	
		};
		Helper h = new Helper();
		h.displayStringArray(names, salaries);

	}
}
