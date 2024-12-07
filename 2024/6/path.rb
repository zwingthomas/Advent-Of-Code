# Read the input from a file
file_path = "input.txt"
grid = File.readlines(file_path, chomp: true)

rows = grid.size
cols = grid.first.size

# Find the starting position and direction
start_row = nil
start_col = nil
direction = :up

grid.each_with_index do |line, r|
  if c = line.index('^')
    start_row, start_col = r, c
    break
  end
end

directions = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]
dir_index = 0 # 0 => up, 1 => right, 2 => down, 3 => left

# Current position
r, c = start_row, start_col

# Track visited positions
visited = Set.new
visited << [r, c]

loop do
  # Try to move forward
  dr, dc = directions[dir_index]
  nr, nc = r + dr, c + dc

  # Check bounds
  if nr < 0 || nr >= rows || nc < 0 || nc >= cols
    # Out of bounds -> we fall off the map
    break
  end

  # Check if next position is a wall
  if grid[nr][nc] == '#'
    # Rotate direction to the right (clockwise)
    dir_index = (dir_index + 1) % 4
    # Do not move yet, just change direction and try again in next iteration
    next
  else
    # Move forward
    r, c = nr, nc
    visited << [r, c]
  end
end

puts visited.size