

def stop_words(*words):
    def vary_sense(func):
        def wrapper(*args):
            message = func(*args)
            for word in words:
               message = message.replace(word, '*')
            return message

        return wrapper
    return vary_sense

@stop_words('pepsi', 'BMW')
def create_slogan(name):
    return '{} drinks pepsi in his new BMW'.format(name.title())

print(create_slogan('bob'))



