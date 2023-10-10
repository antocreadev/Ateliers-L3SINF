import java.util.Random;

public class MyMadInt extends MyInt{
    private int niveauDeFolie; 

    protected static Random r = new Random();

    // constructor 
    public MyMadInt(int your_int, int borne_min, int borne_max, int niveauDeFolie){
        super(your_int, borne_min, borne_max ); 
        this.niveauDeFolie = niveauDeFolie;
    }

    // méthode 
    // @Overload
    public void incremente(){
        int aleatoire = r.nextInt(1, this.getYour_int()+1);
        int result = this.getYour_int() + aleatoire ;
        setYour_int(result);
    }

    @Override
    public boolean equals(Object x) {
        boolean result = false;
        if(x !=null){
            if (x instanceof De){
                MyMadInt xPrime = (MyMadInt) x; 
                result = (this.getYour_int() == xPrime.getYour_int()) && (this.borne_min == xPrime.borne_min) && (this.borne_max == xPrime.borne_max) && (this.borne_min == xPrime.borne_min) && (this.niveauDeFolie == xPrime.niveauDeFolie);
            }
        }
        return result;
    }

    @Override
    public String toString(){
        return "valeur : "+this.getYour_int() + " borne minimum : " + Integer.toString(this.borne_min) + " borne maximum : " + Integer.toString(this.borne_max) + " niveau de folie : " + Integer.toString(this.niveauDeFolie) ;
    }

    public static void main(String[] args) {
        MyMadInt myMadInt = new MyMadInt(2, 0, 10, 5);
        System.out.println(myMadInt);
        myMadInt.incremente();
        System.out.println(myMadInt);
    }
    
}
