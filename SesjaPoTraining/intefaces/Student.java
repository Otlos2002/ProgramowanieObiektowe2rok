package pl.kmi.ujd.otlowski;

public class Student extends Person implements Cloneable, Comparable<Person> {
    private Double gpa;

    public Student(String nazwisko, int year, int month, int day, Double gpa) {
        super(nazwisko, year, month, day);
        this.gpa = gpa;
    }

    @Override
    public String toString() {
        return super.toString()+ getClass().getSimpleName()+
                "[" + gpa +
                ']';
    }

    @Override
    public int compareTo(Person otherObject) {
        int result = super.compareTo(otherObject);
        if(result != 0) return result;
        if(otherObject instanceof Student studentDrugi){
            return Double.compare(this.gpa, studentDrugi.gpa);
        }
        return result;
    }

    @Override
    public Person clone() throws CloneNotSupportedException {
        return super.clone();
    }
}
