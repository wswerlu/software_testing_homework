# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="test create", lastname="test create", address="test create",
                               home_phone="test create", email="test create"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
