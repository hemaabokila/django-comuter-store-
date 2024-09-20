from django.db import models

LAPTOPS_TYPES=(
    ("deel","dell"),
    ("hp","hp"),
    ("aseer","aseer"),
    ("mack","mack"),
)
# Create your models here.
class laptops(models.Model):
    model=models.CharField(max_length=30)
    type=models.CharField(max_length=20,choices=LAPTOPS_TYPES)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=800)
    publishd_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    # image=models.ImageField()
    def __str__(self):
        return self.model
