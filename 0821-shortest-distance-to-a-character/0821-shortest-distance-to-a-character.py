
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = []

        for i in range(len(s)):
            if s[i] == c:
                indexes.append(i)

        answer = []

        for i in range(len(s)):
            distances = []

            for index in indexes:
                distance = abs(i - index)
                distances.append(distance)

            answer.append(min(distances))

        return answer
