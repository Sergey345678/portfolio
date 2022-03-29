from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, LoginForm, ReviewForm, NailMasterForm, AppointmentsForm
from .models import NailMaster, Review, Appointments


def index(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form': form})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            print(form.errors)
        return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()
        return render(request, "form.html", {"form": form})


def logout_user(request):
    logout(request)
    return HttpResponse('Logged out')


def nail_master_list(request):
    nail_masters = NailMaster.objects.all()
    return render(request, 'nail_master_list.html', {'nail_masters': nail_masters})


def nail_master_review_list(request, nail_master_id):
    reviews = Review.objects.filter(nail_master=nail_master_id)
    nail_master = get_object_or_404(NailMaster, pk=nail_master_id)
    return render(request, 'nail_master_review_list.html', {'reviews': reviews, 'nail_master': nail_master})


@login_required
def add_nail_master(request):
    if request.method == 'POST':
        form = NailMasterForm(request.POST)
        if form.is_valid():
            nail_master = NailMaster.objects.create(**form.cleaned_data)
            return redirect('nail_master_review_list', nail_master.id)
    else:
        form = NailMasterForm()
        return render(request, 'form.html', {'form': form})


@login_required
def add_review(request, nail_master_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            nail_master = get_object_or_404(NailMaster, pk=nail_master_id)
            Review.objects.create(nail_master=nail_master, user=user, **form.cleaned_data)
            return redirect('nail_master_review_list', nail_master.id)
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})


@login_required
def user_appointments(request):
    appointments = Appointments.objects.filter(user=request.user)
    return render(request, 'user_appointments.html', {'appointments': appointments})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    if review.user == user:
        review.delete()
        return redirect('nail_master_review_list', review.nail_master.id)
    return HttpResponse('You can delete only your reviews!')


@login_required
def edit_review(request, review_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            review = get_object_or_404(Review, pk=review_id)
            if review.user == user:
                review.text = form.cleaned_data["text"]
                review.save()
                return redirect('nail_master_review_list', review.nail_master.id)
            return HttpResponse('You can edit only your reviews!')
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})


@login_required
def add_appointment(request, nail_master_id):
    if request.method == 'POST':
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            user = request.user
            nail_master = get_object_or_404(NailMaster, pk=nail_master_id)
            Appointments.objects.create(nail_master=nail_master, user=user, **form.cleaned_data)
            return redirect('user_appointments')
    else:
        form = AppointmentsForm()
        return render(request, 'form.html', {'form': form})
