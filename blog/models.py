from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(_('موضوع'), max_length=100)
    content = models.TextField(_('محتوا'))
    date_posted = models.DateTimeField(_('تاریخ انتشار'), default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('نویسنده'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
