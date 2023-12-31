# coding=utf-8
from django.db import models
from django.urls import reverse


class Categoria(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:category', kwargs={'slug': self.slug})


class Produto(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('Categoria', verbose_name='Categoria', null=True, on_delete=models.SET_NULL)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    image = models.ImageField(
        'Imagem', upload_to ='uploads/%Y/%m/%d/', blank=True, null=True
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('core:product', kwargs={'slug': self.slug})