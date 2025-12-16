from string import Formatter



empty = object()


class Prompt():

    __formatter = Formatter()

    @classmethod
    def get_keys(cls, string):
        return list({field_name for _, field_name, _, _ in cls.__formatter.parse(string) if field_name})



    def __init__(self, prompt: str, *args, **kwargs):
        self.prompt = prompt
        self.values = {key: empty for key in self.get_keys(prompt)}
        for x in args: self.set(x)
        for x in kwargs: self.set(x)
        

    def set(self, x):
        if not self.values:
            raise IndexError("Empty Prompt!")
        
        
        if isinstance(x, tuple):
            key = x[0]
            value = x[1]
        else:
            try:
                key = next((key for key, value in self.values.items() if value is empty))
                value = x

            except:
                raise IndexError("no valid keys left!")

        self.values[key] = value


    def __str__(self):
        return self.format()
        

    def format(self, *args, **kwargs): 
        return self.prompt.format(*args, **{**{key: value for key, value in self.values.items() if value is not empty}, **kwargs})

