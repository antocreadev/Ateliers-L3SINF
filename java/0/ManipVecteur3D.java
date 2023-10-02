public class ManipVecteur3D {
    public static void main(String[] args) {
        Vecteur3D A = new Vecteur3D(3, 2, 5);
        System.out.println("A = " + A);
        System.out.println("||A|| = " + A.norme());

        Vecteur3D B = new Vecteur3D(1, 2, 3);
        System.out.println("B = " + B);
        System.out.println("||B|| = " + B.norme());

        System.out.println("A + B = " + Vecteur3D.somme(A, B));
        System.out.println("A + B = " + A.somme(B));
        System.out.println("A . B = " + Vecteur3D.produitScalaire(A, B));
        System.out.println("A . B = " + A.produitScalaire(B));
    }
}
