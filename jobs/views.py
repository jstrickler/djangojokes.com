import html
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from common.utils.email import send_email
from .forms import JobApplicationForm

class JobAppView(FormView):
    template_name = 'jobs/joke_writer.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

    def form_valid(self, form):
        data = form.cleaned_data  # form.cleaned_data['fieldname']
        to = data['email']
        subject = 'job application'
        content = f"""
        <h1>Application Received</h1>
        <ol>
        """
        for field_name, field_data in data.items():
            label = field_name.replace('_', ' ').title()
            entry = html.escape(str(field_data), quote=False)
            content += f'<li>{label}: {entry}</li>'
        content += '</ol>'
        send_email(to, subject, content)
        return super().form_valid(form)
    

class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'

