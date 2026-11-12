package app;

import lib.Helper;
import lib.sorter;

public class Main {

	public static void main(String[] args) {
		//1
		Helper h = new Helper();
		int[] A = h.genRandArray(10, 10, 99);
		h.displayArray(A);
		
		//2
		sorter s = new sorter();
		s.bubbleSort(A);
		h.displayArray(A);
		
	}

}
