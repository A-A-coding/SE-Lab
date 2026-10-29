import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# ---------- item_total ----------
def test_food_item():
    assert item_total("food", 100, 2) == 210

def test_unknown_category():
    with pytest.raises(ValueError):
        item_total("toys", 100, 1)

def test_invalid_price_or_qty():
    with pytest.raises(ValueError):
        item_total("food", -5, 1)

def test_bulk_discount():
    # 100*10 = 1000, -100 = 900, +5% GST (45) = 945
    assert item_total("food", 100, 10) == 945


# ---------- cart_discount ----------
def test_discount_5000_prime():
    assert cart_discount(5000, True, None) == 600

def test_discount_2000():
    assert cart_discount(2000, False, None) == 200

def test_discount_below_2000():
    assert cart_discount(100, False, None) == 0

def test_discount_flat10():
    # 1000 >= 1000 -> 0 + 100
    assert cart_discount(1000, False, "FLAT10") == 100


# ---------- shipping_fee ----------
def test_free_shipping():
    assert shipping_fee(1000, False, False) == 0

def test_shipping_fee_below_500():
    assert shipping_fee(100, False, False) == 40

def test_prime_express():
    assert shipping_fee(100, True, True) == 50

def test_non_prime_express():
    assert shipping_fee(100, False, True) == 140
