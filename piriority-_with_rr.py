def piriority_with_RR_input(no_pro,arr,time_slice):
    time_slice = time_slice#int(input("plese input the time slice "))

    time_slice=0
    no_pro = no_pro#int(input ("Enter the num of proccess"))
    bigger_list=[]
    total_time=0
    smaller_list=[]



    for iterator in range(0,no_pro):
      smaller_list= arr[iterator].split(",")     #input("please input the time  and arraival time and piriority of the process sperated by comma ").split(",")  #here we take the input as list
      smaller_list.append(0)
      smaller_list.append(0)
      smaller_list.append(0)
      smaller_list = [int(i) for i in smaller_list]
      smaller_list.insert(0,str("p{}".format(iterator)) )                                                          # here we write the name of each processor


      total_time =total_time+ int(smaller_list[1])
      bigger_list.append(smaller_list)                                                                                         #here we make list of lists

    return time_slice,bigger_list,no_pro,total_time






def same_piriority(queue):
    same_piriority_queue=[]
    for i in range (1,len(queue)):
        if (queue[0][3]==queue[i][3]):

            same_piriority_queue.append(queue[i])
            if(len(same_piriority_queue)==1):
                same_piriority_queue.insert(0,queue[0])

    return same_piriority_queue



def piriority_with_RR( time_slice,bigger_list,no_pro,total_time):
    current_time=0
    queue=[]
    out_time=[]
    out_queue=[]
    waiting_time_name =[]
    waiting_time_val=[]
    turn_around_queue=[]



    bigger_list.sort(key=lambda x:x[2])

    i=0
    while(i!=len(bigger_list)):                                                #here we puttin the proccess that reached at the second zero into the queue

        if(bigger_list[i][2]==0):
            queue.append(bigger_list[i])
            bigger_list.pop(i)
            i=i-1
        i=i+1
    #same_piriority(queue)


    while (current_time!=total_time):

        while (len(bigger_list )and current_time>=bigger_list[0][2]):
                queue.append(bigger_list[0])
                bigger_list.pop(0)

        queue.sort(key=lambda  x:x[3])




        if (len(queue)==0):                              #### this while to handle the issue if the processor was idle for a time it fill the queue again with the next one
            bigger_list.sort(key=lambda x:x[2])
            element = bigger_list[0]
            while (True):
                 queue.append(bigger_list[0])

                 current_time =bigger_list[0][2]
                 bigger_list.pop(0)

                 if (element[2]!=bigger_list[0][2]):
                     break;
            out_queue.append("null")
            out_time.append(current_time)




        if (len(same_piriority(queue))):

            same_piriority_queue=same_piriority(queue)
            length_of_same_piriority_queue = len(same_piriority_queue)

            while(len(same_piriority_queue)):


                chosen_val =same_piriority_queue[0][1]


                if( time_slice < chosen_val ):                                                        #lw el ba2i fl time bta3 el process is more  than the time slice or equal
                    if(queue[0][5]==0):
                        same_piriority_queue[0][5]=same_piriority_queue[0][5]+1
                        same_piriority_queue[0][4]=current_time-same_piriority_queue[0][3]

                    else:
                        same_piriority_queue[0][4]=same_piriority_queue[0][4]+current_time-same_piriority_queue[0][6]




                    out_time.append(current_time)
                    current_time =current_time+time_slice                                             #here we increase current_time by time slice
                    waiting_time_val.append(same_piriority_queue[0][4])
                    waiting_time_name.append(same_piriority_queue[0][0])
                    turn_around_queue.append(current_time-same_piriority_queue[0][2])
                    same_piriority_queue[0][6]=current_time
                    same_piriority_queue[0][1] = chosen_val  - time_slice                    #here we update the chosen  value after decreasing time slice from it
                    out_queue.append(same_piriority_queue[0][0])
                    #print(same_piriority_queue[0][0])
                    flag_trminated = False



                elif(time_slice==chosen_val or time_slice > chosen_val ):

                    if(queue[0][5]==0):
                        same_piriority_queue[0][5]=same_piriority_queue[0][5]+1
                        same_piriority_queue[0][4]=current_time-same_piriority_queue[0][3]

                    else:
                        same_piriority_queue[0][4]=same_piriority_queue[0][4]+current_time-same_piriority_queue[0][6]



                    if(time_slice==chosen_val ):
                        out_time.append(current_time)
                        current_time=current_time + time_slice                                                     #here we decrese every process py "el ba2i fiha " after excucuting it
                        waiting_time_val.append(same_piriority_queue[0][4])
                        waiting_time_name.append(same_piriority_queue[0][0])
                        turn_around_queue.append(current_time-same_piriority_queue[0][2])
                        same_piriority_queue[0][6]=current_time
                        same_piriority_queue[0][1] = chosen_val - time_slice
                        out_queue.append(same_piriority_queue[0][0])
                        #print(same_piriority_queue[0][0])

                        same_piriority_queue.pop(0)
                        flag_trminated = True


                    elif(time_slice > chosen_val ):
                        out_time.append(current_time)
                        current_time=current_time + chosen_val                              #here we decrese every process py "el ba2i fiha " after excucuting it
                        waiting_time_name.append(same_piriority_queue[0][0])
                        waiting_time_val.append(same_piriority_queue[0][4])
                        turn_around_queue.append(current_time-same_piriority_queue[0][2])
                        same_piriority_queue[0][6]=current_time
                        same_piriority_queue[0][1] = 0
                        out_queue.append(same_piriority_queue[0][0])
                        #print(same_piriority_queue[0][0])
                        same_piriority_queue.pop(0)
                        flag_trminated = True







                if( flag_trminated == False):
                    the_completed_process =same_piriority_queue[0]
                    same_piriority_queue.pop(0)
                    same_piriority_queue.append(the_completed_process)


            for i in range(0,length_of_same_piriority_queue):
                queue.pop(0)

        else:
            out_time.append(current_time)                         #here is different from RR_WITH arrivel as we out time [] is printed before adding current time
            waiting_time_name.append(queue[0][0])
            waiting_time_val.append(current_time-queue[0][2])
            current_time=current_time+queue[0][1]
            turn_around_queue.append(current_time-queue[0][2])
            queue[0][6]=current_time
            out_queue.append(queue[0][0])
            #print(queue.pop(0))
            queue.pop(0)



    total_waiting=0
    total_turnaround=0
    for i in range (0,len(waiting_time_name)):
        total_waiting =waiting_time_val[i]+total_waiting
        total_turnaround=turn_around_queue[i]+total_turnaround

    avg_waiting=(total_waiting/no_pro)
    avg_turn=(total_turnaround/no_pro)




    return out_queue,out_time,waiting_time_name,waiting_time_val,turn_around_queue,avg_waiting,avg_turn






time_slice,bigger_list,no_pro,total_time= piriority_with_RR_input()
list1,list2,list3,list4,list5,avgwaiting,avgturn=piriority_with_RR(time_slice,bigger_list,no_pro,total_time)


print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(avgwaiting)
print(avgturn)






'''
example 1 
3,1,0
4,2,0
1,3,0
2,1,3

example 2 


3,0,2
5,2,6
4,1,3
2,4,5
9,6,7
4,5,4
10,7,10




example 3 

4,0,3
5,0,2
8,0,2
7,0,1
3,0,3

slice =2


'''


