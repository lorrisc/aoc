// + package

public class AppAOC {

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

    public static void main(String[] args) {

        System.out.println("\n\n   ******   DAY 6 - PROBABLY A FIRE HAZARD   *****   \n");

        // Création de la matrice de 1 000 x 1 000
        boolean[][] matrice = new boolean[1000][1000];

        for (boolean[] bs : matrice) {
            for (boolean bs2 : bs) {
                bs2 = false;
            }
        }

        // PART TWO - Création de la matrice de 1 000 x 1 000
        int[][] matrice_p2 = new int[1000][1000];

        for (int[] bs : matrice_p2) {
            for (int bs2 : bs) {
                bs2 = 0;
            }
        }
        

        String[] data_d6_pafh = getLinesFromFile("day6-Probably a Fire Hazard.txt");

        for (String line : data_d6_pafh) {
            if (line != null) {

                // Détecter le mode (turn on, turn off, toggle)
                if(line.startsWith("turn on ")){

                    // Récupérer coordonnées
                    int[] coord_arr = extractCoordLedDay6("turn on ", line);
                    int pos1_x = coord_arr[0];
                    int pos1_y = coord_arr[1];
                    int pos2_x = coord_arr[2];
                    int pos2_y = coord_arr[3];

                    // Allumer chaque led OU Augmenter la luminosité de 1 (PART TWO)
                    for (int i = pos1_x; i <= pos2_x; i++) {
                        for (int j = pos1_y; j <= pos2_y; j++) {
                            matrice[i][j] = true;
                            matrice_p2[i][j] += 1;
                        }
                    }

                } else if(line.startsWith("turn off ")) {

                    // Récupérer coordonnées
                    int[] coord_arr = extractCoordLedDay6("turn off ", line);
                    int pos1_x = coord_arr[0];
                    int pos1_y = coord_arr[1];
                    int pos2_x = coord_arr[2];
                    int pos2_y = coord_arr[3];

                    // Eteindre chaque led OU Diminuer la luminosité de 1 (PART TWO)
                    for (int i = pos1_x; i <= pos2_x; i++) {
                        for (int j = pos1_y; j <= pos2_y; j++) {
                            matrice[i][j] = false;

                            if (matrice_p2[i][j] > 0) {
                                matrice_p2[i][j] -= 1;
                            }
                        }
                    }

                } else if(line.startsWith("toggle ")) {

                    // Récupérer coordonnées
                    int[] coord_arr = extractCoordLedDay6("toggle ", line);
                    int pos1_x = coord_arr[0];
                    int pos1_y = coord_arr[1];
                    int pos2_x = coord_arr[2];
                    int pos2_y = coord_arr[3];

                    // Toggle chaque led OU Augmenter la luminosité de 2 (PART TWO)
                    for (int i = pos1_x; i <= pos2_x; i++) {
                        for (int j = pos1_y; j <= pos2_y; j++) {
                            if (matrice[i][j] == true) {
                                matrice[i][j] = false;
                            } else {
                                matrice[i][j] = true;
                            }

                            matrice_p2[i][j] += 2;
                        }
                    }

                }
                
            }
        }

        // Parcourir la matrice et compter le nombre de led allumées OU compter la luminosité total (PART TWO)
        int nb_led_on = 0;
        int luminosite_total = 0;

        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                if (matrice[i][j] == true) {
                    nb_led_on ++;
                }
                luminosite_total += matrice_p2[i][j];
            }
        }

        System.out.println("Le nombre de led allumés est : " + nb_led_on);
        System.out.println("La luminosté total est de : " + luminosite_total);
    }
}
