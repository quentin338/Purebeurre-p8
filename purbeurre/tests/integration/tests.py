from selenium import webdriver

from django.test import LiveServerTestCase


class AccountTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        self.selenium = webdriver.Chrome()
        self.selenium.implicitly_wait(5)
        super(AccountTestCase, self).setUp()

    def tearDown(self) -> None:
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_existing_user_can_login(self):
        self.selenium.get("http://127.0.0.1:8000/users/login")

        email = self.selenium.find_element_by_id("id_email")
        password = self.selenium.find_element_by_id("id_password")

        self.assertIn("Se connecter", self.selenium.title)

        email.send_keys("test@test.com")
        password.send_keys("test")

        submit_button = self.selenium.find_element_by_css_selector("input.btn-light")
        submit_button.click()

        self.selenium.find_element_by_class_name("fa-sign-out")

        self.assertIn("users/logout/", self.selenium.page_source)
