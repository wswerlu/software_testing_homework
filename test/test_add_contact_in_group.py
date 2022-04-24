from model.contact import Contact
from model.group import Group
import random
import allure


def test_add_some_contact_in_some_group(app, db, orm):
    with allure.step("Given a non-empty group list"):
        app.group.create_group_if_it_not_exist(Group(name="test"))
    with allure.step("Given a non-empty contact list"):
        app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    with allure.step("Given a random group from the list"):
        groups = db.get_group_list()
        group = random.choice(groups)
    with allure.step(f"Given a random contact from the list which is not in the group {group}"):
        contacts = orm.get_contacts_not_in_group(group)
        if contacts == []:
            app.contact.create(Contact(firstname="test"))
            contacts = orm.get_contacts_not_in_group(group)
        contact = random.choice(contacts)
    with allure.step(f"When I add a contact {contact} to the group {group}"):
        app.contact.add_contact_in_group(contact.id, group.id)
    with allure.step("Then the contact added to the group"):
        assert contact in orm.get_contacts_in_group(group)
