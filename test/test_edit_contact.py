from model.contact import Contact
import random
import allure


def test_edit_some_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    with allure.step("Given a non-empty contact list"):
        app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    with allure.step("Given a random contact from the list"):
        some_contact = random.choice(old_contacts)
    with allure.step(f"When I make changes {contact} in the contact {some_contact} from the list"):
        index = old_contacts.index(some_contact)
        contact.id = some_contact.id
        app.contact.edit_contact_by_id(contact, some_contact.id)
    with allure.step("Then the contact info of the contact from the home page is equal as the contact info of "
                     "the contact from the editing page"):
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) \
                   == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
