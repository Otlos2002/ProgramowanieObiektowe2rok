public class Main {
    public static void main(String[] args) {
        Pair<Double> para1 = new Pair<>(5.69, 1.3);
        System.out.println(para1.getFirst());
        System.out.println(para1.getSecond());
        para1.swap();
        System.out.println(para1.getFirst());
        System.out.println(para1.getSecond());
        Pair<Integer> paraT = new Pair<>(6, 9);
        Pair<Integer> para2 = PairUtil.swapp(paraT);
        System.out.println(para2.getFirst());
        System.out.println(para2.getSecond());
        Integer[] sortedarr = {1,2,3,4,5};
        Integer[] unsortedarr = {5,4,2,5,1};
        System.out.println(ArrayUtil.isSorted(sortedarr));
        System.out.println(ArrayUtil.isSorted(unsortedarr));
        System.out.println(ArrayUtil.binSearch(sortedarr, 7));
        System.out.println(ArrayUtil.binSearch(sortedarr, 5));
        for(int i=0; i<unsortedarr.length; i++){
            System.out.println(unsortedarr[i]);
        }
        System.out.println("________--");
        ArrayUtil.selectionSort(unsortedarr);
        for(int i=0; i<unsortedarr.length; i++){
            System.out.println(unsortedarr[i]);
        }

    }
}