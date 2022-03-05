from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.is_contact_present(Contact(firstname="test"))
    app.contact.delete_first_contact()
