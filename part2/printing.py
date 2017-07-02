from reports import *

file_name = "game_stat.txt"
title = "The Sims"

print(get_most_played(file_name))
print(sum_sold(file_name))
print(get_selling_avg(file_name))
print(count_longest_title(file_name))
print(get_date_avg(file_name))
print(get_game(file_name, title))