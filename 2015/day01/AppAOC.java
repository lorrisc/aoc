// + package

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

public class AppAOC {
    public static void main(String[] args) {

        System.out.println("\n\n   ******   DAY 1 - NOT QUITE LISP   *****   \n");

        String data_d1_nql = getStringFromFile("day1-NotQuiteLisp.txt");

        int etg = 0;
        boolean sousSolVisite = false;
        int posCharSousSol = 0;

        for (int i = 0; i < data_d1_nql.length(); i++) {
            if (data_d1_nql.charAt(i) == '(') {
                etg ++;
            } else if (data_d1_nql.charAt(i) == ')') {
                etg --;
            }

            // Partie 2
            if (etg == -1 && sousSolVisite == false) {
                posCharSousSol = i + 1;
                sousSolVisite = true;
            }
        }

        System.out.println("Le pére noël doit se rendre à l'étage n° " + etg + " !");
        System.out.println("Le pére noël est enfin arrivé au sous sol au bout de " + posCharSousSol + " montée et ou descente !");

    }
}
