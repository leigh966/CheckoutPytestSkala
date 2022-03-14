from Checkout import Checkout
import pytest

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_CanAddItemPrice(checkout):
    checkout.addItemPrice("a", 1)

def test_CanAddItem(checkout):
    checkout.addItem("a")