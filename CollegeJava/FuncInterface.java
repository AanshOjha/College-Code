@FunctionalInterface
    interface Square {
        int calculate(int x);
        static int cube(int x) {
            return x * x * x; // This method is not abstract, so it won't break the functional interface contract
        }
    }



public class FuncInterface {
    public static void main(String[] args) {
        Square s = (int x) -> x * x;
        Square n = (int y) -> y * y * y;
        System.out.println("Square of 5 is: " + s.calculate(5));
    }
}
