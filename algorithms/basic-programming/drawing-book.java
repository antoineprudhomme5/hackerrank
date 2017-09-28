import java.util.Scanner;

class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numberOfPages = sc.nextInt();
        int pageToOpen = sc.nextInt();

        int fromRight = (int)Math.floor(pageToOpen / 2);
        int fromLeft = (int)Math.floor(numberOfPages/2) -  (int)Math.floor(pageToOpen/2);
        System.out.println(fromRight > fromLeft ? fromLeft : fromRight);
    }

}
