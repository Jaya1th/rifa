from django.shortcuts import render
from django.db.models import Q
from collections import defaultdict
from .models import CourseProgress, AuthUser  # OpenEdx models
from trainingDataHub.models import EmployeeMaster, EmployeeHeadCountReportDetails  # Custom models


def ai_course_dashboard(request):
    selected_course_id = request.GET.get('course')
    selected_practice = request.GET.get('practice')
    selected_grade = request.GET.get('grade')
    selected_status = request.GET.get('status')

    # -- 1. Filter employee emails by practice
    emp_master_email = EmployeeMaster.objects.filter(
        practice=selected_practice
    ).values_list('email_id', flat=True)

    # -- 2. Get employee details by grade
    emp_headcount_qs = EmployeeHeadCountReportDetails.objects.filter(
        grade_text=selected_grade,
        email_id__in=emp_master_email
    ).values(
        'emp_id', 'emp_name', 'email_id', 'grade_text', 'delivery_manager_name',
        'business_lead_name', 'project_manager_name', 'personal_sub_area'
    )

    # -- 3. Get Auth Users (from openedx)
    auth_users = AuthUser.objects.using('openedx').filter(
        email__in=emp_master_email
    ).values('id', 'email')

    auth_user_id_map = {u['email']: u['id'] for u in auth_users}

    # -- 4. Get course progress
    course_data = CourseProgress.objects.using('openedx').filter(
        courseid=selected_course_id,
        userid__in=auth_user_id_map.values()
    ).values('userid', 'courseid', 'course_progress')

    # -- 5. Merge employee data with course progress
    employee_data = []
    for emp in emp_headcount_qs:
        user_id = auth_user_id_map.get(emp['email_id'])
        emp_courses = [c for c in course_data if c['userid'] == user_id]

        for course in emp_courses:
            status = "Completed" if course['course_progress'] == 100 else "Not Completed"
            if selected_status and selected_status != status:
                continue
            employee_data.append({
                'employee': emp,
                'course_name': course['courseid'],
                'progress': course['course_progress'],
                'status': status
            })

    # -- 6. Summary Stats
    total = len(employee_data)
    completed = sum(1 for e in employee_data if e['status'] == 'Completed')
    not_completed = total - completed
    completion_rate = int((completed / total) * 100) if total > 0 else 0

    # -- 7. Dropdown options
    practices = EmployeeMaster.objects.values_list('practice', flat=True).distinct()
    grades = EmployeeHeadCountReportDetails.objects.values_list('grade_text', flat=True).distinct()
    courses = CourseProgress.objects.using('openedx').values_list('courseid', flat=True).distinct()

    context = {
        'employee_data': employee_data,
        'total': total,
        'completed': completed,
        'not_completed': not_completed,
        'completion_rate': completion_rate,
        'grades': grades,
        'practices': practices,
        'courses': courses,
        'selected_grade': selected_grade,
        'selected_practice': selected_practice,
        'selected_course': selected_course_id,
        'selected_status': selected_status,
    }

    return render(request, 'ai_course_dashboard/dashboard.html', context)
