from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
        }
