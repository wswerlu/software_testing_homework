from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
