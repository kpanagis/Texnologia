@login_required

def update_payment(request):
    title = 'Update Payment Methods'
    description = title
    key = settings.STRIPE_PUBLISHABLE_KEY
    User_Class = User_Class.objects.get(user=request.user)
    current_payment_methods = stripe.PaymentMethod.list(customer=User_Class.stripe_customer_id,
                                                        type='card')
    customer = stripe.User.retrieve(User_Class.stripe_customer_id)
    if request.method == 'POST':
        if request.POST.get('source_obj'):
            logger.info('User is attempting to delete a paid payment method')
            card_id = request.POST.get('source_obj')
            if len(current_payment_methods) > 1:
                stripe.User.delete_source(
                    User_Class.stripe_User_id, card_id
                )
                message = 'This payment method has been removed from your account.'
                messages.info(request, message=message)
                logger.info('User has deleted a payment method')
            elif len(current_payment_methods) <= 1:
                message = 'You must have at least one payment method associated with your account.'
                messages.error(request, message=message)
                logger.info('User failed to delete only payment method.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if request.POST.get('new_prim'):
            logger.info('User is changing their default payment method.')

            card_id = request.POST.get('new_prim')
            print(card_id)
            card = stripe.Card.retrieve(id=card_id, customer=User_Class.stripe_customer_id)
            stripe.User.modify(user_membership.stripe_customer_id,
                                   default_source=card)

            message = 'You have changed your primary payment method.'
            messages.success(request, message=message)
        else:
            logger.info('User is adding a payment method.')
            stripe.User.create_source(
                user_membership.stripe_customer_id,
                source=request.POST.get('stripeToken')
            )
            message = 'You have added this payment method to your account.'
            messages.success(request, message=message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'memberships/update_payment.html',
                  {'title': title, 'description': description, 'key': key,
                   'current_payment_methods': current_payment_methods,
                   'customer': customer})