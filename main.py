import time
import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoute:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)

    # if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
    #     print("the urban route app is working")
    # else:
    #     print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Task 3: Define 8 functions

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            print("The Supportive plan is selected")
        else:
            pass

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            print("The Supportive plan is selected")
        else:
            pass
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        print(phone_code)
        urban_page.sms(phone_code)
        #time.sleep(2)

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            print("The Supportive plan is selected")
        else:
            pass
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        print(phone_code)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        #time.sleep(2)

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            print("The Supportive plan is selected")
        else:
            pass
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        print(phone_code)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
       #time.sleep(2)

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            print("The Supportive plan is selected")
        else:
            pass
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        print(phone_code)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_page.order_blanket_and_handkerchiefs()
        assert urban_page.verification_of_status_blanket_and_handkerchiefs() == True, f"Need to order blanket and handkerchief"
        #time.sleep(2)

    # Task 5: Preparing the ice cream order
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO)
        urban_page.select_plan()
        if urban_page.get_verification_of_plan() == "Supportive":
            print("The Supportive plan is selected")
        else:
            pass
        urban_page.fill_phone_number(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        print(phone_code)
        urban_page.sms(phone_code)
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_page.order_blanket_and_handkerchiefs()
     #   assert urban_page.verification_of_status_blanket_and_handkerchiefs() == True, f"Need to order blanket and handkerchief"
        no_of_ice_cream = 2
        for ice_cream in range(no_of_ice_cream):
            urban_page.order_2_ice_creams()
        #time.sleep(2)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(2)
        # Creating an instance of the UrbanRoutesPage class
        urban_page = UrbanRoutesPage(self.driver)
        urban_page.set_route(data.ADDRESS_FROM,data.ADDRESS_TO) # Entering addresses
        urban_page.select_plan() # Selecting the supportive plan
        if urban_page.get_verification_of_plan() == "Supportive":
            print("The Supportive plan is selected")
        else:
            pass
        urban_page.fill_phone_number(data.PHONE_NUMBER) # Filling up the phone number
        phone_code = helpers.retrieve_phone_code(self.driver)
        print(phone_code)
        urban_page.sms(phone_code) # Getting the generated code
        urban_page.fill_card(data.CARD_NUMBER, data.CARD_CODE) # Adding the credit card details
        urban_page.comment_for_driver(data.MESSAGE_FOR_DRIVER) # Adding message for the driver
        urban_page.order_blanket_and_handkerchiefs() # Ordering the blanket and handkerchief and verify the status
        assert urban_page.verification_of_status_blanket_and_handkerchiefs() == True, f"Need to order blanket and handkerchief"
        no_of_ice_cream = 2
        for ice_cream in range(no_of_ice_cream):
            urban_page.order_2_ice_creams() # Ordering 2 ice creams
        urban_page.car_search_model_appears() # After ordering the taxi, the Car search will appear

        time.sleep(5) # Waiting to verify the "car search" page load properly

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()