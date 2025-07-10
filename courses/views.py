import json
from django.shortcuts import render
from django.db import connections
from collections import defaultdict


def build_tree(employees, enrollments_by_emp):
    tree = {}
    for emp in employees:
        emp_id = emp['employee_id']
        progress_list = enrollments_by_emp.get(emp_id, [])
        avg_progress = int(sum(e['progress'] for e in progress_list) / len(progress_list)) if progress_list else 0

        # Setup roles
        bl = emp['business_leader']
        dm = emp['delivery_manager']
        pm = emp['project_manager']

        if bl not in tree:
            tree[bl] = {
                "id": f"BL_{bl}",
                "name": bl,
                "role": "Business Leader",
                "practice": "All",
                "completion": "N/A",
                "children": {}
            }

        if dm not in tree[bl]["children"]:
            tree[bl]["children"][dm] = {
                "id": f"DM_{dm}",
                "name": dm,
                "role": "Delivery Manager",
                "practice": emp['practice'],
                "completion": "N/A",
                "children": {}
            }

        if pm not in tree[bl]["children"][dm]["children"]:
            tree[bl]["children"][dm]["children"][pm] = {
                "id": f"PM_{pm}",
                "name": pm,
                "role": "Project Manager",
                "practice": emp['practice'],
                "completion": "N/A",
                "children": []
            }

        tree[bl]["children"][dm]["children"][pm]["children"].append({
            "id": emp_id,
            "name": emp['name'],
            "role": "Employee",
            "practice": emp['practice'],
            "completion": f"{avg_progress}%",
            "children": []
        })

    # Convert nested dicts to nested lists
    tree_list = []
    for bl in tree.values():
        bl_children = []
        for dm in bl["children"].values():
            dm_children = []
            for pm in dm["children"].values():
                dm_children.append(pm)
            dm["children"] = dm_children
            bl_children.append(dm)
        bl["children"] = bl_children
        tree_list.append(bl)

    return tree_list


def dashboard(request):
    # Filters
    selected_course = request.GET.get('course')
    selected_practice = request.GET.get('practice')
    selected_grade = request.GET.get('grade')
    selected_status = request.GET.get('status')

    # 1. Fetch Employees
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT employee_id, name, email, grade, practice, region,
                   project_manager, delivery_manager, business_leader
            FROM trainingdatahub_employeeheadcountreportdetails
        """)
        rows = cursor.fetchall()

    employees = [{
        'employee_id': str(row[0]),
        'name': row[1],
        'email': row[2],
        'grade': row[3],
        'practice': row[4],
        'region': row[5],
        'project_manager': row[6],
        'delivery_manager': row[7],
        'business_leader': row[8],
    } for row in rows]

    # Apply filters
    if selected_grade:
        employees = [e for e in employees if e['grade'] == selected_grade]
    if selected_practice:
        employees = [e for e in employees if e['practice'] == selected_practice]

    # 2. Fetch Enrollments
    with connections['openedx'].cursor() as cursor:
        cursor.execute("""
            SELECT user_id, course_id, progress, employee_id
            FROM student_courseenrollment
        """)
        enrollments_raw = cursor.fetchall()

    enrollments_by_emp = defaultdict(list)
    for row in enrollments_raw:
        emp_id = str(row[3])
        enroll = {
            'course_id': row[1],
            'progress': row[2],
            'status': 'Completed' if row[2] == 100 else 'Not Completed'
        }

        # filter inside loop
        if selected_course and enroll['course_id'] != selected_course:
            continue
        if selected_status and enroll['status'] != selected_status:
            continue

        enrollments_by_emp[emp_id].append(enroll)

    # 3. Merge for flat list
    employee_data = []
    for emp in employees:
        for enroll in enrollments_by_emp.get(emp['employee_id'], []):
            employee_data.append({
                'employee': emp,
                'course_name': enroll['course_id'],
                'progress': enroll['progress'],
                'status': enroll['status']
            })

    # 4. Summary Stats
    total = len(employee_data)
    completed = sum(1 for e in employee_data if e['status'] == 'Completed')
    not_completed = total - completed
    completion_rate = int((completed / total) * 100) if total > 0 else 0

    # 5. Chart Data
    course_stats = defaultdict(lambda: {'completed': 0, 'total': 0})
    for e in employee_data:
        c = e['course_name']
        course_stats[c]['total'] += 1
        if e['status'] == 'Completed':
            course_stats[c]['completed'] += 1

    course_labels = list(course_stats.keys())
    course_completion_rates = [
        int((data['completed'] / data['total']) * 100) if data['total'] > 0 else 0
        for data in course_stats.values()
    ]

    chart_data = {
        'course_labels': course_labels,
        'course_rates': course_completion_rates,
    }

    # 6. Tree View Data
    tree_view_data = build_tree(employees, enrollments_by_emp)

    # 7. Dropdown filters
    grades = sorted(set(e['grade'] for e in employees))
    practices = sorted(set(e['practice'] for e in employees))
    all_courses = sorted(set(e['course_name'] for e in employee_data))

    context = {
        'employee_data': employee_data,
        'total': total,
        'completed': completed,
        'not_completed': not_completed,
        'completion_rate': completion_rate,
        'grades': grades,
        'practices': practices,
        'courses': all_courses,
        'selected_grade': selected_grade,
        'selected_practice': selected_practice,
        'selected_course': selected_course,
        'selected_status': selected_status,
        'chart_data': json.dumps(chart_data),
        'tree_view_data': json.dumps(tree_view_data),
    }

    return render(request, 'ai_course_dashboard/dashboard.html', context)
