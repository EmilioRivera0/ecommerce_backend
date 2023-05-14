from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from permissions import permissions
from shopping_history.models import History

# Create your views here.

@login_required()
@permission_required(permissions.ECOMMERCE_CLIENT)
def View_History(request):
    history = History.objects.get(user=request.user.id)
    context = {'products':history.history['history']}
    return render(request, 'shopping_history/history.html', context)
