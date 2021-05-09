from django.shortcuts import render
from tst.models import attendance, employeeOfTheMonth


def home(request):
    """
     This method is used to display home page.


     :param request: it's a HttpResponse from user.


     :type request: HttpResponse.


     :return: this method returns a home page
      which is a HTML page.


     :rtype: HttpResponse.
     """
    return render(request, 'home.html')


def ab_view(request):
    """
     This method is used to display attendance record page.


     :param request: it's a HttpResponse from user.


     :type request: HttpResponse.


     :return: this method returns a attendance record page with all the available entry
      which is a HTML page.


     :rtype: HttpResponse.
     """
    ab_view = attendance.objects.all()
    return render(request, 'ab_view.html', {'av': ab_view})


def ab_input(request):
    """
     This method is used to display attendance input page.


     :param request: it's a HttpResponse from user.


     :type request: HttpResponse.


     :return: this method returns a attendance input page where user can input attendance
      which is a HTML page.


     :rtype: HttpResponse.
     """
    return render(request, 'ab_input.html')


def input_attendance(request):
    """
        This method is used to submit the attendance into the database


        :param request: it's a HttpResponse from user.


        :type request: HttpResponse.


        :return: this method returns the attendance input page which is a html page.


        :rtype: HttpResponse.
        """

    if request.method == 'POST':
        print("This is post")
        employee_id = request.POST['employee_id']
        leave_application = request.POST['leave_application']
        open_date = request.POST['open_date']
        present = request.POST['present']

        ins_att = attendance(employee_id=employee_id, leave_application=leave_application, open_date=open_date,
                             present=present)
        ins_att.save()
        print("the data has been written to the db")

    return render(request, 'ab_input.html')


def employee_of_the_month(request):
    """
     This method is used to display employee of the month  page.


     :param request: it's a HttpResponse from user.


     :type request: HttpResponse.


     :return: this method returns a employee of the month html page  here it has two options.one is view and another
     one is rate pages.


     :rtype: HttpResponse.
     """

    return render(request, 'employee_of_the_month.html')


def attendance_page(request):
    """
     This method is used to display attendance  page.


     :param request: it's a HttpResponse from user.


     :type request: HttpResponse.


     :return: this method returns a attendance html page where it has two options.one is view and another one is input.



     :rtype: HttpResponse.
     """
    return render(request, 'attendance_page.html')


def emb_view(request):
    """
     This method is used to display EOM record page.


     :param request: it's a HttpResponse from user.


     :type request: HttpResponse.


     :return: this method returns a EOM record html page with all the available entry
      w


     :rtype: HttpResponse.
     """
    emb_view = employeeOfTheMonth.objects.all()
    return render(request, 'emb_view.html', {'emb': emb_view})


def emb_rate(request):
    """
     This method is used to display EOM rate record page.


     :param request: it's a HttpResponse from user.


     :type request: HttpResponse.


     :return: this method returns a EOM rate page
      which is a HTML page.


     :rtype: HttpResponse.
     """
    emb_rate = employeeOfTheMonth.objects.all()
    return render(request, 'emb_rate.html', {'er': emb_rate})


def emb_rate_input(request):
    """
            This method is used to submit the Employee's rating  into the database


            :param request: it's a HttpResponse from user.


            :type request: HttpResponse.


            :return: this method returns the EOM rate page which is a html page.


            :rtype: HttpResponse.
            """
    if request.method == 'POST':
        print("This is post")
        employee_id = request.POST['employee_id']
        attendance_point = request.POST['attendance_point']
        project_point = request.POST['project_point']
        attitude_point = request.POST['attitude_point']
        leadership_point = request.POST['leadership_point']
        cooperation_point = request.POST['cooperation_point']
        work_quality_point = request.POST['work_quality_point']
        date = request.POST['date']
        total_point = request.POST['total_point']

        ins_em = employeeOfTheMonth(employee_id=employee_id, attendance_point=attendance_point,
                                    project_point=project_point,
                                    attitude_point=attitude_point, work_quality_point=work_quality_point,
                                    leadership_point=leadership_point, cooperation_point=cooperation_point, date=date,
                                    total_point=total_point)
        ins_em.save()
        print("the data has been written to the db")

    return render(request, 'emb_rate.html')
