
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
  
    x = 0
    # try it with skipping the first number
    [first, second].each do |temp|
        x += 1
        prev_cnt = cnt
        # try it both increasing and decreasing
        [true, false].each do |increasing|
            safe = x - 1
            values.drop(x).each do |value|
                # If it's increasing, stay increasing. If its decreasing, stay decreasing. Check amount.
                if (increasing && value < temp) || (!increasing && value > temp) || ((value - temp).abs < 1 || (value - temp).abs > 3)
                    safe += 1
                    if safe == 2
                        break
                    end
                    # Leave temp as is to remove the unsafe value
                    next
                end
                temp = value
            end
            # if we only removed one at the most, count it
            if safe < 2
                cnt += 1
                break
            end
        end
        # ensure we only count once
        if cnt != prev_cnt
            break
        end
    end
  end

  puts cnt