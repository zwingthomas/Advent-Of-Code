
# initialize cnt
cnt = 0

# Read input from STDIN
while line = gets
    # Skip empty lines
    next if line.strip.empty?
  
    # Split the line into integer values based on whitespace
    values = line.strip.split.map(&:to_i)
  
    first = values[0]
    second = values[1]

    if (first - second).abs < 1 || (first - second).abs > 3
        next
    end

    increasing = first < second

    safe = true
    temp = second
    values.drop(2).each do |value|
        # If it's increasing, stay increating. If its decreasing, stay decreasing. Check amount.
        if (increasing && value < temp) || (!increasing && value > temp) || ((value - temp).abs < 1 || (value - temp).abs > 3)
            safe = false
            break
        end
        temp = value
    end

    cnt += 1 if safe

  end

  puts cnt