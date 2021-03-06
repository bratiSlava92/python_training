from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create_new(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # fill new contact form
        self.fill_contact_form(contact)
        # submit new contact creation
        wd.find_element_by_xpath("(.//input[@name='submit'])[2]").click()
        self.return_to_main_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_bday_bmonth("bday", contact.bday)
        self.change_bday_bmonth("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_aday_amonth("aday", contact.aday)
        self.change_aday_amonth("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_bday_bmonth(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath("(.//option[@value='" + text + "'])").click()

    def change_aday_amonth(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath("(.//option[@value='" + text + "'])[2]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

#    def delete_first_contact(self):
#        wd = self.app.wd
#        self.open_contact_page()
#        wd.find_element_by_name("selected[]").click()
#        wd.find_element_by_xpath(".//input[@value='Delete']").click()
#        wd.switch_to_alert().accept()
#        self.return_to_main_page()
#        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath(".//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_main_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
            wd = self.app.wd
            wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            self.app.open_home_page()

#    def modify_contact(self, new_contact_data):
#        wd = self.app.wd
#        self.open_contact_page()
#        wd.find_element_by_xpath("(.//img[@alt='Edit'])").click()
#        # fill group form
#        self.fill_contact_form(new_contact_data)
#        # submit modification
#        wd.find_element_by_name("update").click()
#        self.return_to_main_page()
#        self.contact_cache = None

    def modify_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath(".//img[@alt='Edit']")[index].click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_main_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath(".//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname))
        return self.contact_cache
