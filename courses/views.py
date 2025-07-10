from django.shortcuts import render
from django.db import connections
from collections import defaultdict

def dashboard(request):
    # 1. Filters from request
    selected_course = request.GET.get('course')
    selected_practice = request.GET.get('practice')
    selected_grade = request.GET.get('grade')
    selected_status = request.GET.get('status')
    selected_region = request.GET.get('region')
    selected_pm = request.GET.get('project_manager')
    selected_dm = request.GET.get('delivery_manager')
    selected_bl = request.GET.get('business_leader')
    search_query = request.GET.get('search', '').strip().lower()

    # 2. Fetch all employees from edu_academy
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT employee_id, name, email, grade, practice, region,
                   project_manager, delivery_manager, business_leader
            FROM trainingDataHub_employeeheadcountreportdetails
        """)
        rows = cursor.fetchall()

    employees = []
    for row in rows:
        emp = {
            'employee_id': str(row[0]),
            'name': row[1],
            'email': row[2],
            'grade': row[3],
            'practice': row[4],
            'region': row[5],
            'project_manager': row[6],
            'delivery_manager': row[7],
            'business_leader': row[8],
        }

        # Search by ID, name, or email
        if search_query:
            if search_query not in emp['employee_id'].lower() and \
               search_query not in emp['name'].lower() and \
               search_query not in emp['email'].lower():
                continue

        employees.append(emp)

    # 3. Apply filters
    if selected_grade:
        employees = [e for e in employees if e['grade'] == selected_grade]
    if selected_practice:
        employees = [e for e in employees if e['practice'] == selected_practice]
    if selected_region:
        employees = [e for e in employees if e['region'] == selected_region]
    if selected_pm:
        employees = [e for e in employees if e['project_manager'] == selected_pm]
    if selected_dm:
        employees = [e for e in employees if e['delivery_manager'] == selected_dm]
    if selected_bl:
        employees = [e for e in employees if e['business_leader'] == selected_bl]

    # 4. Fetch enrollments from openedx
    with connections['openedx'].cursor() as cursor:
        cursor.execute("""
            SELECT user_id, course_id, progress, employee_id
            FROM student_courseenrollment
        """)
        course_rows = cursor.fetchall()

    enrollments_by_emp = defaultdict(list)
    for row in course_rows:
        emp_id = str(row[3])
        enrollments_by_emp[emp_id].append({
            'course_id': row[1],
            'progress': row[2],
            'status': 'Completed' if row[2] == 100 else 'Not Completed'
        })

    # 5. Combine employees + enrollments
    employee_data = []
    for emp in employees:
        emp_id = emp['employee_id']
        for enroll in enrollments_by_emp.get(emp_id, []):
            if selected_status and enroll['status'] != selected_status:
                continue
            if selected_course and enroll['course_id'] != selected_course:
                continue

            employee_data.append({
                'employee': emp,
                'course_name': enroll['course_id'],
                'progress': enroll['progress'],
                'status': enroll['status']
            })

    # 6. Stats
    total_enrollments = len(employee_data)
    completed = sum(1 for e in employee_data if e['status'] == 'Completed')
    not_completed = total_enrollments - completed

    # 7. Dropdown filter data
    grades = sorted(set(e['grade'] for e in employees))
    practices = sorted(set(e['practice'] for e in employees))
    regions = sorted(set(e['region'] for e in employees))
    project_managers = sorted(set(e['project_manager'] for e in employees))
    delivery_managers = sorted(set(e['delivery_manager'] for e in employees))
    business_leaders = sorted(set(e['business_leader'] for e in employees))
    all_courses = sorted(set(enroll['course_id']
                             for emp_list in enrollments_by_emp.values()
                             for enroll in emp_list))

    # 8. Grade-wise and Practice-wise summary
    grade_wise = [{'grade': g, 'total': sum(1 for e in employees if e['grade'] == g)} for g in grades]
    practice_wise = [{'practice': p, 'total': sum(1 for e in employees if e['practice'] == p)} for p in practices]

    # 9. Final context
    context = {
        'employee_data': employee_data,
        'total': total_enrollments,
        'completed': completed,
        'not_completed': not_completed,
        'grades': grades,
        'practices': practices,
        'regions': regions,
        'project_managers': project_managers,
        'delivery_managers': delivery_managers,
        'business_leaders': business_leaders,
        'courses': all_courses,
        'statuses': ['Completed', 'Not Completed'],
        'grade_wise': grade_wise,
        'practice_wise': practice_wise,
        'selected_course': selected_course,
        'selected_practice': selected_practice,
        'selected_grade': selected_grade,
        'selected_status': selected_status,
        'selected_region': selected_region,
        'selected_pm': selected_pm,
        'selected_dm': selected_dm,
        'selected_bl': selected_bl,
        'search_query': request.GET.get('search', ''),
    }

    return render(request, 'ai_course_dashboard/dashboard.html', context)
