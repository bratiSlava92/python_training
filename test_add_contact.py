# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Ivan", middlename="Petrovich", lastname="Sidorov", nickname="nickname",
                                   title="ceo", company="sber", address="address", home_phone="8125556677",
                                   mobile_phone="89998887766", work_phone="8123334455", fax="8123344455", email="test@mail.ru",
                                   email2="test2@mail.ru", email3="test3@mail.ru", homepage="www.test.ru",
                                   address2="address2", phone2="home123", notes="comment"))
    app.logout()
