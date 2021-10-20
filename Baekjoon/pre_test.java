package first_project;

import java.util.Scanner;
import java.util.HashSet;
import java.util.Iterator;

public class test {
	
	public static int[] parent = new int[100];
	public static HashSet<Integer> set = new HashSet<Integer>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int i=0; i<36; i++) {
			parent[i] = i;
		}
		
		int N = sc.nextInt();
		int[][] input = new int[N][N];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				input[i][j] = sc.nextInt();
			}
		}
		
		for(int i=0; i<N-1; i++) {
			for(int j=0; j<N-1; j++) {
				if(input[i][j] == 1 && input[i][j+1] == 1) {
					union(N*i+j, N*i+j+1);
				}
				if(input[i][j] == 1 && input[i+1][j] == 1) {
					union(N*i+j, N*(i+1)+j);
				}
			}
		}
		for(int i=0; i<N-1; i++) {
			if(input[i][N-1] == 1 && input[i+1][N-1] == 1) {
				union(N*i+N-1, N*(i+1)+N-1);
			}
			if(input[N-1][i] == 1 && input[N-1][i+1] == 1) {
				union(N*(N-1)+i, N*(N-1)+(i+1));
			}
		}

		System.out.println(set.size());
		int[] result = new int[set.size()];
		Iterator<Integer> iter = set.iterator();
		int cnt = 0;
		while(iter.hasNext()) {
			int count = 0;
			int crr = iter.next();
			for(int i=0; i<N*N; i++) {
				if(parent[i] == crr) {
					count++;
				}
			}
			result[cnt++] = count;
		}
		for(int i=0; i<set.size(); i++) {
			System.out.print(result[i]+" ");
		}
	}
	
	private static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) {
            parent[y] = x;
        }
        set.add(x);
    }
	private static int find(int x) {
        if (parent[x] == x) {
            return x;
        } else {
            return parent[x] = find(parent[x]);
        }
    }
}
