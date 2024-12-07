# Read input lines and store them in a 2D array (grid)
grid = []

while line = gets
  line = line.chomp
  break if line.empty?
  grid << line.chars
end

# Directions represented as (dx, dy) pairs
directions = [
  [0, 1],   # Right
  [0, -1],  # Left
  [1, 0],   # Down
  [-1, 0],  # Up
  [-1, -1], # Up-Left
  [1, -1],  # Down-Left
  [-1, 1],  # Up-Right
  [1, 1],   # Down-Right
]

height = grid.length
width = grid[0].length
target_word = 'XMAS'
word_length = target_word.length
count = 0

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
        else
          break
        end
        x += dx
        y += dy
      end

      # Increment count if the word matches 'XMAS'
      count += 1 if word == target_word
    end
  end
end

# Output the total count of 'XMAS' found
puts count