import java.util.*;

public class Solution {

    private static class Node {
        private boolean isEndOfString = false;
        private HashMap<Character, Node> children = new HashMap<>();

        public HashMap getChildren() {
            return this.children;
        }

        public Node getChild(Character ch) {
            return this.children.get(ch);
        }

        public boolean getIsEndOfString() {
            return this.isEndOfString;
        }

        public void setIsEndOfString(boolean isEndOfString) {
            this.isEndOfString = isEndOfString;
        }
    }

    private static class Tries {
        private Node root;

        public Tries() {
            this.root = new Node();
        }

        public boolean insert(String str) {
            Node current = this.root;
            int i = 0;

            for (i = 0; i < str.length() - 1; i++) {
                Character ch = str.charAt(i);
                // if this Character is not a child of this Node,
                // add it
                current.getChildren().putIfAbsent(ch, new Node());
                // down the tree
                current = current.getChild(ch);

                if (current.getIsEndOfString()) {
                    return true;
                }
            }

            // for the last node of this string, check if not already in the tries
            // if it's the case, it means that this string is a prefix of another string
            Character ch = str.charAt(i);
            if (current.getChildren().putIfAbsent(ch, new Node()) != null) {
                return true;
            }
            // down the tree
            current = current.getChild(ch);

            // the last node is the end of a string
            current.setIsEndOfString(true);

            return false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Tries tries = new Tries();
        boolean prefix = false;

        int n = sc.nextInt();
        String str = "";
        for (int i = 0; i < n && !prefix; i++) {
            str = sc.next();
            prefix = tries.insert(str);
        }

        if (prefix) {
            System.out.println("BAD SET");
            System.out.println(str);
        } else {
            System.out.println("GOOD SET");
        }
    }
}
