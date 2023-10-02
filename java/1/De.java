class De{
    private String name;
    private int nbFaces;

    public final static int minimumNbFaces= 3;
    public final static int maximumNbFaces= 120;

    // constructor

    // Une instance de Dé peut être créée sans spécifier aucun paramètre. Dans ce cas, par défaut, le dé aura 6 Faces et un nom par défaut “De”. 

    // Une instance de Dé peut aussi être créée en spécifiant un nombre de faces entier passé en paramètre, sous réserve qu’il soit compris dans les bornes (3 et 120).

    // Une instance de Dé peut également être créée en spécifiant un paramètre nom (String).

    public De(){
        this.name = "Dé";
        this.nbFaces = 6; 
    }
    public De(int nbFaces){
        this();
        setNbFaces(nbFaces);
    }

    public De(String name){
        this(); 
        this.name = name;
    }

    // méthodes

    public int getNbFaces(){
        return this.nbFaces;
    }

    public void setNbFaces(int nbFaces){
        if(nbFaces>= minimumNbFaces && nbFaces<=maximumNbFaces){
            this.nbFaces = nbFaces;
        }
        else{
             System.err.println("erreur"); // print erreur 
        }
    }





}