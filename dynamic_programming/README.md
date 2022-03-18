## How to use memoization
>  The memoized program for a problem is similar to the recursive version with a small modification that looks into a lookup table before computing solutions. We initialize a lookup array/dictionary with all initial values as NILL/None. Whenever we need the solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return that value, otherwise, we calculate the value and put the result in the lookup table so that it can be reused later.

### Solution to longest common subsequence problem using memoization

> Problem: *Write a function to find the length of the longest common subsequence between two sequences. E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.*

```
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

### Solution to knapsack problem using memoization
> Problem: *Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than c(the capacity given).*

```
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

## How to use Dynamic Programming
> Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again. 

### Solution to longest common subsequence problem using dynamic programming

```
def lcq_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)] # create a table
    for idx1 in range(n1):
        for idx2 in range(n2):
        
            # Found a match, 
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
                
            # Found no match, select the highest among the two
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1], results[idx1+1][idx2])
    return results[-1][-1]
```

### Solution to knapsack problem using dynamic programming
```
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


# Things to note
- How to create a matrix table in python:
`[ [0 for x in range(5) # the row] for x in range(7) # the column]`
- ???
- ???
- ???
- ???






