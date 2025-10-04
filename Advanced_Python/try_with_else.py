"""
Try:
 #code
 else:
  #code
  if try block successfully run then only else block run otherwise it throws an error
  -> sometimes we want to runa piece of code when try was successful.
"""
"""
try:
    num=int(input("Enter a number: "))
    print(num)
except Exception as e:
    print("Exception Caught,",e)
else:
    print("  if try block successfully run then only else block run otherwise it throws an error")
"""

"""********************   Try with finally  **********************
Python offers a 'finally' clause which ensures execution of a piece of code inspective
of the exception.
syntax:    try: 
                #some code
           except:
                #some code
           finally:
                #some code         #executed reagardless of error!
    finally block always run even if function return 
"""
def final():
    try:
        num=int(input("Enter a number: "))
        print(num)
        return
    except Exception as e:
        print("Exception Caught,",e)
        return
    # finally:
        #print("I am inside of finally block.")

    print("I am inside of finally block.")
    # here finally isnot written so if it runs this block doesn't execute
    #but if we use finally keyword then it will executed in every condition

final()

