import java.util.Scanner;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Solution {

    static void partition(int[] arr, int low, int high) {
        int pivot = arr[0];
        int pivotIndex = high; // where to place the pivot after
        for (int i = high; i > 0; i--) {
            if (arr[i] >= pivot) {
                // replace the value at the pivot position by the value
                // greater than the pivot
                int temp = arr[i];
                arr[i] = arr[pivotIndex];
                arr[pivotIndex] = temp;

                // decrease the pivot position (because this position is taken
                // by a value greater than the pivot)
                pivotIndex--;
            }
        }
        // put the pivot at his place
        int temp = arr[pivotIndex];
        arr[pivotIndex] = arr[low];
        arr[low] = temp;
    }

    static void printArray(int[] arr) {
        String result = Arrays.stream(arr)
                            .mapToObj(String::valueOf)
                            .collect(Collectors.joining(" "));

        System.out.println(result);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        partition(arr, 0, n-1);
        printArray(arr);
    }
}
