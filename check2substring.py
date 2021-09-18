# function to check if small string is 
# there in big string
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
# driver code
string = "abbas RVR"
sub_str ="RVR"
check(string, sub_str)
