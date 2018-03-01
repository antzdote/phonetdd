import unittest
from contacts import Phone

class PhoneTestCase(unittest.TestCase):
    def setUp(self):
        self.phone=Phone()
    def tearDown(self):
        del self.phone

    def test_add_contacts(self):
        respose = self.phone.add("mildred", "0718655260" )
        self.assertEqual(respose, "Success contact added")
    
    def test_delete_contact(self):
        self.phone.phone_book= [{"name": "Mwala", "pnumber":"938477566"}]
        self.assertEqual(1, len(self.phone.phone_book))
        self.phone.delete_phone("Mwala")
        self.assertEqual(0, len(self.phone.phone_book))

    def test_view_all_contacts(self):
        self.phone.phone_book = [{"name": "Mwala", "pnumber":"938477566"},{"name": "bill", "pnumber":"9544775140"},{ "name": "anto", "pnumber":"123477566"}]
        respose = self.phone.phone_book
        value= self.phone.view_all()
        self.assertEqual(respose, value)