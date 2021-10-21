import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(i == 0 || i == N-1) {
					System.out.print("*");
				}
				else if(j == 0 || j == N-1) {
					System.out.print("*");
				}
				else {
					if(i==j) {
						System.out.print("*");
					}
					else if(i+j == N-1) {
						System.out.print("*");
					}
					else {
						System.out.print(" ");
					}
				}
			}
			System.out.println();
		}
	}
}