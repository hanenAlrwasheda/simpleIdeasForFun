instruction = 'Hi!\nUse <show> to see current todos\nUse <new> to create a new todo\n--------------------------------'
allDict = dict()
i = 0
print(instruction)
while True:
    command = input('> ')
    if command == 'new':
        title = input('title:\n')
        content = input('content:\n')
        localDict = {title:content}
        i += 1
        allDict[str(i)] = localDict
    elif command == 'show':
        if len(allDict) == 0:
            print("you have no todos yet, create your first one using the command <new>!")
        for d in list(allDict):
            for ld in list(allDict[d]):
                print(d+') '+ld+': \n'+allDict[d][ld])
    else:
        print(instruction)
