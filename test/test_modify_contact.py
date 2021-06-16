from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Имя", middlename="Отчество", lastname="Фамилия", nickname="nickname",
                                   title="ceo", company="sber", address="изменен", home_phone="8125556677",
                                   mobile_phone="89998887766", work_phone="8123334455", fax="8123344455", email="test@mail.ru",
                                   email2="test2@mail.ru", email3="test3@mail.ru", homepage="www.test.ru",
                                   address2="address2", phone2="home123", notes="comment"))
    app.session.logout()