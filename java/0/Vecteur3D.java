class Vecteur3D {
    private double x, y, z;

    public Vecteur3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vecteur3D() {
        this(0, 0, 0);
    }

    public String toString() {
        return "<" + x + ", " + y + ", " + z + ">";
    }

    public double norme() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public static double produitScalaire(Vecteur3D A, Vecteur3D B) {
        return A.x * B.x + A.y * B.y + A.z * B.z;
    }

    public double produitScalaire(Vecteur3D B) {
        return this.x * B.x + this.y * B.y + this.z * B.z;
    }

    public static Vecteur3D somme(Vecteur3D A, Vecteur3D B) {
        return new Vecteur3D(A.x + B.x, A.y + B.y, A.z + B.z);
    }

    public Vecteur3D somme(Vecteur3D B) {
        return new Vecteur3D(this.x + B.x, this.y + B.y, this.z + B.z);
    }
}

