
def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def open_file(file_name):
    result = []
    for line in open(file_name, "r"):
        line_list = line.strip().split("\t")
        for index, item in enumerate(line_list):
            if isint(item):
                line_list[index] = int(item)
            elif isfloat(item):
                line_list[index] = float(item)
        result.append(line_list)
    return result


def count_games(file_name):
    data = open_file(file_name)
    return len(data)


def decide(file_name, year):
    data = open_file(file_name)
    for line in data:
        if line[2] == year:
            return True
    return False


def get_latest(file_name):
    data = open_file(file_name)
    latest = 0
    for line in data:
        if line[2] > latest:
            latest = line[2]
            game = line[0]
    return game


def count_by_genre(file_name, genre):
    data = open_file(file_name)
    counter = 0
    for line in data:
        if line[3] == genre:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    data = open_file(file_name)
    for num, line in enumerate(data, 1):
        if title in line:
            return num
    raise ValueError


def sort_abc(file_name):
    
    #return a list of strings
    #extra: do not use sort() or sorted()
    pass

def get_genres(file_name):
    #return a list of genres wothout duplicates, in abc order.
    pass

def when_was_top_sold_fps(file_name):
    #int(year of the release)
    #if there is no fps then raise ValueError
    pass
