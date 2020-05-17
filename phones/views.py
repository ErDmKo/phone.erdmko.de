from django.views import generic as views
from django.shortcuts import redirect
from django.urls import reverse

from phones import forms as phonesForms
from phones import models as phonesModels

import logging

logger = logging.getLogger(__name__)

class PhoneView(views.edit.FormView):
    template_name = 'phones/phone_detail.html'
    form_class = phonesForms.TrustForm

    def setup(self, *arg, **kw):
        res = super().setup(*arg, **kw)
        self.obj = phonesModels.Phone.objects.get(
            pk=self.kwargs.get('pk')
        )
        questionObj = phonesModels.TrustQuestion.objects
        if questionObj.filter(
            phone=self.obj
        ).count():
            self.question = questionObj.get(
                phone=self.obj
            )
        else:
            self.question = questionObj.create(
                phone=self.obj,
                yes=0,
                no=0
            )
        return res

    def form_valid(self, form):
        trusInfo = form.cleaned_data['trust']
        if trusInfo == '0':
            self.question.no += 1
        else:
            self.question.yes += 1
        self.question.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'phone-detail',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.obj
        context['question'] = self.question
        return context

class PhoneForm(views.edit.FormView):
    template_name = 'phones/phone.html'
    phone_field = 'number'
    form_class = phonesForms.PhoneForm

    def get_form_kwargs(self):
        initial = super().get_form_kwargs()
        phone = self.request.POST.get(self.phone_field)
        if phone:
            hasOldDate = phonesModels.Phone.objects.filter(
                number=phone
            )[:1]
            if hasOldDate.count():
                instance =  hasOldDate[0]
                initial['instance'] = instance
        return initial

    def form_valid(self, form):
        instance = form.save()
        return redirect('phone-detail', pk=instance.pk)
