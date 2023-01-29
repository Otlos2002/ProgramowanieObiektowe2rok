import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class LineReader {
    public static void main(String[] args){
        ArrayList<String> lines = new ArrayList<>();
        try{
            Scanner scanner = new Scanner(new File("D:\\javaProjekty\\SesjaInterfejstMyself\\plikTekstowy.txt"));
            while (scanner.hasNextLine()){
                lines.add(scanner.nextLine());
            }
            scanner.close();
        }
        catch (FileNotFoundException e){
            System.out.println("File not found");
            return;
        }
        for(String line : lines){
            System.out.println(line);
        }
        System.out.println("Natural order: ");
        lines.sort(null);

        for(String line : lines){
            System.out.println(line);
        }
        System.out.println("Shortest to longest:");

        class LineLengthComparator implements Comparator<String>{
            @Override
            public int compare(String o1, String o2){
                return o1.length() - o2.length();
            }
        }
        lines.sort(new LineLengthComparator());
        for(String line : lines){
            System.out.println(line);
        }
        String[] linie = new String[lines.size()];
        for(int i=0; i< lines.size(); i++){
            linie[i] = lines.get(i);
        }

        for(String line : linie){
            System.out.println(line);
        }
        Arrays.sort(linie,null);
        for(String line : linie){
            System.out.println(line);
        }
        Arrays.sort(linie, new LineLengthComparator());
        for(String line : linie){
            System.out.println(line);
        }

    }
}
