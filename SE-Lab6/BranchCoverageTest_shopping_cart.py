import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# ================= item_total =================
def test_food_item():
    assert item_total("food", 100, 2) == 210

def test_electronics_and_clothing_rates():
    assert item_total("electronics", 100, 1) == 118
    assert item_total("clothing", 100, 1) == 112

def test_unknown_category():
    with pytest.raises(ValueError):
        item_total("toys", 100, 1)

def test_negative_price():
    with pytest.raises(ValueError):
        item_total("food", -1, 1)

def test_zero_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, 0)

def test_negative_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, -3)

def test_zero_price_is_valid():
    assert item_total("food", 0, 1) == 0

def test_qty_just_below_bulk_threshold():
    # qty 9 -> no bulk discount: 900 + 45 = 945
    assert item_total("food", 100, 9) == 945

def test_qty_at_bulk_threshold():
    # qty 10 -> 1000 - 100 = 900, + 45 = 945
    assert item_total("food", 100, 10) == 945

def test_qty_above_bulk_threshold():
    # 100*20 = 2000 - 200 = 1800, + 90 = 1890
    assert item_total("food", 100, 20) == 1890


# ================= cart_discount =================
def test_discount_at_5000():
    assert cart_discount(5000, False, None) == 500

def test_discount_just_below_5000():
    assert cart_discount(4999, False, None) == 200

def test_discount_at_2000():
    assert cart_discount(2000, False, None) == 200

def test_discount_just_below_2000():
    assert cart_discount(1999, False, None) == 0

def test_prime_adds_100():
    assert cart_discount(100, True, None) == 100

def test_not_prime_no_bonus():
    assert cart_discount(100, False, None) == 0

def test_flat10_at_1000():
    assert cart_discount(1000, False, "FLAT10") == 100

def test_flat10_below_1000():
    assert cart_discount(999, False, "FLAT10") == 0

def test_wrong_coupon_code():
    assert cart_discount(1000, False, "SAVE20") == 0

def test_no_coupon_high_value():
    assert cart_discount(1000, False, None) == 0

def test_all_discounts_stack():
    # 500 (cart) + 100 (prime) + 600 (FLAT10 on 6000)
    assert cart_discount(6000, True, "FLAT10") == 1200


# ================= shipping_fee =================
def test_prime_free_shipping():
    assert shipping_fee(100, True, False) == 0

def test_free_shipping_at_500():
    assert shipping_fee(500, False, False) == 0

def test_paid_shipping_below_500():
    assert shipping_fee(499, False, False) == 40

def test_express_non_prime_paid():
    assert shipping_fee(100, False, True) == 140

def test_express_non_prime_free_base():
    assert shipping_fee(1000, False, True) == 100

def test_express_prime():
    assert shipping_fee(100, True, True) == 50
