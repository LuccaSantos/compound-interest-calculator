from django.shortcuts import render


def index(request):
    # form = JurosForm()
    # montante = request.POST.get('montante', '')
    # capital = request.POST.get('capital', '')
    # taxa_de_juros = request.POST.get('taxa_de_juros', '')
    # tempo = request.POST.get('tempo', '')
    # context = {'form': form}
    return render(request, 'core/index.html')
