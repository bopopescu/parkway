from gpiozero import DistanceSensor as distsense
from time import sleep

'''
def status_change(status):
    if status==6:
        print("Status changed to occupied")
    elif status==0:
        print("Status changed to unoccupied")
    else:
        print("ERROR")
'''

if __name__ =="__main__":
    sensor = distsense(trigger = 18, echo = 24)
    dis_vec = [False]*6 

    #init database connection

    while True:
        sleep(2)
        distance = round((sensor.distance*100),2)
        #print ("Distance: {}cm ".format(distance), end = ' ') #check why this is printing together
        
        check = sum(dis_vec)
        if sum(dis_vec)==5 and distance <99:
        	print("Change status to occupied") #run update into query

        if sum(dis_vec)==1 and distance>99:
        	print("Change status to unoccupied")

        if distance <99 :
            dis_vec.append(True)
        else:
            dis_vec.append(False)

        dis_vec.pop(0)        
        




        



        
        

        
    
