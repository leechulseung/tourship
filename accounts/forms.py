from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from .models import Country, Local,Profile
from news.models import Post

COUNTRY_CHOICES = ()
LOCAL_CHOICES = ()

GENDER_CHOICES = (
    ('남성','남성'),
    ('여성','여성'),
    )

POST_PRIVACY_CHOICES = ()

for country in Country.objects.all():
    COUNTRY_CHOICES += (country.id , country.name),

for local in Local.objects.all():
    LOCAL_CHOICES += (local.id, local.name),

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=
        forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'email@tourpin.com',
            })   
        )
    password = forms.CharField(widget=
        forms.PasswordInput(attrs={
            'class' : 'form-control',
            }))

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    address= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    country= forms.ChoiceField(choices=COUNTRY_CHOICES, widget= forms.Select(attrs={
        'class':'form-control col-3 mb-2 mb-sm-0 ml-3 mr-2',
        }))
    local= forms.ChoiceField(choices=LOCAL_CHOICES, widget= forms.Select(attrs={
        'class':'form-control col-3 mb-2 mb-sm-0 mr-0',
        }))

    birthdate= forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        }))
    gender= forms.ChoiceField(choices=GENDER_CHOICES, widget= forms.Select(attrs={
        'class':'form-control mb-2 mb-sm-0 ml-3 mr-2',
        }))

    phone_num= forms.CharField(max_length=11, widget= forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'01012345678'
        }))

    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name',)
        widgets ={
            'username': forms.EmailInput(attrs={
                'class':'form-control',
                "placeholder": "이메일을 입력하세요"
                }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'이름을 입력해 주세요.'
                })
        }

    def save(self):
        user = super().save()
        profile = Profile.objects.create(user=user, 
            phone_num=self.cleaned_data['phone_num'],
            address=self.cleaned_data['address'],
            country= Country.objects.get(id=self.cleaned_data['country']),
            local= Local.objects.get(id=self.cleaned_data['local']),
            gender= self.cleaned_data['gender'],
            birthdate = self.cleaned_data['birthdate'],
            )
        return user

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['country','local','address','title','tourdate','photo','content','privacy']

        widgets={
            'local': forms.Select(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control px-0','placeholder':'상세주소'}),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'제목을 입력하세요.'}),
            'tourdate': forms.TextInput(attrs={'class':'form-control','placeholder':'20170623'}),
            'content': forms.Textarea(attrs={'class':'form-control','placeholder':'내용을 입력하세요.'}),
            'privacy': forms.Select(attrs={'class':'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class':'form-control','multiple':True})
        }

class CheckForm(forms.Form):
    username = forms.CharField(widget=
        forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'email@tourpin.com',
            })   
        )
    password = forms.CharField(widget=
        forms.PasswordInput(attrs={
            'class' : 'form-control',
            }))

    def __init__(self, user,*args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username == self.user.username:
            raise forms.ValidationError("아이디가 틀렸습니다.")
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not self.user.check_password(password):
            raise forms.ValidationError("비밀번호가 틀립니다.")
        return password

class SetupForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetupForm, self).__init__(*args, **kwargs)

    currentPassword = forms.CharField(
            label='현재 비밀번호',
            widget=forms.PasswordInput(attrs={
                'class':'form-control',
                }),required=False,
            )  
    newPassword1 = forms.CharField(
            label='새로운 비밀번호',
            widget=forms.PasswordInput(attrs={
                'class':'form-control',
                }),
            required=False,
            )
    newPassword2 = forms.CharField(
            label='새로운 비밀번호(확인용)',
            widget=forms.PasswordInput(attrs={
                'class':'form-control'
                }),
            required=False,
            )
    address= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})
        ,required=False,)
    country= forms.ChoiceField(choices=COUNTRY_CHOICES, widget= forms.Select(attrs={
        'class':'form-control col-3 mb-2 mb-sm-0 ml-3 mr-2',
        }),required=False,)
    local= forms.ChoiceField(choices=LOCAL_CHOICES, widget= forms.Select(attrs={
        'class':'form-control col-3 mb-2 mb-sm-0 mr-0',
        }),required=False,)
    phone_num= forms.CharField(max_length=11, widget= forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'01012345678'
        }),required=False,)

    def clean_currentPassword(self):
        """
        Validates that the old_password field is correct.
        """
        if self.cleaned_data['currentPassword']:
            currentPassword = self.cleaned_data["currentPassword"]
            if not self.user.check_password(currentPassword):
                raise forms.ValidationError("현재 비밀번호가 틀립니다.")
            return currentPassword

    def clean_newPassword2(self):

        if self.cleaned_data['newPassword2']:
            if not self.cleaned_data['currentPassword']:
                raise forms.ValidationError("현재 비밀번호를 입력해 주세요.")
                
        password1 = self.cleaned_data.get('newPassword1')
        password2 = self.cleaned_data.get('newPassword2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("두 비밀번호가 다릅니다.")
        return password2

    def save(self, commit=True):
        if self.cleaned_data['currentPassword']:    
            password = self.cleaned_data["newPassword2"]
            self.user.set_password(password)
            if commit:
                self.user.save()

        if self.cleaned_data['address']:
            self.user.profile.address = self.cleaned_data['address']
            self.user.profile.country = Country.objects.get(id=self.cleaned_data['country'])
            self.user.profile.local = Local.objects.get(id=self.cleaned_data['local'])
            if commit:
                self.user.profile.save()

        if self.cleaned_data['phone_num']:    
            self.user.profile.phone_num = self.cleaned_data['phone_num']
            if commit:
                self.user.profile.save()
        
        return self.user
