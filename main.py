# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def sort():
    array = [3, 4, 6, 2, 1, 0, 3, 8, 12, 3, 6, 9]
    alreadyOrdered = 0
    lastElement = array[0]

    for element in array:
        if lastElement <= element:
            alreadyOrdered += 1
        else:
            break
        lastElement = element

    print("----Already ordered:", alreadyOrdered)
    for i in range(alreadyOrdered, len(array)):
        print("----Order for:", array[i])
        iInside = i
        for j in range(i-1, -1, -1):
            if array[j] > array[iInside]:
                buffer = array[j]
                array[j] = array[iInside]
                array[iInside] = buffer
                iInside -= 1  # because a[i] moves to left
            else:
                break
        print(array)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sort()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
