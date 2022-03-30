from Graph.Graph import Graph


class UI:
    def __init__(self, file_name):
        file = open(file_name, "r")
        line = file.readline()
        vertices, edges = line.split(" ")
        self.__graph = Graph(int(vertices), int(edges))

    def parse_vertices(self):
        vertices = self.__graph.vertices
        for vertix in vertices:
            print(vertix, end=" ")
        print()

    def check_vertex(self):
        source = int(input("Source: "))
        destination = int(input("Destination: "))
        if self.__graph.check_for_edge(source, destination):
            print(f"There is an edge between {source} and {destination}")
        else:
            print("There is no edge")

    def print_menu(self):
        print("1. Get the number of vertices")
        print("2. Parse the vertices")
        print("3. Check vertex between 2 edges")

    def parse_out_edges(self):
        vertex = input("Vertex: ")
        edges = self.__graph.get_out_edges(vertex)
        for edge in edges:
            print(f"{vertex} - {edge}")
        print()

    def parse_in_edges(self):
        vertex = input("Vertex: ")
        edges = self.__graph.get_in_edges(vertex)
        for edge in edges:
            print(f"{edge} - {vertex}")
        print()

    def run(self):
        while True:
            self.print_menu()
            option = input("> ")
            if option == "1":
                print(f"There are {len(self.__graph.vertices)} vertices")
            elif option == "2":
                self.parse_vertices()
            elif option == "3":
                self.check_vertex()
            else:
                print("Bad command!")
