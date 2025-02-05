import time
import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoute:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        # Method to enter the routing addresses
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        print(f' The routing addresses are "{data.ADDRESS_FROM}" and "{data.ADDRESS_TO}".')

    def test_select_plan(self):
        # Method to select the Supportive plan under the "call a taxi" option
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            print(" The Supportive plan is selected.")
        else:
            urban_page.select_plan()

    def test_fill_phone_number(self):
        # Method to add the phone number
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            pass
        else:
            urban_page.select_plan()
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.sms(phone_code)
        print(f' The phone number is "{data.PHONE_NUMBER}" and the code is "{phone_code}".')

    def test_fill_card(self):
        # Method to add the card in payment system
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            pass
        else:
            urban_page.select_plan()
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        print(" The card is added in payment method.")

    def test_comment_for_driver(self):
        # Method to send message to the Driver
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            pass
        else:
            urban_page.select_plan()
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        print(f' The message to the driver is "{data.MESSAGE_FOR_DRIVER}".')

    def test_order_blanket_and_handkerchiefs(self):
        # Method to select Blankets and handkerchiefs
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            pass
        else:
            urban_page.select_plan()
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_page.order_blanket_and_handkerchiefs()
        assert urban_page.verification_of_status_blanket_and_handkerchiefs() == True, f"Need to order blanket and handkerchief again"
        print(" The blanket and handkerchiefs have ordered for the route.")

    def test_order_2_ice_creams(self):
        # Method to order 2 ice-creams
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            pass
        else:
            urban_page.select_plan()
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_page.order_blanket_and_handkerchiefs()
        no_of_ice_cream = 2
        for ice_cream in range(no_of_ice_cream):
            urban_page.order_2_ice_creams()
        print(" Two ice creams have ordered for the route.")

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            pass
        else:
            urban_page.select_plan()
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_page.order_blanket_and_handkerchiefs()
        assert urban_page.verification_of_status_blanket_and_handkerchiefs() == True, f"Need to order blanket and handkerchief"
        no_of_ice_cream = 2
        for ice_cream in range(no_of_ice_cream):
            urban_page.order_2_ice_creams()
        urban_page.car_search_model_appears()
        time.sleep(2)
        print(" The 'car search' has appeared.")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()