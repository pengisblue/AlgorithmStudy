import sys
import time

sys.stdin = open('input.txt')


class Character:
    def __init__(self, x, y) -> None:
        self.x_index = x
        self.y_index = y
        self.original_y_index = y

    def go_ahead(self):
        self.x_index += 1

    def move_right(self):
        self.y_index += 1

    def move_left(self):
        self.y_index -= 1

    def check_left(self, ladder):
        return self.y_index > 0 and ladder.ladder_map[self.x_index][self.y_index - 1] == 1

    def check_right(self, ladder):
        return self.y_index < len(ladder.ladder_map) - 1 and ladder.ladder_map[self.x_index][self.y_index + 1] == 1

    def is_crossroad(self, ladder):
        return self.check_left(ladder) or self.check_right(ladder)

    def is_end_of_ladder(self, ladder):
        return self.x_index >= len(ladder.ladder_map) - 1

    def is_two(self, ladder):
        return ladder.ladder_map[self.x_index][self.y_index] == 2


class Ladder:
    def __init__(self, ladder_map) -> None:
        self.ladder_map = ladder_map

    def show_minimap(self, character):
        x, y = character.x_index, character.y_index
        size = 11
        half_size = size // 2

        animation = ""
        for i in range(x - half_size, x + half_size + 1):
            for j in range(y - half_size, y + half_size + 1):
                if 0 <= i < 100 and 0 <= j < 100:
                    if i == x and j == y:
                        animation += "😊"  # 캐릭터 위치
                    elif self.ladder_map[i][j] == 1:
                        animation += "□"  # 움직일 수 있는 곳
                        # animation += "⏺️ "  # 움직일 수 있는 곳
                    elif self.ladder_map[i][j] == 0:
                        # animation += "🛤️ "  # 움직일 수 없는 곳
                        animation += "■"  # 움직일 수 없는 곳
                    else:
                        animation += "✨"  # 당첨지역
                else:
                    animation += "❌"  # 맵 바깥
            animation += "\n"

        print(animation)
        time.sleep(0.2)


def search(character: Character, ladder: Ladder):
    while not character.is_end_of_ladder(ladder):

        while not character.is_crossroad(ladder) and not character.is_end_of_ladder(ladder):
            character.go_ahead()
            ladder.show_minimap(character)

        if character.is_end_of_ladder(ladder):
            break

        if character.check_right(ladder):
            while character.check_right(ladder):
                character.move_right()
                ladder.show_minimap(character)
            character.go_ahead()
            ladder.show_minimap(character)

        elif character.check_left(ladder):
            while character.check_left(ladder):
                character.move_left()
                ladder.show_minimap(character)
            character.go_ahead()
            ladder.show_minimap(character)

    return character.is_two(ladder)


if __name__ == '__main__':

    for _ in range(10):
        T = int(input())

        ladder_map = [list(map(int, input().split())) for _ in range(100)]

        lad = Ladder(ladder_map)

        character_list = []

        for i in range(100):
            if lad.ladder_map[0][i] == 1:
                character = Character(0, i)

                character_list.append(character)

        for c in character_list:
            if search(c, lad):
                print(f'#{T} {c.original_y_index}')
                break
