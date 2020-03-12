from django.forms import ModelForm
from django import forms

from .models import Usuarios
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
	('No estoy seguro', 'No estoy seguro'),
	]
class UsuariosForm(forms.ModelForm):
	user = forms.CharField(max_length=10,label='Nombre', help_text='')
	totem= forms.CharField(widget=forms.Select(choices=TOTEM_CHOICES), help_text='Seleciona el totem en el que te encuentres.')
	upload = forms.FileField(widget=forms.FileInput(),label='Imagen', help_text='Sube la foto!')
	email = forms.CharField(required=False,max_length=10,label='Email (Participa en nuestro sorteo)', help_text='Envíanos tu mail si quieres participar en el sorteo de material Fenix!')

	class Meta:
		model = Usuarios
		fields = ('user','totem','upload')
		labels = {
			'user': ('Nombre'),
			'totem': ('totem'),
			'upload': ('imagen'),
			'email': ('email'),

		 }
		


