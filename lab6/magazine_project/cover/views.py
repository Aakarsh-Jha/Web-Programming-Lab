from django.shortcuts import render

def index(request):
    context = {}
    if request.method == "POST":
        message = request.POST.get("message")
        bg_color = request.POST.get("bg_color")
        font_size = request.POST.get("font_size")
        font_color = request.POST.get("font_color")
        image_url = request.POST.get("image_url")

        context = {
            "message": message,
            "bg_color": bg_color,
            "font_size": font_size,
            "font_color": font_color,
            "image_url": image_url,
        }
    return render(request, "cover/index.html", context)
