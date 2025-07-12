import java.util.*;

public class Maps {
    public static void main(String[] args) {
        // HashMap: Unordered, allows null keys/values, not thread-safe
        Map<String, Integer> hashMap = new HashMap<>();
        hashMap.put("Apple", 10);
        hashMap.put("Banana", 20);
        hashMap.put("Orange", 30);
        hashMap.put(null, 40); // allows null key
        System.out.println("HashMap: " + hashMap);
        System.out.println("HashMap get(Apple): " + hashMap.get("Apple"));
        hashMap.remove("Banana");
        System.out.println("HashMap after remove: " + hashMap);

        // LinkedHashMap: Maintains insertion order, allows null keys/values
        Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("Apple", 10);
        linkedHashMap.put("Banana", 20);
        linkedHashMap.put("Orange", 30);
        linkedHashMap.put(null, 40);
        System.out.println("LinkedHashMap: " + linkedHashMap);

        // TreeMap: Sorted by keys, does NOT allow null keys
        Map<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("Apple", 10);
        treeMap.put("Banana", 20);
        treeMap.put("Orange", 30);
        // treeMap.put(null, 40); // Throws NullPointerException
        System.out.println("TreeMap: " + treeMap);

        // Hashtable: Legacy, synchronized, does NOT allow null keys/values
        Map<String, Integer> hashtable = new Hashtable<>();
        hashtable.put("Apple", 10);
        hashtable.put("Banana", 20);
        hashtable.put("Orange", 30);
        // hashtable.put(null, 40); // Throws NullPointerException
        System.out.println("Hashtable: " + hashtable);

        // Common Map methods overview:
        // put(key, value), get(key), remove(key), containsKey(key), containsValue(value), keySet(), values(), entrySet()
        System.out.println("HashMap containsKey('Apple'): " + hashMap.containsKey("Apple"));
        System.out.println("HashMap keySet: " + hashMap.keySet());
        System.out.println("HashMap values: " + hashMap.values());
        System.out.println("HashMap entrySet: " + hashMap.entrySet());
    }
}
