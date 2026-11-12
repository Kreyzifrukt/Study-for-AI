package lib;

public class Helper {

	public void displayStringArray(String[] names, double[] salaries) {
	    for (int i = 0; i < names.length; i++) {
	        System.out.println((i+1)+ ") " + names[i] + " - " + salaries[i]);
	    }
	}

}
