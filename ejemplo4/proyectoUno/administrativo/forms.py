from django.forms import ModelForm
from administrativo.models import Estudiante, Pais 


class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula', 'pais'] 




