from string import Formatter




class Prompt():

    __formatter = Formatter()

    @classmethod
    def get_keys(cls, string):
        return list({field_name for _, field_name, _, _ in cls.__formatter.parse(string) if field_name})



    def __init__(self, prompt: str, *args, **kwargs):
        self.prompt = prompt
        self.values = dict(zip(self.get_keys(prompt), [None])) #irgendwas falsch
        for x in args:  self.set(x)
        for x in kwargs: self.set(x)
        

    def set(self, x):
        if not self.values:
            raise IndexError("Empty Prompt!")
        
        
        if isinstance(x, tuple):
            key = x[0]
            value = x[1]
        else:
            key = next(self.values.keys())
            value = x

        self.values[key] = value


    def __str__(self):
        return self.format()
        
    #TODO:
    def format(self, *args, **kwargs): 
        return self.prompt.format(**kwargs)

