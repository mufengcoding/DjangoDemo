from django.db import models

# Create your models here.


class Student(models.Model):
    SEX_ITEMS = [
        (1, 'boy'),
        (2, 'girl'),
        (0, 'unknow'),
    ]
    STATUS_ITEMS = [
        (0, 'apply'),
        (1, 'pass'),
        (2, 'refuse')
    ]
    name = models.CharField(max_length=128, verbose_name='name')
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='sex')
    profession = models.CharField(max_length=128, verbose_name='job')
    email = models.EmailField(verbose_name='email')
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='phone')

    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='check_status')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created_time')

    @property
    def sex_show(self):
        return dict(self.SEX_ITEMS)[self.sex]

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = 'student_info'
