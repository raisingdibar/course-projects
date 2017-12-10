package min_heap_implemented;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author Joseph Tyler DiBartolo
 */
public class main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here.
        
        /*INSTRUCTIONS: 
                ~ create two heap arraylists.
                ~ Create a menu using which the user can insert/delete/print/sort data in/from the heaps
                ~ The menu should execute as long as the user wants
                ~ Create the test/main as a separate file from the MinHeap class
        */
        
        minHeapImp A = new minHeapImp();
        System.out.println("Printing 'A':");
        A.printHeap();
        
        ArrayList bArray = new ArrayList<Integer>();
        int [] startingB = {5, 3, 1, 45, 46, 45, 8, 4, 13};
        for (int i : startingB) {
            bArray.add(i);
        }
        minHeapImp B = new minHeapImp(bArray);
        System.out.println("Printing 'B':");
        B.printHeap();
        
        System.out.println("Sorting heap B.");
        B.heapSort();
        B.printHeap();
        
        int menu = 0;
        char currHeap = 0;
        Scanner scanner = new Scanner(System. in); 
        
        System.out.println("To exit the program, type 'X'.\n");
        int choice = displayOptions(scanner, menu, currHeap);
        
        while (choice != -1) {
            if (choice == 1) {
                currHeap = 'A';
            } else if (choice == 2) {
                currHeap = 'B';
                choice = 1;
            } else if (choice == 3) {
                //User wants to Insert.
                System.out.print("Please enter an integer: ");
                int toInsert = Integer.parseInt(scanner.nextLine());
                
                if (currHeap == 'A') {
                    A.insertKey(toInsert);
                    System.out.println("Inserted " + toInsert + " to heap A. Current heap size is " + A.getHeapSize() + ". Printing new heap: ");
                    A.printHeap();
                } else {
                    B.insertKey(toInsert);
                    System.out.println("Inserted " + toInsert + " to heap B. Current heap size is " + B.getHeapSize() + ". Printing new heap: ");
                    B.printHeap();
                }
                choice = 1;
            } else if (choice == 4) {
                //User wants to Delete.
                if (currHeap == 'A' && A.getHeapSize() > 0) {
                    int min = A.getHeap().get(0);
                    A.deleteMin();
                    System.out.println("Deleted " + min + " from heap A. Current heap size is " + A.getHeapSize() + ". Printing new heap: ");
                    A.printHeap();
                } else if (currHeap == 'B' && B.getHeapSize() > 0) {
                    int min = B.getHeap().get(0);
                    B.deleteMin();
                    System.out.println("Deleted " + min + " from heap B. Current heap size is " + B.getHeapSize() + ". Printing new heap: ");
                    B.printHeap();
                } else {
                    System.out.println("Desired heap " + currHeap + " is empty. Cannot delete.");        
                }
                choice = 1;
            } else if (choice == 5) {
                //User wants to Print.
                if (currHeap == 'A') {
                    System.out.println("Printing heap A: ");
                    A.printHeap();
                } else {
                    System.out.println("Printing heap B: ");
                    B.printHeap();
                }
                choice = 1;
            } else if (choice == 6) {
                //User wants to Sort.
                if (currHeap == 'A') {
                    System.out.println("Sorting heap A: ");
                    A.heapSort();
                    System.out.println("Printing heap A: ");
                    A.printHeap();
                } else {
                    System.out.println("Sorting heap B: ");
                    B.heapSort();
                    System.out.println("Printing heap B: ");
                    B.printHeap();
                }
                choice = 1;
            } else if (choice == 7) {
                //User wants to switch heaps.
                if (currHeap == 'A') {
                    System.out.println("Switching to heap B.");
                    currHeap = 'B';
                } else {
                    System.out.println("Switching to heap A.");
                    currHeap = 'A';
                }
                choice = 1;
            } 
            choice = displayOptions(scanner, choice, currHeap);
        }
        
    }
    
    static int displayOptions(Scanner s, int i, char currHeap) {
        String choice;
        
        switch (i) {
            
            //Case 0: Choose a heap on which to operate.
            case 0: System.out.print("Please choose a heap - [type] 'A' [or] 'B': ");
                    choice = s.nextLine();
                    if (choice.length() != 1) {
                        System.out.println("Invalid choice entered - please enter a single character 'A' or 'B'.");
                        return 0;
                    } else if (choice.charAt(0) == 'A' || choice.charAt(0) == 'a') {
                        return 1;
                    } else if (choice.charAt(0) == 'B' || choice.charAt(0) == 'b') {
                        return 2;
                    } else if (choice.charAt(0) == 'X' || choice.charAt(0) == 'x') {
                        break;
                    }else {
                        System.out.println("Invalid Heap choice - please enter a single character A or B. Select again.");
                        return 0;
                    }
                    
            //Case 1: Default options for either heap.
            case 1: System.out.print("Heap " + currHeap + " selected. ");
                    System.out.print("Options are: 'I' (Insert), 'D' (Delete Minimum), 'P' (Print), 'S' (Sort), and 'C' (Change Heap). Please choose an action: ");
                    choice = s.nextLine();
                    if (choice.length() != 1) {
                        System.out.println("Invalid choice entered (Case 1) - please enter a single character from the above options.");
                        if (currHeap == 'A') {
                            return 1;
                        } else {
                            return 2;
                        }
                    } else if (choice.charAt(0) == 'I' || choice.charAt(0) == 'i') {
                        return 3;
                    } else if (choice.charAt(0) == 'D' || choice.charAt(0) == 'd') {
                        return 4;
                    } else if (choice.charAt(0) == 'P' || choice.charAt(0) == 'p') {
                        return 5;
                    } else if (choice.charAt(0) == 'S' || choice.charAt(0) == 's') {
                        return 6;
                    } else if (choice.charAt(0) == 'C' || choice.charAt(0) == 'c') {
                        return 7;
                    } else if (choice.charAt(0) == 'X' || choice.charAt(0) == 'x') {
                        break;
                    } else {
                        System.out.println("Invalid choice entered (Case 2) - please enter a single character from the above options.");
                        if (currHeap == 'A') {
                            return 1;
                        } else {
                            return 2;
                        }
                    }
        }
        
        //When the user selects 'X', exit the program.
        return -1;
    }
    
}
