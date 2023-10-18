# Ask the user to enter the number of vertices
n = int(input("Enter the number of vertices: "))

# Initialize an empty list to store the adjacency matrix
G = []

# Ask the user to enter the adjacency matrix row by row
print("Enter the adjacency matrix (0 for no edge, 1 for edge): ")
for i in range(n):
    row = list(map(int, input().split()))  # Convert the input string to a list of integers
    G.append(row)  # Append the row to the matrix

# Define the possible colors
colors = ["Blue", "Red", "Yellow", "Green"]

# Initialize an empty dictionary to store the color assignments
color_dict = {}

# Sort the vertices by their degree in descending order
degrees = [sum(row) for row in G]  # Compute the degree of each vertex
vertices = list(range(len(G)))  # Create a list of vertex indices
vertices.sort(key=lambda x: degrees[x], reverse=True)  # Sort the list by degree

# Assign colors to the vertices using the greedy algorithm
for v in vertices:
    available = colors.copy()  # Make a copy of the possible colors
    for u in range(len(G)):  # Loop through all other vertices
        if G[v][u] == 1 and u in color_dict:  # If u is adjacent to v and already colored
            if color_dict[u] in available:  # If u's color is in the available list
                available.remove(color_dict[u])  # Remove it from the list
    color_dict[v] = available[0]  # Assign v the first available color

# Print the color assignments
for v in color_dict:
    print(f"Vertex {v} is colored {color_dict[v]}")
