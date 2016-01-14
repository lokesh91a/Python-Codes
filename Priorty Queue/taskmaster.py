"""
taskmaster.py
author: James Heliotis
description: Task master implementation
"""


# from stack import Stack as Dispenser
from prioqueue import PriorityQueue as Dispenser

class Task:
    __slots__ = "time_left", "name", "time"

    def __init__( self, name, time ):
        self.time_left = time
        self.name = name
        self.time = time

TICK_CMD = "tick"
ADD_CMD = "add"
QUIT_CMD = "quit"
COMMANDS = ( TICK_CMD, ADD_CMD, QUIT_CMD )

def main():

    tasks = Dispenser(after)
    time = 0

    cmd, args = get_cmd( COMMANDS )
    while cmd != QUIT_CMD:
        if cmd == TICK_CMD:
            time += 1
            if not tasks.isEmpty():
                current = tasks.peek()
                current.time_left -= 1
                if current.time_left == 0:
                    print( "\nTask '" + current.name + \
                           "' completed at time " + str( time ) + "." )
                    tasks.remove()
                    if not tasks.isEmpty():
                        print( "New task is '" + tasks.peek().name + "'." )
                    else:
                        print( "Nothing else to do." )
            else:
                print( "Nothing to do." )
        elif cmd == ADD_CMD:
            new_task = Task( args[ 0 ], int( args[ 1 ] ) )
            tasks.insert( new_task )
            print( "\nAdded. Current task is '" + tasks.peek().name + \
                   "'." )
        else:
            assert True, "PROGRAM ERROR"
        cmd, args = get_cmd( COMMANDS )

    print( "\nTerminating the simulation." )

def get_cmd( choices ):
    line = input( "\nEnter one of " + str( choices ) + ": " ).split()
    cmd = line.pop( 0 )
    while cmd not in choices:
        print( "\n'" + cmd + "' is not a legal command. Try again." )
        line = input( "\nEnter one of " + str( choices ) + ": " ).split()
        cmd = line.pop( 0 )
    return cmd, line

def after(v,u):
    """ Compares two tasks ad returns true or false
            :param   v,u  These are two tasks
            :return: true  if v takes more time than u
                     false if v takes less or equal time than u
    """
    if v.time > u.time:
        return True
    elif v.time < u.time:
        return False
    elif v.time == u.time:
        return False

if __name__ == "__main__":
    main()