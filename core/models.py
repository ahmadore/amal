from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Cause(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='cause-images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    place = models.CharField(max_length=80)
    display_image = models.ImageField(upload_to='event-images', null=True, blank=True)

    def __str__(self):
        return self.title

    def upcoming(self):
        return self.date > timezone.now()

    def passed(self):
        return self.date < timezone.now()

    @property
    def year(self):
        return self.date.year

    @property
    def month(self):
        return self.date.month - 1

    @property
    def day(self):
        return self.date.day


class ImageUpload(models.Model):
    event = models.ForeignKey(Event, related_name='images')
    image = models.ImageField(null=True, blank=True, upload_to='event-images')

    def __str__(self):
        return self.event.title + '--' + str(self.id)


class Trustee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='trustees')
    bios = models.TextField()

    def __str__(self):
        return '%s - %s' %(self.name, self.position)


class ManagementStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='trustees')
    bios = models.TextField()

    def __str__(self):
        return '%s - %s' %(self.name, self.position)
