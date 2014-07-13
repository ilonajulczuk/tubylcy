from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class FormHelperViewMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-8'
        helper.add_input(Submit('submit', 'Submit'))

        context['helper'] = helper
        return context