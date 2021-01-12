class Dog:
    age_factor = 7
    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        age_of_human_for_dog = self.dog_age*Dog.age_factor
        return ('if your dog have been a human he would have felt itself as {} years old.'.format(age_of_human_for_dog))


dog1 = Dog(4)
print(dog1.human_age())