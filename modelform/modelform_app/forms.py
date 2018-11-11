from django.forms import ModelForm
from modelform_app.models import user

class newuser(ModelForm):
    class Meta:
        model=user
        fields="__all__"
        label={'name':'name','email':"Email",'v_mail':"Verify Email",'feedback':"Feedback"}
