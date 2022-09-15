from seleniumbase import BaseCase


class HomePage(BaseCase):
    decline_cookie_btn = 'button[id="onetrust-reject-all-handler"]'
    expected_currency = "GBP"
    currency_button = 'button[data-modal-header-async-type="currencyDesktop"]'
    currency_confirm = 'a[data-modal-header-async-url-param*="GBP"]'
    search_box = 'input[id="ss"]'
    destination = "London"
    check_in_box = 'div[data-calendar2-title="Check-in"]'
    check_in_calendar = 'div[id="bui-calendar-1662725185286mqir"]'
    check_in_date = 'td[data-date="2022-09-16"]'
    check_out_date = 'td[data-date="2022-09-18"]'
    guest_check_box = 'label[id="xp__guests__toggle"]'
    decrease_adults = '[aria-label="Decrease number of Adults"]'
    increase_adults = '[aria-label="Increase number of Adults"]'
    number_of_adults = 'input[id="group_adults"]'
    search_button = 'button[data-et-click*=www_index_search_button_click]'

    def open_home_page(self):
        self.open("https://www.booking.com")

