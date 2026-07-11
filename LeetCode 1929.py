def getConcatenation(nums):
    numeros = []
    for num in nums:
        numeros.append(num)
    for num in nums:
        numeros.append(num)
    return numeros

print(getConcatenation([1,2,3])) # Output: [1,2,3,1,2,3]
