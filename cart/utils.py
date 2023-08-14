from cart.models import Order


def get_or_set_order_session(request):
    # check if order id is in session
    order_id = request.session.get('order_id', None)

    # if order id is not in session, we want to create an order
    if order_id is None:
        order = Order()
        order.save()
        request.session['order_id'] = order.id

    # if order id is in session, we want to get the order
    else:
        try:
            order = Order.objects.get(id=order_id, ordered=False)
        except Order.DoesNotExist:
            order = Order()
            order.save()
            request.session['order_id'] = order.id

    # check if user is authenticated
    if request.user.is_authenticated and order.user is None:
        order.user = request.user
        order.save()

    return order
