# Dynamic Programming

Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again. Following are the two main properties of a problem that suggests that the given problem can be solved using Dynamic programming.

The following are the properties of dynamic programming:

1. Overlapping Subproblems
2. Optimal Substructure

## 1. Overlapping Subproblems Property in Dynamic Programming

Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of the same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed. So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again.

For example, Binary Search doesn’t have common subproblems. If we take an example of following recursive program for Fibonacci Numbers, there are many subproblems that are solved again and again.

```python
# a simple recursive program for Fibonacci numbers
def fib(n):
 if n <= 1:
  return n

 return fib(n - 1) + fib(n - 2)
```

Recursion tree for execution of fib(5)

```python
                         fib(5)
                     /             \
               fib(4)                fib(3)
             /      \                /     \
         fib(3)      fib(2)         fib(2)    fib(1)
        /     \        /    \       /    \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /    \
fib(1) fib(0)
```

We can see that the function fib(3) is being called 2 times. If we would have stored the value of fib(3), then instead of computing it again, we could have reused the old stored value.

The following are two different ways to store the values so that these values can be reused:

1. Memoization (Top Down)
2. Tabulation (Bottom Up)

### 1. Memoization (Top Down)

The memoized program for a problem is similar to the recursive version with a small modification that looks into a lookup table before computing solutions. We initialize a lookup array with all initial values as `None`. Whenever we need the solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return that value, otherwise, we calculate the value and put the result in the lookup table so that it can be reused later.

Following is the memoized version for the nth Fibonacci Number.

```python
# a program for Memoized version of nth Fibonacci number

# function to calculate nth Fibonacci number


def fib(n, lookup):

 # base case
 if n <= 1:
  lookup[n] = n

 # if the value is not calculated previously then calculate it
 if lookup[n] is None:
  lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

 # return the value corresponding to that value of n
 return lookup[n]
# end of function

# Driver program to test the above function


def main():
 n = 34
 # Declaration of lookup table
 # Handles till n = 100
 lookup = [None] * 101
 print ("Fibonacci Number is ", fib(n, lookup))


if __name__ == "__main__":
 main()

```

> Output: Fibonacci Number is  5702887

### 2. Tabulation (Bottom Up)

The tabulated program for a given problem builds a table in bottom-up fashion and returns the last entry from the table. For example, for the same Fibonacci number, we first calculate `fib(0)` then `fib(1)` then `fib(2)` then `fib(3)`, and so on. So literally, we are building the solutions of subproblems bottom-up.

Following is the tabulated version for nth Fibonacci Number.

```python
# Python program Tabulated (bottom up) version

def fib(n):

 # array declaration
 f = [0] * (n + 1)

 # base case assignment
 f[1] = 1

 # calculating the fibonacci and storing the values
 for i in range(2, n + 1):
  f[i] = f[i - 1] + f[i - 2]
 return f[n]

# Driver program to test the above function


def main():
 n = 9
 print ("Fibonacci number is ", fib(n))


if __name__ == "__main__":
 main()

```

## 2. Optimal Substructure Property in Dynamic Programming

 A given problems has Optimal Substructure Property if optimal solution of the given problem can be obtained by using optimal solutions of its subproblems.

For example, the Shortest Path problem has following optimal substructure property:

If a node x lies in the shortest path from a source node u to destination node v then the shortest path from u to v is combination of shortest path from u to x and shortest path from x to v. The standard All Pair Shortest Path algorithm like [Floyd–Warshall](https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/) and Single Source Shortest path algorithm for negative weight edges like [Bellman–Ford](https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/) are typical examples of Dynamic Programming.

On the other hand, the Longest Path problem doesn’t have the Optimal Substructure property. Here by Longest Path we mean longest simple path (path without cycle) between two nodes. Consider the following unweighted graph given in the CLRS book. There are two longest paths from q to t: q→r→t and q→s→t. Unlike shortest paths, these longest paths do not have the optimal substructure property. For example, the longest path q→r→t is not a combination of longest path from q to r and longest path from r to t, because the longest path from q to r is q→s→t→r and the longest path from r to t is r→q→s→t.

## Dynamic Programming Problems and Solution

The following are example problems that can be solved using Dynamic Programming as well as memoization:

### How to use memoization (Top-Down Approach)

> The memoized program for a problem is similar to the recursive version with a small modification that looks into a lookup table before computing solutions. We initialize a lookup array/dictionary with all initial values as None. Whenever we need the solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return that value, otherwise, we calculate the value and put the result in the lookup table so that it can be reused later.

#### Solution to longest common subsequence problem using memoization

> Problem: *Write a function to find the length of the longest common subsequence between two sequences. E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.*

```python
def lcq_memoized(seq1, seq2):
    memo = {} # to store initialized computation
    
    def recurse(idx1, idx2):
        key = idx1, idx2
        
        # Found computation
        if key in memo:
            return memo[key]
        
        # No case
        if idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        
        # Found a match
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
            
        # Found no match, select the highest comparing each side
        else:
            memo[key] = max(recurse(idx1+1, idx2), 
                            recurse(idx1, idx2+1))
        return memo[key]
        
    return recurse(0, 0)
```

#### Solution to knapsack problem using memoization

> Problem: *Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than c(the capacity given).*

```python
def knapsack_memo(capacity, weights, profits):
    memo = {} # store initialized computations
    
    def recurse(idx, remaining):
        key = (idx, remaining)
        
        # Found computation
        if key in memo:
            return memo[key]
            
        # No case
        elif idx == len(weights):
            memo[key] = 0
        
        # Found a match
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
            
        # Found no match, select the highest comparing each sides
        else:
            memo[key] = max(recurse(idx+1, remaining), 
                            profits[idx] + recurse(idx+1, remaining-weights[idx]))
        return memo[key] 
        
    return recurse(0, capacity)
```

### How to use Dynamic Programming

> Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again.

#### Solution to longest common subsequence problem using dynamic programming

```python
def lcq_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)

    # 1. Create a table
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
        
            # Found a match, then add 1 to the next of the current table
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
                
            # Found no match, select the highest among the two
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1], results[idx1+1][idx2])
    return results[-1][-1]
```

#### Solution to knapsack problem using dynamic programming

```python
def knapsack_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for idx in range(n):
        for c in range(capacity+1):
        
            # Found a match
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            
            # Found no match
            else:
                results[idx+1][c] = max(results[idx][c], profits[idx] + results[idx][c-weights[idx]])
            
    return results[-1][-1]
```

### Things to note

- **How to create a matrix table in python**:
`[ [0 for x in range(5) # the row] for x in range(7) # the column]`
- Memoization is a technique to avoid recomputation of the same subproblem.
- ???
- ???
- ???
