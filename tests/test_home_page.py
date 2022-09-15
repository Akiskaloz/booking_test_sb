from selenium.common import NoSuchElementException
from PageElements.home_page import HomePage


class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        print("Running before test")
        self.open_home_page()
        try:
            self.click(HomePage.decline_cookie_btn)
        except NoSuchElementException:
            print("Already accepted")
        self.scroll_to_top()

    def test_home(self):

        confirm_currency = self.get_property(HomePage.currency_button, "GBP")
        if confirm_currency != HomePage.expected_currency:
            self.click(HomePage.currency_button)
            self.click(HomePage.currency_confirm)
        else:
            print("Correct currency selected")

        self.send_keys(HomePage.search_button, HomePage.destination)

        self.click(HomePage.check_in_box)

        try:
            self.click(HomePage.check_in_date)
        except NoSuchElementException:
            print("Try another check-in date")
        self.scroll_to_top()
        try:
            self.click(HomePage.check_out_date)
        except NoSuchElementException:
            print("Try another check-out date")

        self.click(HomePage.guest_check_box)
        while True:
            self.click(HomePage.decrease_adults)
            adults_value = self.get_attribute(HomePage.number_of_adults, 'value')
            if int(adults_value) == 1:
                break

        self.click(HomePage.search_button)
