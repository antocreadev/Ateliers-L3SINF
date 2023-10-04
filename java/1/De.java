import java.util.*;
class De{
    private String name;
    protected int nbFaces;
    protected static Random r = new Random();

    public final static int MINIMUM_NBFACES= 3;
    public final static int MAXIMUM_NBFACES= 120;

    private final static int DEFAULT_NBFACES = 6;

    private static int counter = 0; // static : variable de Class

    // constructor 
    public De(int nbFaces, String name){
        setName(name);
        setNbFaces(nbFaces);
        counter++;
    }

    // @Overload
    public De(int nbFaces){
        this(nbFaces, "");
    }

    // @Overload
    public De(String name){
        this(DEFAULT_NBFACES, name); 
    }

    // @Overload
    public De(){
        this(DEFAULT_NBFACES, null);
    }

    // méthodes
    public int getNbFaces(){
        return this.nbFaces;
    }

    public void setNbFaces(int nbFaces){
        if(nbFaces>= MINIMUM_NBFACES && nbFaces<=MAXIMUM_NBFACES){
            this.nbFaces = nbFaces;
        }
        else{
             System.err.println("erreur : le nombre de face doit être inferieur à " + Integer.toString(MAXIMUM_NBFACES) + " et superieur à " + Integer.toString(MINIMUM_NBFACES) + ". Ansi la valeur va être changer par une valeur par défaut : " + Integer.toString(DEFAULT_NBFACES)); // print erreur 
             this.nbFaces = DEFAULT_NBFACES;
        }
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

    private String setName(String name){
        String result = "Dé n°" + Integer.toString(counter);
        if (name== null || name == "" || name==" "){
            this.name = result;
        }
        else{
            this.name= name;
            result = name;
        }
        return result;
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
        System.out.println(new De(119999, "chose"));
    }
}
