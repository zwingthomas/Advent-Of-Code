map = File.readlines("input.txt", chomp: true)

rows = map.size
cols = map.first.size

# Collect antennas by frequency
antennas = Hash.new { |h,k| h[k] = [] }
map.each_with_index do |line, y|
    line.chars.each_with_index do |ch, x|
        if ch != '.' # An antenna
            antennas[ch] << [x, y]
        end
    end
end

antinode_positions = Set.new

antennas.each do |freq, coords|
    # For each pair of antennas of the same frequency
    coords.combination(2) do |(x1, y1), (x2, y2)|
        dx = x2 - x1
        dy = y2 - y1
        # Antinode beyond (x1, y1)
        ax1, ay1 = (2*x1 - x2), (2*y1 - y2)
        # Antinode beyond (x2, y2)
        ax2, ay2 = (2*x2 - x1), (2*y2 - y1)

        if ax1.between?(0, cols-1) && ay1.between?(0, rows-1)
            antinode_positions << [ax1, ay1]
        end
        
        if ax2.between?(0, cols-1) && ay2.between?(0, rows-1)
            antinode_positions << [ax2, ay2]
        end
    end
end

puts antinode_positions.size