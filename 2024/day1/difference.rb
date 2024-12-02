# Initialize arrays to hold the left and right column values
left_column = []
right_column = []

# Read input from STDIN
while line = gets
  # Skip empty lines
  next if line.strip.empty?

  # Split the line into parts based on whitespace
  parts = line.strip.split

  # Ensure there are at least two elements in the line
  if parts.size >= 2
    # Cast the parts to integers
    left_num = parts[0].to_i
    right_num = parts[1].to_i

    # Add the numbers to their respective arrays
    left_column << left_num
    right_column << right_num
  end
end

# Sort both columns independently
left_column.sort!
right_column.sort!

# Initialize a variable to hold the total difference
total_difference = 0

# Calculate and sum the differences between the sorted columns
left_column.each_with_index do |left_value, index|
  right_value = right_column[index] || 0 # Use 0 if right_column has fewer elements
  difference = left_value - right_value
  total_difference += (difference).abs
end

# Output the total difference
puts total_difference
