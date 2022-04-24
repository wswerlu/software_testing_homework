from model.contact import Contact
from model.group import Group
import random
import allure


def test_delete_some_contact_from_some_group(app, db, orm):
    with allure.step("Given a non-empty group list"):
        app.group.create_group_if_it_not_exist(Group(name="test"))
    with allure.step("Given a non-empty contact list"):
        app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    with allure.step("Given a random group from the list"):
        groups = db.get_group_id_with_contacts()
        if groups == []:
            contacts_list = db.get_contact_list()
            groups_list = db.get_group_list()
            some_contact = random.choice(contacts_list)
            some_group = random.choice(groups_list)
            app.contact.add_contact_in_group(some_contact.id, some_group.id)
            groups = db.get_group_id_with_contacts()
        group_id = random.choice(groups)
    with allure.step(f"Given a random contact from the list which is in the group with id {group_id}"):
        contacts = orm.get_contacts_in_group(Group(id=group_id))
        contact = random.choice(contacts)
    with allure.step(f"When I delete the contact {contact} from the group with id {group_id}"):
        app.contact.delete_contact_from_group(contact.id, group_id)
    with allure.step("Then the contact deleted from the group"):
        assert contact in orm.get_contacts_not_in_group(Group(id=group_id))
