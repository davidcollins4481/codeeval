import java.io.*;

public class SumOfDigits {
    public static void main(String[] args) {
        try {
            FileReader file = new FileReader(args[0]);
            BufferedReader in = new BufferedReader(file);
            String line;
            while ((line = in.readLine()) != null) {
                int sum = 0;
                for (int i = 0; i < line.length();i++) {
                    sum += Integer.parseInt(Character.toString(line.charAt(i)));
                }
                System.out.println(sum);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
