import java.util.*;

public class Solution {

    static long countInversions(int[] arr, int size) {
        int[] temp = new int[size];
        return countInversions(arr, temp, 0, size - 1);
    }

    static long countInversions(int[] arr, int[] temp, int start, int end) {
        long inversions = 0;

        if (start < end) {
            int mid = (start + end) / 2;

            // sort both halves and merge halves
            inversions += countInversions(arr, temp, start, mid);
            inversions += countInversions(arr, temp, mid + 1, end);
            inversions += merge(arr, temp, start, mid, end);
        }

        return inversions;
    }

    static long merge(int[] arr, int[] temp, int start, int mid, int end) {
        long inversions = 0;

        for (int i = start; i <= end; i++) {
            temp[i] = arr[i];
        }

        int curr = start;
        int left = start;
        int right = mid + 1;

        while ((left <= mid) && (right <= end)) {
            if (temp[left] <= temp[right]) {
                arr[curr++] = temp[left++];
            } else {
                arr[curr++] = temp[right++];
                // there are (mid - i) inversions because subarrays are sorted
                inversions += mid + 1 - left;
            }
        }
        while (left <= mid) {
            arr[curr++] = temp[left++];
        }

        return inversions;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // for each test case
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            // read the values
            int n = in.nextInt();
            int[] arr = new int[n];
            for(int arr_i = 0; arr_i < n; arr_i++){
                arr[arr_i] = in.nextInt();
            }
            // print the number of inversions needed to sort it
            long result = countInversions(arr, n);
            System.out.println(result);
        }
        in.close();
    }
}
