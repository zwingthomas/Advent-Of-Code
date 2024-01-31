import java.util.PriorityQueue
import kotlin.Comparator
import java.io.File


fun sumCalories(input: String): Int {
	val caloriesList = input.split("\n")
	return caloriesList.map { it.toIntOrNull() ?: 0 }.sum()
}


fun main() {
    	val maxHeapComparator = Comparator { o1: Int, o2: Int -> o2.compareTo(o1) }
    	// Create a PriorityQueue (Max Heap)
    	val maxHeap = PriorityQueue(maxHeapComparator)
	
	val input = File("input.txt").readText(Charsets.UTF_8)
	val elfByElf = input.split("\n\n")

	elfByElf.forEach { elf ->
		maxHeap.add(sumCalories(elf))
	}

	val most = maxHeap.peek()

	println("The most calories with any elf is: $most")
}

