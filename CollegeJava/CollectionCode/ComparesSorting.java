import java.io.*;
import java.util.*;  

// Class representing a Student, implementing Comparable for natural ordering
class Student implements Comparable<Student> {
    int rollNo;
    String name;
    int age;

    Student(int rollNo, String name, int age) {
        this.rollNo = rollNo;
        this.name = name;
        this.age = age;
    }

    // Natural ordering by rollNo
    @Override
    public int compareTo(Student s) {
        return this.rollNo - s.rollNo;
    }

    @Override
    public String toString() {
        return rollNo + " " + name + " " + age;
    }
}

// Comparator to sort Students by name
class NameComparator implements Comparator<Student> {
    public int compare(Student s1, Student s2) {
        return s1.name.compareTo(s2.name);
    }
}

// Comparator to sort Students by age
class AgeComparator implements Comparator<Student> {
    public int compare(Student s1, Student s2) {
        return s1.age - s2.age;
    }
}

public class ComparesSorting {
    public static void main(String[] args) throws Exception {
        // Sample data
        List<Student> students = new ArrayList<>();
        students.add(new Student(101, "Vijay", 23));
        students.add(new Student(106, "Ajay", 27));
        students.add(new Student(105, "Jai", 21));

        // Sorting using Comparable (by rollNo)
        Collections.sort(students);
        System.out.println("Sorted by rollNo (Comparable):");
        for (Student s : students) System.out.println(s);

        // Sorting using Comparator (by name)
        Collections.sort(students, new NameComparator());
        System.out.println("\nSorted by name (Comparator):");
        for (Student s : students) System.out.println(s);

        // Sorting using Comparator (by age)
        Collections.sort(students, new AgeComparator());
        System.out.println("\nSorted by age (Comparator):");
        for (Student s : students) System.out.println(s);

        // --- Properties class usage ---
        // Properties is used to maintain configuration, key-value pairs
        Properties props = new Properties();
        props.setProperty("username", "admin");
        props.setProperty("password", "12345");

        // Store properties to a file
        try (FileOutputStream fos = new FileOutputStream("config.properties")) {
            props.store(fos, "User Credentials");
        }

        // Load properties from a file
        Properties loadedProps = new Properties();
        try (FileInputStream fis = new FileInputStream("config.properties")) {
            loadedProps.load(fis);
        }

        // Accessing properties
        System.out.println("\nLoaded Properties:");
        System.out.println("username: " + loadedProps.getProperty("username"));
        System.out.println("password: " + loadedProps.getProperty("password"));

        // Most frequent Properties methods: setProperty, getProperty, load, store
    }
}

/*
Overview:
- Comparable: For natural ordering, implement compareTo().
- Comparator: For custom ordering, implement compare().
- Properties: For key-value configuration, use setProperty(), getProperty(), load(), store().
*/
