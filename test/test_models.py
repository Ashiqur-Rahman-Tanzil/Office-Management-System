from django.test import TestCase, Client
from tst.models import attendance, employeeOfTheMonth, employee


class TestModel(TestCase):
    def test_attendance(self):
        b = attendance.objects.create(employee_id='111', leave_application='n', open_date='2021-05-02',
                                      present='1')

        self.assertEqual(str(b), '111')

    def test_employee_of_the_month(self):
        a = employeeOfTheMonth.objects.create(employee_id='111', attendance_point='2', project_point='2',
                                              attitude_point='1', work_quality_point='1',
                                              leadership_point='5', cooperation_point='6', total_point=0,
                                              date='2021-05-02')

        self.assertEqual(str(a), '111')

    def test_employee(self):
        c = employee(employee_id='222', user_name='zahid', user_password='234234', dept_name='R&D')

        self.assertEqual(str(c), '222')


if __name__ == '__main__':
    TestModel()