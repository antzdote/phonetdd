class Contacts(object):
    
    def __init__(self):
        self.contact_list = [] 
    def create_contact(self, name, phon_num):
        contact = {}
        contact['name'] = name
        contact['phon_num'] = phon_num
        self.contact_list.append(contact) 
        return {"message": "Contact created!"}

    
    def view_contact(self, contact):
        for contact in self.contact_list:
            return contact

       
    def delete_contact(self, contact):
        if contact in self.contact_list:
            self.contact_list.remove(contact)
        return {'message':'Contact deleted!'}

    
    def update_contact(self,contact):
        for contact in self.contact_list:
            if contact == contact:
                contact['']
        return {'message': 'Contact updated!'}