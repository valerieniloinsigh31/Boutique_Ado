from django.http import HttpResponse

 class StripeWH_Handler:
      """Handle Stripe Webhooks"""

       def __init__(self, request):
            self.request = request

        def handle_event(self, event):
            """
            Handle an unknown/unexpected/generic webhook event
            """
            return HttpResponse(
                content=f'Unhandled webhook received: {["type"]}',
                status=200)

        def handle_payment_intent_succeeded (self, event):
            """
            Handle the payment intent succeeded hook from Stripe
            """
            return HttpResponse(
                content=f'Webhook received: {["type"]}',
                status=200)
        

        def handle_payment_intent_payment_failed(self, event):
            """
            Handle the payment intent failed hook from Stripe
            """
            return HttpResponse(
                content=f'Webhook received: {["type"]}',
                status=200)
