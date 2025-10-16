def calculate_total_revenue(items):
    """Calculates total revenue = sum(price * quantity) for all items."""
    total = sum(item["price"] * item["quantity"] for item in items)
    return total


sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1},
]

print("Total Revenue:", calculate_total_revenue(sales_data))