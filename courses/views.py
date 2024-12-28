from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from students.models import Student


def home(request):
    ctx = {
        'courses_count': Course.objects.count(),
        'student_count': Student.objects.count()
    }
    return render(request,'index.html', ctx)


def course_list(request):
    courses = Course.objects.all()
    ctx = {'courses': courses}
    return render(request, 'courses/course-list.html', ctx)


def courses_create(request):
    students = Student.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        max_students = request.POST.get('max_students')
        if name and description and duration and price and max_students:
            try:
                duration = int(duration)
                price = float(price)
                max_students = int(max_students)

                Course.objects.create(
                    name=name,
                    description=description,
                    duration=duration,
                    price=price,
                    max_students=max_students
                )
                return redirect('courses:courses_list')
            except ValueError:
                error_message = 'Please enter valid numbers for duration, price, and max students.'
                ctx = {'students': students, 'error': error_message}
                return render(request, 'courses/course-create.html', ctx)
    ctx = {'students': students}
    return render(request, 'courses/course-create.html', ctx)


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = Student.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        max_students = request.POST.get('max_students')

        if name and description and duration and price and max_students:
            try:
                course.name = name
                course.description = description
                course.duration = int(duration)
                course.price = float(price)
                course.max_students = int(max_students)
                course.save()
                return redirect('courses:courses_list')
            except ValueError:
                error_message = 'Please enter valid numbers for duration, price, and max students.'
                ctx = {'course': course, 'students': students, 'error': error_message}
                return render(request, 'courses/course-update.html', ctx)

    ctx = {'course': course, 'students': students}
    return render(request, 'courses/course-update.html', ctx)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    ctx = {'course': course}
    return render(request, 'courses/course-detail.html', ctx)


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('courses:courses_list')
    ctx = {'course': course}
    return render(request, 'courses/course_confirm_delete.html', ctx)