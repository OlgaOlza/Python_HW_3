# Требуется найти в массиве list_1 самый близкий 
# по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# for i in range(len(list_1)):
#     if list_1[i] < k:
#         nearest_num = -k
#     else:
#         nearest_num = nearest_num + 0
#     if list_1[i] >= k and list_1[i] - k <= nearest_num - k:
#         nearest_num = list_1[i]
#     elif list_1[i] <= k and nearest_num - k <= list_1[i] - k:
#         nearest_num = list_1[i]
# print(nearest_num)

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 10
closest_num = min(list_1, key=lambda x: abs(x - k))
print(closest_num)