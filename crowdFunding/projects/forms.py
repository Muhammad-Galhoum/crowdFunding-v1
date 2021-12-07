from django import forms
from .models import Project, ProjectPicture


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'target','start_date', 'end_date', 'category', 'tags']

    def clean(self): # this for check that end date must me greater than start date
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date <= start_date:
            msg = "The end date should be greater than start date."
            self._errors["end_date"] = self.error_class([msg])


class ImageForm(forms.ModelForm):
    class Meta:
        model = ProjectPicture
        fields = ['img_url']

