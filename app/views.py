from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.views import View


def index(request):
    return render(request, "index.html", {"dicts": settings.LOCATIONS})


class Navi(View):
    def get(self, request):
        return render(request, "navi.html")

    def post(self, request):
        try:
            dorm = request.POST.get("dorm", None)
            classroom = request.POST.get("classroom", None)
            if not 0 < int(dorm) < 16:
                raise ValueError("FUCK")

            # classroom = int(classroom)

        except Exception:
            return HttpResponse("表单验证失败，检查表单项")

        return HttpResponseRedirect("/navi/?x={}&y={}".format(settings.LOCATIONS[dorm]["location"][0],
                                                              settings.LOCATIONS[dorm]["location"][1]))
