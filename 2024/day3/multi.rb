ret = 0

# Get all the lines
input_lines = []
while line = gets
  input_lines << line
end

# Combine all lines into one string
input = input_lines.join(" ")

# Extract all matches mul(X,Y)
matches = input.scan(/mul\((-?\d{1,3}),(-?\d{1,3})\)/)

# Convert matches to integers, calculate products, and sum them up
products = matches.map do |x, y|
x.to_i * y.to_i
end
ret += products.sum


puts ret