from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm,
                    UserUpdateForm,
                    ProfileUpdateForm,
                    )
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'اکانت برای{username} ساخته شد میتوانید با وارد کردن اطلاعات کاربری خود ، به حساب خود وارد شوید.  '
                             )
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html', )


def profile(request):
    if request.POST:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'اطلاعات کاربری بروزرسانی شد.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
