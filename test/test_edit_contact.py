from model.contact import Contact
import random


def test_edit_some_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    some_contact = random.choice(old_contacts)
    index = old_contacts.index(some_contact)
    contact.id = some_contact.id
    app.contact.edit_contact_by_id(contact, some_contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
