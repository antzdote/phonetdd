import unittest
from phonebook import Contacts

class TestContactsCase(unittest.TestCase):
    
    
    def test_create_contact(self):
        contact = Contacts()
        response = contact.create_contact("ant", "0718650260")
        self.assertEqual(response['message'], 'Success Contact created!')

        
    def test_view_contact(self):
        contact = Contacts()
        response = contact.create_contact("ant", "0718650260")
        response = contact.view_contact(contact)
        self.assertEqual(response, {'name':"ant", 'phon_num':"0718650260"})

    def test_delete_contact(self):
        contact = Contacts()
        response = contact.delete_contact(contact)
        self.assertEqual(response['message'], 'Warning Contact deleted!')

   
    def test_update_contact(self):
        contact = Contacts()
        response = contact.update_contact(contact)
        self.assertEqual(response['message'], 'Succes Contact updated!')
 
if __name__ == '__main__':
       unittest.main()