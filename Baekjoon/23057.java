import java.util.Scanner;
import java.util.ArrayList;

class Combination{
	private int n;
	private int r;
	private int[] now;
	private ArrayList<ArrayList<Integer>> result;
	
	public ArrayList<ArrayList<Integer>> getResult(){
		return result;
	}
	
	public Combination(int n, int r) {
		this.n = n;
		this.r = r;
		this.now = new int[r];
		this.result = new ArrayList<ArrayList<Integer>>();
	}
	
	public void combination(int[] arr, int depth, int index, int target) {
		if(depth == r) {
			ArrayList<Integer> temp = new ArrayList<>();
			for(int i=0; i<now.length; i++) {
				temp.add(arr[now[i]]);
			}
			result.add(temp);
			return ;
		}
		if(target == n) return ;
		now[index] = target;
		combination(arr, depth+1, index+1, target+1);
		combination(arr, depth, index, target+1);
	}
}

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] num = new int[N];
		int sum = 0;
		for(int i=0; i<N; i++) {
			num[i] = sc.nextInt();
			sum += num[i];
		}
		int[] pos = new int[sum+1];
		
		
		for(int i=1; i<=num.length; i++) {
			Combination comb = new Combination(num.length, i);
			comb.combination(num, 0, 0, 0);
			
			ArrayList<ArrayList<Integer>> result = comb.getResult();
			
			for(int j=0; j<result.size(); j++) {
				int amount = 0;
				for(int k=0; k<result.get(j).size(); k++) {
					amount += result.get(j).get(k);
				}
				pos[amount] -= 1;
			}
		}
		
		int count = -1;
		for(int i=0; i<pos.length; i++) {
			if(pos[i] == 0) count++;
		}
		System.out.println(count);
	}
}