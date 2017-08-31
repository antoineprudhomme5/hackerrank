class Node:

    def __init__(self):
        self.letters = {}
        self.uses = 0

class ContactList:

    def __init__(self):
        self.root = Node()

    """
        Insert a new contact name in the tree of contacts
    """
    def insert_contact(self, name, l = None, i = 0):
        if not l:
            l = self.root

        # if name is empty, quit
        if i >= len(name):
            return

        # insert letter by letter.
        # if the next letter is not in the letters of this node,
        # add the letter
        if name[i] not in l.letters:
            # if this is the last letter
            l.letters[name[i]] = Node()
        # increment the uses of this node
        l.letters[name[i]].uses += 1

        # call recursively this method to insert fully the contact name
        # with the rest of the name
        return self.insert_contact(name, l.letters[name[i]], i+1)


    """
        Down the tree following the partial string
        and return the number of uses of this node
    """
    def count_contact(self, partial):
        if not partial:
            return

        node = self.root
        i = 0
        while i < len(partial):
            if partial[i] not in node.letters:
                # the partial match 0 contact
                return 0

            node = node.letters[partial[i]]
            i += 1

        return node.uses


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
