class PhoneBook:

    def __init__(self, contacts_list = None):
        self.contacts_list = contacts_list or []

    def add_contact(self, name, phone_number):
        if len(phone_number) == 11 and phone_number.startswith("0"):
            contact = {"name": name, "phone_number": phone_number}
            self.contacts_list.append(contact)

    def size_of_contact_list(self) :
        return  len(self.contacts_list)


    def delete_contact(self, delete_name):
        for the_contacts in self.contacts_list:
            if the_contacts["name"] == delete_name:
                self.contacts_list.remove(the_contacts)
                break


    def search_contact(self, name):
        for my_contacts in self.contacts_list:
            if my_contacts["name"] == name:
                return True

        return False


    def clear_contact_list(self):
        if self.contacts_list:
            self.contacts_list.clear()

    #
    # def display_contact(self, contacts_list):
    #     contact_lst = []
    #     for numbers in range(len(contacts_list)):
    #         if numbers in contacts_list:
    #             contact_lst.append(numbers)
    #             return contact_lst
    #         else:
    #             return "contact not found"
    #
