// >>>>>>>> Begin imports >>>>>>>>

import java.awt.image.BufferedImage;
import java.io.File;
import java.util.Scanner;
import javax.imageio.ImageIO;
import java.awt.*;

// Error : "1718,1424,1752"

// <<<<<<<<< End imports <<<<<<<<<

public class rplace {
    public static void main(String[] args) {
        // int sizeSample = 100000000;
        try {
            // String fileName = "../sample " + sizeSample + ".csv";
            String fileName = args[0]; //"../Day 5.csv";
            long tStart = System.currentTimeMillis();
            BufferedImage img = getIMG(fileName);
            long tEnd = System.currentTimeMillis();


            System.out.println(tEnd - tStart);

        } catch (Exception e) {
            System.out.println(e);
        }

    }

    public static BufferedImage getIMG(String fileName) {
        try {
            BufferedImage rplace = new BufferedImage(2000, 2000, BufferedImage.TYPE_INT_ARGB);
            File f = new File(fileName);
            Scanner reader = new Scanner(f);
            reader.nextLine();
            int line = 0;



            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                // System.out.println(data);

                String ts = data.split(",")[0];
                // System.out.println(ts);



                String hexColor = data.substring(data.indexOf("#") + 1, data.indexOf("#") + 7);
                int color = Integer.parseInt(hexColor, 16);
                String coordinates = data.substring(data.indexOf("\"")+1, data.length()-1);
                if (coordinates.length() > 9){
                    System.out.println(data);
                    continue;
                }
                String xStr = coordinates.substring(0, coordinates.indexOf(","));
                String yStr = coordinates.substring(coordinates.indexOf(",") + 1, coordinates.length());
                int x = Integer.parseInt(xStr);
                int y = Integer.parseInt(yStr);

                rplace.setRGB(x, y, new Color(color).getRGB());
                line +=1;
            }
            reader.close();
            File outputfile = new File(fileName + ".png");
            ImageIO.write(rplace, "png", outputfile);
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return null;
    }
}
// "YYYY-MM-DD HH-mm-ss.SSS zzz"