import java.util.Scanner;
import java.util.HashMap;
import java.util.Set;

public class Solution {

    public static final int RANGE = 100;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // count the occurrences in a HashMap
        HashMap<Integer, Integer> counter = new HashMap<>();
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int v = sc.nextInt();
            if (counter.containsKey(v)) {
                counter.put(v, counter.get(v) + 1);
            } else {
                counter.put(v, 1);
            }
        }

        // get the HashMap keys and sort them
        Set<Integer> keys = counter.keySet();
        int[] keysArray = new int[keys.size()];
        int i = 0;
        for (Integer k : keys) {
            keysArray[i++] = k;
        }
        sort(keysArray);

        for (int k: keysArray) {
            for (i = 0; i < counter.get(k); i++) {
                System.out.print(k + " ");
            }
        }
    }

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

    static void sort(int[] arr) {
        sort(arr, 0, arr.length - 1);
    }

    static void sort(int[] arr, int low, int high) {
        if (low < high) {

            int pivotIndex = partition(arr, low, high);

            sort(arr, low, pivotIndex-1);
            sort(arr, pivotIndex+1, high);
        }
    }

}
