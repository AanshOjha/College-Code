import java.util.*;

// Demonstrates Set interface and its common implementations
public class Sets {
    public static void main(String[] args) {
        // HashSet: No order, allows null, fast operations
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Apple");
        hashSet.add("Banana");
        hashSet.add("Orange");
        hashSet.add("Apple"); // Duplicate, will not be added
        hashSet.add(null);

        System.out.println("HashSet: " + hashSet);
        System.out.println("HashSet contains 'Banana'? " + hashSet.contains("Banana"));
        hashSet.remove("Orange");
        System.out.println("HashSet after removing 'Orange': " + hashSet);

        // LinkedHashSet: Maintains insertion order
        Set<String> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add("Apple");
        linkedHashSet.add("Banana");
        linkedHashSet.add("Orange");
        linkedHashSet.add("Apple"); // Duplicate, will not be added

        System.out.println("LinkedHashSet: " + linkedHashSet);

        // SortedSet Interface and TreeSet implementation
        // TreeSet: Sorted order, no nulls allowed
        SortedSet<String> treeSet = new TreeSet<>();
        treeSet.add("Banana");
        treeSet.add("Apple");
        treeSet.add("Orange");
        treeSet.add("Aansh");
        // treeSet.add(null); // Throws NullPointerException

        System.out.println("TreeSet: " + treeSet);
        System.out.println("First element in TreeSet: " + treeSet.first());
        System.out.println("Last element in TreeSet: " + treeSet.last());
        System.out.println("TreeSet headSet('Banana'): " + treeSet.headSet("Banana"));
        System.out.println("TreeSet tailSet('Banana'): " + treeSet.tailSet("Banana"));

        // Overview: All Set implementations do not allow duplicates.
        // HashSet: Fastest, no order.
        // LinkedHashSet: Maintains insertion order.
        // TreeSet: Sorted order, no nulls.
        // Common methods: add(), remove(), contains(), size(), isEmpty(), clear(), iterator()
    }
}
