// Game of Pooks
import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int test = sc.nextInt();
        for (int i = 0; i < test ; i++) {
            int num = sc.nextInt();
            if (num == 2 || num == 3) {
                System.out.println(num - 1);
            } else {
                System.out.println(num);
            }
        }
	}
}
