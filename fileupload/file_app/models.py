from django.db import models

# Create your models here.
# from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    description = models.TextField()
    chegirma = models.IntegerField(default=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return self.product_name
