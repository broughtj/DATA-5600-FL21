# Constants
SIX = 6
NINE = 9
TWENTY = 20


def is_nugget_number(candidate: float) -> bool:
    for i in range(candidate // SIX + 1):
        for j in range(candidate // Nine + 1):
            for k in range(candidate // TWENTY + 1):
                if(i*SIX + j*NINE + k*TWENTY == candidate):
                    return True            
    return False
    
    
## main 


candidate = SIX
largest = 0
in_a_row = 0

while(in_a_row < SIX):
    if(is_nugget_number(candidate)):
        in_a_row += 1
    else:
        largest = candidate
        in_a_row = 0
    candidate += 1
    
print(f"The largest number you cannot get is: {largest}")