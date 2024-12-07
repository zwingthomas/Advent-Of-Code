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

# Directions in order: up, right, down, left
DIRECTIONS = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]

def simulate(grid, start_row, start_col)
  # Find initial direction based on '^' (up)
  dir_index = 0 # 0 => up, 1 => right, 2 => down, 3 => left

  # Current position
  r, c = start_row, start_col

  # Track states for loop detection: (row, col, dir_index)
  visited_states = Set.new
  visited_states << [r, c, dir_index]

  loop do
    # Attempt to move forward
    dr, dc = DIRECTIONS[dir_index]
    nr, nc = r + dr, c + dc

    # Check bounds
    if nr < 0 || nr >= grid.size || nc < 0 || nc >= grid.first.size
      # Out of bounds - we fall off the map
      return :no_loop
    end

    # Check if next position is a wall (#)
    if grid[nr][nc] == '#'
      # Turn right (clockwise)
      dir_index = (dir_index + 1) % 4
      # Check if turning right and staying in same place leads to a repeated state
      # Record after turn as well because direction changed
      state = [r, c, dir_index]
      if visited_states.include?(state)
        return :loop
      else
        visited_states << state
      end
      # Don't move yet, next iteration we try again
      next
    else
      # Move forward
      r, c = nr, nc
      state = [r, c, dir_index]
      if visited_states.include?(state)
        # We visited this state before, so it's a loop
        return :loop
      else
        visited_states << state
      end
    end
  end
end

# Remove the '^' character and replace it with '.' for easier manipulation
grid = grid.map do |line|
  line.gsub('^', '.')
end

count_loop_positions = 0

(0...rows).each do |r|
  (0...cols).each do |c|
    next if grid[r][c] != '.'  # Only try placing '#' where there is '.' 

    # Temporarily place '#'
    original_char = grid[r][c]
    grid[r][c] = '#'

    # Run simulation
    result = simulate(grid, start_row, start_col)

    count_loop_positions += 1 if result == :loop

    # Restore original char
    grid[r][c] = original_char
  end
end

puts count_loop_positions