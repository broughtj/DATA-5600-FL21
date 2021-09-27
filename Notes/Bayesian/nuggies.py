def is_nugget_number(candidate) -> bool:
    ## We don't know what goes here
    ## We are assuming for now that it exists magically
    ## We'll figure it out later
    return 3.14

## main
SIX = 6
NINE = 9
TWENTY = 20

in_a_row = 0
candidate = 6
largest = None

while(in_a_row < SIX):
    if(is_nugget_number(candidate)):
        in_a_row += 1
    else:
        largest = candidate
        in_a_row = 0
    candidate += 1 

print(f"The largest number I cannot get is: {largest}")







    
    
