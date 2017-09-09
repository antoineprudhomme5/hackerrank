import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class Solution {

    static int partition(int[] arr, int low, int max) {

        int pivot = arr[low];
        ArrayList<Integer> left = new ArrayList<Integer>();
        ArrayList<Integer> right = new ArrayList<Integer>();

       for (int i = low + 1; i <= max; i++) {
           if (arr[i] > pivot) {
               right.add(arr[i]);
           } else {
               left.add(arr[i]);
           }
       }

       int pivotIndex = left.size() + low;
       copy(left, arr, low);
       arr[pivotIndex] = pivot;
       copy(right, arr, pivotIndex + 1);

       return pivotIndex;
   }

   static void copy(ArrayList<Integer> list, int arr[], int index) {
       for (int num : list) {
              arr[index++] = num;
       }
   }

    // this partition method works, but it's not the right "temp output" for the challenge ...
    /*
    static int partition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = high + 1;

        for (int j = high; j >= low; j--) {
            if (arr[j] >= pivot) {
                i--;
                int temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }

        return i;
    }
    */

    static void sort(int[] arr, int low, int high) {
        if (low < high) {

            int pivotIndex = partition(arr, low, high);

            sort(arr, low, pivotIndex-1);
            sort(arr, pivotIndex+1, high);

            printArray(arr, low, high);
        }
    }

    static void printArray(int[] arr, int low, int high) {
        for (int i = low; i <= high; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("");
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();


        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        sort(arr, 0, n-1);
    }
}
