class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None


def remove_index(ll, index):
    tmp = ll.head
    for i in range(index-1):
        tmp = tmp.next
    tmp.next = tmp.next.next
    return tmp


def insert_end(ll, nde):
    tmp = ll.head
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = nde
    return ll


def insert_top(ll, nde):
    tmp = ll.head
    ll.head = nde
    ll.head.next = tmp
    return ll


def main():
    ll = linkedlist()
    ll.head = node(44)
    ll.head.next = node(36)
    ll.head.next.next = node(96)
    ll.head.next.next.next = node(10)
    ll.head.next.next.next.next = node(60)
    ll.head.next.next.next.next.next = node(99)
    # ll.head.next = ll2 = node(36)
    # ll2.next = ll3 = node(90)
    # ll3.next = ll4 = node(10)
    # ll4.next = ll5 = node(60)
    # ll5.next = node(99)
    insert_top(ll, node(104))
    insert_end(ll, node(57))
    remove_index(ll, 4)



if __name__ == "__main__":
    main()