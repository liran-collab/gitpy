# Initialize variables
list1 : list[int] = [1,3,4,7,9]
list2 : list[int] = [3,4,8,9,10,12]

def sort_two_list(list1 : list[int], list2: list[int]) -> list[int]:
    list3 : list[int] = []
    i : int  = 0
    j : int = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    print(list3)

if __name__ == "__main__":
    sort_two_list(list1,list2)