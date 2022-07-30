// >>>>>>>> Begin imports >>>>>>>>

import java.awt.image.BufferedImage;
import java.io.File;
import java.util.Scanner;
import javax.imageio.ImageIO;
import java.awt.*;
import java.util.Arrays;
import java.util.List;


// Error : "1718,1424,1752"

// <<<<<<<<< End imports <<<<<<<<<

public class filter {
    public static void main(String[] args) {
        try {
            System.out.print("[");
            for (int i = 0; i < args.length; i++) {
                System.out.print(args[i] + ", ");
            }
            System.out.println("]");
            if (args.length == 0) {
                System.out.println("Please use the following format: java timelapse <fileName> <filter>");
                return;
            }
            String fileName = args[0];
            long tStart = System.currentTimeMillis();
            getIMG(fileName, Arrays.asList(args[1].split(",")));
            long tEnd = System.currentTimeMillis();

            System.out.println(tEnd - tStart);
        } catch (Exception e) {
            System.out.println(e);
        }

    }

    public static void getIMG(String fileName, List<String> filter) {
        try {
            BufferedImage rplace = new BufferedImage(2000, 2000, BufferedImage.TYPE_INT_ARGB);
            File f = new File(fileName);
            Scanner reader = new Scanner(f);
            reader.nextLine();
            int line = 0;


            for (String data : filter) {
                System.out.print("[");
                for(char c : data.toCharArray()) {
                    System.out.print("'" + c + "', ");
                }
                System.out.println("]");
            }

            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                // String ts = data.split(",")[0];

                String hexColor = data.substring(data.indexOf("#") + 1, data.indexOf("#") + 7);
                if (filter.contains(hexColor)){
                    int color = Integer.parseInt(hexColor, 16);

                    Tuple<Integer, Integer> coordinates = getCoordinates(data);
                    int x = coordinates.x;
                    int y = coordinates.y;

                    if (( (!hexColor.equals("000000")) && (!hexColor.equals("FFFFFF"))) || rplace.getRGB(x, y) == 0){
                        rplace.setRGB(x, y, new Color(color).getRGB());
                    }

                }

                if (line % 1000000 == 0){
                    System.out.print("#");
                }
                line += 1;
            }
            reader.close();
            ImageIO.write(rplace, "png", new File(fileName + ".png"));
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return;
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