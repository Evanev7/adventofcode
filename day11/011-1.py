from pathlib import Path


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        if self.next != None:
            return str(self.val + " " + str(self.next))
        else:
            return str(self.val)


with open(f"{Path(__file__).parent.resolve()}/011.txt") as file:
    data = file.read().strip()
    "125 17"

    _stones = data.split(" ")
    first_stone = LinkedList(_stones[0])

    cur = first_stone
    for i in _stones[1:]:
        cur.next = LinkedList(i)
        cur = cur.next

    # I want to do this in place
    for i in range(25):
        cur = first_stone
        while cur != None:
            if cur.val == "0":
                cur.val = "1"
            elif len(cur.val) % 2 == 0:
                left, right = cur.val[: len(cur.val) // 2], cur.val[len(cur.val) // 2 :]
                cur.val = str(int(left))
                _stone = LinkedList(str(int(right)))
                _stone.next = cur.next
                cur.next = _stone
                # ew ew references ew
                cur = _stone
            else:
                cur.val = str(2024 * int(cur.val))
            cur = cur.next

    tot = 1
    cur = first_stone
    while cur.next != None:
        tot += 1
        cur = cur.next
    print(tot)
