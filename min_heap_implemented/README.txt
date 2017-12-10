
Joseph Tyler DiBartolo
CSCI311 HW#2: Implement A Min-Heap


How to Compile and Run the Program:

	This program was written in Java, with the main.java being the program that is run by the user. To compile and run this program, one must be in the parent directory of the current directory (ie. the parent of min_heap_implemented). In the parent directory, to compile the program, run: "javac min_heap_implemented/main.java"; to execute the program, run: "java min_heap_implemented.main".

	When the user first runs the program, two minHeapImp objects are created. (Note: minHeapImp objects extend the minHeap interface, which includes all the methods required by this assignment.) Heap 'A' is initialized as empty, and heap 'B' is initialied with some contents. When heap B is initialized, it is immediately built into a min-heap, but not sorted; heapSort() is automatically called on heap B so that it is a sorted heap by the point when control is opened to the user.

	Once both heaps are initialized, the user is prompted with options, the first option being to select a heap on which to operate; the user will select either 'A' or 'B'. (Note: at any time *other than when entering an integer to insert into a heap*, the user can enter 'X' to exit the program.) From there, the options to insert, delete the minimum, print, and sort the current heap are shown; also shown is the option to enter 'C' to change over from heap A to B or vice-versa. From there, the user can carry out any of the required functions for this program.


Discussion:

	This homework took me approximately 10 hours in total to complete. About the same amount of time was spent on creating the minHeap class as was creating a main function that had extensive menu options and intuitive user flow. Although I didn't mind spending time on the main function, it definitely took more time than expected since the user had to be able to do multple actions to either heap. It was not terribly difficult to translate the pseudo-code we have learned into a Java min-Heap implementation, but it forced me to dive deeper into the min-Heap-related algorithms and, by the end of the assignment, I had a much better intuitive understanding of heaps and heapSort.

	I wrote my heaps to run with a starting index of zero, and once my functions to find parent, left child, and right child indices were written to account for a 0-index, I had no further problem using a starting index of 0. I did have some problems, however, with implementing the required functions as static functions that accepted parameters; I found it much easier to implement this in Java when the heap-related-methods were object-methods called by a minHeap object, since they would by default have access to the private ArrayList<Integer> "heap", and this way there was less of a chance of passing the wrong heap object around.


Sample IO:

  //Run the program from the terminal.
	$ java HW_02_11626044/main

  //The following code is displayed as soon as the user runs the program, before any decisions are made.
	Empty ArrayList initialized as heap.
	Printing 'A':


	Heapified input-List built and set as heap.
	Printing 'B':
	1
	3 5
	4 46 45 8
	45 13 

	Sorting heap B.
	Starting heapSort procedure.
	1
	3 4
	5 8 13 45
	45 46 

	To exit the program, type 'X'.

  //From here, the user can make decisions.

  //Example 1: the user selects heap B, deletes the minimum object, and resorts the heap.

	Please choose a heap - [type] 'A' [or] 'B': B
	Heap B selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: d
	Deleted 1 from heap B. Current heap size is 8. Printing new heap: 
	3
	5 4
	45 8 13 45
	46 

	Heap B selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: s
	Sorting heap B: 
	Starting heapSort procedure.
	Printing heap B: 
	3
	4 5
	8 13 45 45
	46 

  //Example 2: the user selects heap A, inserts keys {1, 4, 6, 3, 19, 12, 5}, and sorts the heap.

	Please choose a heap - [type] 'A' [or] 'B': A
	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 1
	Inserted 1 to heap A. Current heap size is 1. Printing new heap: 
	1


	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 4
	Inserted 4 to heap A. Current heap size is 2. Printing new heap: 
	1
	4 

	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 6
	Inserted 6 to heap A. Current heap size is 3. Printing new heap: 
	1
	4 6


	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 3
	Inserted 3 to heap A. Current heap size is 4. Printing new heap: 
	1
	3 6
	4 

	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 19
	Inserted 19 to heap A. Current heap size is 5. Printing new heap: 
	1
	3 6
	4 19 

	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 12
	Inserted 12 to heap A. Current heap size is 6. Printing new heap: 
	1
	3 6
	4 19 12 

	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 5
	Inserted 5 to heap A. Current heap size is 7. Printing new heap: 
	1
	3 5
	4 19 12 6


	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: s
	Sorting heap A: 
	Starting heapSort procedure.
	Printing heap A: 
	1
	3 4
	5 6 12 19

  //Example 3: the user selects heap B, deletes the minimum, resorts the heap, then switches over to heap A, inserts {2, 3, 1, 5, 1}, and sorts the heap.

	Please choose a heap - [type] 'A' [or] 'B': b
	Heap B selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: d
	Deleted 1 from heap B. Current heap size is 8. Printing new heap: 
	3
	5 4
	45 8 13 45
	46 

	Heap B selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: s
	Sorting heap B: 
	Starting heapSort procedure.
	Printing heap B: 
	3
	4 5
	8 13 45 45
	46 

	Heap B selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: c
	Switching to heap A.
	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 2
	Inserted 2 to heap A. Current heap size is 1. Printing new heap: 
	2


	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 3
	Inserted 3 to heap A. Current heap size is 2. Printing new heap: 
	2
	3 

	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 1
	Inserted 1 to heap A. Current heap size is 3. Printing new heap: 
	1
	3 2


	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 5
	Inserted 5 to heap A. Current heap size is 4. Printing new heap: 
	1
	3 2
	5 

	Heap A selected. Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: i
	Please enter an integer: 1
	Inserted 1 to heap A. Current heap size is 5. Printing new heap: 
	1
	1 2
	5 3 


Pseudo-Code:

	buildMinHeap():
		for index i = parent(heapSize) to 0:
			minHeapify(i)

	minHeapify(int i):
		minIndex = i
        if (index of i.left-child is in-bounds && heap[i.left-child] < heap[i]):
            minIndex  = index of i.left-child
        if (index of i.right-child is in-bounds && heap[i.right-child] < heap[minIndex]):
            minIndex = index of i.right-child
        if (minIndex != i):
            exchangeKeys(i, minIndex)
            minHeapify(minIndex)

	heapSort():
        buildMinHeap()
        initialHeapSize = heapSize
        while (heapSize > 0):
            exchangeKeys(0, heapSize - 1)
            heapSize -= 1
            minHeapify(0)
		//Restore the true size of the heap after decrementing to allow proper sorting.
        heapSize = initialHeapSize
		//Reverse the direction of the heap array so that it is in min --> max order, ie. a sorted min-heap.
        reverse(this.heap)

	exchangeKeys(int a, int b):
        aKey = heap[a]
        bKey = heap[b]
        heap[a] = bKey
        heap[b] = aKey

	insertKey(int key):
        heap.add(key)
        heapSize += 1
        buildMinHeap()

	deleteMin():
        buildMinHeap()
        if (heapSize > 0):
            exchangeKeys(0, heapSize - 1)
            heapSize -= 1
            heap.remove(heapSize)
            minHeapify(0)

