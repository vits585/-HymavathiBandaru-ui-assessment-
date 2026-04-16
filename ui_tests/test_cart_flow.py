from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Here we need to Open website
        home = HomePage(page)
        home.navigate()

        # Then Select a product
        product_name = home.select_first_product()

        # After that add an item into Add to cart
        product = ProductPage(page)
        product.add_to_cart()

        # Check into item is added in cart so need to Go to cart
        product.go_to_cart()

        # Finally we need to check here as item is added to cart and Validate the item as well
        cart = CartPage(page)
        assert cart.get_cart_item_name() == product_name
        assert cart.get_cart_count() == 1

        # Here we will check it as after remove an item from cart is it still visible or not(check cart is empty or not)
        cart.remove_item()
        assert cart.is_cart_empty()

        browser.close()
