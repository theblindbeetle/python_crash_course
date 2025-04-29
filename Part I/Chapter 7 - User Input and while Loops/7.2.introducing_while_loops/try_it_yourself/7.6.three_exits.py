"""
7-6. Three Exits:

• Write different versions of either Exercise 7-4 or Exercise 7-5
    that do each of the following at least once:

•  Use a conditional test in the while statement to stop the loop.

•  Use an active variable to control how long the loop runs.

•  Use a break statement to exit the loop when the user enters a 'quit' value.
"""
SIZE = 3
price = ['free', '$10', '$15']
movie_theater = 'free space'
seats = 0
while movie_theater != 'full':
    age = input("Introduce your age: ")
    if age == 'quit':
        break
    elif int(age) < 3:
        print(f"Ticket fair is: {price[0]}")
    elif int(age) < 12:
        print(f"Ticket fair is: {price[1]}")
    elif int(age) >= 12:
        print(f"Your ticket fair is: {price[0]}")
    seats += 1
    movie_theater = 'full' if seats >= SIZE else movie_theater

message = "\n------------------------\n"
message += "Movie theater is full. Thanks for your preference."
print(message)

