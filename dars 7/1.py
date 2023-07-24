# class House:
#     PRICE_TYPES = {
#         "oddiy": 200,
#         "luks": 1000
#     }
#
#     def __init__(self, type_room, service, stay_time):
#         self.type_room = type_room
#         self.servise = service
#         self.stay_time = stay_time
#
#     def get_info(self):
#         info = f"\nSizning broningiz: \nXona turi - {house.type_room}, \nQoshimcha xizmatlaar - {house.servise}," \
#                f" \nMuddat - {house.stay_time} kun \numumiy narxi - {self.price_change()} $"
#         return info
#
#     def price_change(self):
#         price = 0
#         if house.type_room in self.PRICE_TYPES:
#             price += self.PRICE_TYPES.get(house.type_room)
#
#         return house.stay_time * price
#
#
# type_room = input("qanaqa xona tanlaysiz:\noddiy\nluks\n>>> ")
# service = input("qoshimcha xizmatlar mavjudmi:\nha/yoq\n>>> ")
# stay_time = int(input("qancha muddat qolasz: "))
#
# house = House(type_room, service, stay_time)
#
# print(house.get_info())


words = ['flower', 'fly', 'flask']
s = "(){)"


# a = 0
# b = 1
# for i, d in enumerate(s):
#     print(i, d.)
#     # if i.numerator:
#     #     print(i[a], i[b])


# def is_valid(s):
#     stack = []
#     bracket_map = {')': '(', '}': '{', ']': '['}
#
#     for char in s:
#         if char in bracket_map:
#             if stack and stack[-1] == bracket_map[char]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(char)
#
#     return not stack
#
#
# print(is_valid(s))

list1 = [1, 2, 4]
list2 = [1, 2, 3, 4]

# res = []
# print(list1 + list2)
#
# for i in list2:
#     if i in list1:
#         res.append(i)
#         res.append(i)
# print(res)


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        res = []
        for i in list1:
            if i in list2:
                res.append(i)
                res.append(i)
            else:
                res.append(i)
        for i in list2:
            if i not in res:
                res.append(i)
                # res.append(i)
        return res


print(Solution().mergeTwoLists(list1, list2))
