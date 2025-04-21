class MessageWriterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.custom_message = "Hello from Middleware 1!"
        return self.get_response(request)
