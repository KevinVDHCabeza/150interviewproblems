def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort(reverse=True)
    return [i for i,x in enumerate(citations) if x>i]

if __name__ == "__main__":
    citations= [8,4,5,3,10,6,2,7,1]
    print(hIndex(citations))
