class Phone(object):
    def __init__(self):
        self.phone_book = []

    def add(self, name, pnumber):
        #use a dictionary to store the contacts and their name
        phone_book_dict={}
        phone_book_dict['name'] =name
        phone_book_dict['pnumber']= pnumber
        self.phone_book.append(phone_book_dict)
        return "Success contact added"

    def delete(self, name, pnumber):
        pass

    def view(self, name, pnumber):
        view_all = [phone for phone in self.phone_book]
        return view_all

    def update_contact(self, name, pnumber):
        pass

    