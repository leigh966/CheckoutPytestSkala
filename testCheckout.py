from Checkout import Checkout
import pytest

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout


def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_CanCalculateCorrectTotal(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal()==3

def test_CanAddDiscountRule(checkout):
    checkout.addDiscount("a",3,2)

def test_CanApplyDiscountRule(checkout):
    checkout.addDiscount("a",3,2)
    for number in range(0,3):
        checkout.addItem("a")
    assert checkout.calculateTotal() == 2