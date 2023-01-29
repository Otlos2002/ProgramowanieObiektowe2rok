import java.util.ArrayList;
import java.util.Objects;

public class ArrayUtil {
    public static <T extends Comparable<T>> boolean isSorted(T[] array){
        for(int i=0; i<array.length-1; i++){
            if(array[i].compareTo(array[i+1]) >0){
                return false;
            }
        }
        return true;
    }
    public static <T> void dopisz(ArrayList<? extends T> pierwsza, ArrayList<T> druga){
        druga.addAll(pierwsza);
    }
    public static <T> void dopisz_suoer(ArrayList<T> pierwsza, ArrayList<? super T> druga){
        druga.addAll(pierwsza);
    }
    public static <T extends Comparable<T>> Integer binSearch(T[] array, T query){
        for(int i=0; i< array.length; i++){
            if(array[i].compareTo(query) == 0){
                return i;
            }
        }
        return -1;
    }
    public static <T extends Comparable<T>> void selectionSort(T[] array){
        for(int i=0; i< array.length-1; i++){
            int minIndex = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[j].compareTo(array[minIndex]) < 0) {
                    minIndex = j;
                }
            }
            T temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;
        }
    }
    public static <T extends Comparable<T>> void bubbleSort(T[]lista){
        for (int i=0; i< lista.length-1;i++){
            for(int j=0; j< lista.length-i-1;j++){
                if(lista[j].compareTo(lista[j+1]) > 0 ){
                    T temp = lista[j];
                    lista[j] = lista[j+1];
                    lista[j+1] = temp;
                }
            }
        }
    }

}
