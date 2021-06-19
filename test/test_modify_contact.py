from model.contact import Contact


def test_modify_main_contact_data(app):
    app.contact.modify_contact(Contact(firstname="Имя", middlename="Отчество", lastname="Фамилия", address="изменен",
                                       mobile_phone="89998887766", email="test@mail.ru", bday="4", bmonth="April", byear="1990"))
