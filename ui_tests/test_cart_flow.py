from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Step 1: Open website
        home = HomePage(page)
        home.navigate()

        # Step 2: Select product
        product_name = home.select_first_product()

        # Step 3: Add to cart
        product = ProductPage(page)
        product.add_to_cart()

        # Step 4: Go to cart
        product.go_to_cart()

        # Step 5: Validate
        cart = CartPage(page)
        assert cart.get_cart_item_name() == product_name
        assert cart.get_cart_count() == 1

        # (Optional Bonus)
        cart.remove_item()
        assert cart.is_cart_empty()

        browser.close()
