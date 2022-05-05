/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner ip = new Scanner(System.in);
		int test = ip.nextInt();
		while (test-->0) {
		    int n = ip.nextInt(), x = ip.nextInt();
		    int[] arr = new int[n];
		    int m = 0, p = 0;
		    for (int i = 0;i < n ;i++) {
		        arr[i] = ip.nextInt();
		        p += Math.ceil((double)arr[i] / x);
		        m = Math.max(arr[i],m);
		    }
		    System.out.println(Math.min(m,p));
		}
	}
}
