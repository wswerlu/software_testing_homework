from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select
import time


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_name("firstname", contact.firstname)
        self.change_field_name("lastname", contact.lastname)
        self.change_field_name("address", contact.address)
        self.change_field_name("home", contact.homephone)
        self.change_field_name("email", contact.email)

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init add creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        # select contact
        wd.find_element_by_css_selector(f'input[value="{id}"]').click()
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to.alert.accept()
        time.sleep(1)
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # init contact editing
        wd.find_elements_by_css_selector("[alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        # init contact editing
        wd.find_element_by_xpath(f"//a[contains(@href, '{id}')]/img[@alt='Edit']").click()

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # open contact details
        wd.find_elements_by_css_selector("[alt='Details']")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_contact_if_it_not_exist(self, contact):
        wd = self.app.wd
        if self.count() == 0:
            self.create(contact)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_from_details_page(self, index):
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def clear(self, string):
        return re.sub("[.() /-]", "", string)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobilephone,
                                            contact.workphone, contact.secondaryphone]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

    def add_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(contact_id)
        self.select_group_by_id_for_add_contact(group_id)
        # submit adding
        wd.find_element_by_css_selector("[value='Add to']").click()
        self.go_to_group_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'input[value="{id}"]').click()

    def select_group_by_id_for_add_contact(self, id):
        wd = self.app.wd
        Select(wd.find_element_by_name("to_group")).select_by_value(id)

    def go_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[contains(text(), "group page ")]').click()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_group_by_id_for_delete_contact(group_id)
        self.select_contact_by_id(contact_id)
        # submit adding
        wd.find_element_by_name("remove").click()
        self.go_to_group_page()
        self.contact_cache = None

    def select_group_by_id_for_delete_contact(self, id):
        wd = self.app.wd
        Select(wd.find_element_by_name("group")).select_by_value(id)
