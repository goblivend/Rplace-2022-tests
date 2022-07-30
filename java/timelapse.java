// >>>>>>>> Begin imports >>>>>>>>

import java.awt.image.BufferedImage;
import java.io.File;
import java.util.Scanner;
import javax.imageio.ImageIO;
import java.awt.*;

// Error : "1718,1424,1752"

// <<<<<<<<< End imports <<<<<<<<<

public class timelapse {
    public static void main(String[] args) {
        try {
            if (args.length == 0) {
                System.out.println("Please use the following format: java timelapse <fileName> <rate> <output folder>");
                return;
            }
            String fileName = args[0];
            long tStart = System.currentTimeMillis();
            BufferedImage img = getIMG(fileName, Integer.parseInt(args[1]), args[2]);
            long tEnd = System.currentTimeMillis();

            System.out.println(tEnd - tStart);
        } catch (Exception e) {
            System.out.println(e);
        }

    }

    public static BufferedImage getIMG(String fileName, int rate, String destination) {
        try {
            BufferedImage rplace = new BufferedImage(2000, 2000, BufferedImage.TYPE_INT_ARGB);
            File f = new File(fileName);
            Scanner reader = new Scanner(f);
            reader.nextLine();
            int line = 0;



            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                // String ts = data.split(",")[0];

                String hexColor = data.substring(data.indexOf("#") + 1, data.indexOf("#") + 7);
                int color = Integer.parseInt(hexColor, 16);

                Tuple<Integer, Integer> coordinates = getCoordinates(data);
                int x = coordinates.x;
                int y = coordinates.y;

                rplace.setRGB(x, y, new Color(color).getRGB());
                line +=1;

                if (line % rate == 0){
                    ImageIO.write(rplace, "png", new File(destination + (line / rate) + ".png"));
                    System.out.println(destination + (line / rate) + ".png");
                }
            }
            reader.close();
            ImageIO.write(rplace, "png", new File(destination + (line / rate) + ".png"));
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return null;
    }

    public static Tuple<Integer, Integer> getCoordinates(String data){
        String coordinates = data.substring(data.indexOf("\"")+1, data.length()-1);
        if (coordinates.length() > 9){
            System.out.println(data);
            return null;
        }

        String xStr = coordinates.substring(0, coordinates.indexOf(","));
        String yStr = coordinates.substring(coordinates.indexOf(",") + 1, coordinates.length());

        int x = Integer.parseInt(xStr);
        int y = Integer.parseInt(yStr);

        return new Tuple<Integer, Integer>(x, y);
    }
}
// "YYYY-MM-DD HH-mm-ss.SSS zzz"