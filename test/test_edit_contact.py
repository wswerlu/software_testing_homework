from model.contact import Contact


def test_edit_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="test edit"))
    app.session.logout()


def test_edit_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(address="test edit"))
    app.session.logout()


def test_edit_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(email="test edit"))
    app.session.logout()
