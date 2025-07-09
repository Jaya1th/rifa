from django.shortcuts import render
from .models import Employee, Course, Enrollment
from django.db.models import Count

def dashboard(request):
    selected_course = request.GET.get('course')
    selected_practice = request.GET.get('practice')
    selected_grade = request.GET.get('grade')
    selected_status = request.GET.get('status')

    enrollments = Enrollment.objects.all()

    if selected_course:
        enrollments = enrollments.filter(course_id=selected_course)
    if selected_status:
        enrollments = enrollments.filter(status=selected_status)

    employees = Employee.objects.all()
    if selected_practice:
        employees = employees.filter(practice=selected_practice)
    if selected_grade:
        employees = employees.filter(grade=selected_grade)

    employee_data = []
    for emp in employees:
        emp_enrollments = enrollments.filter(employee_id=emp.employee_id)
        for en in emp_enrollments:
            course = Course.objects.filter(course_id=en.course_id).first()
            employee_data.append({
                'employee': emp,
                'course_name': course.course_name if course else en.course_id,
                'progress': en.progress,
                'status': en.status
            })

    total_enrollments = enrollments.count()
    completed = enrollments.filter(status="Completed").count()
    not_completed = enrollments.filter(status="Not Completed").count()

    grade_wise = employees.values('grade').annotate(total=Count('grade'))
    practice_wise = employees.values('practice').annotate(total=Count('practice'))

    context = {
        'employee_data': employee_data,
        'total': total_enrollments,
        'completed': completed,
        'not_completed': not_completed,
        'grade_wise': grade_wise,
        'practice_wise': practice_wise,
        'courses': Course.objects.all(),
        'grades': Employee.objects.values_list('grade', flat=True).distinct(),
        'practices': Employee.objects.values_list('practice', flat=True).distinct(),
    }

    return render(request, 'dashboard.html', context)
