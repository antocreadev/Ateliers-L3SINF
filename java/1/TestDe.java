public class TestDe {
    public static void main(String[] args) {
        De de1 = new De(6);
        System.out.println(de1.lancer(de1.getNbFaces()));
        System.out.println(de1.getNbFaces());


        De de2 =  new De();
        System.out.println(de2.getNbFaces());

        De de3 =  new De("DE 3");
        System.out.println(de3.getNbFaces());

        System.out.println("nombre de de : " + De.getCounter());
        

    }
}
