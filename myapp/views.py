from django.shortcuts import render

from .models import WordBank
from .forms import MyForm, WordBankForm

def formfun(request):
    context = {
            'e1': 'nope',
            'e2': 'nope',
            'e3': 'nope',
            'e4': 'nope',
            'e5': 'nope',
            'form': MyForm()
            }
    if request.method == 'GET':
        pass
    else:
        f = MyForm(request.POST)
        if f.is_valid():
            print("Valid!")
        else:
            print("Invalid!")
        context['e1'] = len(f.cleaned_data) == 3
        context['e2'] = f.is_valid()
        context['e3'] = f.cleaned_data['two'] == -1
        context['e4'] = 'nope' # len(f.cleaned_data['three']) > 0
        context['e5'] = len(f.errors) == 2

    return render(request, 'myapp/formfun.html', context=context)


def wordbank(request):
    form = WordBankForm()

    context = {'wordbank': WordBank.objects.order_by('english'), 'form':form}
    return render(request, 'myapp/wordbank.html', context=context)
