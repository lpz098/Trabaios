from ast import List


def runningSum(nums: List[int]) -> List[int]:
        soma = 0 
        resposta = []
        for n in nums:
            soma += n
            resposta.append(soma)
        return resposta
    
print(runningSum([1,2,3,4]))  # Output: [1,3,6,10]