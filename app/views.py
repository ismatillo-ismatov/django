from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views import generic
from .models import *
from .form import LeadForm,LeadModelForm


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def leanding_page(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request,'landing.html',context)

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request,'leads/lead_list.html',context)


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }

    return render(request,'leads/lead_detail.html',context)


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class =  LeadModelForm
    def get_success_url(self):
        return "app:list"

def create_lead(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/app")
    context = {
        "form":form
    }
    return render(request,"leads/lead_create.html",context)


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse('app:update')

def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("/app")
    context = {
        "lead":lead,
        "form":form
    }
    return render(request, "leads/lead_update.html",context)


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("app:list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/app")

# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form":form,
#         "lead":lead
#     }
#     return render(request,"leads/lead_update.html",context)
