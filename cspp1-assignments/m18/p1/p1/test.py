def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = 6
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
        print(documents)