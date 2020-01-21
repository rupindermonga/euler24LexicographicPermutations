#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def CreatingPermutations(n):
    result_perms = [[]]
    for i in n:
        new_perms = []
        for perm in result_perms:
            for j in range(len(perm)+1):
                new_perms.append(perm[:j]+[i]+perm[j:])
                result_perms = new_perms
    return result_perms

def CreatingNumbers(n):
    permu = CreatingPermutations(n)
    final_list =[]
    for list in range(len(permu)):
        number = 0
        for element in permu[list]:
            number += permu[list][element]*(10**element)
        final_list.append(number)
    return final_list

def FindingLexiPerm(n,m):
    final_list = CreatingNumbers(n)
    final_list= sorted(final_list)
    final_number = final_list[m-1]
    print(f"{final_number:010d}")
        

FindingLexiPerm([0,1,2,3,4,5,6,7,8,9],1000000)