N = int(raw_input())

for grupos in range(N):
    grupo = int(raw_input())

    if grupo % 2 == 0:
        media = grupo / 2
        print media, media
    else:
        media = grupo / 2
        print media, media + 1
