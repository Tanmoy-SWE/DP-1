from django.forms import ModelForm
from .models import Course
 
class CourseForm(ModelForm):
   class Meta:
       model = Course
       fields = ['Course_code', 'Course_name', 'total_credit', 'desc']
