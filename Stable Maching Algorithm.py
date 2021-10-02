

N = 5 #Here ,No. of cars = No. of Slots = 5
def carPreferslot1Overslots(matrix, car, slot, slot1):
	for i in range(N): 
		if (matrix[car][i] == slot1): #preference to slot1
			return True
		if (matrix[car][i] == slot): #preference to slot
			return False
def stableMatching(matrix): 
	carPartner = [-1 for i in range(N)]  #initially all cars are free(-1)
	slotFree = [False for i in range(N)]  #initially slots set to false means slots are free
	freeCount = N                #initially both the car and slot set to free
	while (freeCount > 0):  #Here we are starting the iteration through slots
		slot = 0              #starting from first free slot
		while (slot < N): 
			if (slotFree[slot] == False): #got here the first free slot
				break
			slot += 1
		i = 0
		while i < N and slotFree[slot] == False:  #starting with that free slot 
			car = matrix[slot][i]                #preferences
			if (carPartner[car - N] == -1):        #here if car is free
				carPartner[car - N] = slot        #then pair car with slot
				slotFree[slot] = True
				freeCount -= 1     #1 slot paired,so decreasing freecount by 1
			else:                    #else if car is already paired
				slot1= carPartner[car - N]  #find the slot of that car
				if (carPreferslot1Overslots(matrix,car,slot,slot1) == False): #check car's preference once again,then if car prefers slot than slot1
					carPartner[car - N] = slot                                   #then pair car with slot
					slotFree[slot] = True
					slotFree[slot1] = False                   #Now slot1 is rejected and is free now
			i += 1
	print("Car ", " Slot") 
	for i in range(N): 
		print(i + N, "\t", carPartner[i])  #Print the final matched stable pairs of Cars And Slots
      
        
matrix = [[5,6,8,7,9],
          [6,5,7,9,8],
          [7,8,9,6,5],
          [5,7,6,9,8],
          [9,7,8,5,6],
          
          [4,2,3,1,0],
          [4,3,1,0,2],
          [0,2,3,1,4],
          [3,2,0,1,4],
          [2,3,4,0,1]]
#The above matrix has 0-2*N (Here N=5)rows 0-4 is for car code 
# and their pref. and 5-9 is for car-slot code and their preferences.

stableMatching(matrix) 

