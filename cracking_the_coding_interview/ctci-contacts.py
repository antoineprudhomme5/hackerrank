class Node:

    def __init__(self, is_name = False):
        self.letters = {}
        self.is_name = is_name

class ContactList:

    def __init__(self):
        self.root = Node()

    """
        Insert a new contact name in the tree of contacts
    """
    def insert_contact(self, name, l = None):
        if not l:
            l = self.root

        # if name is empty, quit
        if not name:
            return

        # insert letter by letter.
        # if the next letter is not in the letters of this node,
        # add the letter
        if name[0] not in l.letters:
            # if this is the last letter, remember that this node is the end of a word
            l.letters[name[0]] = Node(len(name) == 1)

        # call recursively this method to insert fully the contact name
        # with the rest of the name
        return self.insert_contact(name[1:], l.letters[name[0]])


    """
        Count the number of name in the contact list that begin
        with the 'partial' string
    """
    def count_contact(self, partial):
        if not partial:
            return

        subtree = self.root
        # go down the tree until we reach the node that corespond to the 'partial'
        while len(partial):
            if partial[0] not in subtree.letters:
                # the partial match 0 contact
                return 0

            subtree = subtree.letters[partial[0]]
            partial = partial[1:]

        # count recursively the number of name in this subtree
        return self.count_contact_recursive_part(subtree)

    """
        Count the number of Node where the 'is_name' attribute
        is True in the given tree
    """
    def count_contact_recursive_part(self, tree):
        count = 0

        if tree.is_name:
            count += 1

        letters = tree.letters.keys()
        if len(letters):
            for letter in letters:
                count += self.count_contact_recursive_part(tree.letters[letter])

        return count


# create the contact list
contact_list = ContactList()

# read each operations
n = int(input().strip())
for _ in range(n):
    op, contact = input().strip().split(' ')

    if op == "add":
        contact_list.insert_contact(contact)
    else:
        print(contact_list.count_contact(contact))
