from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Student, Course, Result
from django.contrib import messages
from datetime import date

#Home page
def home(request):
    content={
        "variable1": Student.objects.all().count(),
        "variable2": Course.objects.all().count(),
        "variable3": Result.objects.all().count()
    }
    return render(request, "home.html", content)

#Add Student Page
def addstudent(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        family_name = request.POST.get('familyname')
        full_name = first_name + ' ' + family_name
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        student=Student(first_name=first_name, family_name=family_name, full_name=full_name, dob=dob, email=email)
        student.save()
        messages.success(request, "Student is added Successfully !!")    
    return render(request, "addstudent.html")

#List Student Page
def liststudent(request):
    return render(request, "liststudent.html",{
        "students": Student.objects.all()
    })

#Add Course Page
def addcourse(request):
    if request.method == 'POST':
        course_name = request.POST.get('coursename')
        course=Course(course_name=course_name)
        course.save()
        messages.success(request, "Course is added Successfully !!")
    return render(request, "addcourse.html")
 
#List Course Page
def listcourse(request):
    return render(request, "listcourse.html",{
        "courses": Course.objects.all()
    })

#Add Result Page
def addresult(request):
    if request.method == 'POST':
        course_selected_name = request.POST.get('c_selected')
        full_selected_name = request.POST.get('s_selected')
        score = request.POST.get('score_selected')
        result=Result(course_selected_name=course_selected_name, full_selected_name=full_selected_name, score=score )
        result.save()
        messages.success(request, "Result is added Successfully !!")
        return render(request, "addresult.html",{
        "s_s_s": Student.objects.values("full_name"),
        "c_c": Course.objects.values("course_name")
        })
    else:
        return render(request, "addresult.html",{
        "s_s_s": Student.objects.values("full_name"),
        "c_c": Course.objects.values("course_name")
        })

#List Result Page
def listresult(request):
    return render(request, "listresult.html",{
        "results": Result.objects.all(), 
        "full_selected_name":Student.objects.values("full_name"),
        "course_selected_name":Course.objects.values("course_name")
    })

#Delete Button in Student List
def delete_student(request, id):
    student =Student.objects.get(id=id)
    student.delete()
    return redirect("liststudent")

#Delete Button in Course List
def delete_course(request, id):
    course =Course.objects.get(id=id)
    course.delete()
    return redirect("listcourse")