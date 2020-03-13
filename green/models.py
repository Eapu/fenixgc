from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):

	def get_queryset(self):
		return super(PublishedManager, self).get_queryset()\
				.filter(status='published')


class La_Cilla(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'La_Cilla'

	def __str__(self):
		return self.title
class Degollada_del_Humo(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Degollada_del_Humo'

	def __str__(self):
		return self.title


class Acusa(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Acusa'

	def __str__(self):
		return self.title


class Tejeda(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Tejeda'

	def __str__(self):
		return self.title


class Lugarejos(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Lugarejos'

	def __str__(self):
		return self.title

class Las_Hoyas(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Las_Hoyas'

	def __str__(self):
		return self.title

class Tamadaba(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Tamadaba'

	def __str__(self):
		return self.title

class Degollada_del_Sargento(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Degollada_del_Sargento'

	def __str__(self):
		return self.title
class Fin_del_Mundo(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Fin_del_Mundo'

	def __str__(self):
		return self.title
class Cruz_de_Maria(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Cruz_de_Maria'

	def __str__(self):
		return self.title
class Cuevas_del_Caballero(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Cuevas_del_Caballero'

	def __str__(self):
		return self.title

class Fuentefria(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Fuentefria'

	def __str__(self):
		return self.title
class Cueva_Corcho(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Cueva Corcho'

	def __str__(self):
		return self.title

class Doña_Paca(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Doña Paca'

	def __str__(self):
		return self.title
class Galaz(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Galaz'

	def __str__(self):
		return self.title
class Pajaritos(models.Model):

	STATUS_CHOICES = (
			('draft', 'Draft'),
			('published', 'Published'),
			)

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	author = models.CharField(max_length=20,null=True, blank=True)
	image = models.FileField(null=True, blank=True)
	link = models.URLField(blank=True, null=True)
	place = models.TextField(max_length=20,null=True, blank=True)
	body = RichTextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="published")
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )
	class Meta:
		verbose_name_plural = 'Pajaritos'

	def __str__(self):
		return self.title

