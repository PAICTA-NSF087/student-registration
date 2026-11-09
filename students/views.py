from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def student_list(request):
    query = request.GET.get('q', '')
    students = Student.objects.all().order_by('last_name')
  
    if query:
        students = students.filter(
            Q(student_number__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )

    return render(request, 'students/student_list.html', {
        'students': students,
        'query': query,
    })

def student_create(request):
    form =  StudentForm(request.POST  or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Register Student',
    })

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)

    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student',
    })

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_comfirm_delete.html', {
        'student': student,
    })