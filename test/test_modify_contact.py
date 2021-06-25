from model.contact import Contact


def test_modify_main_contact_data(app):
    if app.contact.count() == 0:
        app.contact.create_new(
            Contact(firstname="Ivan", middlename="Petrovich", lastname="Sidorov", nickname="nickname",
                    title="ceo", company="sber", address="address", home_phone="8125556677",
                    mobile_phone="89998887766", work_phone="8123334455", fax="8123344455",
                    email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru",
                    homepage="www.test.ru", bday="18", bmonth="July", byear="1993", aday="25", amonth="May",
                    ayear="2008", address2="address2", phone2="home123", notes="comment"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Имя", middlename="Отчество", lastname="Фамилия", address="изменен",
                                       mobile_phone="89998887766", email="test@mail.ru", bday="4", bmonth="April", byear="1990")
    contact.id = old_contacts[0].id
    app.contact.modify_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
