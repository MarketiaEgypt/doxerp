from settings.models import Setting


def my_data(request):
    my_data = Setting.objects.last()
    return {'my_data': my_data}