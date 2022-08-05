from typing import List
import math

class Solution:
    def strToInt(self, str: str) -> int:
        num = 0
        temp =[]
        number=0
        x=0

        for i in str:
            if i == ' ':
                continue
            elif i in ['0','1','2','3','4','5','6','7','8','9','+','-']:
                temp.append(i)

        # print(temp)

        if num != 0:
            print(0)
            return 0
        else:
            if temp[0] == '+':
                j=len(temp)-2
                for i  in range(1,len(temp)):
                    # print(temp)
                    # print(j)
                    if temp[i] in ['+','-']:
                        j = j - 1
                        continue
                    else:
                        number = number + math.pow(10,j)*(ord(temp[i])- ord('0'))
                        j=j-1

                if number > 2147483647:
                    return 2147483647
                else:
                    # print(number)
                    return number*(+1)

            elif temp[0] == '-':
                j=len(temp)-2
                for i  in range(1,len(temp)):
                    print(temp)
                    print(j)
                    if temp[i] in ['+','-']:
                        j = j - 1
                        continue
                    else:
                        number = number + math.pow(10,j)*(ord(temp[i])- ord('0'))
                        j=j-1

                if number > 2147483648 :
                    return -2147483648
                else:
                    # print(number * (-1))
                    return number * (-1)

            else:
                j = len(temp) - 1
                for i in range(0, len(temp)):
                    if temp[i] in ['+', '-']:
                        j = j - 1
                        continue
                    else:
                        number = number + math.pow(10, j) * (ord(temp[i]) - ord('0'))
                        j = j - 1

                if number > 2147483647:
                    return 2147483647
                else:
                    # print(number)
                    return number


    strToInt(strToInt," + dw       912834  word ")

