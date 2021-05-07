from django.db import models


class employee(models.Model):#didnt use this one.
    """
       This class is extended from the Model class so it has all the functionality
       of the model class.

       this class used to create objects for database entry
       """
    employee_id = models.IntegerField(primary_key=True)
    user_password = models.CharField(max_length=40)
    user_name = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=200)

    def __str__(self):
        return self.employee_id


class employeeOfTheMonth(models.Model):
    """
          This class is extended from the Model class so it has all the functionality
          of the model class.

          this class used to create objects for database entry
          """
    employee_id = models.IntegerField()
    attendance_point = models.IntegerField()
    project_point = models.IntegerField()
    attitude_point = models.IntegerField()
    work_quality_point = models.IntegerField()
    leadership_point = models.IntegerField()
    cooperation_point = models.IntegerField()
    total_point = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.employee_id


class attendance(models.Model):
    """
          This class is extended from the Model class so it has all the functionality
          of the model class.

          this class used to create objects for database entry
          """
    employee_id = models.IntegerField()
    leave_application = models.TextField()
    open_date = models.DateField("today's date")
    present = models.IntegerField()

    def __str__(self):
        return self.employee_id
