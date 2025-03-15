Automated tests covering the full process of ordering a taxi. 

The tests covers:

-Setting the address

-Selecting Supportive plan(Tip: don't forget to make an if condition whether this tariff is selected or not. To avoid unnecessary clicks that lead to test failures )

-Filling in the phone number(Tip: don't forget to use the retrieve_phone_code() method from the helpers.py file to retrieve the sms code)

-Adding a credit card (Tip: the ‘Link’ button may not become clickable until the card CVV field on the “Adding a card” modal id=”code” class=”card-input” loses focus. To change focus you can simulate the user pressing TAB or clicking somewhere else on the screen).

-Writing a comment for the driver

-Ordering a Blanket and handkerchiefs (Tip: there are two selectors to be aware of here. One selector to click on and one to run assert on to verify that the state changed).

-Ordering 2 Ice creams

-Order a taxi with the ‘Supportive’ tariff. The car search modal window should appear. (Tip: When ordering, don't forget to add a message for the driver)
