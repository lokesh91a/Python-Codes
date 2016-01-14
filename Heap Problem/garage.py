__author__ = 'Sahil Jasrotia and Lokesh Agrawal'

class Job:
    '''
    This is the Job class that defines the actual Job in Garag
    Job Object will maintain location of a Job in both the heaps
    '''
    __slots__ = 'cathyindex','howardindex','jobname','time','cost'

    def __init__(self,val,cathyindex=0,howardindex=0):
        '''
        Constructor to initialize the Job object
        '''
        self.jobname = val[0]
        self.time = float (val[1])
        self.cost = float (val[2])
        self.cathyindex = cathyindex
        self.howardindex = howardindex

class Garage:
    '''
    Garage class which implements the actually Job evaluation algorithm
    '''
    __slots__ = 'cathylist', 'howardlist','size'

    def __init__(self):
        # Initialize the garage object
        self.cathylist = []
        self.howardlist = []
        self.size = 0

    def __inserttocathylist(self,loc):
        '''
        This function inserts the incoming job to cathy list using heap
        algorithm
        :param loc: The location where the job needs to be inserted to the list
        '''

        # Base case. Return if a node doesnt have a parent
        if loc == 0:
            return
        else:
            # recursively check if current Jobs cost is greater than its parent cost.
            # If it so then swap the current Job with its parent. The below logic will
            # bubble up the highest cost Job to the top of the list
            parent = (loc-1)//2
            if self.cathylist[loc].cost > self.cathylist[parent].cost:
                self.cathylist[loc],self.cathylist[parent] = self.cathylist[parent],self.cathylist[loc]
                self.cathylist[loc].cathyindex = loc
                self.cathylist[parent].cathyindex = parent
                return self.__inserttocathylist(parent)

    def heapifycathy(self,loc):
        '''
        This function heapifies the cathy's list after a Job is deleted from the Heap
        :param loc: current location of the Job in the heap which we are comparing
        '''

        # Recursively Compare the current Job with its child jobs to get the costliest
        # Job at the top of the Heap. This algorithm with bubble down the cheap Job to its
        # correct location
        max = loc
        leftchild = (2*loc) +1
        rightchild = (2*loc) + 2
        if leftchild > self.size-1 and rightchild > self.size-1:
            return
        if leftchild <= self.size-1:
            if self.cathylist[leftchild].cost > self.cathylist[max].cost:
                max = leftchild
        if rightchild <= self.size-1:
            if self.cathylist[rightchild].cost > self.cathylist[max].cost:
                max = rightchild
        if loc == max:
            return
        self.cathylist[loc],self.cathylist[max] = self.cathylist[max],self.cathylist[loc]
        self.cathylist[loc].cathyindex,self.cathylist[max].cathyindex = self.cathylist[max].cathyindex,\
                                                                        self.cathylist[loc].cathyindex
        return self.heapifycathy(max)

    def heapifyhoward(self,loc):
        '''
        This function heapifies the howard list after a Job is deleted from the Heap
        :param loc: current location of the Job in the heap which we are comparing
        '''

        # Recursively Compare the current Job with its child jobs to get the min time
        # taking Job at the top of the Heap. This algorithm with bubble down the highest
        # time taking Job to its correct position
        min = loc
        leftchild = (2*loc) +1
        rightchild = (2*loc) + 2
        if leftchild > self.size-1 and rightchild > self.size-1:
            return
        if leftchild <= self.size-1:
            if self.howardlist[leftchild].time < self.howardlist[min].time:
                min = leftchild
        if rightchild <= self.size-1:
            if self.howardlist[rightchild].time < self.howardlist[min].time:
                min = rightchild
        if loc == min:
            return
        self.howardlist[loc],self.howardlist[min] = self.howardlist[min],self.howardlist[loc]
        self.howardlist[loc].howardindex,self.howardlist[min].howardindex = self.howardlist[min].howardindex,\
                                                                            self.howardlist[loc].howardindex
        return self.heapifyhoward(min)

    def __inserttohowardlist(self,loc):
        '''
        This function inserts the incoming job to howard list using heap
        algorithm
        :param loc: The location where the job needs to be inserted to the list
        '''

        # Base case. Return if a node doesnt have a parent
        if loc == 0:
            return
        else:
            # recursively check if current Jobs time is less than its parent time.
            # If it so then swap the current Job with its parent. The below logic will
            # bubble up the lowest time taking Job to the top of the list
            parent = (loc-1)//2
            if self.howardlist[loc].time < self.howardlist[parent].time:
                self.howardlist[loc],self.howardlist[parent] = self.howardlist[parent],self.howardlist[loc]
                self.howardlist[loc].howardindex = loc
                self.howardlist[parent].howardindex = parent
                return self.__inserttohowardlist(parent)

    def addjob(self,val):
        '''
        Add Job to cathy's list and to the Howard's list
        :param val: the job that needs to be added
        '''

        # Adds the Jobs to both Job list and then maintain the heap property
        # The Job object will maintain location of job in both the heaps
        job = Job(val,self.size,self.size)
        self.cathylist.append(job)
        self.howardlist.append(job)
        self.size +=1
        self.__inserttocathylist(self.size-1)
        self.__inserttohowardlist(self.size-1)

    def deletecathyjob(self):
        '''
        Delete cathy's Job from the heap when cathy is ready for doing Job.
        Also delete the same Job from the Howard's list and then heapify both
        the heaps
        '''
        if len(self.cathylist)==0:
            print("No Job for Cathy to assign")
            return
        else:
            print("Cathy starting job " + self.cathylist[0].jobname)
            howardindex = self.cathylist[0].howardindex
            self.size -=1
            if self.size == 0:
                self.cathylist.pop(self.size)
                self.howardlist.pop(self.size)
            else:
                self.cathylist[0]= self.cathylist.pop(self.size)
                self.cathylist[0].cathyindex = 0
                if howardindex == self.size:
                    self.howardlist.pop(self.size)
                else:
                    self.howardlist[howardindex] = self.howardlist.pop(self.size)
                    self.howardlist[howardindex].howardindex = howardindex
                    self.heapifyhoward(howardindex)
                self.heapifycathy(0)

    def deletehowardjob(self):
        '''
        Delete Howard's Job from the heap when Howard is ready for doing Job.
        Also delete the same Job from the Cathy's list and then heapify both
        the heaps
        '''
        if len(self.howardlist) == 0:
            print("No Job for Howard to assign")
            return
        else:
            print("Howard starting job " + self.howardlist[0].jobname)
            cathyindex = self.howardlist[0].cathyindex
            self.size -=1
            if self.size == 0:
                self.cathylist.pop(self.size)
                self.howardlist.pop(self.size)
            else:
                self.howardlist[0]= self.howardlist.pop(self.size)
                self.howardlist[0].howardindex = 0
                if cathyindex == self.size:
                    self.cathylist.pop(self.size)
                else:
                    self.cathylist[cathyindex] = self.cathylist.pop(self.size)
                    self.cathylist[cathyindex].cathyindex = cathyindex
                    self.heapifycathy(cathyindex)
                self.heapifyhoward(0)

def main():
    '''
    This is the main function which runs the garage as an when Job
    comes. The data structure we are using is two heaps each for cathy
    and howard
    :return: None
    '''

    # Initialize the Garage class so that Jobs can be performed.
    garage = Garage()
    try:
        filename = input("Enter File Name: ")
        # Read the file for incoming Jobs
        with open(filename) as f:
            for line in f:
                line = line.strip()
                # If Cathy is ready for the Job let her do it
                if line == 'Cathy ready':
                    garage.deletecathyjob()
                elif line == 'Howard ready':
                    # If Howard is ready for the Job let him do it
                    garage.deletehowardjob()
                elif len(line) == 0:
                    continue
                else:
                    # New Job has arrived so add it to garage
                    line = line.split(' ')
                    print("New job arriving! Job name: " + line[0] + ", " + line[1] + " hours and $" + line[2])
                    garage.addjob(line)
    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    main()