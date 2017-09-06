import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        String[] array = new String[n];
        for (int i = 0; i < n; i++) {
            array[i] = in.next();
        }

        Arrays.sort(array, new Comparator<String>() {
            public int compare(String x, String y) {
                if (x.length() == y.length()) {
                    return x.compareTo(y);
                }

                return x.length() - y.length();
            }
        });

        for (int i = 0; i < n; i++) {
            System.out.println(array[i]);
        }
    }
}
