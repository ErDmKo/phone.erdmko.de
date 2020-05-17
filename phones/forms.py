import re
from phones import models as phoneModels
from django import forms

clearPhoneRegex = re.compile(r'[^\d+]')

yesNo = (
    (0, 'Нет'),
    (1, 'Да'),
)

class TrustForm(forms.Form):
    trust = forms.ChoiceField(
        label = 'Тем кто звонил с этого номера можно доверять?',
        widget=forms.RadioSelect,
        choices=yesNo
    )

class PhoneForm(forms.ModelForm):

    def clean_number(self):
        phone = clearPhoneRegex.sub('', self.cleaned_data['number'])
        if len(phone) < 3:
            raise forms.ValidationError('Слишком короткий номер')
        if len(phone) > 10:
            raise forms.ValidationError('Слишком длинный номер')
        return phone

    class Meta:
        model = phoneModels.Phone
        fields = ['number']
