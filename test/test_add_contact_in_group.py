from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_in_some_group(app, db, orm):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_in_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)
