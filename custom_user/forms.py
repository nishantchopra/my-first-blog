from django import forms
from custom_user.models import AuthUser



import re
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.ModelForm):       
        password = forms.CharField(widget=forms.PasswordInput())
        confirm_password = forms.CharField(widget=forms.PasswordInput())
        
        class Meta:
                model= AuthUser
                fields = ('first_name','username','email','password')


        def clean(self):
                cleaned_data=super(RegistrationForm,self).clean()
                data=cleaned_data.get('password')
                data1=cleaned_data.get('confirm_password')
                if data!=data1:
                        self.add_error('confirm_password',"password doesn't match")






                # def is_valid(self):
       #         valid=super(RegistrationForm,self).is_valid()
       #         password1 = self.cleaned_data.get('password')
       #         password2 = self.cleaned_data.get('confirm_password')
       #         if valid and password1==password2:
       #                 return True
       #         else:
       #                 self.add_error('password',"password doesn't match")
                        
