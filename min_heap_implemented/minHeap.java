package min_heap_implemented;

/**
 *
 * @author Joseph Tyler DiBartolo
 */
public interface minHeap {
    
    void buildMinHeap();
    
    void insertKey(int key);
    
    void deleteMin();
    
    void printHeap();
    
    void heapSort();
    
}
