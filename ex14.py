

def main():
    x = int(input('x='))
    
    # (cond)?true_expr:false_expr

    m = x ** 2 if x > 0 else x * 2 
    
    print(f'm={m}')

    print('-- main --')

######################
main()