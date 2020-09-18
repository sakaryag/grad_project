from numpy import array
import first_come
import shortest_time
import my_method
import functions
import init

def Factory(method):

    method_name = {
        "1": first_come,
        "2": shortest_time,
        "3": my_method,
    }
    ret=method_name[method].method.assign()

    return ret

if __name__ == "__main__":
    print('Enter Your Choice:')
    print('1 -> First Come First Serve')
    print('2 -> Shortest Time Serve')
    print('3 -> New Method')

    x= input()
    a = Factory(x)
