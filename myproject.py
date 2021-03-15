from numpy import array
import first_come
import shortest_time
import my_method
import my_method_old
import functions
import init

def Factory(method):

    method_name = {
        "1": first_come,
        "2": shortest_time,
        "3": my_method,
        "4": my_method_old,
    }
    problem =method_name[method].method()

if __name__ == "__main__":

    print('Enter Your Choice:')
    print('1 -> First Come First Serve')
    print('2 -> Shortest Time Serve')
    print('3 -> New Method')
    print('4 -> Old Method')
    #x= 4
    Factory('4')
