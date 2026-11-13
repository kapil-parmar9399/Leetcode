class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue=deque()
        time=0
        for i in range(len(tickets)):
            queue.append((i,tickets[i]))

        while queue :
            index, remaining =queue.popleft()

            remaining -=1
            time+=1


            if index==k and remaining ==0 :
                return time 

            if remaining >0 :
                queue.append((index,remaining))

        return time                  