# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Petrovich", lastname="Sidorov", nickname="nickname",
                                   title="ceo", company="sber", address="address", home_phone="8125556677",
                                   mobile_phone="89998887766", work_phone="8123334455", fax="8123344455",
                                   email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru",
                                   homepage="www.test.ru", bday="18", bmonth="July", byear="1990", aday="25", amonth="May",
                                   ayear="2008", address2="address2", phone2="home123", notes="comment")
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
