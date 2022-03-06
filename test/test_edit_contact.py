from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.create_contact_if_is_not_exist(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname="test edit"))


def test_edit_contact_address(app):
    app.contact.create_contact_if_is_not_exist(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(address="test edit"))


def test_edit_contact_email(app):
    app.contact.create_contact_if_is_not_exist(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(email="test edit"))
