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

cnt = 0
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
    cnt += update[update.length / 2] if valid
end

puts cnt


