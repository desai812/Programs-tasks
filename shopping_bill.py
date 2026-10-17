# Task 01 - Shopping Bill (GST first, discount after) - Python


def calculate_electronics_gst(a, b):
    """Step 1: (a + b) + 18% GST"""
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


def calculate_fashion_gst(c, d):
    """Step 2: (c + d) + 13% GST"""
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst


def calculate_food_gst(e):
    """Step 3: e + 7% GST"""
    gst = e * 7 / 100
    return e + gst


def total_bill(a, b, c, d, e):
    """Step 4: sum of the three GST amounts"""
    electronics = calculate_electronics_gst(a, b)
    fashion = calculate_fashion_gst(c, d)
    food = calculate_food_gst(e)
    return electronics + fashion + food


def calculate_discounted_bill(a, b, c, d, e):
    """Step 5: total after GST minus 20% discount (final payable amount)"""
    total = total_bill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


if __name__ == "__main__":
    # Sample test values supplied directly (no input())
    a, b, c, d, e = 100, 100, 100, 100, 100

    electronics = calculate_electronics_gst(a, b)
    fashion = calculate_fashion_gst(c, d)
    food = calculate_food_gst(e)
    total = total_bill(a, b, c, d, e)
    final_amount = calculate_discounted_bill(a, b, c, d, e)
    discount = total - final_amount

    print("===== SHOPPING BILL (Python) =====")
    print(f"Electronics: (Rs.{a} + Rs.{b}) + 18% GST = Rs.{electronics:.2f}")
    print(f"Fashion    : (Rs.{c} + Rs.{d}) + 13% GST = Rs.{fashion:.2f}")
    print(f"Food       : Rs.{e} + 7% GST            = Rs.{food:.2f}")
    print(f"Total after GST      : Rs.{total:.2f}")
    print(f"20% discount         : Rs.{discount:.2f}")
    print(f"Final payable amount : Rs.{final_amount:.2f}")
    print()
    print(f"Total after GST = Rs.{total:.2f} | Discount = Rs.{discount:.2f} | "
          f"Final payable amount = Rs.{final_amount:.2f}")
