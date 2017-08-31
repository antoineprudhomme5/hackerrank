import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        // read array from STDIN
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }

        // bubble sort, with counter of swaps
        int swapCounter = 0;
        int lastSortedIndex = n - 1;
        boolean sorted = false;
        while (!sorted) {
            sorted = true;
            for (int i = 0; i < lastSortedIndex; i++) {
                if (arr[i] > arr[i+1]) {
                    sorted = false;
                    swapCounter++;
                    // swapp the 2 values
                    int temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                }
            }
        }

        System.out.println("Array is sorted in " + swapCounter + " swaps.");
        System.out.println("First Element: " + arr[0]);
        System.out.println("Last Element: " + arr[n-1]);

    }
}
