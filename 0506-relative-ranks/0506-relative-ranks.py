class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new = score.copy()
        new.sort(reverse=True)

        answer = []

        for i in score:
            rank = new.index(i) + 1

            if rank == 1:
                answer.append("Gold Medal")
            elif rank == 2:
                answer.append("Silver Medal")
            elif rank == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(rank))

        return answer