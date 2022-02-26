# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="test create", lastname="test create", address="test create",
                               home_phone="test create", email="test create"))
    app.session.logout()
