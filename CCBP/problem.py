str_num_list = input().split(",")
pair_sum = int(input())


def convert_str_to_int(str_list):
    new_list = []
    for i in str_list:
        int_num = int(i)
        new_list.append(int_num)
    return new_list


def get_unique_pairs(int_list, pair_sum):
    stop_index = len(int_list) - 1
    unique_pairs_set = set()
    for curr_index in range(stop_index):
        num_1 = int_list[curr_index]
        num_2 = pair_sum - num_1
        remaining_list = int_list[curr_index + 1:]
        if num_2 in remaining_list:
            pair = (num_1, num_2)
            sorted_pair = tuple(sorted(pair))
            unique_pairs_set.add(sorted_pair)

    return unique_pairs_set


int_list = convert_str_to_int(str_num_list)
unique_pairs = get_unique_pairs(int_list,pair_sum)

for pair in unique_pairs:
    print(pair)

