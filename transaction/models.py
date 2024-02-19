from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class userTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField( max_length=50)
    transaction_date = models.DateField(auto_now_add = True)
    amount = models.DecimalField(decimal_places=2, max_digits = 12)

    def __str__(self):
        return self.transaction_type