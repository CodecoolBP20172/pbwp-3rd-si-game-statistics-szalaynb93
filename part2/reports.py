import math


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


def get_most_played(file_name):
    data = open_file(file_name)
    most_played = 0
    for line in data:
        if line[1] > most_played:
            most_played = line[1]
            game = line[0]
    return game


def sum_sold(file_name):
    data = open_file(file_name)
    total_sold = 0
    for line in data:
        total_sold += line[1]
    return total_sold


def get_selling_avg(file_name):
    data = open_file(file_name)
    total_sold = 0
    for line in data:
        total_sold += line[1]
    number_of_lines = 0
    for line in data:
        number_of_lines += 1
    avg_sold = total_sold / number_of_lines
    return avg_sold


def count_longest_title(file_name):
    data = open_file(file_name)
    longest_title = 0
    for line in data:
        if len(line[0]) > longest_title:
            longest_title = len(line[0])
    return longest_title


def get_date_avg(file_name):
    data = open_file(file_name)
    total_years = 0
    for line in data:
        total_years += line[2]
    number_of_lines = 0
    for line in data:
        number_of_lines += 1
    avg_date = total_years / number_of_lines
    math.ceil(avg_date)
    return avg_date


def get_game(file_name, title):
    data = open_file
    inform = None
    for line in data:
        if line[0] == str(title):
            inform = (""" "Game: " + "%s" + '\n' + "%d" + " million copies sold" + "\n" +
             "Release date: " + "%d" + "\n" + "Genre: " + "%s" + '\n' +
             "Produced by: " + "%s" """ % (line[0], line[1], line[2], line[3], line[4]))
    return inform
