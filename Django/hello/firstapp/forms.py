from django import forms


class UserForm(forms.Form):
	
	name = forms.CharField(label = "Имя",
	initial='Noname',
	help_text='Введите свое имя')
	
	age = forms.IntegerField(label="Возраст",
	initial='18',
	min_value = 18,
	max_value = 70,
	help_text='Введите свой возраст',
	required=False)

	email = forms.EmailField(required=False)
	field_order = ["name","age","email"]

class UserForm2(forms.Form):
	name = forms.CharField(min_length = 3)
	age = forms.IntegerField(min_value=1, max_value=100)
	required_css_class = "field"
	error_css_class = "error"

