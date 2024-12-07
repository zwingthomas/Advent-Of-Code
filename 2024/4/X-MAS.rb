# Read input lines and store them in a 2D array (grid)
grid = []

while line = gets
  line = line.chomp
  break if line.empty?
  grid << line.chars
end

# Directions represented as (dx, dy) pairs
directions = [
#   [0, 1],   # Right
#   [0, -1],  # Left
#   [1, 0],   # Down
#   [-1, 0],  # Up
  [-1, -1], # Up-Left
  [1, -1],  # Down-Left
  [-1, 1],  # Up-Right
  [1, 1],   # Down-Right
]

height = grid.length
width = grid[0].length
target_word = 'MAS'
word_length = target_word.length
count = 0
mas = []
midpoint = [-1, -1]

# Iterate over each cell in the grid
(0...height).each do |i|
  (0...width).each do |j|
    # Check each direction from the current cell
    directions.each do |dx, dy|
      word = ''
      x, y = i, j

      # Build the word in the current direction
      word_length.times do
        if x.between?(0, height - 1) && y.between?(0, width - 1)
          word += grid[x][y]
          if "A" == grid[x][y]
            midpoint = [x, y]
          end
        else
          break
        end
        x += dx
        y += dy
      end

      # Increment count if the word matches 'XMAS'
      if word == target_word
        if midpoint.inspect == [-1, -1]
            puts midpoint.inspect
        end
        mas << midpoint 
      end
    end
  end
end

counter = Hash.new(0)
mas.each do |item|
    counter[item] += 1
    if counter[item] == 2
        count += 1
    end
end

# Output the total count of 'XMAS' found
puts count