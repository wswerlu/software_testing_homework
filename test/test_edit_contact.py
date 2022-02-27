from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="test edit", lastname="test edit", address="test edit",
                                           home_phone="test edit", email="test edit"))
    app.session.logout()
