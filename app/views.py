from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.conf import settings
# Create your views here.
from .locations import dorm_b, room_floor
from django.views import View


def index(request):
    return render(request, "index.html", {"dicts": dorm_b})


class Navi(View):
    def get(self, request, *args):
        print(args)
        return render(request, "navi.html")

    def post(self, request):
        dorm = request.POST.get("dorm", None)
        classroom = request.POST.get("classroom", None)

        try:
            try:
                classroom = int(classroom)
            except ValueError:
                raise ValueError("教室输入非法")
            if not 0 < int(dorm) < 16:
                raise ValueError("宿舍楼号错误")
            if classroom not in room_floor:
                raise ValueError("教室号找不到")
        except ValueError as e:
            return render(request, "index.html", {"error_message": str(e), "dicts": dorm_b}, )
        print(room_floor[classroom])
        x = dorm_b[dorm]["location"][0]
        y = dorm_b[dorm]["location"][1]
        entry = ",".join(room_floor[classroom])
        return render(request, "navi.html", {"x": x, "y": y,
                                             "classroom_entry": entry})

