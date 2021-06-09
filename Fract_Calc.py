# Definition of function

def div_op(numer,denom):

# Define variable for final calculation

    div_res=(numer/denom);


# Prompt user for numerator for division function 
   
num=(input("Enter your numerator: "));

# Integerise numerator variable

numer=int(num);

# Prompt user for denominator for division function

num=(input("Enter your denominator: "));

# Integerise numerator variable

denom=int(num); 
  
# Message to appear if user attempts to divide by zero

if denom == 0:

    print("Error - You cannot divide by 0. Please choose an appropriate denominator")

elif denom > 0:

    print("{0}/{1} = {2}".format(numer,denom,div_res))
        

