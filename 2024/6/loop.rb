file_path = "input.txt"
grid = File.readlines(file_path, chomp: true)

rows = grid.size
cols = grid.first.size

# Find the starting position and direction
start_row = nil
start_col = nil

grid.each_with_index do |line, r|
    if c = line.index('^')
        start_row, start_col = r, c
        break
    end
end

DIRECTIONS = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]

def simulate(grid, start_row, start_col, detect_loop: true)
    # Initially facing up
    dir_index = 0 # 0 => up, 1 => right, 2 => down, 3 => left
    r, c = start_row, start_col

    visited_states = Set.new
    visited_states << [r, c, dir_index]

    visited_positions = Set.new
    visited_positions << [r, c]

    loop do
        dr, dc = DIRECTIONS[dir_index]
        nr, nc = r + dr, c + dc

        # Check bounds
        if nr < 0 || nr >= grid.size || nc < 0 || nc >= grid.first.size
            # Fell off the map
            return detect_loop ? :no_loop : visited_positions
        end

        # Check for wall
        if grid[nr][nc] == '#'
            # Turn right
            dir_index = (dir_index + 1) % 4
            if detect_loop
                state = [r, c, dir_index]
                return :loop if visited_states.include?(state)
                visited_states << state
            end
        # Don't move yet, just changed direction
        else
            # Move forward
            r, c = nr, nc
            visited_positions << [r, c]
            if detect_loop
                state = [r, c, dir_index]
                return :loop if visited_states.include?(state)
                visited_states << state
            end
        end
    end
end

count = 0
(0...rows).each do |r|
    (0...cols).each do |c|
        # Skip the guard's original starting position
        next if [r, c] == [start_row, start_col]
  
        # Only try placing an obstruction where there was originally a '.'
        next unless grid[r][c] == '.'
  
        # Temporarily place '#'
        original_char = grid[r][c]
        grid[r][c] = '#'
  
        # Run the simulation
        result = simulate(grid, start_row, start_col)
  
        count += 1 if result == :loop
  
        # Restore original char
        grid[r][c] = original_char
    end
end

puts count