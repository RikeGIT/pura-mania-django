from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(
        label="Usuário",
        error_messages={
            'required': 'Campo obrigatório.'
        }
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        error_messages={
            'required': 'Campo obrigatório.',
            'invalid': 'Informe um email válido.'
        }
    )

    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        help_text="Sua senha deve ter pelo menos 8 caracteres.",
        error_messages={
            'required': 'Campo obrigatório.'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Nome de usuário em uso")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError("A senha deve conter pelo menos 8 caracteres.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
