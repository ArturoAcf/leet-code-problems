import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        sumRabbits=0
        maxAnswer=max(answers)
        countsAnswers=[0]*(maxAnswer+1)
        totalRabbits=0

        sumRabbits=0
        maxAnswer=max(answers)
        countsAnswers=[0]*(maxAnswer+1)
        totalRabbits=0

        for i in range(0, maxAnswer+1):
            countsAnswers[i]=answers.count(i)
            if i==0:
                totalRabbits+=countsAnswers[i]
            else:
                sumRabbits=countsAnswers[i]/(i+1)
                if sumRabbits.is_integer():
                    totalRabbits+=(i+1)*sumRabbits
                else:
                    totalRabbits+=(i+1)*math.ceil(sumRabbits)

        return int(totalRabbits)
