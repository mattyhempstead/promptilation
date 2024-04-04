# Define a function to print numbers from 1 to 10 on a single line with a newline at the end
def hello():
    print(*range(1, 11), sep=' ', end='\n')

# Run the hello code 10 times
for _ in range(10):
    hello()
