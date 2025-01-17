import data
import helpers

#from helpers import is_url_reachable
#from data import URBAN_ROUTES_URL

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Task 4: Check the Server is on.
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Task 3: Define 8 functions
    def test_set_route(self):
        # Add in S8
        print("function created for setting route")
        pass
    def test_select_plan(self):
        # Add in S8
        print("function created for selecting plan")
        pass
    def test_fill_phone_number(self):
        # Add in S8
        print("function created for filling phone number")
        pass
    def test_fill_card(self):
        # Add in S8
        print("function created for filling the card information")
        pass
    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment to driver")
        pass
    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for ordering blanket and handkerchief")
        pass
    # Task 5: Preparing the ice cream order
    def test_order_2_ice_creams(self):
        print("function created for ordering 2 ice creams")
        for i in range(2):
            # Add in S8
            pass
    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for searching car model")
        pass