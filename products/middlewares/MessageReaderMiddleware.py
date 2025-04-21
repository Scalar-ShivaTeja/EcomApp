# myproject/middleware/message_reader.py

class MessageReaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        message = getattr(request, "custom_message", "No message set.")
        if message:
            print(f"Middleware 2 received: {message}")
            # Clean up
            del request.custom_message

        return self.get_response(request)