from numpy import array

class First_Come:


    def assign(self, sth):

        #sort and assign

        return sth

class Shortest_Time:


    def assign(self, sth):


        print(Job[0][4]) #arrive time

        #availability check and assignment

        return sth

class My_Method:

    def assign(self, sth):

        #availability check and assignment

        return sth

def Factory(method):

    method_name = {
        "1": First_Come,
        "2": Shortest_Time,
        "3": My_Method,
    }

    return method_name[method]()

class Functions:
    #check tactile paving
    def tp(vector):
        a=0 #if no tactile paving
        a=1 #if there is a tactile paving
        return a

    #path finder
    def path(job,drone):
        return 3;

    # flying time calculator
    def ft(job, drone):
        a=path(job,drone)/V[drone]

        return a;

    #consumption calculator
    def consumption(job):
        α=1
        β=2
        γ=3
        ret=E_i[job]*(α*Job[2][job])+D_i[job]*(β*Job[2][job])+J_i *(γ*Job[2][job])

        return ret;

    #current charge at time t
    def C(drone_number,t):
        return 1;

    #return time calculator
    def r(i,j):
        return ft(i,j);

    #going time calculator
    def g(i,j):
        return ft(i,j);

    #recharging time calculator
    def ct(i):
        θ=1
        return consumption(i)/ θ;

    #W_ij assign
    def assignment(job,drone):
        result[job][drone]=1
        return 1;




if __name__ == "__main__":

    Map = [[0 for x in range(50)] for y in range(50)]

    #job vector definition
    job_counter=2
    drone_counter=3
    #Job[][0]=vector
    #Job[][1]=type
    #Job[][2]=duration
    #Job[][3]=assign time
    #Job[][4]=arrival_time
    Job = [[0 for x in range(5)] for y in range(job_counter)]

    Job[0][2]=5
    Job[0][4]=0
    #
    Job[1][2]=10
    Job[1][4]=5
    V =array([5]*  drone_counter) #drone speed
    #W_ij
    result =[[0 for x in range(drone_counter)] for y in range(job_counter)]

    #base coordinates of drones
    BC =[(0,0)] *  drone_counter

    BC[0]=(1,1)
    BC[1]=(0,3)
    BC[2]=(1,5)

    #boolean arrays no need yet
    E_i =array([0]*  job_counter,dtype=bool)
    D_i =array([0]*  job_counter,dtype=bool)
    J_i =array([0]*  job_counter,dtype=bool)
    R_ij =array([0]*  job_counter,dtype=bool)
    G_ij =array([0]*  job_counter,dtype=bool)
    Q_i =array([0]*  job_counter,dtype=bool)
    IDLE_j =array([0]*  drone_counter,dtype=bool)
    Ch_j =array([0]*  drone_counter,dtype=bool)

    print('Enter Your Choice:')
    print('1 -> First Come First Serve')
    print('2 -> Shortest Time Serve')
    print('3 -> New Method')

    x= input()

    a = Factory(x)

    message = ["a", "b", "c"]

    a.assign(message[0])
