from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(
            Contact(firstname="Ivan", middlename="Petrovich", lastname="Sidorov", nickname="nickname",
                    title="ceo", company="sber", address="address", home_phone="8125556677",
                    mobile_phone="89998887766", work_phone="8123334455", fax="8123344455",
                    email="test@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru",
                    homepage="www.test.ru", bday="18", bmonth="July", byear="1990", aday="25", amonth="May",
                    ayear="2008", address2="address2", phone2="home123", notes="comment"))
    app.contact.delete_first_contact()
