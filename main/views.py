from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406395335',
        'name': 'Jaysen Lestari',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)