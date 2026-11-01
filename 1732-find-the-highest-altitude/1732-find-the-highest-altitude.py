class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest=0
        altitude=0
        for i in range(len(gain)):
            altitude+=gain[i]

            if altitude > highest:
                highest = altitude 



        return highest        