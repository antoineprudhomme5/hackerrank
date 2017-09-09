import java.util.Scanner;

public class Solution {

    public static final int RANGE = 100;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] values = new int[RANGE];
        for (int i = 0; i < n; i++) {
            values[sc.nextInt()]++;
            sc.next();
        }

        long runningSum = 0;
        for (int i = 0; i < RANGE; i++) {
            runningSum += values[i];
            System.out.print(runningSum + " ");
        }

    }

}
