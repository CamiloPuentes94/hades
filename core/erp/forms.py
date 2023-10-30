from django.forms import *

from core.erp.models import Category


class CategoryForm(ModelForm):

    # de esta manera podemos cambiar los atributos del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        # columnas del formulario
        fields = '__all__'
        widgets = {
            'name': TextInput(
                # de esta manera se puede colocar atributos
                attrs= {
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    # 'autocomplete': 'off'
                }
            ),
            'desc': Textarea(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    # 'autocomplete': 'off',
                    'rows': 3,
                    'cols': 3
                }
            )
        }
