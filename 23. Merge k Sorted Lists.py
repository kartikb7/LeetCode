def mergeKLists(lists):
    list_iter = [0] * len(lists)
    iter_complete = False
    final_list = []


    while not iter_complete:
        min_val = 9999999
        chosen_list = 0
        for list_num in range(len(lists)):
            if list_iter[list_num] <= len(lists[list_num]) - 1 and lists[list_num][list_iter[list_num]] <= min_val:
                min_val = lists[list_num][list_iter[list_num]]
                chosen_list = list_num

        final_list.append(min_val)
        list_iter[chosen_list] += 1

        iter_complete = True

        for list_num in range(len(lists)):
            if list_iter[list_num] <= len(lists[list_num]) - 1:
                iter_complete = False

    return final_list

list_of_lists = [[1,4,5],[1,3,4],[2,6]]
print(mergeKLists(list_of_lists))