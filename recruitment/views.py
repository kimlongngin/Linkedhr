from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView
from linkedhr.models import Recruitment, UserProfile

from .forms import RecruitmentForm
#from linkedhr.forms import ExperienceForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User


class RecruitmentUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Recruitment
    form_class = RecruitmentForm
    template_name = 'recruitment_update.html'
    fields = ['company', 'branch', 'title', 'position', 'sub_position', 'salary', 'number_of_employee',
              'experience', 'start_date', 'due_date', 'email', 'phone_number', 'address', 'description']
    success_message = "Recruitment was updated successfully"

    def get_form(self):
        return RecruitmentForm(self.request.user.id, **self.get_form_kwargs())

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        chUpd = get_object_or_404(Recruitment, id = self.kwargs['pk'], is_status=True)
        #chUpd = Recruitment.objects .get(id = self.kwargs['pk'], is_status=True)
        if chUpd.count_update > 0:
            return render(request, "update_error.html")

        userprofile_data = UserProfile.objects.filter(user_id=self.request.user.id, is_status=True)
        for i in userprofile_data:
            if userprofile_data.count() > 0:
                if i.is_recruit == "1":
                    return super(self.__class__, self).dispatch(request, *args, **kwargs)
                else:
                    return render(request, "document/error.html")
            else:
                return render(request, "document/error.html")

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = RecruitmentForm(request.user.id)
        chUpd = get_object_or_404(Recruitment, id=self.kwargs['pk'], is_status=True)
        # chUpd = Recruitment.objects .get(id = self.kwargs['pk'], is_status=True)
        if chUpd.count_update > 0:
            return render(request, "update_error.html")


        userprofile_data = UserProfile.objects.filter(user_id=self.request.user.id, is_status=True)
        if userprofile_data.count() > 0:
            for i in userprofile_data:
                if i.is_recruit == "1":
                    self.object = self.get_object()
                    return super(RecruitmentUpdateView, self).get(request, *args, **kwargs)
                else:
                    return render(request, "document/error.html")
        else:
            return render(request, "document/error.html")

    def get_success_url(self):
        if self.kwargs['pk']:
            Recruitment.objects.filter(id = self.kwargs['pk']).update(count_update=1)
            # return reverse_lazy('linkedhr:recruitment-update', kwargs={'pk': self.kwargs['pk']})
            return reverse_lazy('linkedhr:myuserprofile_without_pk')
        raise Http404("Please check user login.")

class RecruitmentCreateView(SuccessMessageMixin, generic.CreateView):
    model = Recruitment
    form_class = RecruitmentForm
    template_name = 'recruiment_create.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # Br = get_object_or_404(Branch, id = self.kwargs['pk'], is_status=True)
        userprofile_data = UserProfile.objects.filter(user_id=self.request.user.id, is_status=True)
        for i in userprofile_data:
            if userprofile_data.count() > 0:
                if i.is_recruit == "1":
                    return super(self.__class__, self).dispatch(request, *args, **kwargs)
                else:
                    return render(request, "document/error.html")
            else:
                return render(request, "document/error.html")

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = RecruitmentForm(request.user.id)
        userprofile_data = UserProfile.objects.filter(user_id=self.request.user.id, is_status=True)
        if userprofile_data.count() > 0:
            for i in userprofile_data:
                if i.is_recruit == "1":
                    return render(request, self.template_name, {'form': form})
                else:
                    return render(request, "document/error.html")
        else:
                return render(request, "document/error.html")

    @method_decorator(login_required)
    def post(self, request):
        form = RecruitmentForm(self.request.user, request.POST)
        userprofiledata = UserProfile.objects.filter(user_id=request.user.id)

        if userprofiledata.count() > 0:
            for i in userprofiledata:
                if i.is_recruit == '1':
                    if form.is_valid():
                        recruitment = form.save(commit=False)
                        recruitment.user_id = request.user
                        recruitment.save()
                        company = form.cleaned_data['company']
                        branch = form.cleaned_data['branch']
                        position = form.cleaned_data['position']
                        title = form.cleaned_data['title']
                        sub_position = form.cleaned_data['sub_position']
                        salary = form.cleaned_data['salary']
                        number_of_employee = form.cleaned_data['number_of_employee']
                        experience = form.cleaned_data['experience']
                        start_date = form.cleaned_data['start_date']
                        due_date = form.cleaned_data['due_date']
                        email = form.cleaned_data['email']
                        phone_number = form.cleaned_data['phone_number']
                        address = form.cleaned_data['address']
                        description = form.cleaned_data['description']
                        job_type = form.cleaned_data['job_type']

                        messages.success(request, "Created sucessfully !")
                    args = {'form': form}
                    return render(request, self.template_name, args)
                else:
                    return render(request, 'error.html')

        else:
            return redirect('linkedhr:login')