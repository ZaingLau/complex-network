

def cal_the_classes_number(list):
    if len(list) == 0:
        num = 0
    else:
        sub_list = []
        sub_list.append(list[0])
        for content in list:
            if content not in sub_list:
                sub_list.append(content)
            else:
                continue
        num = len(sub_list)
    return num


def get_the_class_number(string):
    sum = 0
    for i in range(len(string)):
        if (string[i] >= "0") and (string[i] <= "9"):
            sum += 1
    return sum


