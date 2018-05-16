from django.forms.widgets import TextInput

class DateInput(TextInput):
    input_type = 'date'

class PasswordInput(TextInput):
    input_type = 'password'