import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;

public class Lowercase {

    public static void main(String[] args) {
        File file = new File(args[0]);
        try {
            BufferedReader in  = new BufferedReader(new FileReader(file));
            String line;
            while ((line = in.readLine()) != null) {
                String[] lineArray = line.split(" ");
                if (lineArray.length > 0) {
                    System.out.println(line.toLowerCase());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
     }
}
