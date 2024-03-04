from django.shortcuts import render
from .models import Transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.

@login_required
def transactions(request):
    transactions = Transaction.objects.filter(tailor=request.user)
    paginator = Paginator(transactions,6)
    page_obj = paginator.get_page(1)
    return render(request,'transactions/transactions.html',{'page_obj':page_obj})

@login_required
def filter_transactions(request):
    transactions = Transaction.objects.filter(tailor=request.user)
    search_query = request.GET.get('search','')
    if search_query:
        transactions = transactions.filter(
            Q(order__customer__first_name__icontains=search_query) |
            Q(order__id__icontains=search_query)
        )
    paginator = Paginator(transactions,6)
    page_num = request.GET.get('page')
    print(page_num)
    page_obj = paginator.get_page(page_num)
    transactions_data = list(page_obj.object_list.values('order__id','amount', 'order__customer__first_name','order__customer__profile'))
    print(transactions_data)
    page_data = {
        'number':page_obj.number,
        'num_pages':page_obj.paginator.num_pages,
        'has_next':page_obj.has_next(),
        'has_previous':page_obj.has_previous(),
        'previous_page_number':page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None,

    }
    return JsonResponse({'page_obj':page_data,'transactions':transactions_data})