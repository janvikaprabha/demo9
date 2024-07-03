
from django.db import models
from django.urls import reverse

class Departments(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='department',blank=True)



    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'


    def get_url(self):
        return reverse('collegeapp:products_by_department',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)



class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)

    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='department',blank=True)
    seats=models.IntegerField()

    def get_url(self):
        return reverse('collegeapp:prodCatdetail',args=[self.department.slug,self.slug])


    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'


    def __str__(self):
        return '{}'.format(self.name)



class CSE(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='cse', blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='cse'
        verbose_name_plural='cses'


    def __str__(self):
        return self.name


class ICE(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='ice', blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='ice'
        verbose_name_plural='ices'


    def __str__(self):
        return self.name

class EEE(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='eee', blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='eee'
        verbose_name_plural='eee'


    def __str__(self):
        return self.name

class MECHANICAL(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='mechanical', blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='mechanical'
        verbose_name_plural='mechanical'


    def __str__(self):
        return self.name

class CIVIL(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='civil', blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='civil'
        verbose_name_plural='civil'


    def __str__(self):
        return self.name

class ECE(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='ece', blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='ece'
        verbose_name_plural='ece'


    def __str__(self):
        return self.name

