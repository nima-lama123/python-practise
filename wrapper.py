def announce(f):
    def wrapper():
        print ("about to run")
        f()
        print("done with ")
    return wrapper
@ announce
def hello():
    print("hello world")
hello()