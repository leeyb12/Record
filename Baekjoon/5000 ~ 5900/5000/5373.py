import sys
input = sys.stdin.readline


def rotate_face(face, cw):
    # 3x3 면 자체 회전
    if cw:   # 시계
        return list(map(list, zip(*face[::-1])))
    else:    # 반시계
        return list(map(list, zip(*face)))[::-1]


def rotate(cube, cmd):
    face, d = cmd[0], cmd[1]
    cw = (d == '+')

    # 면 자체 회전
    cube[face] = rotate_face(cube[face], cw)

    if face == 'U':
        temp = cube['F'][0][:]
        if cw:  # U+
            cube['F'][0] = cube['R'][0][:]
            cube['R'][0] = cube['B'][0][:]
            cube['B'][0] = cube['L'][0][:]
            cube['L'][0] = temp
        else:   # U-
            cube['F'][0] = cube['L'][0][:]
            cube['L'][0] = cube['B'][0][:]
            cube['B'][0] = cube['R'][0][:]
            cube['R'][0] = temp

    elif face == 'D':
        temp = cube['F'][2][:]
        if cw:  # D+
            cube['F'][2] = cube['L'][2][:]
            cube['L'][2] = cube['B'][2][:]
            cube['B'][2] = cube['R'][2][:]
            cube['R'][2] = temp
        else:   # D-
            cube['F'][2] = cube['R'][2][:]
            cube['R'][2] = cube['B'][2][:]
            cube['B'][2] = cube['L'][2][:]
            cube['L'][2] = temp

    elif face == 'F':
        temp = cube['U'][2][:]
        if cw:  # F+
            for i in range(3):
                cube['U'][2][i] = cube['L'][2 - i][2]
                cube['L'][2 - i][2] = cube['D'][0][2 - i]
                cube['D'][0][2 - i] = cube['R'][i][0]
                cube['R'][i][0] = temp[i]
        else:   # F-
            for i in range(3):
                cube['U'][2][i] = cube['R'][i][0]
                cube['R'][i][0] = cube['D'][0][2 - i]
                cube['D'][0][2 - i] = cube['L'][2 - i][2]
                cube['L'][2 - i][2] = temp[i]

    elif face == 'B':
        temp = cube['U'][0][:]
        if cw:  # B+
            for i in range(3):
                cube['U'][0][i] = cube['R'][i][2]
                cube['R'][i][2] = cube['D'][2][2 - i]
                cube['D'][2][2 - i] = cube['L'][2 - i][0]
                cube['L'][2 - i][0] = temp[i]
        else:   # B-
            for i in range(3):
                cube['U'][0][i] = cube['L'][2 - i][0]
                cube['L'][2 - i][0] = cube['D'][2][2 - i]
                cube['D'][2][2 - i] = cube['R'][i][2]
                cube['R'][i][2] = temp[i]

    elif face == 'L':
        temp = [cube['U'][i][0] for i in range(3)]
        if cw:  # L+
            for i in range(3):
                cube['U'][i][0] = cube['B'][2 - i][2]
                cube['B'][2 - i][2] = cube['D'][i][0]
                cube['D'][i][0] = cube['F'][i][0]
                cube['F'][i][0] = temp[i]
        else:   # L-
            for i in range(3):
                cube['U'][i][0] = cube['F'][i][0]
                cube['F'][i][0] = cube['D'][i][0]
                cube['D'][i][0] = cube['B'][2 - i][2]
                cube['B'][2 - i][2] = temp[i]

    elif face == 'R':
        temp = [cube['U'][i][2] for i in range(3)]
        if cw:  # R+
            for i in range(3):
                cube['U'][i][2] = cube['F'][i][2]
                cube['F'][i][2] = cube['D'][i][2]
                cube['D'][i][2] = cube['B'][2 - i][0]
                cube['B'][2 - i][0] = temp[i]
        else:   # R-
            for i in range(3):
                cube['U'][i][2] = cube['B'][2 - i][0]
                cube['B'][2 - i][0] = cube['D'][i][2]
                cube['D'][i][2] = cube['F'][i][2]
                cube['F'][i][2] = temp[i]


T = int(input())
for _ in range(T):
    n = int(input())
    cmds = input().split()

    cube = {
        'U': [['w'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)]
    }

    for cmd in cmds:
        rotate(cube, cmd)

    for row in cube['U']:
        print(''.join(row))
