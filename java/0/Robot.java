// Toutes les class ont une méthode toString() qui est une méthode « héritée » de la classe Object
class Robot {
    private String ref; // private : appartenant à la Classe Robot (n'est pas accessible dans une autre
                        // class)
    private String name;
    private int x, y;
    private int orientation;

    public static final int NORD = 1; // public pour accéder en dehors de la class, static car ce sont des variables
                                      // de la classe et pas unique à chaque instance
    public static final int SUD = 2;
    public static final int EST = 3;
    public static final int OUEST = 4;

    private static int counter = 0; // static : variable de Class
    // static : permet de dire que cette variable n'est pas unique à chaque instance
    // (il a une seul variable pour toute les instances)

    // Constructeur par défaut
    public Robot(String name, int x, int y, int orientation) {
        this.name = name;
        this.x = x;
        this.y = y;
        this.orientation = orientation;
        this.ref = "robot" + Integer.toString(counter);
        counter++;
    }

    // Surcharge du constructeur par défaut
    public Robot(String name) {
        this(name, 0, 0, Robot.NORD); // appelle un constructeur
    }

    // méthodes
    public void setOrientation(int orientation) {
        if (orientation <= 4 && orientation >= 1) {
            this.orientation = orientation;
        }
    }

    public void deplacer() {
        if (this.orientation == NORD) {
            this.y++;
        } else if (this.orientation == EST) {
            this.x++;
        } else if (this.orientation == SUD) {
            this.y--;
            if (this.y < 0) {
                this.y = 0;
            }
        } else if (this.orientation == OUEST) {
            this.x--;
            if (this.x < 0) {
                this.x = 0;
            }
        }
    }

    public String afficheToi() {
        return this.name + this.ref + Integer.toString(this.x) + Integer.toString(this.y)
                + Integer.toString(this.orientation);
    }

    // redefinition de la méthode tostring (méthode « héritée » de la classe Object)
    public String toString() {
        return this.name + this.ref + Integer.toString(this.x) + Integer.toString(this.y)
                + Integer.toString(this.orientation);
    }

    // main
    public static void main(String[] args) { // le main est obligatoire
        Robot tata = new Robot("Toto", 10, 20, Robot.SUD);
        Robot tutu = new Robot("Titi");

        System.out.println(tata.afficheToi());
        System.out.println(tutu.afficheToi());

    }
}
