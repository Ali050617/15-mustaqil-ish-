from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from courses.models import Course
from django.contrib import messages


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)


def student_create(request):
    courses = Course.objects.all()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        course_id = request.POST.getlist('course')

        if first_name and last_name and email and phone_number and course_id:
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
            )
            student.course.set(course_id)
            return redirect('students:student_list')
    ctx = {'courses': courses}
    return render(request, 'students/student-create.html', ctx)


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        course = request.POST.get('course')
        if first_name and last_name and email and phone_number and course:
            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            student.phone_number = phone_number
            student.course = course
            student.save()
            return redirect(student.get_detail_url())
    ctx = {'student': student}
    return render(request, 'students/student-create.html', ctx)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)


def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('students:student_list')
    ctx = {'student': student}
    return render(request, 'students/student-delete-confirm.html', ctx)