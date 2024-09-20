class Person:
    def __init__(self,name,age):
       self._name = name 
       self._age = age

    def __str__(self):
        return f"Person(name: {self._name}, age: {self._age})"

    def get_age(self):
        return self._age


def std_dev(person_list):
    total = 0

    #get total of ages
    for person in person_list:
        total += person.get_age()

    # found the mean / average of the ages
    mean_of_ages = total / len(person_list)

    # subtract the mean from each age, and square the result and add
    list_of_results = []
    for person in person_list:
        new_result = (person.get_age() - mean_of_ages) ** 2
        list_of_results.append(new_result)

    # Caldulating the mean of the squared results : this is the variance
    total_mean = 0
    for result in list_of_results:
        total_mean += result
    variance = total_mean / len(list_of_results)

    #square root the variance to obtain the population standard deviation
    std = variance ** .5
    return std

p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
answer = std_dev(person_list)
print(answer)