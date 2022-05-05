/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner ip = new Scanner  (System.in);
	    int test = ip.nextInt();
	    while (test-->0) {
	        int num = ip.nextInt(), m = ip.nextInt(), x = ip.nextInt();
	        if(x + 1 > m){
	              System.out.println(0);
	        }
	        else {
	             System.out.println((x * num) / (x + 1));
	        }
	    }
	}
}
