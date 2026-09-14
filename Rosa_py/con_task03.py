a = 4036
b = 8406
total = 0 

for number in range(a, b + 1):
    if number % 2 == 1:
        total = total + number
print(total)

# Rosalind team are really trash at the explanations before the actual problem
""" Line-by-Line Breakdown
a = 100 and b = 200
This is simply defining your starting and ending points. When you download the real dataset, you will change these numbers to whatever Rosalind gives you.

total = 0
Before we start counting, we need an empty bucket to hold our math. We are creating a variable called total and setting it to zero.

for number in range(a, b + 1):
This line does the heavy lifting. The range() function generates a list of every single number from 100 up to 200. (Remember, we use b + 1 so that it actually includes 200). The for number in... part tells Python: "Take the first number in this list, call it number, and run the code below. Then take the second number, call it number, and run the code below... until the list is done."

if number % 2 == 1:
Now we are inside the loop, looking at one specific number. This is our bouncer at the door. The % 2 divides the number by 2 and looks at the remainder. If the remainder is exactly equal (==) to 1, the number is odd, and it is allowed to move to the next line. If it is even, the remainder is 0, so the code skips the next line entirely.

total = total + number
If the number was odd, it makes it to this line. This tells Python: "Look at whatever is currently in our total bucket, add the new odd number to it, and save that new value back into the total bucket."

print(total)
This line is pushed all the way back to the left (it is not indented). That tells Python this line is outside the loop. It means: "Only print the total bucket after the loop is completely finished looking at every single number."
