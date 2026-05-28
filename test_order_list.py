import unittest
from order_list import Order, OrderLinkedList


class TestOrderLinkedList(unittest.TestCase):

    # Normal Test Cases

    def test_append_single_order(self):
        orders = OrderLinkedList()

        orders.append(Order(1, "Aden", "Laptop", 900))

        self.assertEqual(orders.head.order.order_id, 1)

    def test_append_multiple_orders(self):
        orders = OrderLinkedList()

        orders.append(Order(1, "Aden", "Laptop", 900))
        orders.append(Order(2, "John", "Phone", 600))
        orders.append(Order(3, "Sara", "Headphones", 120))

        self.assertEqual(orders.head.order.order_id, 1)
        self.assertEqual(orders.head.next.order.order_id, 2)
        self.assertEqual(orders.head.next.next.order.order_id, 3)

    def test_reverse_multiple_orders(self):
        orders = OrderLinkedList()

        orders.append(Order(1, "Aden", "Laptop", 900))
        orders.append(Order(2, "John", "Phone", 600))
        orders.append(Order(3, "Sara", "Headphones", 120))

        orders.reverse()

        self.assertEqual(orders.head.order.order_id, 3)
        self.assertEqual(orders.head.next.order.order_id, 2)
        self.assertEqual(orders.head.next.next.order.order_id, 1)

    # Edge Test Cases

    def test_reverse_empty_list(self):
        orders = OrderLinkedList()

        orders.reverse()

        self.assertIsNone(orders.head)

    def test_display_empty_list(self):
        orders = OrderLinkedList()

        self.assertIsNone(orders.head)

    def test_reverse_single_order(self):
        orders = OrderLinkedList()

        orders.append(Order(1, "Aden", "Laptop", 900))

        orders.reverse()

        self.assertEqual(orders.head.order.order_id, 1)


if __name__ == "__main__":
    unittest.main()
