__author__ = 'Lokesh Agrawal' , 'Sahil Jasrotia'
import math
from set import SetType
from collections.abc import Iterator
class LinkedHashTable(SetType):

    __slots__ = 'size', 'capacity', 'first', 'last', 'list', 'modcount', 'load_limit', 'min_bucket'

    def __init__(self, initial_num_buckets=100, load_limit=0.75):
        """
        This class just keeps the state information about the
        'size', or number of entries in the set.
        (So, all sets must manually maintain their number of entries.)
        """
        self.size = 0
        self.capacity = initial_num_buckets
        self.first = None
        self.last = None
        self.modcount = 0
        self.load_limit = load_limit
        self.min_bucket = 10
        #for checking the condition of minimum buckets
        if self.min_bucket>initial_num_buckets:
            self.capacity = self.min_bucket
        self.list = [None]*self.capacity
    def find(self, obj):
        """
        This function is the helping function for contains
        :param obj:
        :return:True  : If the objects is found in hashtable
                False : If the object is not found in hash table
                index : the index at which the object is supposed to be
        """
        index = self.hashvalue(obj)
        pointer = self.list[index]

        if pointer != None:
            #if object is found at the index in list
            if pointer.value == obj:
                return True, index

            else:
                #if object is found at somewhere in the linkedlist in the
                # hashtable
                while pointer.chain != None:
                    pointer = pointer.chain
                    if pointer.value == obj:
                        return True, index
                if pointer.value == obj:
                        return True, index

        #otherwise return false
        return False, index

    def contains( self, obj ):
        """
        Is the given obj in the set?
        The answer is determined through use of the '==' operator,
        i.e., the __eq__ method.
        :return: True iff obj or its equivalent has been added to this set
                       and not removed
        """
        #calls a helping function find and prints the result
        decision, index = self.find(obj)
        return decision


    def add( self, obj ):
        """
        Insert a new object into the set.
        Do not add if self.contains(obj).
        :param obj: the object to add
        :return: None
        :post: self.contains( obj )
        """
        #checks if the loadlimit has been exceeded then calls the rehash
        # function with the new capacity of list
        if self.size//self.capacity>=self.load_limit:
            self.rehash(2*self.capacity)

        #call the find method to check if list already contains obj
        decision, index = self.find(obj)

        #if it already contains the obj then return without doing anything
        if decision == True:
            return

        index = self.hashvalue(obj)
        pointer = self.list[index]

        #case when the object to be added is the first one
        if self.size == 0:
            self.list[index] = node(obj)
            self.first = self.list[index]
            self.last = self.list[index]

        #case when object to be added is not first and the index at which it
        # will be added containe None
        elif self.list[index] == None:
            self.list[index] = node(obj)
            self.last.next = self.list[index]
            self.list[index].previous = self.last
            self.last = self.list[index]

        #case when object to be added is not first and it is added as the last
        #element in the linked list present at the index
        else:
            while pointer.chain != None:
                pointer = pointer.chain
            pointer.chain = node(obj)
            self.last.next = pointer.chain
            pointer.chain.previous = self.last
            self.last = pointer.chain

        #increase the size and modcount by 1
        self.size = self.size + 1
        self.modcount = self.modcount + 1

    def remove( self, obj ):
        """
        Remove an object from the set.
        :param obj: the value to remove
        :return: None
        :post: not self.contains( obj )
        """

        #Checks if the load factor is less than 1-load_factor then call the
        # rehash function with the capacity as presentcapacity/2
        if self.size//self.capacity<=(1-self.load_limit):
            self.rehash(self.capacity//2)

        #call the find function to check if the hashset contains the object to
        # be removed or not
        decision, index = self.find(obj)
        pointer = self.list[index]


        if decision:
            #case when the object to be removed is the first object in the
            # sequence
            if self.first.value == obj:
                self.list[index] = self.first.chain
                self.first = self.first.next

            #case when the object to be removed is not first object in the
            # sequence but is present at the index
            elif self.list[index].value == obj:
                if self.list[index].value == self.last.value:
                    self.last.previous.next = None
                    self.last = self.last.previous
                    self.list[index] = self.list[index].chain

                else:
                    self.list[index].previous.next = self.list[index].next
                    self.list[index].next.previous = self.list[index].previous
                    self.list[index] = self.list[index].chain

            #case when the object to be removed is present somewhere in the
            # linked list
            else:
                #finds the position of the obj in the linked list(one back than
                #  it should be)
                while pointer.chain.value != obj:
                    pointer = pointer.chain

                #if last is equal to this pointer
                if self.last.value == pointer.chain.value:
                    temp = pointer.chain
                    pointer.chain = pointer.chain.chain
                    temp.previous.next = temp.next
                    self.last.previous.next = None
                    self.last = self.last.previous

                #if last is not equal to this pointer
                else:
                    temp = pointer.chain
                    pointer.chain = pointer.chain.chain
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous

            #Decrese the size and modification count by 1
            self.size = self.size - 1
            self.modcount = self.modcount + 1

        else:
            raise Exception('Trying to remove ' + obj +  ' which doesnt exist')

    def __iter__( self ):
        """
        Build an iterator.
        :return: an iterator for the current elements in the set
        """
        #creates an object of iterator and returns the object of iterator
        iterator = self.iterator(self.first, self.last, self.modcount)
        return iterator


    def hashvalue(self, obj):
        '''
        Creates the hashvalue of the obj and dives it by the currentcapacity
        and returns it
        :param obj: The object whose hashvalue is to be calculated
        :return:index: the place where this object is supposed to be
        '''
        st = str(obj)
        hashvalue = 0
        for number in range(len(st)):
            hashvalue = hashvalue + (ord(st[number])*(31**number))
        hashvalue = hashvalue%self.capacity
        return hashvalue

    def rehash(self, newcapacity):
        """
        Rehash function rehases the list
        :param newcapacity: new capacity: increases in case of add and decreases
                            in case of remove
        :return:
        """
        #new capacity is assigned
        self.capacity = newcapacity

        #size becomes 0
        self.size = 0

        #new list with None type is created of new capacity
        self.list = [None]*self.capacity

        #reference of first is taken in a variable
        oldfirst = self.first

        #For all elements which can be traveresed through first(all), new
        #hashtable is made
        while oldfirst.next != None:
            self.add(oldfirst.value)
            oldfirst = oldfirst.next
        self.add(oldfirst.value)

    def __str__(self):
        """
        to string method.
        :return:Returns the content of the table
        """
        #iterator = self.__iter__()
        pointer = self.first
        result=''
        while pointer.next != None:
            result = result + pointer.value + '\n'
            pointer = pointer.next
        A = result + pointer.value
        return A

    class iterator(Iterator) :
        """
        Class Iterator which extends the original Iterator class
        and returns the object one by one in the sequence of addition
        """
        __slots__ = 'first', 'last', 'modcount', 'pointer'

        def __init__(self, first, last, modcount):
            self.first = first
            self.last = last
            self.modcount = modcount
            self.pointer = first

        def __iter__(self):
            return self

        def hasnext(self):
            return self.pointer != None

        #Returns value if exist otherwise stops Iteration
        def __next__(self):
            if self.modcount != self.modcount:
                raise ValueError
            if self.hasnext():
                value = self.pointer.value
                self.pointer = self.pointer.next
                return value
            else:
                raise StopIteration()

class node:
    """
    node class which is used to store 4 references
    value   : value of object
    previous: reference of previous object added
    next    : refrence of next object that will be added
    chain   : reference of chain link(link of node in linkedlist) if exists
    """
    __slots__=  'value', 'previous', 'next', 'chain'

    def __init__(self, value, previous, next, chain):
        self.value = value
        self.previous = previous
        self.next = next
        self.chain = chain

    def __init__(self, value, previous):
        self.value = value
        self.previous = previous
        self.next = None
        self.chain = None

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
        self.chain = None