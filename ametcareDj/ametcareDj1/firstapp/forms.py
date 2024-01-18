from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'registration-form-input'}),
        label='ФИ пользователя:'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'registration-form-input'}),
        label='Email:'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'registration-form-input'}),
        label='Пароль:'
    )
class UserInfo(forms.Form):
    GENDER_CHOICES = (("male", "Мужской"), ("female", "Женский"))
    TASK_CHOICES = (("lose-w", "Похудение"), ("up-w", "Набор массы"), ("n-w", "Поддержание формы"))

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'registration-form'}),
        label="Пол:"
    )
    weight = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'registration-form-input'}),
        label='Вес:'
    )
    height = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'registration-form-input'}),
        label='Рост:'
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'registration-form-input'}),
        label='Возраст:'
    )
    task = forms.ChoiceField(
        choices=TASK_CHOICES,
        widget=forms.Select(attrs={'class': 'registration-form-input'}),
        label="Цель:"
    )

from django import forms

class PreferencesForm(forms.Form):
    PREFERENCES_CHOICES = [
        ("Хлебобулочные изделия", "Хлебобулочные изделия"),
        ("Кисломолочная продукция", "Кисломолочная продукция"),
        ("Сладкие блюда", "Сладкие блюда"),
        ("Острые блюда", "Острые блюда"),
        ("Овощные блюда", "Овощные блюда"),
        ("Морепродукты", "Морепродукты"),
        ("Мясные блюда", "Мясные блюда"),
        ("Жареные блюда", "Жареные блюда"),
        ("Блюда на пару", "Блюда на пару"),
        ("Итальянская кухня", "Итальянская кухня"),
        ("Японская кухня", "Японская кухня"),
        ("Французская кухня", "Французская кухня"),
        ("Китайская кухня", "Китайская кухня"),
        ("Мексиканская кухня", "Мексиканская кухня"),
        ("Индонезийская кухня", "Индонезийская кухня"),
        ("Испанская кухня", "Испанская кухня"),
    ]

    preferences = forms.MultipleChoiceField(
        choices=PREFERENCES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'check_input'}),
        required=False,

    )

class AllergyForm(forms.Form):
    ALLERGIES_CHOICES = [
        ("Яблоки", "Яблоки"),
        ("Глютен", "Глютен"),
        ("Лактоза", "Лактоза"),
        ("Морепродукты", "Морепродукты"),
        ("Соя", "Соя"),
        ("Яйцо", "Яйцо"),
        ("Орехи", "Орехи"),
    ]

    allergies = forms.MultipleChoiceField(
        choices=ALLERGIES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'check_input'}),
    )
