package pl.kmi.ujd.otlowski;
import java.time.LocalDate;
import java.util.Objects;

public class Person implements Cloneable, Comparable<Person> {

    private String nazwisko;
    private LocalDate dataUrodzenia;

    public Person(String nazwisko, int year, int month, int day) {
        this.nazwisko = nazwisko;
        dataUrodzenia = LocalDate.of(year,month,day);
    }

    public String getNazwisko() {
        return nazwisko;
    }

    public LocalDate getDataUrodzenia() {
        return dataUrodzenia;
    }

    @Override
    public int compareTo(Person otherObject) {
        int result = nazwisko.compareTo(otherObject.nazwisko);
        if (result != 0) return result;
        return dataUrodzenia.compareTo(otherObject.dataUrodzenia);
    }

    @Override
    public Person clone() throws CloneNotSupportedException {
        return (Person)super.clone();
    }

    @Override
    public boolean equals(Object otherObject) {
        if (this == otherObject) return true;
        if (otherObject == null || getClass() != otherObject.getClass()) return false;
        Person person = (Person) otherObject;
        return nazwisko.equals(person.nazwisko) && dataUrodzenia.equals(person.dataUrodzenia);
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() +"[" +
                 nazwisko + ", "+
                 dataUrodzenia +
                ']';
    }

}
