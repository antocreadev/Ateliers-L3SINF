import java.util.*;
class De{
    private String name;
    private int nbFaces;
    protected static Random r = new Random();

    public final static int minimumNbFaces= 3;
    public final static int maximumNbFaces= 120;

    private static int counter = 0; // static : variable de Class


    public De(int nbFaces, String name){
        this.name = name; 
        this.nbFaces = setNbFaces(nbFaces);
        counter++;
    }

    // @Overload
    public De(int nbFaces){
        this(nbFaces, "Dé n°" + Integer.toString(counter));
    }

    // @Overload
    public De(String name){
        this(6, name ); 
    }

    // @Overload
    public De(){
        this(6, "Dé n°" + Integer.toString(counter));
    }

    // méthodes
    public int getNbFaces(){
        return this.nbFaces;
    }

    public Integer setNbFaces(int nbFaces){
        int result = minimumNbFaces;
        if(nbFaces>= minimumNbFaces && nbFaces<=maximumNbFaces){
            this.nbFaces = nbFaces;
            result = nbFaces;
        }
        else{
             System.err.println("erreur"); // print erreur 
        }
        return result;
    }

    public Integer lancer(){
        //Pour générer un nombre aléatoire entre 0 et nb (exclu)
        int nbAleatoire= r.nextInt(1, this.nbFaces+1);
        return nbAleatoire;
    }

    // @Overload
    public Integer lancer(int nbLancer){
        int result= lancer();
        for (int i=1; i<nbLancer; ++i){
            int nbAleatoire =  lancer();
            if (result< nbAleatoire){
                result = nbAleatoire;
            }
        }
        return result;
    }

    static public Integer getCounter(){
        return counter;
    }

    @Override
    public String toString(){
        return "name : "+this.name + " nombre de faces : " + Integer.toString(this.nbFaces);
    }

   @Override
   public boolean equals(Object x) {
    boolean result = false;
    if(x !=null){
        De xPrime = (De) x; // casting | Down cast (convert Object to De())
        // cast ne convertie pas vraiment, aucun constructeur n'est appellé (c'est poir caché au compilateur, conversion entre nous et le compilateur)
        if (x instanceof De){
            result = (this.name == xPrime.name) && (this.nbFaces == xPrime.nbFaces);
            // this.nbFaces est un Objet String mais le `==` fonctionne car optimisation de la machine virtuelle. On pourait utiliser la méthode equals de l'Objet String (qui est déjà redéfini)
        }
        }
        return result;
    }

    public static void main(String[] args) {
        De de1 = new De("de1");
        De de2 = new De("de1");
        Object o1 = new De("de1"); // up casting 
        System.out.println(de1);
        System.out.println(de1.lancer(2));
        System.out.println(de1.equals(o1));
        System.out.println(de1);
    }
}
