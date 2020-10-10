# ------------------------Sho8l Seka ----------------------

def Time1(time):
    Q=round(time,1)
    return Q


def CheckArrive(Time,ArriveTime):
     if ArriveTime<=Time:
        return True
     else:
         return False


def InputSjfPreemptive():
    NoOfProcesses = int(input())  # "Enter the no. of processes: "
    Process = []
    ArrivalT = []
    Burst = []
    RemainingTime = []
    for i in range(NoOfProcesses):
        data = input()  # Enter the process,arrival time,burst time
        X = data.split(',')
        Process.append(X[0])
        ArrivalT.append(X[1])
        Burst.append(X[2])
        RemainingTime.append(round(float(Burst[i]), 1))
    return NoOfProcesses,Process,ArrivalT,Burst,RemainingTime



def SJFPreemptive(NoOfProcesses,Process,ArrivalT,Burst,RemainingTime):
    ProcessIn = []
    TimeIn = []
    zyadat = []
    min=10000
    AA = 0
    index=0
    while AA < NoOfProcesses:
        zyadat.append(1000)
        AA += 1
    mgmo3Elzyadat = 0
    TotalWaitingTime = 0
    for i in range(NoOfProcesses):
        for x in range(i + 1, NoOfProcesses):
            if ((float(ArrivalT[i]) + float(Burst[i])) < float(ArrivalT[x])):
                if ((float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))) < zyadat[i]):
                    zyadat[i] = float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))
    for i in range (NoOfProcesses):
        if float(ArrivalT[i])<min:
           min=float(ArrivalT[i])
           index=i
    if min > 0:
        mgmo3Elzyadat += min

    for i in range(NoOfProcesses):
        if (zyadat[i] < 1000):
            mgmo3Elzyadat += zyadat[i]


    Time = 0
    TimeAfter = 0
    i = 0
    z = 0
    flag = 0
    TotalBurst = 0
    while z < NoOfProcesses:
        TotalBurst += float(Burst[z])
        z += 1
    TotalBurst += mgmo3Elzyadat
    TrueIndex = index
    while Time1(Time) <= TotalBurst:
        while i < 100000:
            if (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex])) == True and flag == 1):
                TimeIn.append(Time1(Time))
                ProcessIn.append("Null")
                flag = 0

            elif (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex]))) == True and (RemainingTime[TrueIndex] > 0.11):
                flag1 = 0
                counter = 0
                while counter < (len(Process)):
                    if (CheckArrive(Time1(Time), float(ArrivalT[counter])) == True) and (
                            RemainingTime[counter] < RemainingTime[TrueIndex]) and (RemainingTime[counter] > 0):
                        ProcessIn.append(Process[TrueIndex])
                        TimeIn.append(Time1(Time))
                        if ((TimeIn[len(TimeIn) - 1] == TimeIn[len(TimeIn) - 2]) and len(TimeIn) > 1):
                            ProcessIn.pop()
                            TimeIn.pop()
                        # print(Process[TrueIndex])
                        # print(Time1(Time))
                        flag1 = 1
                        IndexProcessOfLeastBurst = counter
                        TrueIndex = IndexProcessOfLeastBurst
                        TimeAfter = Time1(Time)
                    elif (CheckArrive(Time1(Time), float(ArrivalT[counter])) != True) or (
                            RemainingTime[counter] > RemainingTime[TrueIndex] or (len(Process) == 1)):
                        if flag1 != 1:
                            IndexProcessOfLeastBurst = TrueIndex

                    counter += 1
                RemainingTime[IndexProcessOfLeastBurst] -= 0.1
                RemainingTime1 = ['%.1f' % elem for elem in RemainingTime]
                # print(RemainingTime1[IndexProcessOfLeastBurst])
                Time += round(0.1, 1)

                i += 1

            elif (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex]))) == True and (
                    -0.1 <= RemainingTime[TrueIndex] <= 0.12):
                # print(Process[TrueIndex]+" is finished")
                Time += 0.1
                ProcessIn.append(Process[TrueIndex])
                TimeIn.append(Time1(Time))
                ProcessWaitingTime = (Time1(Time)) - round(float(ArrivalT[TrueIndex]), 1) - round(
                    float(Burst[TrueIndex]), 1)
                # print(("Process Waiting time is: ")+str(Time1(ProcessWaitingTime)))
                TotalWaitingTime += ProcessWaitingTime
                del Process[TrueIndex]
                del ArrivalT[TrueIndex]
                del Burst[TrueIndex]
                del RemainingTime[TrueIndex]
                del RemainingTime1[TrueIndex]
                i += 1
                TrueIndex = 0
                TimeAfter = Time1(Time)
                if (len(Process) == 0):
                    break

            elif (CheckArrive(TimeAfter, float(ArrivalT[TrueIndex])) == False):
                flag = 1
                Time += 0.1
                Time = Time1(Time)
                TimeAfter = Time1(Time)
        if (len(Process) == 0):
            break
    # for b in range(len(ProcessIn)):
    #     print(ProcessIn[b])
    #     print(TimeIn[b])

    AvgWaitingTime = TotalWaitingTime / NoOfProcesses
    return ProcessIn,TimeIn,AvgWaitingTime
    #print(("total AVG waiting time: ") + str(AvgWaitingTime))





