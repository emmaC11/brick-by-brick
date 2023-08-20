from django import template
from cart.utils import get_or_set_order_session

register = template.Library()


@register.filter
def cart_item_count(request):
    # get order from the session & count the number of OrderItems quantity & return that num
    order = get_or_set_order_session(request)
    count = order.legoorderitems.count()
    return count
