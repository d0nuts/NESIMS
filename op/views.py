from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Report


# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'op/index.html'

    def get_queryset(self):
        return Report.objects.order_by("-id")


class ReportCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Report
    fields = ['title', 'category', 'location', 'description']
    success_message = "%(title)s was created successfully"
    success_url = reverse_lazy('op:report-add')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )


class ReportDelete(LoginRequiredMixin, DeleteView):
    model = Report
    success_url = reverse_lazy('op:index')


# class DetailView(LoginRequiredMixin, generic.DetailView):
#     model = Report
#     template_name = 'op/detail.html'

def updateDetails(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request, 'op/detail.html', {'report': report, 'pk': pk})

def delete(request, pk):
    report = get_object_or_404(Report, pk=pk)


    report.delete()
    #return render(request, 'op/index.html')
    return HttpResponseRedirect(reverse('op:index'))