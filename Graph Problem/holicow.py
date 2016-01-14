import  math

class type:
    '''
    A vertex which contains 3 parameters
    type: type as cow or a paintball
    name: name of the paintball or a cow
    neighbours: list of all its neighbours
    '''
    __slots__ = 'type', 'name', 'neighbours'

    def __init__(self, type, name):
        self.type = type
        self.name = name

        #initializes the neighbours as a empty list
        self.neighbours = []


def distance(datanew, dataold):
    '''

    :param datanew: a vertex of type paintball
    :param dataold: a vertex of any type
    :return: true : if a paintball or a cow is in the range of the particular
                    paintball
             false: if a paintball or a cow is not in the range of the
                    particular paintball
    '''
    return (math.sqrt(math.pow(float(datanew[2])-float(dataold[2]),2) +
                      math.pow(float(datanew[3])-float(dataold[3]),2)))<= float(dataold[4])

def makedictionary1(graph, value, filename, dataold):
    '''
    value is the vertex of the type paintball. This function updates all the
    neighbours of this vertex if anyone is in its range

    :param graph: to read and store data
    :param value: name of the paintball or a key in the graph
    :param filename: name of the file
    :param dataold: line of data read from the previous fucntion which called
                    this
    :return: None
    '''
    with open(filename) as file:
         for lines in file:
             lines = lines.strip()
             datanew = lines.split(' ')
             if len(datanew)==0:
                 continue
             #if distance between two vertices is in the range of the paintball
             #and this paintball is not same as the old one
             if distance(datanew, dataold) and dataold[1] != datanew[1]:
                 #first thi vertex is added to the graph by making its entry
                 #in the graph as a keya and its value as vertex
                 if datanew[1] not in graph:
                     graph[datanew[1]]= type(datanew[0], datanew[1])
                 #this new vertex is now added as a neighbour of the original
                 #vertex
                 value.neighbours.append(graph[datanew[1]])

def makedictionary2(graph, filename):
    '''
    Starts reading a file.
    If a cow comes then make its entry in the graph because a cow has no
    neighbours since the graph is directed.

    If a paintball comes then this paintball along with some other parameters
    is passed to a different function

    :param graph: to store the data
    :param filename: to read the datafrom
    :return: None
    '''
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                data = line.split(' ')
                if len(data)==0:
                    continue
                if data[0] == 'paintball':
                    #if this paintball has not been read already
                    if data[1] not in graph:
                        #its name ahs been made a key and value is made of the
                        #type node(vertex)
                        #data[0] type of vertex and data[1] is name of vertex
                        graph[data[1]]= type(data[0], data[1])
                    #this vertex is passed to the helping function
                    makedictionary1(graph, graph[data[1]], filename, data)
                else:
                    graph[data[1]] = type(data[0], data[1])
    except:
        print("Please run the program again and enter the correct name of file")

def triggernow(name, newkey, graph, cowscolor, paintedcowscount, visitednodes):
    '''
    This is a recursive function which calls itself if another paintball is
    triggered by a paintball
    :param name: name always remains the same in this recursive function when
                 it calls itself because we are trying to study the effect of
                 some particular color only at once
    :param newkey: If another paintball is triggered by a paintball the name of
                   the triggered paintball is passed as a newkey
    :param graph: to study all the neighbours of a each paintball and names of
                  vertices
    :param cowscolor: to store the data in this while triggering each paintball
    :param paintedcowscount: to store the count of number of cows painted by
                             each paintball
    :return: None
    '''

    #loop runs for all its neighbours
    for value in graph[newkey].neighbours:
        #if a neighbour is a cow
        if value.type == 'cow':
            #count of the original triggered color is increased by 1
            paintedcowscount[name] = paintedcowscount[name] + 1

            #printed a message that this cow is painted by this color
            print("         " + value.name + " is painted " + newkey + "!")

            #if this cow doent exist in the dictionary then its added and
            #its value is first initialzed as a empty list and the name of
            #color is added
            #cowscolor[name] is again a dicrionary of {cow name: painted colors}
            if value.name not in cowscolor[name]:
                cowscolor[name][value.name] = []

            #if it exists then  name of the color is added in the cows list
            cowscolor[name][value.name].append(graph[newkey].name)

        #if neighbour is a paintball
        else:
            #if this paintball has not been triggered already
            if value.name not in visitednodes:
                visitednodes.append(value.name)
                #prints a message that this paintball is triggered by this
                # paintball
                print("         " + value.name + " paintball is triggered by " + newkey + " paint ball")

                #same function is called again with all same parameters but the
                #newkey which is now the name of the new triggered paintball
                triggernow(name, value.name, graph, cowscolor, paintedcowscount, visitednodes)



