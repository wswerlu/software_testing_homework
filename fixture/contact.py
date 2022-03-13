from model.contact import Contact


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
        self.change_field_name("home", contact.home_phone)
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
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init first contact editing
        wd.find_element_by_css_selector("[alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

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
                phone = element.find_element_by_css_selector("td:nth-child(5)").text
                email = element.find_element_by_css_selector("td:nth-child(6)").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address,
                                                  home_phone=phone, email=email, id=id))
        return list(self.contact_cache)
