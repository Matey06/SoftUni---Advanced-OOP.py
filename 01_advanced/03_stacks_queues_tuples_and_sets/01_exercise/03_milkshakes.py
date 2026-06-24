from collections import deque

chocolates_stack = [int(el) for el in input().split(", ")]
milks = deque(int(el) for el in input().split(", "))

milkshakes = 0

while milkshakes < 5 and (chocolates_stack and milks):
    if chocolates_stack[-1] <= 0 or milks[0] <= 0:
        if chocolates_stack[-1] <= 0:
            chocolates_stack.pop()
        if milks[0] <= 0:
            milks.popleft()
    elif chocolates_stack[-1] == milks[0]:
        milkshakes += 1
        chocolates_stack.pop()
        milks.popleft()
    else:
        milks.rotate(-1)
        chocolates_stack[-1] -= 5


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates_stack)) if chocolates_stack else 'empty'}")
print(f"Milk: {', '.join(map(str, milks)) if milks else 'empty'}")
