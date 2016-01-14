""" 
file: tests.py
description: 3 test cases for linkedhashtable
"""

__author__ = [ "Lokesh Agrawal", "Sahil Jasrotia" ]

from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    for word in a_set:
        print( word, end=" " )
    print()

def test1():
    """
    This test checks the size, ordering, remove, contains and add
    adds some objects in order
    try to add duplicate objects
    check contains on some objects
    removes some objects
    check contains on removed objects
    """
    print("Test 1 :")
    table = LinkedHashTable()
    table.add( "This" )
    table.add( "is" )
    table.add( "test" )
    table.add( "one" )
    table.add( "which" )
    table.add( "checks" )
    table.add( "the" )
    table.add( "ordering" )
    table.add( "of" )
    table.add( "the" )
    table.add( "data" )
    table.add( "entered" )
    table.add( "in" )
    table.add( "hashset" )

    #checks for duplicate values
    table.add( "ordering" )
    table.add ( "entered" )
    table.add ( "hashset" )
    table.add ( "one" )

    print_set( table )
    print("Size " + str(table.size))

    #Checks the contains function
    print( "'This' in table?", table.contains( "This" ) )
    print( "'is' in table?", table.contains( "is" ) )
    print( "'test' in table?", table.contains( "test" ) )
    print( "'one' in table?", table.contains( "one" ) )
    print( "'of' in table?", table.contains( "of" ) )
    print( "'the' in table?", table.contains( "the" ) )
    print( "'hashset' in table?", table.contains( "hashset" ) )

    print('\nRemoving some data')
    table.remove( "ordering" )
    table.remove( "This" )
    table.remove( "is" )
    table.remove( "the" )
    table.remove( "hashset" )
    table.remove( "test" )

    print_set( table )
    print("Size " + str(table.size))

    print( "'ordering' in table?", table.contains( "ordering" ) )
    print( "'hashset' in table?", table.contains( "hashset" ) )
    print( "'the' in table?", table.contains( "the" ) )



def test2():
    """
    Adds few objects in the hashset
    check contains function on few
    Now, in this test all elements which were added are removed from the hashset
    size is checked
    Now, again contains is checked for few
    :return:
    """
    print("\nTest 2 : ")
    table = LinkedHashTable()
    table.add( "This" )
    table.add( "is" )
    table.add( "test" )
    table.add( "2" )
    table.add( "which" )
    table.add( "checks" )
    table.add( "the" )
    table.add( "hashset" )

    print_set( table )
    print("Size " + str(table.size))
    print( "'2' in table?", table.contains( "2" ) )
    print( "'three' in table?", table.contains( "three" ) )
    print( "'hashset' in table?", table.contains( "hashset" ) )


    table.remove( "This" )
    table.remove( "is" )
    table.remove( "test" )
    table.remove( "2" )
    table.remove( "which" )
    table.remove( "checks" )
    table.remove( "the" )
    table.remove( "hashset" )

    print_set( table )
    print("Size " + str(table.size))
    print( "'two' in table?", table.contains( "two" ) )
    print( "'three' in table?", table.contains( "three" ) )
    print( "'hashset' in table?", table.contains( "hashset" ) )


def test3():
    """
    This is last test which checks the following things

    adds 4 objects
    removes 3 of them
    Now, it tries to remove the object which doesn't exist which raises an
    exception "Trying to remove ' + obj +  ' which doesnt exist"
    """
    print("\nTest 3 : ")
    table = LinkedHashTable(1)
    table.add( "I" )
    table.add( "am" )
    table.add( "last" )
    table.add( "test" )

    print_set( table )
    print("Size " + str(table.size))
    print( "'I' in table?", table.contains( "I" ) )
    print( "'am' in table?", table.contains( "am" ) )
    print( "'last' in table?", table.contains( "last" ) )


    table.remove( "I" )
    table.remove( "am" )
    table.remove( "last" )

    print()
    print_set( table )
    print("Size " + str(table.size))
    print( "'I' in table?", table.contains( "I" ) )
    print( "'am' in table?", table.contains( "am" ) )
    print( "'last' in table?", table.contains( "last" ) )

    table.remove(" 'remove' ")

if __name__ == '__main__':
    test1()
    test2()
    test3()

