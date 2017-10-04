from channels.binding.websockets import WebsocketBinding
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.

class Report(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    priority = (('G', 'Green'), ('Y', 'Yellow'), ('R', 'Red'),)

    def get_absolute_url(self):
        return reverse('op:detail', kwargs={'pk': self.pk})

    # def get_absolute_url(self):
    #    return reverse('op:report-add')

    def __str__(self):
        return self.title


class ReportBinding(WebsocketBinding):
    model = Report
    stream = "intval"
    fields = ["title", "time", "category", "description"]

    @classmethod
    def group_names(cls, *args, **kwargs):
        return ["binding.op"]

    def has_permission(self, user, action, pk):
        return True
