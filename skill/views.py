from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView
from linkedhr.models import Skill, UserProfile
from .forms import SkillForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
class SkillCreateView(SuccessMessageMixin, CreateView):
    model = Skill
    template_name = 'skill/skill_create.html'
    success_message = "Created successfully"
    fields = ['title']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        userprofiledata = UserProfile.objects.filter(user_id=request.user.id)
        if userprofiledata.count() > 0:
            for i in userprofiledata:
                if i.is_recruit == '2':
                    return super(self.__class__, self).dispatch(request, *args, **kwargs)
                else:
                    return render(request, 'error.html')
        else:
            raise Http404("Please check user log in !")
 
    def get(self, request):
        form = SkillForm()
        if request.user.is_authenticated():
            userprofiledata = UserProfile.objects.filter(user_id=request.user.id)
            if userprofiledata.count() > 0:
                for i in userprofiledata:
                    if i.is_recruit == '2':
                        data_skill = Skill.objects.filter(user_id = request.user.id)
                        if data_skill.count() < 26 :
                            args = {'form': form, 'data_skill':data_skill}
                            return render(request, self.template_name, args)
                        else:
                            return render(request, 'skill_overflow.html')
                    else:
                        return render(request, 'error.html')
            else:
                return redirect('linkedhr:userprofile')
        else:
            return redirect('linkedhr:login')

    @method_decorator(login_required)
    def post(self, request):
        form = SkillForm(request.POST)
        if request.user.is_authenticated():
            userprofiledata = UserProfile.objects.filter(user_id=request.user.id)
            if userprofiledata.count() > 0:
                for i in userprofiledata:
                    if i.is_recruit == '2':
                        if form.is_valid():
                            skill = form.save(commit=False)
                            skill.user_id = request.user
                            skill.save()
                            title = form.cleaned_data['title']
                            messages.success(request, "Created sucessfully !")

                        data_skill = Skill.objects.filter(user_id=request.user.id)
                        args = {'form': form, 'data_skill':data_skill}
                        return render(request, self.template_name, args)
                    else:
                        return render(request, 'error.html')
            else:
                return redirect('linkedhr:userprofile')

        else:
            return redirect('linkedhr:login')