def InputSjfNonPreemptive():
    NoOfProcesses = int(input())  # "Enter the no. of processes: "
    Process = []
    ArrivalT = []
    Burst = []
    for i in range(NoOfProcesses):
        data = input()  # Enter the process,arrival time,burst time
        X = data.split(',')
        Process.append(X[0])
        ArrivalT.append(X[1])
        Burst.append(X[2])
    return NoOfProcesses,Process,ArrivalT,Burst

def SJFNonPreemptive(NoOfProcesses,Process,ArrivalT,Burst):
    zyadat = []
    ProcessIn = []
    TimeIn = []
    flag = 0
    AA = 0
    index=0
    min=10000
    while AA < NoOfProcesses:
        zyadat.append(1000)
        AA += 1
    mgmo3Elzyadat = 0
    TotalWaitingTime = 0
    for i in range(NoOfProcesses):
        for x in range(i + 1, NoOfProcesses):
            if (float(ArrivalT[i]) + float(Burst[i]) < float(ArrivalT[x])):
                if ((float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))) < zyadat[i]):
                    zyadat[i] = float(ArrivalT[x]) - (float(ArrivalT[i]) + float(Burst[i]))

    for i in range (NoOfProcesses):
        if float(ArrivalT[i])<min:
           min=float(ArrivalT[i])
           index=i
    if min > 0:
        mgmo3Elzyadat += min

    for i in range(NoOfProcesses):
        if (zyadat[i] < 1000):
            mgmo3Elzyadat += zyadat[i]

    Time = 0
    TotalBurst = 0
    z = 0
    while z < NoOfProcesses:
        TotalBurst += float(Burst[z])
        z += 1
    TotalBurst += mgmo3Elzyadat
    TrueIndex = index
    while Time <= TotalBurst:
        while i < 100000:
            if (CheckArrive(Time, float(ArrivalT[TrueIndex])) == True and flag == 1):
                TimeIn.append(Time1(Time))
                ProcessIn.append("Null")
                flag = 0
            elif (CheckArrive(Time, float(ArrivalT[TrueIndex])) == True):
                flag1 = 0
                counter = 0
                while counter < len(Process):
                    if (CheckArrive(Time, float(ArrivalT[counter])) == True and float(Burst[counter]) < float(Burst[TrueIndex])):
                        flag1 = 1
                        IndexProcessOfLeastBurst = counter
                        TrueIndex = IndexProcessOfLeastBurst
                    else:
                        if flag1 != 1:
                            IndexProcessOfLeastBurst = TrueIndex
                    counter += 1

                i += 1
                Time += float(Burst[TrueIndex])
                ProcessIn.append(Process[TrueIndex])
                TimeIn.append(Time1(Time))
                # print(Time)
                # print(Process[TrueIndex]+" is finshed")
                ProcessWaitingTime = (Time1(Time)) - round(float(ArrivalT[TrueIndex]), 1) - round(float(Burst[TrueIndex]), 1)                # print(("Process Waiting time is: ")+str(ProcessWaitingTime))
                TotalWaitingTime += ProcessWaitingTime
                del Process[TrueIndex]
                del ArrivalT[TrueIndex]
                del Burst[TrueIndex]
                TrueIndex = 0
                if (len(Process) == 0):
                    break
            elif (CheckArrive(Time, float(ArrivalT[TrueIndex])) == False):
                flag = 1
                Time += 0.1
                Time = Time1(Time)
        if (len(Process) == 0):
            break
    #for b in range(len(ProcessIn)):
        #print(ProcessIn[b])
        #print(TimeIn[b])
    AvgWaitingTime = TotalWaitingTime / NoOfProcesses
    #print(("total AVG waiting time: ") + str(AvgWaitingTime))
    return ProcessIn, TimeIn, AvgWaitingTime





def main():
    SchedularType=input()
    if SchedularType=="sjf preemptive":
        NoOfProcesses, Process, ArrivalT, Burst, RemainingTime=InputSjfPreemptive()
        ProcessIn,TimeIn,AvgWaitingTime=SJFPreemptive(NoOfProcesses, Process, ArrivalT, Burst, RemainingTime)

        # --------------------------------For Testing Only---------------------------------

        for b in range(len(ProcessIn)):
            print(ProcessIn[b])
            print(TimeIn[b])
        print(("total AVG waiting time: ") + str(AvgWaitingTime))

        # ----------------------------------------------------------------------------------
    elif SchedularType=="sjf non preemptive":
        NoOfProcesses, Process, ArrivalT, Burst = InputSjfNonPreemptive()
        ProcessIn, TimeIn, AvgWaitingTime = SJFNonPreemptive(NoOfProcesses, Process, ArrivalT, Burst)
        # --------------------------------For Testing Only---------------------------------

        for b in range(len(ProcessIn)):
            print(ProcessIn[b])
            print(TimeIn[b])
        print(("total AVG waiting time: ") + str(AvgWaitingTime))

        # ----------------------------------------------------------------------------------





if __name__ == '__main__': main()