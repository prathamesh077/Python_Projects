# words = ["bat", "python", "Prathamesh"]
# # for a in words:
# print(len(words))
# -----------------------------------------------

# users = {'xcxc': 'active', 'Mandge': 'inactive', 'nitesh': 'active'}

# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# active_users = {}
# for user, status in users.copy().items():
#     if status == 'active':
#         active_users[user] = status
# ---------------------------------------------------
# q = ['ilove', 'Raj', 'and', 'meet', 'Soon'] 
# for i in range(len(q)):
#     print(q[i], i)

# -------------------------------------------------

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '=', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found the even number", num)
#         continue
#     print("Found an odd number", num)

from enum import Enum
class Color(Enum):
    GREEN = 'green'
    RED = 'red'
    BLACK = 'Black'
while Color:
    color = Color(input("Enter your choice of 'red', 'green', 'Black': "))
    match color:
        case Color.RED:
            print('I see the Red Color!')
        case Color.GREEN:
            print('I know grass is Green')
        case Color.BLACK:
            print('Black is good in fashion.. Right?')


