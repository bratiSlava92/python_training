from model.contact import Contact
from random import randrange


def test_delete_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create_new(
            Contact(firstname="Ivan", middlename="Petrovich", lastname="Sidorov", nickname="nickname",
                    title="ceo", company="sber", address="address", home_phone="8125556677",
                    mobile_phone="89998887766", work_phone="8123334455", fax="8123344455",
                    email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru",
                    homepage="www.test.ru", bday="18", bmonth="July", byear="1990", aday="25", amonth="May",
                    ayear="2008", address2="address2", phone2="home123", notes="comment"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts


# def test_delete_first_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create_new(
#            Contact(firstname="Ivan", middlename="Petrovich", lastname="Sidorov", nickname="nickname",
#                    title="ceo", company="sber", address="address", home_phone="8125556677",
#                    mobile_phone="89998887766", work_phone="8123334455", fax="8123344455",
#                    email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru",
#                    homepage="www.test.ru", bday="18", bmonth="July", byear="1990", aday="25", amonth="May",
#                    ayear="2008", address2="address2", phone2="home123", notes="comment"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.delete_first_contact()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[0:1] = []
#    assert old_contacts == new_contacts
