from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Mission
from .models import Mission, Expense 
import jdatetime


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [ 'amount']
class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['date', 'factory']
    date = forms.CharField(
        label='تاریخ',
        widget=forms.DateInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': ' تاریخ شمسی نمونه 1403/10/10'}),
    )
    # فیلد مکان
    factory = forms.CharField(
        label='کارخانه',  # لیبل برای مکان
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کارخانه و محل ماموریت را وارد کنید'}),
    )
    def clean_date(self):
        date = self.cleaned_data.get('date')
        try:
            jdatetime.datetime.strptime(date, '%Y/%m/%d')  # اعتبارسنجی تاریخ شمسی
        except ValueError:
            raise forms.ValidationError("فرمت تاریخ وارد شده صحیح نیست.")
        return date



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'description', 'amount', 'factory']
    date = forms.CharField(
        label='تاریخ',
        widget=forms.DateInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': ' تاریخ شمسی نمونه 1403/10/10'}),
    )
    amount = forms.IntegerField(
        label='مبلغ(تومان)',
        widget=forms.NumberInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'لطفا مبلغ را وارد کنید'}),
    )
    description = forms.CharField(
        label='توضیحات',  # لیبل برای مکان
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'توضیحات'}),
    )
    factory = forms.CharField(
        label='کارخانه',  # لیبل برای مکان
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کارخانه و محل ماموریت را وارد کنید'}),
    )
    def clean_date(self):
        date = self.cleaned_data.get('date')
        try:
            jdatetime.datetime.strptime(date, '%Y/%m/%d')  # اعتبارسنجی تاریخ شمسی
        except ValueError:
            raise forms.ValidationError("فرمت تاریخ وارد شده صحیح نیست.")
        return date
      
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("مبلغ باید بزرگ‌تر از صفر باشد.")
        return amount

        
MONTH_CHOICES = [
    (1, 'فروردین'),
    (2, 'اردیبهشت'),
    (3, 'خرداد'),
    (4, 'تیر'),
    (5, 'مرداد'),
    (6, 'شهریور'),
    (7, 'مهر'),
    (8, 'آبان'),
    (9, 'آذر'),
    (10, 'دی'),
    (11, 'بهمن'),
    (12, 'اسفند'),
]

class ReportForm(forms.Form):
    month = forms.ChoiceField(choices=MONTH_CHOICES, label='ماه')