_callbacks = {}

def register(hook, value=0):
    def register_callback(func):
        return func
