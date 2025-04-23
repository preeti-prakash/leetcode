"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3."""






def romanToInt(s: str) -> int:
        sum=0
        roman_array=[]
        list_of_characters = list(s)
        print("array of characters",list_of_characters)
        for i in range(len(list_of_characters)):
            print(list_of_characters[i])
            if list_of_characters[i] == 'I':
                print("entered I module")
                num=1
                print("num after add",num)
                roman_array.append(num)
                print("areray roman",roman_array)
            if list_of_characters[i]== 'V':
                num_V=5
                roman_array.append(num_V)
            if list_of_characters[i]== 'X':
                num_X=10
                roman_array.append(num_X)
            if list_of_characters[i]== 'L':
                num_L=50
                roman_array.append(num_L)
            if list_of_characters[i]== 'C':
                num_C=100
                roman_array.append(num_C)
            if list_of_characters[i]== 'D':
                num_D=500
                roman_array.append(num_D)
            if list_of_characters[i]== 'M': 
                num_M=1000
                roman_array.append(num_M)
        print("areray roman",roman_array)
        for i in range(len(roman_array)):
            if i > 0 and roman_array[i] > roman_array[i - 1]:
                sum += roman_array[i] - 2 * roman_array[i - 1]
            else:
                sum += roman_array[i]
        return sum

# print(romanToInt("III"))
# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))


# def romanToInt(s: str) -> int:
#     roman_dict = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }

#     total = 0
#     prev_value = 0

#     print(reversed(s))
#     for char in reversed(s):
#         print(char)
#         current = roman_dict[char]
#         if current < prev_value:
#             total -= current
#         else:
#             total += current
#             prev_value = current

#     return total

# # Test cases
# print(romanToInt("III"))      # 3
# print(romanToInt("LVIII"))    # 58
# print(romanToInt("MCMXCIV"))  # 1994 ✅
