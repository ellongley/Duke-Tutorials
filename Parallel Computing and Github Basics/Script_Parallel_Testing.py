from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = np.array([(x+1) for x in range(size)]) #so at least one obj per node
    #data = np.append(data,[9,9,9,9]) #this wont work, can only scatter # = size for this command
    print('we will be scattering:',data)
else:
    data = None

data_scat = comm.scatter(data,root=0)
print('rank',rank,'has scattered data = ', data_scat)
if rank == 0:
    print('this is rank 0')
    print('data = ',data)
    print('data_scat = ',data_scat)

data_scat = data_scat*2
dataNew = comm.gather(data_scat,root=0)
if rank == 0:
    print('this is rank 0, dataNew = ', dataNew)
print(rank,'check',dataNew)#for other non-0 nodes, this will report None
print(rank,'check',data_scat)#the nodes still retained the gathered data 
