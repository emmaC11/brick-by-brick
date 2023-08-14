def get_or_set_order_session(request):
    # check if order id is in session
    order_id = request.session.get('order_id', None)

    