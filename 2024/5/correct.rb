# Read the input from a file
file_path = "input.txt" # Replace with your actual file path
lines = File.readlines(file_path, chomp: true)

# Initialize a hashmap built with empty sets as the default value
before = Hash.new { |hash, key| hash[key] = Set.new }
updates = []

lines.each do |line|
    if line.include?("|")
        # Process map data
        x, y = line.split("|").map(&:to_i)
        before[y].add(x)
    elsif line.include?(",")
        # Process 2D array data
        updates << line.split(",").map(&:to_i)
    end
end

incorrectly_ordered = []
updates.each do |update|
    valid = true
    prefix = Set.new
    update_set = Set.new(update)
    update.each do |value|
        # If there are constraints
        if before.key?(value)
            # Check if all elements required to be before the prefix are in the prefix
            filtered_before = before[value] & update_set # if they exist in the line at all
            # Ensure the prefix contains all values set out in before
            unless filtered_before.subset?(prefix)
                valid = false
                break
            end
        end
        prefix.add(value)
    end
    incorrectly_ordered << update if !valid
end

# Kahn's algorithm (topological sort)
def kahn_topological_sort(nodes, edges)
  
    # Compute in-degree
    in_degree = Hash.new(0)
    nodes.each { |n| in_degree[n] = 0 }
  
    edges.each do |_from, to|
        to.each { |t| in_degree[t] += 1 }
    end
  
    # Initialize queue with nodes of in-degree 0
    queue = in_degree.select { |_k, v| v == 0 }.map { |k, _v| k }
  
    order = []
    while !queue.empty?
        current = queue.shift
        order << current
        # Decrement in-degree of neighbors
        if edges[current]
            edges[current].each do |neighbor|
                in_degree[neighbor] -= 1
                queue << neighbor if in_degree[neighbor] == 0
            end
        end
    end
  
    return order.length == nodes.size ? order : [] # Return empty is there is a cycle
end

#                                           #
#  Reorder the incorrectly ordered updates  #
#                                           #
sum_of_middles = 0
  
incorrectly_ordered.each do |update|
    nodes = Set.new(update)
  
    # Build adjacency list for edges
    edges = Hash.new { |h, k| h[k] = Set.new }
  
    # add edges (x->y)
    update.each do |y|
        if before.key?(y)
            (before[y] & nodes).each do |x|
                edges[x].add(y)
            end
        end
    end
  
    # Perform Kahn's
    sorted = kahn_topological_sort(nodes, edges)
  
    # Find the middle element of the sorted array
    if !sorted.empty?
        middle_index = sorted.length / 2
        sum_of_middles += sorted[middle_index]
    end
end
  
puts sum_of_middles


