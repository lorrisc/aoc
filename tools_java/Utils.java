// + package

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Utils {

    public static int[] extractCoordLedDay6(String mode, String line) {
        // Extraire infos coordonnées
        line = line.replace(mode, "");
        line = line.replace(" through ", ";");

        String[] coord = line.split(";");

        String pos1 = coord[0];
        String pos2 = coord[1];

        // Coordonnée point initial x, y
        String[] pos1_xy = pos1.split(",");
        int pos1_x = Integer.parseInt(pos1_xy[0]);
        int pos1_y = Integer.parseInt(pos1_xy[1]);

        // Coordonnée point final x, y
        String[] pos2_xy = pos2.split(",");
        int pos2_x = Integer.parseInt(pos2_xy[0]);
        int pos2_y = Integer.parseInt(pos2_xy[1]);

        int[] coord_arr = {pos1_x, pos1_y, pos2_x, pos2_y};
        return coord_arr;
    }

    public static String getStringFromFile(String fileName) {

        try (Scanner scanner = new Scanner(new FileInputStream(fileName))) {
            /*----- Lecture du fichier -----*/
            String ch_file = "";
            while (scanner.hasNextLine()) {
                String ch = scanner.nextLine();
                ch = ch.trim();
                ch_file += ch;
            }
            return ch_file;
        } catch (FileNotFoundException fne) {
            return fileName + " est absent !";
        }
    }

    public static String[] getLinesFromFile(String fileName) {

        try (Scanner scanner = new Scanner(new FileInputStream(fileName))) {
            /*----- Lecture du fichier -----*/
            String[] lines = new String[10];

            int i = 0;
            while (scanner.hasNextLine()) {
                if (i < lines.length) {
                    lines[i] = scanner.nextLine();
                } else {
                    lines = Arrays.copyOf(lines, lines.length * 2);
                    lines[i] = scanner.nextLine();
                }
                i ++;
            }
            return lines;
        } catch (FileNotFoundException fne) {
            String[] lines = new String[0];
            return lines;
        }
    }
}
