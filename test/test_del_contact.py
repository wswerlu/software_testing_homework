from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    app.contact.delete_first_contact()
