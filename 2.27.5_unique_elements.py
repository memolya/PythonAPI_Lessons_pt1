def new_func(line):
    result = []
    for word in line:
        if word not in result:
            result.append(word)
        else:
            continue
    print(*result, sep = '\n')


new_func(line=input().split())