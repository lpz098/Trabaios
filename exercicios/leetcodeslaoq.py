from ast import List


def maximumWealth( accounts: List[List[int]]) -> int:
        maior = 0

        for cliente in accounts:
            total = 0

            for conta in cliente:
                total += conta

            if total > maior:
                maior = total

        return maior
    
#print(maximumWealth([[1,2,3],[3,2,1]]))  # Output: 6
