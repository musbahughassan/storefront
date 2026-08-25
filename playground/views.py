from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, OrderItem, Customer
from tags.models import TaggedItem
from django.db.models import DecimalField, ExpressionWrapper, Value, F, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum


# Create your views here.
def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TaggedItem.objects.select_related("tag").filter(content_type=content_type, object_id=1)
    return render(request, "hello.html", {"name": "Django-Backend", "tags": list(queryset)})
