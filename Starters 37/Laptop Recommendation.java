import java.util.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner ip = new Scanner(System.in);
		int test = ip.nextInt();
		for (int t = 0 ; t < test ; t++) {
		    int n = ip.nextInt();
		    int[] arr = new int[n];
		    int[] brr = new int[10];
		    for (int i = 0 ; i < n ; i++) {
		        arr[i] = ip.nextInt();
		    }
		    for (int j = 0 ; j < n ; j++) {
		        brr[arr[j] - 1]++;
		    }
		    int max = brr[0];
		    int res = 0;
		    for (int k = 0; k < 10 ; k++) {
		        if (max < brr[k]) {
		            max = brr[k];
		            res = k;
		        }
		    }
		    Arrays.sort(brr);
		    if (brr[8] == brr[9]) {
		        System.out.println("CONFUSED");
		    }
		    else {
		        System.out.println(res + 1);
		    }
		} 
	}
}
