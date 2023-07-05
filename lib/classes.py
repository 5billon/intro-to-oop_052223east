class Cat:
    # This special method runs everytime an instance is created
    def __init__(self, name_given, age_given):
        self.name = name_given
        self._age = age_given
    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if new_age > 30:
            print('cats dont live that long!')
        else:
            self._age = new_age

    age = property(get_age, set_age)

    
    # an instance method, a method we can call on an instance
    # e.g. c1.meow()
    @property
    def meow(self):
        print(f'I am {self.name}, mee-yaow')


    def __repr__(self):
        return f'<Cat name = {self.name} age = {self.age}>'