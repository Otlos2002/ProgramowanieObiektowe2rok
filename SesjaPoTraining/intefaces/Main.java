import pl.kmi.ujd.otlowski.Person;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException {
        Person p1 = new Person("Otlowski", 2002, 06, 02);
        System.out.println(p1);
        Person p2 = new Person("Ciesielski", 2002, 12, 28);
        Person p3 = new Person("Ciesielski", 2002, 12, 28);
        System.out.println(p2);
        System.out.println(p1.compareTo(p2));
        System.out.println(p1.equals(p2));
        System.out.println(p2.equals(p3));
        System.out.println(p2.compareTo(p3));
        Person p4 = p2.clone();
        System.out.println(p2.equals(p4));
        System.out.println(p4);

    }
}