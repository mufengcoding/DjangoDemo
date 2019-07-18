from django import forms

from .models import Student

# 方法一
# class StudentForm(forms.Form):
#     name = forms.CharField(label='name', max_length=128)
#     sex = forms.ChoiceField(label='sex', choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='profession', max_length=128)
#     email = forms.EmailField(label='email', max_length=128)
#     qq = forms.CharField(label='qq', max_length=128)
#     phone = forms.CharField(label='phone', max_length=128)
#

# 方法二


class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('must be number！')
        return int(cleaned_data)
    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'phone', 'qq'
        )
