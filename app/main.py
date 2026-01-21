class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for p_dict in people:
        new_person = Person(p_dict["name"], p_dict["age"])
        result_list.append(new_person)
    for p_dict in people:
        person_instance = Person.people[p_dict["name"]]

        if p_dict.get("wife"):
            person_instance.wife = Person.people[p_dict["wife"]]
        if p_dict.get("husband"):
            person_instance.husband = Person.people[p_dict["husband"]]

    return result_list
