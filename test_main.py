import pytest
import main


@pytest.fixture
def happy_cart():
    return [main.CartItem("Eggs", 1.99, "Wic Eligible food"),
            main.CartItem("Expensive Hat", 185.68, "Clothing"),
            main.CartItem("Jump Rope", 7.29, "Toy")]


def test_happy_mass(happy_cart):
    assert main.calculate_charge("Massachusetts", happy_cart) == 196.21


def test_happy_maine(happy_cart):
    assert main.calculate_charge("Maine", happy_cart) == 205.57


def test_happy_nh(happy_cart):
    assert main.calculate_charge("New Hampshire", happy_cart) == 194.96


def test_negative_cost():
    cart = [main.CartItem("Eggs", 1.99, "Wic Eligible food"),
            main.CartItem("Expensive Hat", -185.68, "Clothing"),
            main.CartItem("Jump Rope", 7.29, "Toy")]
    assert main.calculate_charge("Massachusetts", cart) == 196.21


def test_zero_cost():
    cart = [main.CartItem("Eggs", 0, "Wic Eligible food")]
    assert main.calculate_charge("Massachusetts", cart) == 0


def test_bad_state():
    cart = [main.CartItem("Eggs", 1.99, "Wic Eligible food")]
    assert pytest.raises(ValueError, main.calculate_charge, "Florida", cart)


def test_empty_cart():
    cart = []
    assert main.calculate_charge("Massachusetts", cart) == 0
