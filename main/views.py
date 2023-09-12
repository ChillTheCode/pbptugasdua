def show_main(request):
    context = {
        'name': 'Edwin Daniel Toliansa',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)