# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
    # Create a table to store results of subproblems 
    n = len(s)+1
    m = len(t)+1
    dp = [[0 for j in range(n)] for i in range(m)] 
    # Fill d[][] in bottom up manner 
    for i in range(m): 
        for j in range(n): 
  
            # If first string is empty, only option is to 
            # isnert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
    
    for i in range(1,m):
        for j in range(1,n):

            ins = dp[i][j-1] + 1
            deletion = dp[i-1][j] + 1
            match = dp[i-1][j-1]
            mismatch = dp[i-1][j-1] + 1
            
            #print(i,",",j)

            if t[i-1]==s[j-1]:
                dp[i][j] = min(ins,deletion, match)
            else:
                dp[i][j] = min(ins,deletion,mismatch)
            
    #print(np.array(dp))
    return dp[m-1][n-1]

if __name__ == "__main__":
    print(edit_distance(input(),input()))
