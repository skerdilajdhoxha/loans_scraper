from django.db import models


class Loan(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    loan_url = models.CharField(max_length=256, blank=True, null=True)
    signature_date = models.CharField(max_length=256, blank=True, null=True)
    signed_amount = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    country_url = models.CharField(max_length=256, blank=True, null=True)
    sector = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()
