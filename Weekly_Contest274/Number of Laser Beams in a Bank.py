class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        first = bank[0].count('1')
        last = total = 0
        for i in range(1, len(bank)):
            last = bank[i].count('1')
            if last == 0: continue
            total += (first * last)
            first = last
        return total
