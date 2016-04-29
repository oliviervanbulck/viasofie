from django.test import TestCase


class ViaSofieViewsTest(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('panden' in resp.context)
        self.assertTrue('foto' in resp.context)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'home')

    def test_dossier(self):
        resp = self.client.get('/dossiers/')
        self.assertEqual(resp.status_code, 200)

    def test_panden(self):
        resp = self.client.get('/panden/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'panden')

    def test_about(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'about')

    def test_contact(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'contact')

    def test_services(self):
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('nbar' in resp.context)
        self.assertEqual(resp.context['nbar'], 'contact')