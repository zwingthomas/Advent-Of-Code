map = File.readlines("input.txt", chomp: true)

rows = map.size
cols = map.first.size

# Collect all "antennas" by "frequency"
antennas = Hash.new { |h,k| h[k] = [] }
map.each_with_index do |line, y|
    line.chars.each_with_index do |ch, x|
        if ch != '.'
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
        g = dx.gcd(dy)
        dx /= g
        dy /= g

        # Traverse the line forward from x1 & y1
        x, y = x1, y1
        while x.between?(0, cols-1) && y.between?(0, rows-1)
            antinode_positions << [x, y]
            x += dx
            y += dy
        end

        # Traverse the line backward from x1 & y1
        x, y = x1 - dx, y1 - dy
        while x.between?(0, cols-1) && y.between?(0, rows-1)
            antinode_positions << [x, y]
            x -= dx
            y -= dy
        end
    end
end

puts antinode_positions.size