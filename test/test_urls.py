from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tst.views import home, emb_view, emb_rate, attendance_page, ab_view, ab_input, input_attendance, \
    employee_of_the_month, emb_rate_input


class TestUrls(SimpleTestCase):
    def test_home_urls_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_attendance_page_urls_is_resolved(self):
        url = reverse('attendance_page')
        print(resolve(url))
        self.assertEqual(resolve(url).func, attendance_page)

    def test_ab_view_urls_is_resolved(self):
        url = reverse('ab_view')
        print(resolve(url))
        self.assertEqual(resolve(url).func, ab_view)

    def test_ab_input_urls_is_resolved(self):
        url = reverse('ab_input')
        print(resolve(url))
        self.assertEqual(resolve(url).func, ab_input)

    def test_input_attendance_urls_is_resolved(self):
        url = reverse('input_attendance')
        print(resolve(url))
        self.assertEqual(resolve(url).func, input_attendance)

    def test_employee_of_the_month_urls_is_resolved(self):
        url = reverse('employee_of_the_month')
        print(resolve(url))
        self.assertEqual(resolve(url).func, employee_of_the_month)

    def test_emb_view_urls_is_resolved(self):
        url = reverse('emb_view')
        print(resolve(url))
        self.assertEqual(resolve(url).func, emb_view)

    def test_emb_rate_urls_is_resolved(self):
        url = reverse('emb_rate')
        print(resolve(url))
        self.assertEqual(resolve(url).func, emb_rate)

    def test_emb_rate_input_urls_is_resolved(self):
        url = reverse('emb_rate_input')
        print(resolve(url))
        self.assertEqual(resolve(url).func, emb_rate_input)


if __name__ == '__main__':
    TestUrls()
