from django.db import models

class users(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    mobilenum=models.IntegerField()
    emailid=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    isActive=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class expense(models.Model):
    user=models.CharField(max_length=120)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    expense_name=models.CharField(max_length=200)
    amount=models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.expense_name