import random


class Graph:
    def __init__(self, vertices, edges):
        self.__inbound = {}
        self.__outbound = {}
        self.__cost = {}
        self.__vertices = list(range(vertices))
        self.__edges = edges
        print(self.__edges)
        for vertex in range(vertices):
            self.__inbound[vertex] = []
            self.__outbound[vertex] = []

    def add_edge(self, source, destination, cost):
        if (source, destination) in self.__cost.keys():
            raise ValueError("Edge already in graph")
        self.__outbound[source].append(destination)
        self.__inbound[destination].append(source)
        self.__cost[(source, destination)] = cost

    def remove_edge(self, source, destination):
        if (source, destination) not in self.__cost.keys():
            raise ValueError("Edge not in graph")
        self.__outbound[source].pop(destination)
        self.__inbound[destination].pop(source)
        del self.__cost[(source, destination)]

    def add_vertix(self, vertix):
        if vertix in self.__vertices:
            raise ValueError("Vertix already in graph")
        self.__vertices.append(vertix)

    def remove_vertix(self, vertix):
        if vertix not in self.__vertices:
            raise ValueError("Vertix not in graph")
        self.__vertices.pop(vertix)
        for edge in self.__outbound[vertix]:
            self.__inbound[edge].pop(vertix)
            self.__outbound.pop(edge)
            del self.__cost[vertix, edge]
        del self.__outbound[vertix]

        for edge in self.__inbound[vertix]:
            self.__outbound[edge].pop(vertix)
            self.__inbound.pop(edge)
            del self.__cost[edge, vertix]
        del self.__inbound[vertix]

    def read_graph(self, file_name):
        file = open(file_name, "r")
        file.readline()
        for index in range(self.__edges):
            line = file.readline()
            source, destination, cost = line.split(" ")
            self.add_edge(int(source), int(destination), int(cost))
        file.close()

    @property
    def vertices(self):
        return self.__vertices

    def parse_vertices(self):
        return self.vertices

    def check_for_edge(self, source, destination):
        if destination in self.__outbound[source]:
            return True
        return False

    def get_out_edges(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("Not in graph")
        return iter(self.__outbound[vertex])

    def get_in_edges(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("Not in graph")
        return iter(self.__inbound[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.__vertices.append(vertex)
            self.__inbound[vertex] = []
            self.__outbound[vertex] = []
        else:
            raise ValueError("Already exists")

    def modify_edge(self, edge, new_value):

        if edge not in self.__cost:
            raise ValueError("Edge not in graph")

        self.__cost[edge] = new_value

        # if new_value in self.__edges:
        #    raise ValueError("New value already in graph")

        # if edge not in self.__edges:
        #    raise ValueError("Edge not in graph")

        # for i in range(len(self.__edges)):
        #    if self.__edges[i] == edge:
        #        self.__edges[i] = new_value
        #        break

        # self.__inbound[new_value] = self.__inbound[edge]
        # self.__outbound[new_value] = self.__outbound[edge]
        # del self.__inbound[edge]
        # del self.__outbound[edge]

    def get_degree(self, vertex):
        return len(self.__outbound[vertex]), len(self.__inbound[vertex])


def generate_random_graph(vertex_count, edge_count):
    graph = Graph(vertex_count, edge_count)
    edges = 0
    while edges < edge_count:
        try:
            graph.add_edge(random.randint(0, vertex_count - 1), random.randint(0, vertex_count - 1),
                           random.randint(0, 100))
            edges += 1
        except ValueError:
            pass
    return graph
