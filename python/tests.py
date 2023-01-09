import surfshop
import unittest

class SurfingTests(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
    output = self.cart.add_surfboards(quantity=1)
    self.assertEqual(output, f'Successfully added 1 surfboard to cart!')
  
  def test_add_surfboards(self):
    for i in range(2, 5):
      with self.subTest(i = i):
        output = self.cart.add_surfboards(i)
        self.assertEqual(output, f'Successfully added {i} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  def test_too_many_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 6)

  # @unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def test_checkout_date(self):
    date = self.cart.set_checkout_date()
    self.assertRaises(surfshop.CheckoutDateError,self.cart.set_checkout_date())
unittest.main()