from django.urls import reverse_lazy


class RegisterOrLoginMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return reverse_lazy('book_list')
