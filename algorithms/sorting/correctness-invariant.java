import java.io.*;
import java.util.*;

public class Solution {

    public static void insertionSort(int[] arr){
        for (int i = 1; i < arr.length; i++){
            int value = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > value) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = value;
        }

        printArray(arr);
    }

    static void printArray(int[] arr) {
        for(int n: arr){
            System.out.print(n+" ");
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] ar = new int[n];
        for(int i=0;i<n;i++){
            ar[i]=in.nextInt();
        }
        insertionSort(ar);
    }
}
