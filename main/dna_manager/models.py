from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class DNASample(models.Model):
    sample = models.TextField(blank=False, null=False)
    is_mutant = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.sample


class Stats(models.Model):
    mutant_samples = models.IntegerField(blank=False, null=False)
    human_samples = models.IntegerField(blank=False, null=False)
    ratio = models.FloatField(blank=False, null=False)


# method for updating
@receiver(post_save, sender=DNASample)
def update_stock(sender, instance, **kwargs):
    previous_stat = Stats.objects.all().first()
    human_sample = 1 if not instance.is_mutant else 0
    mutant_sample = 1 if instance.is_mutant else 0
    if previous_stat is not None:
        previous_stat.human_samples += human_sample
        previous_stat.mutant_samples += mutant_sample
        previous_stat.ratio = min(previous_stat.human_samples,
                                  previous_stat.mutant_samples)/max(previous_stat.mutant_samples,
                                                                    previous_stat.human_samples)
        previous_stat.ratio = round(previous_stat.ratio, 2)
        previous_stat.save()
    else:
        Stats.objects.create(mutant_samples=mutant_sample, human_samples=human_sample, ratio=0)
