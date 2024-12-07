ret = 0
do_mode = true  # Start in 'do' mode

# Get all the lines
input_lines = []
while line = gets
  input_lines << line
end

# Combine all lines into one string
input = input_lines.join(" ")

# Cool, but inefficient
# # Use StringScanner to process the input string -> LEARNIN
# require 'strscan'

# s = StringScanner.new(input)

# while not s.eos?
#   if s.scan(/do\(\)/)
#     do_mode = true
#   elsif s.scan(/dont\(\)/)
#     do_mode = false
#   elsif s.scan(/mul\((-?\d{1,3}),(-?\d{1,3})\)/)
#     if do_mode
#       x = s[1].to_i
#       y = s[2].to_i
#       ret += x * y
#     end
#   else
#     s.scan(/./)  # Skip any other character
#   end
# end

# Split input into tokens using regex
tokens = input.scan(/do\(\)|don't\(\)|mul\(-?\d{1,3},-?\d{1,3}\)|./)

tokens.each do |token|
  if token == 'do()'
    do_mode = true
  elsif token == "don't()"
    do_mode = false
  elsif token =~ /mul\((-?\d{1,3}),(-?\d{1,3})\)/
    if do_mode
      x = $1.to_i
      y = $2.to_i
      ret += x * y
    end
  end
end

puts ret