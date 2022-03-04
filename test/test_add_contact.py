# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="test create", lastname="test create", address="test create",
                               home_phone="test create", email="test create"))
