// + package

public class AppAOC {

    public static void main(String[] args) {

        System.out.println("\n\n   ******   DAY 2 - I WAS TOLD THERE WOULD BE NO MATH   *****   \n");

        String[] data_d2_iwttwbnm = getLinesFromFile("day2-I Was Told There Would Be No Math.txt");

        int surfaceTotal = 0;
        int longueurRubanTotal = 0;

        // Parcourir chaque dimensions
        for (String dimension : data_d2_iwttwbnm) {
            if (dimension != null) {
                String dim_cote[] = dimension.split("x");

                int l = Integer.parseInt(dim_cote[0]);
                int w = Integer.parseInt(dim_cote[1]);
                int h = Integer.parseInt(dim_cote[2]);

                int surface = 2 * l * w + 2 * w * h + 2 * l * h; // Surface pour chaque cadeau
                
                int surface_supp;
                int longueur_ruban;

                // Calculer la surface supplémentaire et calculer la longueur du ruban
                if (l <= w && l <= h) {
                    int minCote = l;
                    int moyCote = Math.min(w, h);
                    surface_supp = minCote * moyCote;
                    longueur_ruban = minCote * 2 + moyCote * 2;
                }
                else if (w <= l && w <= h) {
                    int minCote = w;
                    int moyCote = Math.min(l, h);
                    surface_supp = minCote * moyCote;
                    longueur_ruban = minCote * 2 + moyCote * 2;
                } else {
                    int minCote = h;
                    int moyCote = Math.min(l, w);
                    surface_supp = minCote * moyCote;
                    longueur_ruban = minCote * 2 + moyCote * 2;
                };

                longueur_ruban += l * w * h;

                surfaceTotal += surface;
                surfaceTotal += surface_supp;

                longueurRubanTotal += longueur_ruban;

            }
        }

        System.out.println("Surface papier cadeau à commander : " + surfaceTotal);
        System.out.println("La longueur total de ruban est de : " + longueurRubanTotal);

    }
}