def trigger(graph, cowscolor, paintedcowscount):
    '''
    This function checks each vertex in graph one by one and if its a paintball
    then it passes this paintball name to a helping function
    :param graph: to read each vertex
    :param cowscolor: to store the respective data
    :param paintedcowscount: to store the respective data
    :return: None
    '''
    for keys in graph:
        visitednodes =[]
        #Checks if a vertex is a paintball
        if graph[keys].type == 'paintball':
            visitednodes.append(keys)
            #initializes the value of this key as an empty dictionary
            cowscolor[graph[keys].name] = {}

            #initialized the no. of cows painted by it as 0
            paintedcowscount[keys] = 0
            print("Triggering " + graph[keys].name + " paint ball...")

            #calls another function trigger now
            triggernow(graph[keys].name, keys, graph, cowscolor, paintedcowscount, visitednodes)
    print()

def maxcolor(paintedcowscount):
    '''
    This function finds the paintball by which total colors on total painted
    cows is maximum
    :param paintedcowscount:
    :return: key        : name of the paintball
             maximum    : count of total paints
    '''
    maximum = 0
    key = ''
    for keys in paintedcowscount:
        if paintedcowscount[keys]>maximum:
           key = keys
           maximum = paintedcowscount[keys]
    return key, maximum

def makegraph(graph, filename):
    '''
    it makes a graph by reading the file given and prints the graph in the
    form of a adjacency list
    :param graph: to store the data
    :param filename: to read the content from
    :return: None
    '''

    #calls a helping function
    makedictionary2(graph, filename)

    #prints the graph in the proper format
    for keys in graph:
        print(keys + " connectedTo: [",end="")
        res = ""
        for val in graph[keys].neighbours:
            res += val.name + ", "
        print(res[0:len(res)-2]+ "]")
    print()


def result(paintedcowscount, cowscolor):
    '''

    :param paintedcowscount: to compare each color on the basis of the number
                             of cows painted by it
    :param cowscolor:        to print the the data for that particular color
    :return: None
    '''

    #Calls a function maxcolor which returns the color which painted the
    # maximum no of painted cows and count of the paint
    goodcolor, count = maxcolor(paintedcowscount)

    #if count is 0 then no cows has been painted. It prints the message and
    #returns from there
    if count == 0:
        print("No cows are painted by any starting paint ball!")
        return
    #If some cows has been painted then it prints the name of the color and
    # the respective data in the proper format
    print("Triggering the " + goodcolor + " paint ball is the best choice with " + str(count) + " total paint on the cows:")

    #keys are names of cows and goodcolor is the name of the color
    for keys in cowscolor[goodcolor]:
        print(keys + "'s colors: {",end="")
        res = ""
        for val in cowscolor[goodcolor][keys]:
            res += val + ", "
        print(res[0:len(res)-2]+ "}")

def main():
    '''
    Main function which call functions one by one
    :return: None
    '''
    # asks for the filename to read data from user
    filename = input("Enter the name of the file: ")

    #stores all the vertices in the form of dictionary in which key: name
    # and value: node
    graph = {}

    #Stores what happens when each paintball is triggered one by one in the
    # form of dictionary inside a dictionary
    #cowscolor:{paintball name: {cows name: all colors this cow has been painted}}
    cowscolor = {}

    #Stores the count of of the number of cows painted by each color
    #paintedcowscount = {paintball name: total number of cows painted}
    paintedcowscount = {}

    #calls the function to make a graph out of the file by making vertices of
    #each paintball and each cow and prints the graph in the form of adjacency
    #list
    makegraph(graph, filename)

    #Trigger every paintball one by one and prints whatever happens by
    #triggering this paintball
    trigger(graph, cowscolor, paintedcowscount)

    #prints the paintball which painted maximum number of cows and
    #which cows were painted by which color
    result(paintedcowscount, cowscolor)

main()