public class PairUtil {
    public static <T> Pair<T> swapp(Pair<T> para){
        return new Pair<>(para.getSecond(), para.getFirst());
    }
}
