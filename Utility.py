import random

def RollDice():
    dice_result = random.randint(1, 20)
    return dice_result


def SplitDictionary(dict, start_key, stopping_key):
    new_dict = {}
    counter = 0
    key_list = list(dict.keys())
    for item in key_list:
        counter = counter + 1
        if item == start_key:
            for item2 in key_list[counter - 1:]:
                new_dict[item2] = dict[item2]
                if item2 == stopping_key:
                    return new_dict
                

def RemoveInnerList(list1):
    new_list = []
    for i in range(len(list1)):
        inner_list = list1[i]
        for j in range(len(inner_list)):
            if isinstance(inner_list ,list):
                new_list.append(inner_list[j])
            else:
                new_list.append(inner_list)
    return new_list

def CompareStats(list):
    return_list = []
    roll_list = []
    for value in list:
        roll_dice = RollDice()
        roll_list.append(roll_dice)
        return_list.append(value - roll_dice)
    
    return return_list, roll_list









