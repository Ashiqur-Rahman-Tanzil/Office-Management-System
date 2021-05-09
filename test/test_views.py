from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse('home')
        self.employee_of_the_month = reverse('employee_of_the_month')
        self.attendance_page = reverse('attendance_page')
        self.emb_view = reverse('emb_view')
        self.emb_rate = reverse('emb_rate')
        self.ab_view = reverse('ab_view')
        self.input_attendance = reverse('input_attendance')
        self.emb_rate_input = reverse('emb_rate_input')

    def test_emb_view(self):
        response = self.client.get(reverse('emb_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emb_view.html')

    def test_emb_rate(self):
        response = self.client.get(reverse('emb_rate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emb_rate.html')

    def test_ab_view(self):
        response = self.client.get(reverse('ab_view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ab_view.html')

    def test_input_attendance(self):
        response = self.client.post('/input_attendance/', {
            'employee_id=': '111',
            'leave_application': 'n',
            'open_date': '05/06/2022',
            'present': '1'

        })

        response.status_code

    def test_emb_rate_input(self):
        response = self.client.post('/emb_rate_input/', {
            'employee_id=': '111',
            'attendance_point': '1',
            'date': '05/06/2022',
            'project _point': '1',
            'attitude_point': '1',
            'work_quality_point': '1',
            'leadership_point': '1',
            'cooperation_point': '2',
            'total_point': '2'

        })

        response.status_code

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_employee_of_the_month(self):
        response = self.client.get(reverse('employee_of_the_month'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee_of_the_month.html')

    def test_attendance_page(self):
        response = self.client.get(reverse('attendance_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'attendance_page.html')

    def test_attendance_page(self):
        response = self.client.get(reverse('attendance_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'attendance_page.html')


if __name__ == '__main__':
    TestViews()
