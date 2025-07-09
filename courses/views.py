from django.shortcuts import render
from django.db import connections
from collections import defaultdict

def dashboard(request):
    selected_course = request.GET.get('course')
    selected_practice = request.GET.get('practice')
    selected_grade = request.GET.get('grade')
    selected_status = request.GET.get('status')

    # 1. Get Employee Info from eduacademy DB
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT employee_id, name, email, grade, practice, region,
                   project_manager, delivery_manager, business_leader
            FROM trainingDataHub_employeeheadcountreportdetails;
        """)
        rows = cursor.fetchall()

    employees = []
    for row in rows:
        employees.append({
            'employee_id': str(row[0]),
            'name': row[1],
            'email': row[2],
            'grade': row[3],
            'practice': row[4],
            'region': row[5],
            'project_manager': row[6],
            'delivery_manager': row[7],
            'business_leader': row[8]
        })

    # 2. Apply Employee Filters
    if selected_grade:
        employees = [e for e in employees if e['grade'] == selected_grade]
    if selected_practice:
        employees = [e for e in employees if e['practice'] == selected_practice]

    # 3. Get Enrollments from openedx DB
    with connections['openedx'].cursor() as cursor:
        cursor.execute("""
            SELECT user_id, course_id, progress, employee_id
            FROM student_courseenrollment;
        """)
        course_rows = cursor.fetchall()

    enrollments = defaultdict(list)
    for row in course_rows:
        emp_id = str(row[3])
        enrollments[emp_id].append({
            'course_id': row[1],
            'progress': row[2],
            'status': 'Completed' if row[2] == 100 else 'Not Completed'
        })

    # 4. Apply Status and Course Filters
    employee_data = []
    for emp in employees:
        for enroll in enrollments.get(emp['employee_id'], []):
            if selected_status and enroll['status'] != selected_status:
                continue
            if selected_course and enroll['course_id'] != selected_course:
                continue

            employee_data.append({
                'employee': emp,
                'course_name': enroll['course_id'],  # No lookup from Course table
                'progress': enroll['progress'],
                'status': enroll['status']
            })

    # 5. Count Stats
    total_enrollments = len(employee_data)
    completed = sum(1 for e in employee_data if e['status'] == 'Completed')
    not_completed = total_enrollments - completed

    # 6. For Dropdown Filters
    grades = sorted(set(e['grade'] for e in employees))
    practices = sorted(set(e['practice'] for e in employees))
    courses = sorted(set(enroll['course_id'] for enroll_list in enrollments.values() for enroll in enroll_list))

    # 7. Context
    context = {
        'employee_data': employee_data,
        'total': total_enrollments,
        'completed': completed,
        'not_completed': not_completed,
        'grade_wise': [{'grade': g, 'total': sum(1 for e in employees if e['grade'] == g)} for g in grades],
        'practice_wise': [{'practice': p, 'total': sum(1 for e in employees if e['practice'] == p)} for p in practices],
        'grades': grades,
        'practices': practices,
        'courses': courses
    }

    return render(request, 'ai_course_dashboard/dashboard.html', context)
