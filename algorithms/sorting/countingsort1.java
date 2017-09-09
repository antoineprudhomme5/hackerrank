import java.util.Scanner;
import java.util.HashMap;

public class Solution {

    public static final int RANGE = 100;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

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

        for (int i = 0; i < RANGE; i++) {
            System.out.print((counter.containsKey(i) ? counter.get(i) : 0) + " ");
        }
    }

}
