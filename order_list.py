class Order:
    def __init__(self, order_id, customer, details, total=0):
        self.order_id = order_id
        self.customer = customer
        self.details = details
        self.total = total

    def __str__(self):
        return (
            f"Order ID: {self.order_id}, "
            f"Customer: {self.customer}, "
            f"Details: {self.details}, "
            f"Total: ${self.total}"
        )


class Node:
    def __init__(self, order):
        self.order = order
        self.next = None


class OrderLinkedList:
    def __init__(self):
        self.head = None

    def append(self, order):
        new_node = Node(order)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        if current is None:
            print("No orders in the list.")
            return

        while current:
            print(current.order)
            current = current.next

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


if __name__ == "__main__":
    orders = OrderLinkedList()

    orders.append(Order(1, "Aden", "Laptop", 900))
    orders.append(Order(2, "John", "Phone", 600))
    orders.append(Order(3, "Sara", "Headphones", 120))

    print("Original Order List:")
    orders.display()

    orders.reverse()

    print("\nReversed Order List:")
    orders.display()
