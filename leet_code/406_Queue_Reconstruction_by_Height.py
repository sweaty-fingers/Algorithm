class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Parameters
        -----------
        people : list[list[h: int, k: int]]
        h: 키, k: 자기보다 키가 크거나 같은 사람의 수

        result : list[list[h: int, k: int]]
        """

        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])

        result = []

        while people:
            person = people.pop(0)
            result.insert(person[1], [person[0], person[1]])

        return result
