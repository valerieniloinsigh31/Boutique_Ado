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
                content=f'Webhook received: {["type"]}',
                status=200)