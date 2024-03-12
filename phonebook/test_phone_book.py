
from phone_book import PhoneBook



def test_if_phone_book_can_add_contacts():
    phone_book = PhoneBook()

    assert phone_book.size_of_contact_list() is 0
    phone_book.add_contact("Ada", "07890876543")
    assert phone_book.size_of_contact_list() is 1

    #phone_book.clear_contact_list()
    #assert phone_book.size_of_contact_list() is 0


def test_phone_book_is_empty_before_adding_contact():
    phone_book2 = PhoneBook()
    assert phone_book2.size_of_contact_list() is 0

def test_contact_can_be_deleted():
    phone_book = PhoneBook()

    assert phone_book.size_of_contact_list() is 0
    phone_book.add_contact("Ada", "07890876543")
    phone_book.add_contact("john", "07890876543")
    assert phone_book.size_of_contact_list() is 2

    phone_book.delete_contact("Ada")
    assert phone_book.size_of_contact_list() is 1

    #phone_book.clear_contact_list()
    #assert phone_book.size_of_contact_list() is 0


def test_can_search_for_contacts():
    phone_book = PhoneBook()

    phone_book.add_contact("Ada", "07890876543")
    phone_book.add_contact("john", "07890876543")
    assert phone_book.search_contact("john") is True
    assert phone_book.size_of_contact_list() is 2

    #phone_book.clear_contact_list()
    #assert phone_book.size_of_contact_list() is 0

def test_can_clear_all_contact_list():
    phone_book = PhoneBook()

    assert phone_book.size_of_contact_list() is 0
    phone_book.add_contact("Ada", "07890876543")
    phone_book.add_contact("john", "07890876543")

    #phone_book.clear_contact_list()
    #assert phone_book.size_of_contact_list() is 0



