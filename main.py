ratings = [5, 3, 3, 4, 4, 2, 1, 5, 4, 5, 5, 5, 5, 5, 4, 1]

five_star = ratings.count(5)
four_star = ratings.count(4)
three_star = ratings.count(3)
two_star = ratings.count(2)
one_star = ratings.count(1)

amounts = [five_star, four_star, three_star, two_star, one_star]

#x = str(y) / len(ratings) * 100) + "%"

percent_of_five = str(five_star / len(ratings) * 100) + "%"
percent_of_four = str(four_star / len(ratings) * 100) + "%"
percent_of_three = str(three_star / len(ratings) * 100) + "%"
percent_of_two = str(two_star / len(ratings) * 100) + "%"
percent_of_one = str(one_star / len(ratings) * 100) + "%"

percent = [percent_of_five, percent_of_four, percent_of_three, percent_of_two, percent_of_one]

print("Star ratings:")
print("-----------------")
print(f"Five stars: {[percent[0]]} | {amounts[0]}")
print(f"Four stars: {percent[1]} | {amounts[1]}")
print(f"Three stars: {percent[2]} | {amounts[2]}")
print(f"Two stars: {percent[3]} | {amounts[3]}")
print(f"One stars: {percent[4]} | {amounts[4]}")