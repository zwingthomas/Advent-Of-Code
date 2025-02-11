disk_map = File.read("input.txt", chomp: true)

# Parse the input string into runs of (file_length, free_length, file_length, ...)
# The problem states digits alternate between file lengths and free space lengths.
runs = []
disk_map.chars.each_slice(1) do |slice|
  runs << slice.first.to_i
end

# Now runs is something like [2,3,3,1,3,1,2,1,4,1,4,1,3,1,4,0,2]
# This sequence represents alternating file/free runs starting with a file run.
# We need to interpret '0' as '10'.
runs.map! { |r| r == 0 ? 10 : r }

# We'll construct the actual disk:
# The pattern is file_length, free_length, file_length, free_length, ...
file_blocks = []  # This will store the final disk arrangement
file_id = 0
is_file = true

runs.each do |length|
  if is_file
    # Append file_id repeated 'length' times
    length.times { file_blocks << file_id }
    file_id += 1
  else
    # Append '.' repeated 'length' times for free space
    length.times { file_blocks << '.' }
  end
  is_file = !is_file
end

# Now we have an array like:
# [0,0, '.', '.', '.', 1,1,1, '.', '.', '.', 2, ...]
# matching the example given.

# Compaction process:
# While there exists a '.' to the left of any file block at a higher index:
# Move the last file block (rightmost non-'.') to the leftmost '.'.
loop do
  leftmost_dot = file_blocks.index('.')
  break if leftmost_dot.nil? # no free spaces at all
  # We must ensure there's a file block after this '.' to move from the right end.
  
  # Find the rightmost file block
  rightmost_file_index = file_blocks.rindex { |b| b != '.' }
  break if rightmost_file_index.nil? # no file blocks
  
  # If the leftmost '.' is to the left of any file block that appears after it,
  # we proceed. If not, we are done.
  # Check if there's a file block index > leftmost_dot
  any_file_after_dot = file_blocks[leftmost_dot+1..-1]&.any? { |b| b != '.' }
  break unless any_file_after_dot
  
  # Move that rightmost file block to the leftmost dot
  block_to_move = file_blocks[rightmost_file_index]
  file_blocks[rightmost_file_index] = '.'
  file_blocks[leftmost_dot] = block_to_move
end

# Compute the checksum:
# sum of (position * file_id) for all file blocks.
checksum = 0
file_blocks.each_with_index do |block, pos|
  if block.is_a?(Integer)
    checksum += pos * block
  end
end

puts checksum