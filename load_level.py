from objects.class_Player import Player
from objects.class_Platform import Platform
from objects.class_Dog import Dog


def load_level(level_number):
    """
    Create a level structure using the txt layout
    Args: level number
    """
    level_file = open('levels/level' + str(level_number) + '.txt', 'r')
    level_length = int(level_file.readline().split()[0])
    platform_height = int(level_file.readline().split()[0])
    platform_width = int(level_file.readline().split()[0])
    player_height = int(level_file.readline().split()[0])
    player_width = int(level_file.readline().split()[0])
    enemy_height = int(level_file.readline().split()[0])
    enemy_width = int(level_file.readline().split()[0])
    level_length *= platform_width
    platforms = []
    enemies = []
    player = ""
    y = 0
    for line in level_file:
        if line[0] != '[' and line[0] != ']':
            for x in range(len(line)):
                if line[x] == '-':
                    platforms.append(Platform(x * platform_width, y * platform_height, platform_width, platform_height))
                elif line[x] == 'P':
                    player = Player(x * platform_width, y * platform_height, player_width, player_height)
                elif line[x] == 'e':
                    enemies.append(Dog(x * platform_width, y * platform_height, enemy_width, enemy_height))
        else:
            y -= 1
        y += 1
    level_height = y * platform_height
    return [level_length, level_height, player, platforms, enemies]
