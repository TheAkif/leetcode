class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
                
        num = 0
        last_value = ""
        for i,value in enumerate(s):
            if i > 0 and mapping[last_value] < mapping[value] and num > 0:
                mapping[value] = mapping[value] - mapping[last_value]
                num-= mapping[last_value]
                num += mapping[value]
            else:
                num += mapping[value]
            last_value = value
        return num
