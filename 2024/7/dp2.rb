def can_produce_target?(target, nums)
    # DP state
    possible_values = [nil] * (nums.size + 1)
    possible_values[1] = Set.new([nums[0]])
    (2..nums.size).each do |i|
        current_num = nums[i-1]
        new_values = Set.new
        possible_values[i-1].each do |val|
            new_values << val + current_num
            new_values << val * current_num
            new_values << (val.to_s + current_num.to_s).to_i
        end
        possible_values[i] = new_values
    end
    possible_values[nums.size].include?(target)
end
  
input_data = File.readlines("input.txt", chomp: true)
  
sum = 0
input_data.each do |line|
    target_str, numbers_str = line.split(':')
    target = target_str.strip.to_i
    nums = numbers_str.strip.split.map(&:to_i)
  
    if can_produce_target?(target, nums)
        sum += target
    end
end
  
puts sum