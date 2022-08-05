from typing import List
import string



class Solution(object):

    # ----------------------方法一：暴力破解---------------------------------------
    def isNumber(self, s):
        float=1
        temp=0
        for index, val in enumerate(s):

            #情况1：包含其他字母
            if val in ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                # print("false")
                float = float + 1
                # return "false"

            #情况2：字符串e/E后包含小数点 或字符串前方数字为0
            elif val == 'e' or val=='E':
                if len(s) == 1 or index == 0:
                    # print("false")
                    float = float + 1
                    # return "false"
                else:
                    if ( '.' in s[index:len(s)]):
                        # print("false")
                        float = float + 1

            #情况3：小数点数量大于1、小数点后为空、小数点后存在字母e/E
            elif val == '.':
                temp=temp+1
                if len(s) == 1 or index == len(s)-1:
                    # print("false")
                    float = float + 1
                    # return "false"
                else:
                    if ('e' in s[index:len(s)-1]) or ('E' in s[index:len(s)-1]):
                        # print("false")
                        float = float + 1
                        # return "false"

                        # return "true"

            #情况4：符号字符+、-连续出现在字符串
            elif val == '+' or val == '-':
                if(s[index+1] == '+' or s[index+1] == '-'):
                    # print("false")
                    float = float + 1
                    # return "false"

                    #print("true")
                    # return "true"
            #情况5：输入非数字的其他字符
            elif val not in ['0','1','2','3','4','5','6','7','8','9',' ','e','E']:
                    float = float + 1

            # 情况6：输入空格
            elif( len(s) == 1 and val == ' '):
                float = float + 1

        if float > 1 or temp > 1:   #情况3：小数点数量大于1
            print("false")
            return False
        else:
            print("true")
            return True

    # isNumber(isNumber, "0e0")

    # ----------------------方法二：暴力破解---------------------------------------
    # 使用try ..except来解
    class Solution2:
        def isNumber2(self, s: str) -> bool:
            try:
                int(s)
                return True
            except:
                try:
                    float(s)
                    return True
                except:
                    return False


        isNumber2(isNumber2, "0e0")

