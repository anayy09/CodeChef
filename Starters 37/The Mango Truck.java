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
		for (int i = 0; i < test; i++) {
		    int x = ip.nextInt(), y = ip.nextInt(), z = ip.nextInt();
		    System.out.println((z - y) / x);
		}
	}
}
