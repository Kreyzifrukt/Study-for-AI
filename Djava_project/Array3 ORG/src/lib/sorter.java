package lib;

public class sorter {

	public void bubbleSort(int[] X) {
		int N = X.length;
		int temp = 0;
		
		for (int i = 0; i<N-1; i++) {
			for (int j =0; j < N - i - 1; j++) {
				if (X[j] > X[j + 1]) {
					temp = X[j];
					X[j] = X[j + 1];
					X[j+1] = temp;
				}
			}
		}
	}
}
