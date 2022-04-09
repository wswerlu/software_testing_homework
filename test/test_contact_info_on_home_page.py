from random import randrange
from model.contact import Contact


def test_contact_info_on_home_page_with_ui(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == \
           app.contact.merge_emails_like_on_home_page(contact_from_edit_page)


def test_contact_info_on_home_page_with_ui_and_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for index in range(len(contacts_from_home_page)):
        contact_from_home_page = contacts_from_home_page[index]
        contact_from_db = contacts_from_db[index]
        assert contact_from_home_page.firstname == contact_from_db.firstname.strip()
        assert contact_from_home_page.lastname == contact_from_db.lastname.strip()
        assert contact_from_home_page.address == contact_from_db.address.strip()
        assert contact_from_home_page.all_phones_from_home_page == \
               app.contact.merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == \
               app.contact.merge_emails_like_on_home_page(contact_from_db)
