from django.test import TestCase

# Create your views  tests here.


class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")


class AboutViewTest(TestCase):
    def test_about_view(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
