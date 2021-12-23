class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])

        result = []

        while people:
            person = people.pop(0)
            result.insert(person[1], [person[0], person[1]])

        return result
