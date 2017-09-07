import java.util.PriorityQueue;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int nbCookies = sc.nextInt();
        int sweetness = sc.nextInt();

        // fill the cookies heap
        PriorityQueue<Integer> cookies = new PriorityQueue<>();
        while (nbCookies-- > 0) {
            // insert cookie in the heap
            cookies.add(sc.nextInt());
        }

        int operations = 0;
        // increase cookies sweetness
        while (sweetness > cookies.peek()) {
            // not enough cookies in the heap
            // it's imposible, print -1
            if (cookies.size() < 2) {
                operations = -1;
                break;
            }

            int c1 = cookies.poll();
            int c2 = cookies.poll();
            int newCookie = c1 + 2*c2;
            cookies.add(newCookie);
            operations++;
        }

        System.out.println(operations);
    }

}
