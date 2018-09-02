from django import forms

class ToDoform(forms.Form):
    text = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={'class': 'form-control' ,'placeholder' : 'Enter ToDo List' ,'aria-label' : 'ToDo','aria-describedby':'add-btn'}
    ))
