// >>>>>>>> Begin imports >>>>>>>>

import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

// <<<<<<<<< End imports <<<<<<<<<

public class averageColor {
    public static void main(String[] args) {
        int sizeSample = 1000000;
        try {
            FileWriter fw = new FileWriter("../averageColor.txt", true);

            long tStart = System.currentTimeMillis();
            getAVG(sizeSample);
            long tEnd = System.currentTimeMillis();

            String content = "sample " + sizeSample + ".csv : java : " + ((tEnd - tStart)/1000.0d)+ "\n";
            System.out.print(content);
            fw.write(content);
            fw.close();
        } catch (Exception e) {
            System.out.println(e);
        }

    }

    public static void getAVG(int sizeSample) {
        String fileName = "../sample " + sizeSample + ".csv";
        try {
            File f = new File(fileName);
            Scanner reader = new Scanner(f);
            reader.nextLine();
            double count = 0;
            double color = 0;
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                String hexColor = data.substring(data.indexOf("#") + 1, data.indexOf("#") + 7);
                color += Integer.parseInt(hexColor, 16);
                count++;
            }
            reader.close();
            System.out.println("average color : 0x" + Integer.toHexString((int) (color / count)));
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}