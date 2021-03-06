#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.
#@author:gvnaakhilsurya

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    L=[ ]
    for i in aDict.values():
        if type(i) == list:
            L.extend(i)
        else:
            L.append(i)
    return len(L)

def main():
    # aDict={}
    # s=input()
    # l=s.split()
    # if l[0][0] not in aDict:
    #     aDict[l[0][0]]=[l[1]]
    # else:
    #     aDict[l[0][0]].append(l[1])
        aDict = {1:[1,2,3],2:[1,5,3,4],4:[8,9,7,8]}
        print(how_many(aDict))


if __name__== "__main__":
    main()