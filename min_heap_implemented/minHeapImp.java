package min_heap_implemented;

import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author Joseph Tyler DiBartolo
 */
public class minHeapImp implements minHeap{
    
    private ArrayList<Integer> heap;
    private int heapSize;
    
    public minHeapImp() {
        this.heap = new ArrayList();
        this.heapSize = 0;
        System.out.println("Empty ArrayList initialized as heap.");
    }
    
    public minHeapImp(ArrayList<Integer> list) {
        this.heapSize = list.size();
        this.setHeap(list);
        buildMinHeap();
        System.out.println("Heapified input-List built and set as heap.");
    }
    
    //NOTE: All array indices use i = 0 as the starting index of the array.
    
    static int parent(int i) {
        int adj = i + 1;
        return (int) Math.floor(adj/2) - 1;
    }
    
    static int left(int i) {
        int adj = i + 1;
        return (adj*2) - 1;
    }
    
    static int right(int i) {
        int adj = i + 1;
        return (adj*2);
    }
    
    public void setHeap(ArrayList<Integer> heap) {
        this.heapSize = heap.size();
        this.heap = heap;
    }
    
    public ArrayList<Integer> getHeap() {
        return this.heap;
    }
    
    public int getHeapSize() {
        return this.heapSize;
    }
    
    @Override
    public void buildMinHeap() {
        //System.out.println("Beginning buildMinHeap procedure on heap of object " + this.toString());
        
        for (int i = parent(heapSize); i > -1; i--) {
            //System.out.println("about to call heapify from within buildMinHeap at index " + i);
            minHeapify(i);
        }
        
        //System.out.println("buildMinHeap finished for pbject " + this.toString());
    }
    
    private void minHeapify(int i){
        
        //System.out.println("heapifying for index " + i);
        int lIn = left(i);
        //System.out.println("left child is at index " + lIn);
        int rIn = right(i);
        //System.out.println("right child is at index " + rIn);
        int minIn = i;
        
        if (inBounds(lIn)) {
            //System.out.println("left child in bounds at index " + lIn + ", key " + this.heap.get(lIn));
            if(inBounds(rIn)) {
                //System.out.println("right child in bounds at index " + rIn + ", key " + this.heap.get(rIn));
            } else {
                //System.out.println("right child out of bounds");
            }
        } else {
            //System.out.println("neither child in bounds for index i = " + i);
        }
        
        if (inBounds(lIn) && this.heap.get(lIn) < this.heap.get(minIn)) {
            //System.out.println("setting lIn as minIn");
            minIn  = lIn;
        }        
        if (inBounds(rIn) && this.heap.get(rIn) < this.heap.get(minIn)) {
            //System.out.println("setting rIn as minIn");
            minIn = rIn;
        }
        
        if (minIn != i) {
            //System.out.println("minIn != i --> exchanging indices " + i + " and " + minIn);
            exchangeKeys(i, minIn);
            //System.out.println("about to call heapify at index " + minIn);
            minHeapify(minIn);
        }
        
        //System.out.println("minIn == i --> returning");
    }
    
    @Override
    public void heapSort() {
        
        System.out.println("Starting heapSort procedure.");
        buildMinHeap();
        int totalSize = this.heapSize;
        
        while (this.heapSize > 0){
            //System.out.println("In heapSort loop with heapSize = " + this.heapSize);
            exchangeKeys(0, heapSize - 1);
            this.heapSize -= 1;
            minHeapify(0);
        }
        //System.out.println("Heap size is now 0. All items have been sorted in place.");
        this.heapSize = totalSize;
        Collections.reverse(this.heap);
        //System.out.println("Restoring original heapSize to enable printing.");
        
    }
    
    private void exchangeKeys(int a, int b) {
        
        int aKey = this.heap.get(a);
        int bKey = this.heap.get(b);
        
        this.heap.set(a, bKey);
        this.heap.set(b, aKey);
         
    }
    
    private boolean inBounds(int i){
        if (i > -1 && i < this.heapSize) {
            return true;
        }
        return false;
    }
    
    private int binLog(int x) {
        return (int) (Math.log(x) / Math.log(2));
    }

    @Override
    public void insertKey(int key) {
        this.heap.add(key);
        this.heapSize += 1;
        buildMinHeap();
    }

    @Override
    public void deleteMin() {
        buildMinHeap();
        if (heapSize > 0){
            exchangeKeys(0, heapSize - 1);
            this.heapSize -= 1;
            this.heap.remove(heapSize);
            minHeapify(0);
        }
    }

    @Override
    public void printHeap() {
        //System.out.println("Printing heap: ");
        int currHeight = 0;
        int rowSize = 1;
        int lastKeyInRowIndex = 0;
        for (int i = 0; i < heapSize; i++) {
            
            if (i != 0 && currHeight != binLog(i+1)) {
                currHeight = binLog(i+1);
                rowSize = currHeight * 2;
                lastKeyInRowIndex += rowSize;
            }
            
            if(i == lastKeyInRowIndex) {
                System.out.println(this.heap.get(i));
            } else {
                System.out.print(this.heap.get(i) + " ");
            }
            
        }
        System.out.println("\n");
    }
    
}
