from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label=_('ایمیل')
    )

    # error_messages = {
    #     'password_mismatch': _("دو رمز عبور وارد شده باهم مطابقت ندارند."),
    #
    # }

    # username = forms.CharField(
    #     label=_('نام کاربری'),
    #     help_text=_('150 حرف یا کمتر . فقط حروف و @/./+/-/_ .'),
    # )

    # password1 = forms.CharField(
    #     label=_("رمز عبور"),
    #     widget=forms.PasswordInput
    # )
    # password2 = forms.CharField(
    #     label=_("تایید رمز عبور"),
    #     widget=forms.PasswordInput,
    #     help_text=_("برای تایید ، همان رمز عبور بالا را وارد کنید")
    # )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label=_('نام کاربری'))
    email = forms.EmailField(
        label=_('ایمیل')
    )

    class Meta:
        model = User
        fields = [
            'email',
            'username'
        ]


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label=_('تصویر')
    )

    class Meta:
        model = Profile
        fields = [
            'image',
        ]
