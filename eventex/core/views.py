from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from eventex.core.models import Speaker, Talk


class GenericHomeView(TemplateResponseMixin, View):
    object_list = None
    context_object_name = None

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = {self.context_object_name: self.object_list}
        context.update(kwargs)
        return context


class HomeView(GenericHomeView):
    template_name = 'index.html'
    object_list = Speaker.objects.all()
    context_object_name = 'speakers'


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }

    return render(request, 'core/talk_list.html', context)
