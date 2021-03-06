'''
From programming challenges - dropbox website
--------------------------------------------------------
Of the boatload of perks Dropbox offers, the ones most threatening to our engineers' waistlines are the daily lunches, the fully-stocked drink fridge, and a full-length bar covered with every snack you could want. All of those calories add up. Luckily, the office is also well-equipped with ping-pong, a DDR machine, and a subsidized gym right across the street that can burn those calories right back off. Although we often don't, Dropboxers should choose the food they eat to counterbalance the activities they perform so that they don't end up with caloric deficit or excess.

Help us keep our caloric intake in check. You'll be given a list of activities and their caloric impact. Write a program that outputs the names of activities a Dropboxer should choose to partake in so that the sum of their caloric impact is zero. Once an activity is selected, it cannot be chosen again.

Input
Your program reads an integer N (1 <= N <= 50) from STDIN representing the number of list items in the test input. The list is comprised of activities or food items and its respective calorie impact separated by a space, one pair per line. Activity names will use only lowercase ASCII letters and the dash (-) character.

Output
Output should be sent to stdout, one activity name per line, alphabetized. If there is no possible solution, the output should be no solution. If there are multiple solutions, your program can output any one of them. Solutions should be non-trivial, so don't send us cat > /dev/null, you smart aleck.

Sample Input

2
red-bull 140
coke 110

Sample Output
-------
no solution


12
free-lunch 802
mixed-nuts 421
orange-juice 143
heavy-ddr-session -302
cheese-snacks 137
cookies 316
mexican-coke 150
dropballers-basketball -611
coding-six-hours -466
riding-scooter -42
rock-band -195
playing-drums -295

Output
------
coding-six-hours
cookies
mexican-coke'''

'''
Thought Process:
    This problem is structurally similar to a scheduling problem and I used the most popular tool called dynamic programming to solve it.
    I used a simple recursion with 2 cases.
        Either the element is in the optimized solution in which case you can add that element to you prescribed diet and keep recusring until 0
        or the element is not in the optimized solution in which case you ignore the element and keep recursing.
'''
diets = []
def memoizer(f):
    cache = {}
    def _f(*args):
        try:
            level,total,_ = args
            return cache[(level,total)]
        except KeyError:
            level,total,_ = args
            value = cache[(level,total)] = f(*args)
            return value
        except TypeError:
            return f(*args)
    return _f

@memoizer
def best_diet(level,total_calories,prescribed_diet=[]):
    if level < 0:
        return list()
    diet_name,calories = diets[level]
    if calories+total_calories == 0:
        prescribed_diet.append(diet_name)
        return prescribed_diet
    possible_prescribed_diet = best_diet(level-1,total_calories,list(prescribed_diet)) 
    if possible_prescribed_diet:
        return possible_prescribed_diet
    else:
        prescribed_diet.append(diet_name)
        return best_diet(level-1,total_calories+calories,list(prescribed_diet))

if __name__ == '__main__':
    with open(r'Tests/test_fix_your_diet.in','rU') as fhandle:
        n = int(fhandle.readline())
        for _ in range(n):
            diet_name,calories = fhandle.readline().strip().split(' ')
            diets.append((diet_name,int(calories)))
    prescribed_diet = best_diet(len(diets)-1,0,[])
    if prescribed_diet:
        prescribed_diet.sort()
        for diet_name in prescribed_diet:
            print diet_name
    else:
        print 'no solution'
