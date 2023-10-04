public class DePipe extends De {
    private int valueMinimum; 
    private int nombre; 
    private int name;

    // constructor 
    public DePipe(int valueMinimum, int nombre, String name){
        // super
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

    public static void main(String[] args) {
        DePipe dePipe1 = new DePipe(1222);
        System.out.println(dePipe1.getValueMinimum());
        System.out.println(dePipe1.getNbFaces());
    }
}


