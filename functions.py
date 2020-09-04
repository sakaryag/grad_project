from init import initiation
class Functions(initiation):
    #check tactile paving

    def check_availability(drone,time_start,time_end):
        #add way to go and return

        for x in range (time_end-time_start):
            if(initiation.Drone[drone][x+time_start]==1):
                return 0
        return 1
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
        #return ft(i,j);
        return 2
    #going time calculator
    def g(i,j):
        #return ft(i,j);
        return 2
    #recharging time calculator
    def ct(i):
        θ=1
        return consumption(i)/ θ;

    #W_ij assign
    def assignment(job,drone):
        if(Functions.check_availability(drone,job)==1):
            initiation.result[job][drone]=1
            for x in range(initiation.Job[job][3].astype(int)):
                initiation.Drone[drone][x]==1
            return 1;
        else:
            return 0;
