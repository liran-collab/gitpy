# Initialize variables
list1 : list[int] = [1,3,4,7,9]
list2 : list[int] = [3,4,8,9,10,12]

def sort_lists(list1 : list[int], list2 : list[int]) -> list[int]:
    list3 = list1 + list2
    list3.sort()
    return (list3)

if __name__ == "__main__":
    print(sort_lists(list1, list2))