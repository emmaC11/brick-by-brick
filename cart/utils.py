from cart.models import Order


def get_or_set_order_session(request):
    # check if order id is in session
    order_id = request.session.get('order_id', None)

    # if order id is not in session, we want to create an order
    if order_id is None:
        order = Order()
        order.save()
        request.session['order_id'] = order.id

    