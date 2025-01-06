from django.db import models
from django.shortcuts import reverse
from courses.base_models import BaseModel


class Course(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_students = models.PositiveIntegerField()

    def get_detail_url(self):
        return reverse('courses:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('courses:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('courses:delete', args=[self.pk])

    def __str__(self):
        return self.name


