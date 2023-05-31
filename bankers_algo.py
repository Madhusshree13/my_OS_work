
# # Python3 program to illustrate
# # Banker's Algorithm
 
# # Number of processes
# P = 5
 
# # Number of resources
# R = 3
 
# # Function to find the need of each process
# def calculateNeed(need, maxm, allot):
 
#     # Calculating Need of each P
#     for i in range(P):
#         for j in range(R):
             
#             # Need of instance = maxm instance -
#             # allocated instance
#             need[i][j] = maxm[i][j] - allot[i][j]
 
# # Function to find the system is in
# # safe state or not
# def isSafe(processes, avail, maxm, allot):
#     need = []
#     for i in range(P):
#         l = []
#         for j in range(R):
#             l.append(0)
#         need.append(l)
         
#     # Function to calculate need matrix
#     calculateNeed(need, maxm, allot)
 
#     # Mark all processes as infinish
#     finish = [0] * P
     
#     # To store safe sequence
#     safeSeq = [0] * P
 
#     # Make a copy of available resources
#     work = [0] * R
#     for i in range(R):
#         work[i] = avail[i]
 
#     # While all processes are not finished
#     # or system is not in safe state.
#     count = 0
#     while (count < P):
         
#         # Find a process which is not finish
#         # and whose needs can be satisfied
#         # with current work[] resources.
#         found = False
#         for p in range(P):
         
#             # First check if a process is finished,
#             # if no, go for next condition
#             if (finish[p] == 0):
             
#                 # Check if for all resources
#                 # of current P need is less
#                 # than work
#                 for j in range(R):
#                     if (need[p][j] > work[j]):
#                         break
                     
#                 # If all needs of p were satisfied.
#                 if (j == R - 1):
                 
#                     # Add the allocated resources of
#                     # current P to the available/work
#                     # resources i.e.free the resources
#                     for k in range(R):
#                         work[k] += allot[p][k]
 
#                     # Add this process to safe sequence.
#                     safeSeq[count] = p
#                     count += 1
 
#                     # Mark this p as finished
#                     finish[p] = 1
 
#                     found = True
                 
#         # If we could not find a next process
#         # in safe sequence.
#         if (found == False):
#             print("System is not in safe state")
#             return False
         
#     # If system is in safe state then
#     # safe sequence will be as below
#     print("System is in safe state.",
#               "\nSafe sequence is: ", end = " ")
#     print(*safeSeq)
 
#     return True
 
# # Driver code
# if __name__ =="__main__":
     
#     processes = [0, 1, 2, 3, 4]
 
#     # Available instances of resources
#     avail = [3, 3, 2]
 
#     # Maximum R that can be allocated
#     # to processes
#     maxm = [[7, 5, 3], [3, 2, 2],
#             [9, 0, 2], [2, 2, 2],
#             [4, 3, 3]]
 
#     # Resources allocated to processes
#     allot = [[0, 1, 0], [2, 0, 0],
#              [3, 0, 2], [2, 1, 1],
#              [0, 0, 2]]
 
#     # Check system is in safe state or not
#     isSafe(processes, avail, maxm, allot)



# def main():
#     processes = int(input("number of processes : "))
#     resources = int(input("number of resources : "))
#     max_resources = [int(i) for i in input("maximum resources : ").split()]

#     print("\n-- allocated resources for each process --")
#     currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

#     print("\n-- maximum resources for each process --")
#     max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

#     allocated = [0] * resources
#     for i in range(processes):
#         for j in range(resources):
#             allocated[j] += currently_allocated[i][j]
#     print(f"\ntotal allocated resources : {allocated}")

#     available = [max_resources[i] - allocated[i] for i in range(resources)]
#     print(f"total available resources : {available}\n")

#     running = [True] * processes
#     count = processes
#     while count != 0:
#         safe = False
#         for i in range(processes):
#             if running[i]:
#                 executing = True
#                 for j in range(resources):
#                     if max_need[i][j] - currently_allocated[i][j] > available[j]:
#                         executing = False
#                         break
#                 if executing:
#                     print(f"process {i + 1} is executing")
#                     running[i] = False
#                     count -= 1
#                     safe = True
#                     for j in range(resources):
#                         available[j] += currently_allocated[i][j]
#                     break
#         if not safe:
#             print("the processes are in an unsafe state.")
#             break

#         print(f"the process is in a safe state.\navailable resources : {available}\n")


# if __name__ == '__main__':
#     main()



# Banker's Algorithm

# Driver code:
if __name__=="__main__":
	
	# P0, P1, P2, P3, P4 are the Process names here
	n = 5 # Number of processes
	m = 3 # Number of resources
	
	# Allocation Matrix
	alloc = [[0, 1, 0 ],[ 2, 0, 0 ],
			[3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]]
	
	# MAX Matrix
	max = [[7, 5, 3 ],[3, 2, 2 ],
			[ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]]
	
	avail = [3, 3, 2] # Available Resources
	
	f = [0]*n # this array keeps track of whether the process has been allocated to a resource or not
	ans = [0]*n #this is an array that keeps track of the safe sequence of the array
	ind = 0 # index value of the answers
	for k in range(n):
		f[k] = 0  # this creates an array of value 0's
		
	need = [[ 0 for i in range(m)]for i in range(n)]
	for i in range(n):
		for j in range(m):
			need[i][j] = max[i][j] - alloc[i][j]
	y = 0
	for k in range(5):
		for i in range(n):
			if (f[i] == 0):
				flag = 0
				for j in range(m):
					if (need[i][j] > avail[j]):
						flag = 1
						break
				
				if (flag == 0):
					ans[ind] = i
					ind += 1
					for y in range(m):
						avail[y] += alloc[i][y]
					f[i] = 1
					
	print("Following is the SAFE Sequence")
	
	for i in range(n - 1):
		print(" P", ans[i], " ->", sep="", end="")
	print(" P", ans[n - 1], sep="")
