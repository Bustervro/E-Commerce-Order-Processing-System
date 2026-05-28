# E-Commerce-Order-Processing-System
# Order Processing System Using a Singly Linked List

## Problem Description

This project simulates an e-commerce order processing system using a singly linked list.

Orders are stored in the order they are received. Due to a change in fulfillment strategy, the system now needs to process the most recent orders first.

To solve this problem, the linked list is reversed so the newest orders appear at the front of the list.

---

## Features

- Create orders
- Append orders to a singly linked list
- Display orders
- Reverse the linked list
- Unit testing with normal and edge cases

---

## Files

- `order_list.py` → Main linked list implementation
- `test_order_list.py` → Unit tests
- `diagram.md` → Linked list diagram
- `requirements.txt` → Dependencies

---

## How to Run

### Run the Program

```bash
python order_list.py
```

### Run Unit Tests

```bash
python -m unittest test_order_list.py
```

---

## Normal Test Cases

1. Add one order
2. Add multiple orders
3. Reverse multiple orders

---

## Edge Test Cases

1. Reverse empty list
2. Display empty list
3. Reverse single order list

---

## Time Complexity

| Operation | Complexity |
|---|---|
| append() | O(n) |
| display() | O(n) |
| reverse() | O(n) |

---

## Space Complexity

| Operation | Complexity |
|---|---|
| append() | O(1) |
| reverse() | O(1) |
| display() | O(1) |

---

## Clarifying Questions

1. Should duplicate order IDs be allowed?
2. Should order IDs be auto-generated?
3. Should orders support searching or deletion?
4. Should the newest order always be processed first after reversal?

---

## Optimization Discussion

The reverse() function reverses the linked list in place instead of creating a second list.

Benefits:
- Saves memory
- Uses O(1) extra space
- Efficient for large datasets

Trade-Off:
- Original order is permanently changed unless reversed again.
