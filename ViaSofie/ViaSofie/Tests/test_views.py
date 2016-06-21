from webbrowser import browser

from django.test import TestCase
from django_selenium.livetestcases import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ViaSofieViewsTest(TestCase):
    """
    Tests voor startpagina
    """
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('panden' in resp.context)
        self.assertTrue('foto' in resp.context)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'home')

    """
    Tests voor dossierpagina
    """
    def test_dossier(self):
        resp = self.client.get('/dossiers/')
        self.assertEqual(resp.status_code, 200)

    """
    Tests voor pandenpagina
    """
    def test_panden(self):
        resp = self.client.get('/panden/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'panden')

    """
    Tests voor "over ons"-pagina
    """
    def test_about(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'about')

    """
    Tests voor contactpagina
    """
    def test_contact(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'contact')


class ViaSofieSeleniumTests(SeleniumLiveTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testMenubalk(self):
        self.browser.get('localhost:8000')
        self.browser.find_element_by_link_text("Panden").click()
        self.assertEqual(self.browser.find_element_by_class_name("active").text, "Panden")
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_link_text("Over ons").click()
        self.assertEqual(self.browser.find_element_by_class_name("active").text, "Over ons")
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_link_text("Contact").click()
        self.assertEqual(self.browser.find_element_by_class_name("active").text, "Contact")

    def testContactUsPositive(self):
        self.browser.get('localhost:8000/contact/')
        self.browser.find_element_by_name('email').send_keys('test@test.com')
        self.browser.find_element_by_name('question').send_keys('test')
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_name('sendMail').click()
        self.browser.implicitly_wait(1)
        self.assertTrue(self.browser.find_element_by_name('successAlert'))

    def testContactUsNegative(self):
        self.browser.get('localhost:8000/contact/')
        self.browser.find_element_by_name('email').send_keys('test@test.com')
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_name('sendMail').click()
        self.browser.implicitly_wait(1)
        self.assertTrue(self.browser.find_element_by_name('errorAlert'))

        self.browser.get('localhost:8000/contact/')
        self.browser.find_element_by_name('question').send_keys('test')
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_name('sendMail').click()
        self.browser.implicitly_wait(1)
        self.assertTrue(self.browser.find_element_by_name('errorAlert'))

        self.browser.get('localhost:8000/contact/')
        self.browser.find_element_by_name('email').send_keys('test.com')
        self.browser.find_element_by_name('question').send_keys('test')
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_name('sendMail').click()
        self.browser.implicitly_wait(1)
        try:
            self.assertFalse(self.browser.find_element_by_name('successAlert').is_displayed())
            raise Exception()
        except:
            self.assertTrue(True)