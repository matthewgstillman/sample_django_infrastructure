from django.shortcuts import render


def index(request):
    return render(request, 'newMI2020/index.html')


def courses(request):
    return render(request, 'newMI2020/courses.html')


def jobs(request):
    return render(request, 'newMI2020/jobs.html')


def iotdevelopers(request):
    return render(request, 'newMI2020/iotdevelopers.html')


def courseinfo(request):
    return render(request, 'newMI2020/courseinfo.html')
