from django.db import models
from courses.models import Course
from django.shortcuts import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    course = models.ManyToManyField(Course, related_name='students')

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"