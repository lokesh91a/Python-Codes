"""
priorityqueue.py
author: Sahil Jasrotia and Lokesh Agrawal
description: A Priority queue implementation
"""
class LinkedNode:

    #Defining class variables
    __slots__ = ('value','link')

    def __init__(self,value,link=None):
        """ Create a node with a particular value
        """
        self.value = value
        self.link = link

class PriorityQueue:

    #Class Variables.
    __slots__ = "front","comparator"


    def __init__( self , comparator):
        """ Create a new empty queue.
        """
        self.front = None
        self.comparator = comparator

    def __str__( self ):
        """ Return a string representation of the contents of
            this queue, oldest value first.
        """
        result = "PriorityQueue["
        n = self.front

        #All values are saved in the result till the time it doesnt find next
        #link
        while n != None:
            result += " " + str( n.value )
            n = n.link
        result += " ]"

        #returns result
        return result

    def isEmpty( self ):
        """ Tells if this queue is empty
            :param   self: passing the reference of queue to chcek on its
                           contents
            :return: true  if queue is empty
                     false if queue is not empty
        """
        return self.front == None

    def enqueue( self, newValue ):
        """ Each node is added at location depending on the priority it has
            :param   self: passing the reference of queue to chcek on its
                           contents
					 newValue: The new Value that needs to be added to queue
            :return: None
        """
        newNode = LinkedNode( newValue )
        node = self.front

        #If queue is empty then adds a new node
        if self.front == None:
            self.front = newNode

        else:
            #Comparator is a function from taskmaster which returns true or
            #false. If true is returned then a new node is added and made as
            #front
            if self.comparator(node.value,newNode.value):
                newNode.link = self.front
                self.front = newNode
            else:
                #loop will execute till the time it will find the last node in
                #queue
                while node.link != None:
                    # We are enqueueing the elements depending on the priorty
                    # parameters set by the camparator function
                    if self.comparator(node.link.value,newNode.value):
                        newNode.link = node.link
                        node.link = newNode
                        break;
                    #node points to the next node
                    node = node.link
					
				        # We traversed the whole list and if we were not able to add
			          # the element to the list means this is the least priorty task
				        # so add it to the end of the queue
                if node.link == None:
                    node.link = newNode

    def dequeue( self ):
        """ Deletes a node from the queue
            :param   self: passing the reference of queue to chcek on its
                           contents
            :return: None
        """
        assert not self.isEmpty(), "Dequeue from empty queue"
        self.front = self.front.link

    def peek( self ):
        """ Returns the element of the queue which is waiting for coming out
            :param   self: passing the reference of queue to chcek on its
                           contents
            :return: Returns front of queue
        """
        assert not self.isEmpty(), "peek on empty stack"
        return self.front.value

    insert = enqueue
    remove = dequeue

def why_not(v,u):
    return False

def test():
    """ Test method. If why_not is given as an input
        then first element will be returned always
            :param   None
            :return: None
    """
    my_q = PriorityQueue(why_not)
    my_q.enqueue(8)
    my_q.enqueue(4)
    my_q.enqueue(3)
    my_q.enqueue(7)
    my_q.enqueue(2)
    my_q.enqueue(5)
    my_q.enqueue(1)
    print("why_not Comparator Test")
    print(my_q)    
    
    #Prints top of queues
    print("Dequeuing  " + str(my_q.peek()))
    
    print( "Removing:", my_q.peek() )
    my_q.remove()
    print( my_q )

    #It gives the output from the queue based on the priorty.
    #Lower the id highest the priorty in this case
    my_q = PriorityQueue(lambda v, u: id(v) > id(u))
    my_q.enqueue(8)
    my_q.enqueue(4)
    my_q.enqueue(3)
    my_q.enqueue(7)
    my_q.enqueue(2)
    my_q.enqueue(5) 
    print("lambda Comparator Test")   
    print(my_q)
    print("Dequeuing  " + str(my_q.peek()))
    
    print( "Removing:", my_q.peek() )
    my_q.remove()
    print( my_q )

if __name__ == '__main__':
    test()
