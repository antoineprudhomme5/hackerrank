import java.util.Scanner;
import java.util.HashMap;

public class Solution {

    private static class Node {

        private int uses;
        private HashMap<Character, Node> children = new HashMap<>();

        public Node() {
            this.uses = 0;
        }

        public int getUses() {
            return this.uses;
        }

        public HashMap getChildren() {
            return this.children;
        }

        public Node getChild(Character ch) {
            return this.children.get(ch);
        }

        public void addUse() {
            this.uses++;
        }

    }

    private static class ContactTree {

        private Node root;

        public ContactTree() {
            this.root = new Node();
        }

        /**
         * Insert a new contact name in the contact tree
         *
         * @param String name : the contact name
         * @return void
         */
        public void insertContact(String name) {
            Node current = this.root;
            // put each Character of the name in the tree
            for (int i = 0; i < name.length(); i++) {
                Character ch = name.charAt(i);
                // if this Character is not a child of this Node,
                // add it
                current.getChildren().putIfAbsent(ch, new Node());
                // down the tree
                current = current.getChild(ch);
                // increment the number of uses of the current Node
                current.addUse();
            }
        }

        /**
         * Down the tree following the partial string
         * and return the number of uses of this node
         *
         * @param String partial
         * @return int : the number of name starting by partial
         */
        public int countContacts(String partial) {
            Node current = this.root;
            // go down the tree
            for (int i = 0; i < partial.length(); i++) {
                Character ch = partial.charAt(i);
                // if this Character is not a child of the current node,
                // return 0 (the partial matches 0 name)
                current = current.getChild(ch);
                if (current == null) {
                    return 0;
                }
            }
            
            return current.getUses();
        }

    }

    public static void main(String[] args) {
        ContactTree contactTree = new ContactTree();

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++){
            String op = in.next();
            String contact = in.next();

            if (op.equals("add")) {
                contactTree.insertContact(contact);
            } else {
                System.out.println(contactTree.countContacts(contact));
            }

        }
    }
}
