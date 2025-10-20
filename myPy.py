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

# def sort_two_list_better(list1 : list[int], list2: list[int]) -> list[int]:
#     list3 : list[int] = []
#     for num in list1:
#         list3.append(num)
    
#     for num in list2:
#         list3.append(num)

#     for i in range(1, len(list3)):
#         temp : int = list3[i]
#         j = i - 1
#         while j >= 0 and temp < list3[j]:
#             list3[j + 1] = list3[j]
#             j -= 1
#         list3[j + 1] = temp

#     print(list3)

if __name__ == "__main__":
    sort_two_list(list1,list2)