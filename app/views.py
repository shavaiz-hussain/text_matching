from django.conf import settings
from django.shortcuts import HttpResponse, render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from throttle.decorators import throttle

from app.models import Key, Value

from .levenshtein import levenshtein_ratio_and_distance


@throttle(zone="default")
@csrf_exempt
def index(request):
    keys = Key.objects.all()
    if request.method == "GET":
        return render(request, "home.html", context={"keys": keys})
    elif request.method == "POST":
        results = []
        select_key = request.POST.get("key-list")
        if select_key:
            for value in Value.objects.values_list("name", flat=True):
                if value != "":
                    percentage = levenshtein_ratio_and_distance(value, select_key)
                    if percentage > settings.MATCHING_PERCENTAGE:
                        results.append({"value": value, "percentage": percentage})
        return render(
            request,
            "home.html",
            context={"keys": keys, "results": results, "selected_key": select_key},
        )
