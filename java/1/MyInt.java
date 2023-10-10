import java.util.Random;

public class MyInt {
    private int your_int;
    protected int borne_min; 
    protected int borne_max;

    // constructor 
    public MyInt(int your_int, int borne_min, int borne_max){
        this.borne_min = borne_min; 
        this.borne_max = borne_max;
        setYour_int(your_int); // default value in Int in java is 0 when value is not define
    }
    public MyInt(int borne_min, int borne_max){
        this(0, borne_min, borne_max);
    }

    // méthodes 
    public int getYour_int() {
        return your_int;
    }

    public void setYour_int(int your_int){
        if (your_int>= this.borne_min && your_int <= this.borne_max){
            this.your_int = your_int;
        }
    }
    public void incremente(){
        int result = this.your_int +1;
        setYour_int(result);
    }
    // Overload 
    public void incremente(int n){
        int result = this.your_int +n;
        setYour_int(result);
    }

    @Override
    public boolean equals(Object x) {
        boolean result = false;
        if(x !=null){
            if (x instanceof De){
                MyInt xPrime = (MyInt) x; 
                result = (this.your_int == xPrime.your_int) && (this.borne_min == xPrime.borne_min) && (this.borne_max == xPrime.borne_max);
            }
        }
        return result;
    }

    @Override
    public String toString(){
        return "valeur : "+this.your_int + " borne minimum : " + Integer.toString(this.borne_min) + " borne maximum : " + Integer.toString(this.borne_max);
    }
    public static void main(String[] args) {

        MyInt myInt1 = new MyInt(5, 0, 10);
        System.out.println(myInt1);

        // myInt1.incremente(9);
        // myInt1.incremente();
        // myInt1.incremente();
        // myInt1.incremente();
        // myInt1.incremente(9);

        // System.out.println(myInt1);
    }
}

