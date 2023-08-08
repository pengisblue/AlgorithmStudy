# 문자열 폭발
# 아직 못품

from collections import deque

string_list = input()

bomb_str = list(input())
bomb = deque(bomb_str)

bomb_len = len(bomb_str)

temp_string = string_list

bomb_bool = True

while bomb_bool:
    result = deque([])
    temp_buffer = deque([])

    bomb_bool = False
    for i in temp_string:
        temp_buffer.append(i)
        if temp_buffer == bomb:
            temp_buffer = deque([])
            bomb_bool = True
        elif len(temp_buffer) == bomb_len:
            result.append(temp_buffer.popleft())

    while temp_buffer:
        result.append(temp_buffer.popleft())

    temp_string = ''.join(result)

if result:
    print(temp_string)
else:
    print("FRULA")
