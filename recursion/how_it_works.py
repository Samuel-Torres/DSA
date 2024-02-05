# examples:

def fun(n):
    if n <= 0: # base case
        print(f"n is now {n}, process complete, end program.")
        return "Completed"
    else: # condition which gets us closer to the main goal.
        print(f"n is greater than 0 so minus 1 is now {n - 1}")
        fun(n - 1)

fun(100)


