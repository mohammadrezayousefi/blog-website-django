from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('کاربر'))
    image = models.ImageField(_('تصویر'), default='defult.jpg', upload_to='profile-pics')

    def __str__(self):
        return f' پروفایل {self.user.username}'

    def save(self , *args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        else:
            img.save(self.image.path)
