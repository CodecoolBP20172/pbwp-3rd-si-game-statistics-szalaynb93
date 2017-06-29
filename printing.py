from reports import *
file_name = "game_stat.txt"
print count_games(file_name)
print decide(file_name, 1999)
print get_latest(file_name)
print count_by_genre(file_name, "RPG")
print get_line_number_by_title(file_name, "Counter-Strike")