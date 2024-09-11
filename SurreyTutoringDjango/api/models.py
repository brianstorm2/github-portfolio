from django.db import models

# Create your models here.
class price_list(models.Model):
    one_on_one = models.DecimalField(max_digits=5, decimal_places=2, default=25.00)
    two_on_one = models.DecimalField(max_digits=5, decimal_places=2, default=35.00)
    three_on_one = models.DecimalField(max_digits=5, decimal_places=2, default=45.00)

    def __str__(self):
        return f"Price List (1-on-1: £{self.one_on_one}, 2-on-1: £{self.two_on_one}, 3-on-1: £{self.three_on_one})"