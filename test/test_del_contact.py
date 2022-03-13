from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

