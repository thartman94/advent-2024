import bisect
from datetime import datetime 

def main():
    start = datetime.now()
    with open('data.txt') as input_file:
        lines = input_file.readlines()
        lines = [line.strip().split('   ') for line in lines]
        
        left, right = [], []
        ans = 0
        
        for line in lines:
            bisect.insort(left, int(line[0])) 
            bisect.insort(right, int(line[1]))
        
        for i in range(len(left)):
            ans += abs(left[i] - right[i])
            
        print("Duration", (datetime.now() - start).total_seconds())
        print(ans)
        
main()