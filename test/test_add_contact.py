# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="sdfasdfs", lastname="asdfsdfas", address="jgkghjk",
                               home_phone="ewefsdf", email="asdfdsfs"))
    app.logout()