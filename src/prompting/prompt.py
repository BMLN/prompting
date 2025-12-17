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
        self.formatters = {}
        for x in args: self.set(x)
        for x in kwargs: self.set(x)
        

    def __str__(self):
        return self.format()
        
    

    def set(self, x):

        if not self.values:
            raise KeyError("Empty Prompt!")
        
        
        if isinstance(x, tuple):
            if not x[0] in self.values:
                raise KeyError(f"Prompt does not contain {x[0]}!")

            key = x[0]
            value = x[1]
        else:
            try:
                key = next((key for key, value in self.values.items() if value is empty))
                value = x

            except StopIteration:
                raise KeyError("no valid keys left!")

        self.values[key] = value



    def set_formatter(self, key, formatter):

        if key not in self.values:
            raise KeyError(f"Prompt does not contain {key}!")
        
        if not callable(formatter):
            raise TypeError("Formatter must be callable")
        
        self.formatters[key] = formatter



    def format(self, *args, **kwargs):
        
        return self.prompt.format(**
            { 
                key: (value if not key in self.formatters else self.formatters[key](value)) 
                for key, value in zip(
                    self.values.keys(), 
                    list(args) + list((self.values | kwargs).values())
                ) 
                if value is not empty 
            }
        )