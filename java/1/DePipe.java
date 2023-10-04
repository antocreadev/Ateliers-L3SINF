public class DePipe extends De {
    private int valueMinimum; 

    // constructor 
    public DePipe(int valueMinimum, String name, int nbFaces){
        super(nbFaces, name); // rappelle le constructeur parent
        if (valueMinimum>=0 && valueMinimum<=maximumNbFaces){
            this.valueMinimum = valueMinimum;
        }
        else{
            this.valueMinimum = 0; // default value
        }
    }

    // méthodes
    public Integer getValueMinimum(){
        return this.valueMinimum;
    }

    @Override
    public Integer lancer(){
        /* va appeler la methode lancer parent tant que le result est inferieur à la valueMinimum
        int result;
        do {
            result  = super.lancer(); // super. -> va appeler la méthode dans le parent
            System.out.println(result);
        }while (result < this.valueMinimum);
        return result;
        */
        // r est protected donc j'ai accès dans son enfant (et dans le package)
        return r.nextInt(this.getValueMinimum(), this.getNbFaces()+1);
    }
    public static void main(String[] args) {
        DePipe dePipe1 = new DePipe(5, "depipos", 6);
        System.out.println(dePipe1.getValueMinimum());
        System.out.println(dePipe1);
        System.out.println(dePipe1.lancer());
    }
}


