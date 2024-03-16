
def test():
    '''
    This is just doc string test.
    '''
    print("This is a test function")


# This will change the doc string of the function
test.__doc__ = "This is a test function2"
help(test)
