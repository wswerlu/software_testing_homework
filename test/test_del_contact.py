from model.contact import Contact
import random
import allure


def test_delete_some_contact(app, db, check_ui):
    with allure.step("Given a non-empty contact list"):
        app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    with allure.step("Given a random contact from the list"):
        contact = random.choice(old_contacts)
    with allure.step(f"When I delete the contact {contact} from the list"):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step("Then the new contact list is equal to the old contact list with the deleted contact"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) \
                   == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

