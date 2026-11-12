package lib;

import java.util.ArrayList;

public class Demo {
	public void Example1() {
		var numbers = new ArrayList<Integer>(10);
		final int N = 10;
		int x = 10;
		for (int i = 0; i < N; i++) {
			x = (i + 1) * 10;
			numbers.add(x);
		}
		System.out.println(numbers);
		//ArrayList<integer> numbers = new ArrayList<integer>();
		
	}
}
