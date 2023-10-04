public class DeMemoire extends De{
    private int lastLancer;

    // constructor 
    public DeMemoire(int nbFaces, String name){
        super(nbFaces, name);
        this.lastLancer = super.lancer();
    }

    // méthodes
    @Override
    public Integer lancer(){
        int result;
        do {
            result  = super.lancer(); // super. -> va appeler la méthode dans le parent
        }while (this.getLastLancer() == result);
        setLastLancer(result);
        return result;
    }

    public int getLastLancer() {
        return lastLancer;
    }

    private void setLastLancer(int lastLancer){
        this.lastLancer = lastLancer;
    }
    public static void main(String[] args) {
        DeMemoire deMemoire1 = new DeMemoire(6, "dePipe1");
        System.out.println(deMemoire1.lancer());
        System.out.println(deMemoire1.lancer());
        System.out.println(deMemoire1.lancer());
        System.out.println(deMemoire1.lancer());
        System.out.println(deMemoire1.lancer());
        System.out.println(deMemoire1.lancer());
    }
}
