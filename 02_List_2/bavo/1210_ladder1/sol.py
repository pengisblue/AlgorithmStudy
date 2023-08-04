import sys
import time

sys.stdin = open('input.txt')


class Character:
    def __init__(self, x, y, ladder) -> None:
        self.x_index = x
        self.y_index = y
        self.ladder = ladder
        self.original_y_index = y

    def go_ahead(self):
        self.x_index += 1
        self.show_minimap()

    def move_right(self):
        self.y_index += 1
        self.show_minimap()

    def move_left(self):
        self.y_index -= 1
        self.show_minimap()

    def check_left(self):
        return self.y_index > 0 and self.ladder[self.x_index][self.y_index - 1] == 1

    def check_right(self):
        return self.y_index < len(self.ladder) - 1 and self.ladder[self.x_index][self.y_index + 1] == 1

    def is_crossroad(self):
        return self.check_left() or self.check_right()

    def is_end_of_ladder(self):
        return self.x_index >= len(self.ladder) - 1

    def is_two(self):
        return self.ladder[self.x_index][self.y_index] == 2

    def show_minimap(self):
        x, y = self.x_index, self.y_index
        size = 11
        half_size = size // 2

        animation = ""
        for i in range(x - half_size, x + half_size + 1):
            for j in range(y - half_size, y + half_size + 1):
                if 0 <= i < 100 and 0 <= j < 100:
                    if i == x and j == y:
                        animation += "😊"  # 캐릭터 위치
                    elif self.ladder[i][j] == 1:
                        # animation += "□"  # 움직일 수 있는 곳
                        animation += "⏺️ "  # 움직일 수 있는 곳
                    elif self.ladder[i][j] == 0:
                        animation += "🛤️ "  # 움직일 수 없는 곳
                        # animation += "■"  # 움직일 수 없는 곳
                    else:
                        animation += "✨"  # 당첨지역
                else:
                    animation += "❌"  # 맵 바깥
            animation += "\n"

        print(animation)
        time.sleep(0.2)


    


def search(character: Character):
    while not character.is_end_of_ladder():

        while not character.is_crossroad() and not character.is_end_of_ladder():
            character.go_ahead()

        if character.is_end_of_ladder():
            break

        if character.check_right():
            while character.check_right():
                character.move_right()
            character.go_ahead()

        elif character.check_left():
            while character.check_left():
                character.move_left()
            character.go_ahead()

    return character.is_two()


if __name__ == '__main__':

    for _ in range(10):
        T = int(input())

        ladder_map = [list(map(int, input().split())) for _ in range(100)]


        character_list = []

        for i in range(100):
            if ladder_map[0][i] == 1:
                character = Character(0, i, ladder_map)

                character_list.append(character)

        for c in character_list:
            if search(c):
                print(f'#{T} {c.original_y_index}')
                break