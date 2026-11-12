package lib;

import java.util.Random;

public class Helper {
	
	public int[] genRandArray(int N, int a, int b) {
		int[] X = new int[N];
		Random rand = new Random();
		int x = 0;
		
		for (int i = 0; i <N; i++) {
			x = rand.nextInt((b-a)+ 1) + a;
			X[i] = x;
		}
		
		return X;
	}
	
	public void displayArray(int[] X) {
		for (int x : X) {
			System.out.printf("  %d", x);
		}
		System.out.println();
	}
}
