#Dynamic Programming
class FibSolution:
    #Recurssion
    def fibrecursive(self,n:int):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fibrecursive(n-1)+self.fibrecursive(n-2)

    def fibseries(self,n:int):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fibseries(n-1)+self.fibseries(n-2)

    #TopdownMemorization
    def fib2(self,n:int):
        memo = {0:0,1:1}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        return f(n)

    def fib2_1(self,n:int):
        memo = {}
        if n==0:
            return 0
        if n==1:
            return 1
        print(memo)
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.fib2_1(n-1)+self.fib2_1(n-2)
            return memo[n]

    #BottomUp dynamic programming - tabulation
    def fib3(self,n:int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        # prev =0
        # cur =1
        # for i in range(2,n+1):
        #     prev,cur = cur,prev+cur
        # return cur
        #output = [0] *(n+1)
        output = [0,1]
        #output[0]=0
        #output[1]=1
        for i in range(2,n+1):
            output.append(0)
            output[i]=output[i-2]+output[i-1]
        print(output)
        return output[n]

    def fib3_1(self,n:int):
        prev=0
        cur=1

        if n==0:
            return prev
        if n==0:
            return cur
        #print(prev,end=" ")
        for fib in range(2,n+1):
            print("before -->","prev=",prev,"cur=",cur)
            prev,cur = cur, prev+cur
            print("After -->", "prev=", prev, "cur=", cur)
            print()
        return cur

    def fib4(self,n:int):
        golden_ratio=(1+(5**0.5))/2
        return int(round((golden_ratio**n)/(5**0.5)))

# 0,1,2,3,4,5,6
#[0,1,1,2,3,5,8]
if __name__ == '__main__':
    f = FibSolution()
    n=6
    print("n is :: " ,n)
    #print(f.fibrecursive(n))
    #for  i in range(n):
    #    print(f.fibseries(i))

    # print(f.fib2(n))
    #
    # print(f.fib3(n))
    #
    # print(f.fib4(n))
    #
    print(f.fib2_1(n))
    #
    # print(f.fib3_1(n))

# [5,3,10,60,4,6,18]

#3+60+6
#5+10+4+18
