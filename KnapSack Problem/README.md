# KnapSack Problem

## The Problem
The first step to solving this problem is to understand the parameters involved. You will be given:  

 - the total amount of weight you can carry (weight_cap)  
 - the weights of all of the items in an array (weights)  
 - the values of all of the items in an array (values)  

My function should return the maximum value that you will be able to carry.  

### Result
This dynamic algorithm has a big O runtime of O(n * weight_cap) 
compared to the recursive implementation’s runtime of O(2^n).
While this optimized runtime might seem worse using small cases, it is much more efficient as the parameters grow.
