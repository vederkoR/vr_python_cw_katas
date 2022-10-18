import re


def num_str_generator(i=0):
    while True:
        i += 1
        yield i


def true_index_calculator(str_num, shift):
    length = len(str_num)
    if length == 1:
        return int(str_num) - length
    int_num = int(str_num)
    first_part = (int_num - int((length - 1) * "9")) * length
    second_part = 9 * sum([int(str(i) + (i - 1) * "0") for i in range(1, length)])
    return first_part + second_part - length + shift


def find_position_easy(string):
    index = num_str_generator()
    substring = string
    while True:
        val_num = str(next(index))
        if string == substring:
            locked_index = val_num
            shift = 0
        for j in val_num:
            if j == substring[0]:
                substring = substring[1:]
                if substring == "":
                    return true_index_calculator(locked_index, shift=shift), locked_index
            else:
                shift = +1
                substring = string
                if j == substring[0]:
                    substring = substring[1:]
                    if substring == "":
                        return true_index_calculator(locked_index), locked_index


def list_operator(lst):
    answer = []
    for inr_lst in lst:
        if inr_lst[0].replace('9', "") == "":
            answer.append((inr_lst[0], 0))
            continue
        shift = 0
        number = ''
        flag = False
        start = 0
        if inr_lst[0].rstrip("9")[-1] == 'd':
            flag = True
            start = 1
        for inx in range(len(inr_lst[start])):
            if inr_lst[start][inx] == "d":
                smb = "d"
                j = start
                while smb == "d":
                    j += 1
                    if flag and j >= len(inr_lst):
                        smb = "0"
                        break
                    smb = inr_lst[j][inx]
            else:
                smb = inr_lst[start][inx]
            number += smb
        shift = len(inr_lst[0]) - len(inr_lst[0].replace("d", ""))
        if flag:
            number = str(int(number) - 1)
            if len(str(int(number) + 1)) > len(number):
                shift -= 1
        answer.append((number, shift))
    return sorted(answer, key=lambda x: (x[0], x[1]))[0]


def find_lowest(string):
    lws = min([int(i) for i in string.replace("0", "")])
    indices = [i for i, x in enumerate(string) if x == str(lws)]
    sqns = []
    for j in indices:
        if j == 0:
            sqns.append((string[j:] + string[:j], 0))
        else:
            sqns.append((string[j:] + string[:j], len(string) - j))

    sqns.sort(key=lambda x: int(x[0]))
    return sqns[0]


def find_position_algorithmic(string):
    if string.replace("0", "") == "":
        string += "1"
    answer_list = []
    if string in "12345678910111213":
        return "12345678910111213".index(string)

    else:
        for i in range(2, len(string) + 1):
            if answer_list:
                answer_list = [m for m in answer_list if not [x for x in m if x.startswith("0")]]
                if not answer_list:
                    return true_index_calculator(*find_lowest(string)), answer_list, list_operator(answer_list)
                return true_index_calculator(*list_operator(answer_list)), answer_list, list_operator(answer_list)
            string_to_check = (i - 1) * "d" + string + (i - 1) * "d"

            for j in range(i):
                list_to_check = []
                for q in range(int(len(string_to_check) / i)):
                    list_to_check.append(string_to_check[j + q * i:j + i + q * i])
                list_to_check = [b for b in list_to_check if len(b) == i]
                for ind in range(len(list_to_check) - 1):
                    temp_1 = list_to_check[ind][0:len(list_to_check[ind]) - 1] + str(
                        int(list_to_check[ind][-1]) + 1)[-1]

                    if temp_1[-1] == "0":
                        if temp_1.replace("9", "") == "0":
                            temp_1 = "1" + len(temp_1) * "0"
                        else:
                            n_ind = 2
                            while temp_1[0 - n_ind] == '9':
                                n_ind += 1
                            temp_1 = temp_1[0:len(temp_1) + 1 - n_ind]
                            if temp_1 and temp_1[-1] != 'd':
                                temp_1 = temp_1[0:len(temp_1) - 1] + str(int(temp_1[-1]) + 1)
                            temp_1 += (n_ind - 1) * "0"

                    temp_2 = len(list_to_check[ind + 1].rstrip("d"))
                    temp_1 = temp_1[0:len(temp_1) - (i - temp_2)] + (i - temp_2) * "d"

                    if not re.match(temp_1.replace("d", r"\d"), list_to_check[ind + 1].replace("d", "9")):
                        break
                else:
                    answer_list.append(list_to_check)

    answer_list = [m for m in answer_list if not [x for x in m if x.startswith("0")]]
    return true_index_calculator(*list_operator(answer_list)), answer_list, list_operator(answer_list)


print(find_position_algorithmic("9100"))


