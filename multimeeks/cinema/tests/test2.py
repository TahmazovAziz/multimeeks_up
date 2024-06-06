import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestingSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_signup_fire(self):
        self.driver.get('http://127.0.0.1:8000/users/users/login/')
        self.driver.find_element(By.ID,'id_username').send_keys("test title")
        self.driver.find_element(By.ID,'id_password').send_keys("test pass")
        self.driver.find_element(By.ID,'submit').click()
        self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit        
    
if __name__ == '__main__':
    unittest.main()