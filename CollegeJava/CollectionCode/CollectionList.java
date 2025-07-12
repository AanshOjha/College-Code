import java.util.*;

// Demonstrates usage of Iterator, Collection, List, ArrayList, LinkedList, Vector, Stack, Queue
public class CollectionList {
    public static void main(String[] args) {
        System.out.println("It works!");

        // 1. Collection Interface (implemented by List, Set, Queue, etc.)
        Collection<String> collection = new ArrayList<>(Arrays.asList("D", "E", "F"));
        System.out.println("Collection: " + collection);

        // 2. List Interface (ordered, allows duplicates)
        List<String> arrayList = new ArrayList<>(Arrays.asList("A", "B", "C"));
        List<String> linkedList = new LinkedList<>(Arrays.asList("2", "G", "H"));
        List<String> vector = new Vector<>(Arrays.asList("X", "Y", "Z"));

        System.out.println("ArrayList: " + arrayList);
        System.out.println("LinkedList: " + linkedList);
        System.out.println("Vector: " + vector);

        // 3. Iterator Interface (traverse collections)
        Iterator<String> it = arrayList.iterator();
        System.out.print("Iterating ArrayList: ");
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
        System.out.println();

        // 4. ArrayList basic usage
        arrayList.add("D");
        arrayList.remove("B");
        System.out.println("Modified ArrayList: " + arrayList);

        // 5. LinkedList basic usage (addFirst, addLast)
        linkedList.addFirst("First");
        linkedList.addLast("Last");
        System.out.println("Modified LinkedList: " + linkedList);

        // 6. Vector basic usage
        vector.add("W");
        vector.remove(1);
        System.out.println("Modified Vector: " + vector);

        // 7. Stack (LIFO, extends Vector)
        Stack<String> stack = new Stack<>();
        stack.push("Stack1");
        stack.push("Stack2");
        stack.push("Stack3");
        System.out.println("Stack: " + stack);
        System.out.println("Stack pop: " + stack.pop()); // removes top element

        // 8. Queue Interface (FIFO, implemented by LinkedList, PriorityQueue, etc.)
        Queue<String> queue = new LinkedList<>();
        queue.offer("Q1");
        queue.offer("Q2");
        queue.offer("Q3");
        System.out.println("Queue: " + queue);
        System.out.println("Queue poll: " + queue.poll()); // removes head

        // 9. Enhanced for-loop for iteration (works for all collections)
        System.out.print("For-each over LinkedList: ");
        for (String s : linkedList) {
            System.out.print(s + " ");
        }
        System.out.println();

        // 10. Commented: Other common methods
        // arrayList.get(index), arrayList.set(index, value), arrayList.size()
        // linkedList.peek(), linkedList.poll()
        // vector.elementAt(index)
        // stack.peek(), stack.empty()
        // queue.peek(), queue.isEmpty()
    }
}
