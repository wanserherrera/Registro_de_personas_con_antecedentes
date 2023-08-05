from django.forms import ModelForm
from .models import *
from django import forms
class RPenalesForm(forms.ModelForm):
    #fechasentencia = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    #idpersona = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-select"}))
    #nrodoc = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"floatingInput" }))

    #fechasentencia = forms.DateField()
    #print(type(fechasentencia).__name__)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        Char={            
            "class":"form-control"
        }
        Inte={            
            "class":"form-select"
        }

        for field in self.fields:
            #print(field) 
            #print(type(self.fields[field]).__name__)
            if type(self.fields[field]).__name__ == 'ModelChoiceField':
                self.fields[field].widget.attrs.update(Inte)
            if type(self.fields[field]).__name__ == 'CharField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'IntegerField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'DateTimeField':
                #self.fields[field] = forms.DateField()
                self.fields[field].widget.attrs.update(Char)
                self.fields[field].widget.input_type = 'datetime-local'
    
    class Meta:
        model = Rpenales
        fields = '__all__'
        exclude = ['idusercrea', 'idusermodifica', 'maqcrea', 'maqmodifica', 'activo', 'estado', 'idpersona','nrodoc']
        #widgets = {
        #    'idpersona' : forms.Select(attrs={"class":"form-select"}),
        #    'fechasentencia' : forms.DateInput(attrs={'type':'date', "class":"form-control"}),
        #    'nrodoc' : forms.TextInput(attrs={"class":"form-control","id":"floatingInput" }),
        #    'nombreepenal': forms.TextInput(attrs={"class":"form-control","id":"floatingInput" }),

        #}
    
class RFamiliaresForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        Char={            
            "class":"form-control",
           
        }
        Inte={            
            "class":"form-select"
        }

        for field in self.fields:
            if type(self.fields[field]).__name__ == 'ModelChoiceField':
                self.fields[field].widget.attrs.update(Inte)
            if type(self.fields[field]).__name__ == 'CharField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'IntegerField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'DateTimeField':
                self.fields[field].widget.attrs.update(Char)
                self.fields[field].widget.input_type = 'datetime-local'
    
    class Meta:
        model = Rfamiliares
        fields = '__all__'
        exclude = ['idusercrea', 'idusermodifica', 'maqcrea', 'maqmodifica', 'activo', 'estado', 'idpersona']

class IFFAAForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        Char={            
            "class":"form-control",
           
        }
        Inte={            
            "class":"form-select"
        }

        for field in self.fields:
            if type(self.fields[field]).__name__ == 'ModelChoiceField':
                self.fields[field].widget.attrs.update(Inte)
            if type(self.fields[field]).__name__ == 'CharField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'IntegerField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'DateTimeField':
                self.fields[field].widget.attrs.update(Char)
                self.fields[field].widget.input_type = 'datetime-local'
    
    class Meta:
        model = Iffaa
        fields = '__all__'
        exclude = ['idusercrea', 'idusermodifica', 'maqcrea', 'maqmodifica', 'activo', 'estado', 'nrodoc', 'idpersona']
        
class MsitpolicialForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        Char={            
            "class":"form-control",
           
        }
        Inte={            
            "class":"form-select"
        }

        for field in self.fields:
            if type(self.fields[field]).__name__ == 'ModelChoiceField':
                self.fields[field].widget.attrs.update(Inte)
            if type(self.fields[field]).__name__ == 'CharField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'IntegerField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'DateTimeField':
                self.fields[field].widget.attrs.update(Char)
                self.fields[field].widget.input_type = 'datetime-local'
    
    class Meta:
        model = Msitpolicial
        fields = '__all__'
        exclude = ['idusercrea', 'idusermodifica', 'maqcrea', 'maqmodifica', 'activo', 'estado']


class IpoliciaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        Char={            
            "class":"form-control",
           
        }
        Inte={            
            "class":"form-select"
        }

        for field in self.fields:
            if type(self.fields[field]).__name__ == 'ModelChoiceField':
                self.fields[field].widget.attrs.update(Inte)
            if type(self.fields[field]).__name__ == 'CharField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'IntegerField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'DateTimeField':
                self.fields[field].widget.attrs.update(Char)
                self.fields[field].widget.input_type = 'datetime-local'
    
    class Meta:
        model = Ipolicia
        fields = '__all__'
        exclude = ['idusercrea', 'idusermodifica', 'maqcrea', 'maqmodifica', 'activo', 'estado', 'nrodoc', 'idpersona']


class RfiliacionpoliticaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        Char={            
            "class":"form-control",
           
        }
        Inte={            
            "class":"form-select"
        }

        for field in self.fields:
            if type(self.fields[field]).__name__ == 'ModelChoiceField':
                self.fields[field].widget.attrs.update(Inte)
            if type(self.fields[field]).__name__ == 'CharField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'IntegerField':
                self.fields[field].widget.attrs.update(Char)
            if type(self.fields[field]).__name__ == 'DateTimeField':
                self.fields[field].widget.attrs.update(Char)
                self.fields[field].widget.input_type = 'datetime-local'
    
    class Meta:
        model = Rfiliacionpolitica
        fields = '__all__'
        exclude = ['idusercrea', 'idusermodifica', 'maqcrea', 'maqmodifica', 'activo', 'estado', 'nrodoc', 'idpersona']