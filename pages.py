from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_A_TAXI_BUTTON_LOCATOR = (By.XPATH, '(//button[@class = "button round"])')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '(//div[text() = "Supportive"])[1]')
    PHONE_NO_BUTTON_LOCATOR = (By.CSS_SELECTOR, "div.np-text")
    ENTERING_PHONE_NO_LOCATOR = (By.ID, 'phone')
    PHONE_NO_NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text() = "Next"]')
    ENTERING_CODE_LOCATOR = (By.ID, "code")
    CODE_PAGE_CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text() = "Confirm"]')
    PAYMENT_METHOD_LOCATOR = (By.CSS_SELECTOR, 'div.pp-text')
    PAYMENT_METHOD_ADD_CARD_LOCATOR = (By.XPATH, '//div[text() = "Add card"]')
    CARD_NUMBER_LOCATOR = (By.XPATH, '//input[@class ="card-input"]')
    CARD_CODE_LOCATOR = (By.XPATH, '(//input[@id= "code"])[2]')
    ADDING_A_CARD_TITLE_LOCATOR = (By.XPATH, '//div[text() = "Adding a card"]')
    ADDING_A_CARD_LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text() = "Link"]')
    PAYMENT_METHOD_CLOSE_LOCATOR = (By.XPATH, '(//button[@class = "close-button section-close"])[3]')
    COMMENT_FOR_DRIVER_LOCATOR = (By.ID, "comment")
    BLANKET_HANDKERCHIEFS_SLIDE_LOCATOR = (By.CLASS_NAME, "switch")
    BLANKET_HANDKERCHIEFS_CHECK_LOCATOR = (By.CLASS_NAME, "switch-input")
    ICE_CREAM_SELECTION_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'div.counter-plus')
    ORDER_TAXI_BUTTON_LOCATOR =(By.CSS_SELECTOR, 'button.smart-button')

    def __init__(self,driver):
        self.driver = driver

    def enter_from_location(self,ADDRESS_FROM):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(ADDRESS_FROM)

    def enter_to_location(self,ADDRESS_TO):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(ADDRESS_TO)

    def set_route(self,ADDRESS_FROM,ADDRESS_TO):
        self.enter_from_location(ADDRESS_FROM)
        self.enter_to_location(ADDRESS_TO)

    def select_plan(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def get_verification_of_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).text

    def fill_phone_number(self,PHONE_NUMBER):
        self.driver.find_element(*self.PHONE_NO_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.ENTERING_PHONE_NO_LOCATOR).send_keys(PHONE_NUMBER)
        self.driver.find_element(*self.PHONE_NO_NEXT_BUTTON_LOCATOR).click()

    def sms(self,phone_code):
        self.driver.find_element(*self.ENTERING_CODE_LOCATOR).send_keys(phone_code)
        self.driver.find_element(*self.CODE_PAGE_CONFIRM_BUTTON_LOCATOR).click()

    def fill_card(self,CARD_NUMBER,CARD_CODE):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()
        self.driver.find_element(*self.PAYMENT_METHOD_ADD_CARD_LOCATOR).click()
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(CARD_NUMBER)
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(CARD_CODE)
        self.driver.find_element(*self.ADDING_A_CARD_TITLE_LOCATOR).click()
        self.driver.find_element(*self.ADDING_A_CARD_LINK_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.PAYMENT_METHOD_CLOSE_LOCATOR).click()

    def comment_for_driver(self,MESSAGE_FOR_DRIVER):
        self.driver.find_element(*self.COMMENT_FOR_DRIVER_LOCATOR).send_keys(MESSAGE_FOR_DRIVER)

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEFS_SLIDE_LOCATOR).click()

    def verification_of_status_blanket_and_handkerchiefs(self):
        return self.driver.find_element(*self.BLANKET_HANDKERCHIEFS_CHECK_LOCATOR).get_property("checked")

    def order_2_ice_creams(self):
        self.driver.find_element(*self.ICE_CREAM_SELECTION_BUTTON_LOCATOR).click()

    def car_search_model_appears(self):
        self.driver.find_element(*self.ORDER_TAXI_BUTTON_LOCATOR).click()






#













