from django.shortcuts import render
from django.db import connections
from collections import defaultdict
from .models import *
from trainingDataHub.models import EmployeeMaster, EmployeeHeadCountReportDetails
def ai_course_dashboard(request):
    selected_course_id = request.GET.get('course')
    selected_practice = request.GET.get('practice')
    selected_grade = request.GET.get('grade')
    selected_status = request.GET.get('status')

  

       
    emp_master_email=EmployeeMaster.objects.filter(practice=selected_practice).values( 'email_id')
    emp_hedcount_obj = EmployeeHeadCountReportDetails.objects.filter(grade__in=selected_grade).values('emp_id','emp_name','email_id','grade_text','delivery_manager_name','business_lead_name','project_manager_name',' personal_sub_area')
    course_data= CourseProgress.objects.using('openedx').filter(courseid__in=selected_course_id).values('course_id','course_progress','user_id ')
    auth_user = AuthUser.objects.using('openedx').filter(email=emp_master_email).values('id')
    employee_enrolled_data=course_data.filter(userid__in=auth_user)
