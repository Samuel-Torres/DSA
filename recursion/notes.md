What is recursion?
    - a routine that calls itself directly or indirectly.

    Recursive functions are written like this:

        function name(params...):
            base_case:
                return something
            if statement:
                name(params...)

    
    Recurrance relation:

 def calculate_rec(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate_rec(n - 1)

calculate_rec(4)       


