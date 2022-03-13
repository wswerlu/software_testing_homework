from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test edit")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_address(app):
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(address="test edit")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_email(app):
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(email="test edit")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
