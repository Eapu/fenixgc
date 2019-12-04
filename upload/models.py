from django.db import models

TOTEM_CHOICES= [
	('La_Cilla', 'Mirador de La Cilla'),
	('Galaz', 'Mesas de Galaz'),
	('Fuente_Fria', 'Fuente Fría'),
	('Montaña_Pajaritos', 'Montaña Pajaritos'),
	('Doña Paca', 'Doña Pacas'),
	('Mirador_de_Tejeda', 'Mirador de Tejeda'),
	('Cuevas_del_Caballero', 'Cuevas_del_Caballero'),
	('Las_Hoyas', 'Las Hoyas'),
	('Acusa', 'Acusa'),
	('Degollada_del_Sargento', 'Degollada del Sargento'),
	('Lugarejos', 'Lugarejos'),
	('Degollada_del_Humo', 'Degollada del Humo'),
	('Cruz de María', 'Cruz de María'),
	('Área Recreativa Tamadaba', 'Área Recreativa Tamadaba'),
	('Fin del Mundo', 'Fin del Mundo'),

	]
class Usuarios(models.Model):
	user = models.CharField(max_length=10, blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	upload = models.FileField()
	totem = models.CharField(max_length=50, choices=TOTEM_CHOICES, default='Mirador de La Cilla')

	class Meta:
		verbose_name_plural = 'Usuarios'

	def __str__(self):
		return self.user

