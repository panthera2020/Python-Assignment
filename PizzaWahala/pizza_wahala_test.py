from unittest import TestCase

from pizza_wahala import *

class PizzaDeliveryTest(TestCase):

	def test_thatWhen_iGetThe_numberOf_guestAnd_pizzaType_iGetThe_numberOfBoxes_userWillBuy(self):

		expected_number_of_Boxes = box_number_for(45,'odogwu')

		actual_number_of_boxes = 4

		self.assertEqual(expected_number_of_Boxes, actual_number_of_boxes)

	def test_thatWhen_iGetThe_numberOf_guestAnd_pizzaType_iGetThe_numberOfSlices_thatWillBeLeft(self):

		expected_number_of_slices = slices_left_in(45, 'odogwu')

		actual_number_of_slices = 3

		self.assertEqual(expected_number_of_slices, actual_number_of_slices)

	def test_thatWhen_iGetThe_numberOf_guestAnd_pizzaType_iGetThe_totalPrice_forTheBoxes_ofPizzaBought(self):

		expected_price = price_for(45, 'odogwu')

		actual_price = 20800

		self.assertEqual(expected_price, actual_price)

	def test_ifPizzaType_inputedIsCorrect(self):

		expected_answer = is_valid_pizza('Odogwu')

		actual_answer = True

		self.assertEqual(expected_answer, actual_answer)

	def test_ifNumberOf_guestIsA_validDigit(self):

		expected_answer = is_valid_digit(45):

		actual_answer = True

		self.assertEqual(expected_answer, actual_answer)