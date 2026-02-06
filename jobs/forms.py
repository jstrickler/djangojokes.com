from datetime import date
from django import forms
from django.core.exceptions import ValidationError

# from .validators import my_other_validator

def validate_future_date(value):
    if value < date.today():
        raise ValidationError(message=f"{value} is in the past", code="past_date")

class JobApplicationForm(forms.Form):
    EMPLOYMENT_TYPES = (
        (None, '--Please Choose--'),
        ('ft', 'Full-time'),
        ('pt', 'Part-time'),
    )

    DAYS = (
        (1, 'Mon'),
        (2, 'Tue'),
        (3, 'Wed'),
        (4, 'Thu'),
        (5, 'Fri'),
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()

    email = forms.EmailField()

    website = forms.URLField(
        required=False,
        widget = forms.URLInput(attrs={'placeholder': 'https://www.example.com'})
    )

    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPES)

    this_year = date.today().year
    years_range = [this_year, this_year + 1]
    start_date = forms.DateField(
        help_text="The earliest date you can start",
        widget = forms.SelectDateWidget(
            attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'},
            years=years_range,
            empty_label=('choose year', 'choose month', 'choose day'),
        ),
        validators=[validate_future_date],
    )
    available_days = forms.TypedMultipleChoiceField(
        choices = DAYS,
        coerce=int,
        help_text = 'select all days you can work',
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked': True},
        ),
    )
    desired_hourly_wage = forms.DecimalField(
        min_value=10,
        max_value=100,
        widget=forms.NumberInput(attrs={'step': '0.25'}),
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols':'75', 'rows': '8'},
        )
    )
    confirmation = forms.BooleanField(
        label='I certify that the info I provided is true',
    )