import java.util.ArrayList;
import java.util.List;

public class DeFaceAutre extends De{
    private ArrayList<Object> elementsInDe;


    // constructor 
    public DeFaceAutre(int nbFaces, String name, ArrayList<Object> elementsInDe ){
        super(nbFaces, name);
        setElementsInDe(elementsInDe);
    }

    public DeFaceAutre(){
        super();
        setNbFaces(0);
        setElementsInDe(null);
    }

    // méthodes 
    public ArrayList<Object> getElementsInDe(){
        return this.elementsInDe;
    }

    public Object getResultLancer(){
        int index_random = super.lancer()-1;
        return this.elementsInDe.get(index_random);
    }


    public void setElementsInDe(ArrayList<Object> elementsInDe){
        if (elementsInDe instanceof ArrayList<Object> ){
            if(elementsInDe.size() != this.getNbFaces()){
                System.err.println("erreur : la taille du Dé est différent du nombre d'élément dans le dé. Donc elementsInDe va être vide");
                this.elementsInDe = new ArrayList<Object>();
        }
        else {
            this.elementsInDe = elementsInDe;
        }
        }
        else{
            if (elementsInDe !=null){System.err.println("erreur : elementsInDe n'est pas un ArrayList<Object>. Donc elementsInDe va être un ArrayList<Object> vide");}
            this.elementsInDe = new ArrayList<Object>();
        }
    }

    public void addElementsInDe(Object o){
        if (elementsInDe instanceof ArrayList<Object>){
            this.elementsInDe.add(o);
            this.nbFaces++;
        }
        else{
            System.err.println("erreur : elementsInDe n'est pas un ArrayList<Object>. Donc elementsInDe va être un ArrayList<Object> vide");
            // this.elementsInDe = new ArrayList<Object>();
        }
    }

    @Override
    public void setNbFaces(int nbFaces){
        this.nbFaces = nbFaces;
    }
    public static void main(String[] args) {

        // 1ER CONSTRUCTEUR 
        ArrayList<Object> testArrayList = new ArrayList<Object>();
        testArrayList.add(13);
        testArrayList.add("1");
        testArrayList.add("voir");
        testArrayList.add(23);
        DeFaceAutre de1 = new DeFaceAutre(4, "de1", testArrayList);
        System.out.println(de1);
        System.out.println(de1.getResultLancer());

        // 2E CONSTRUCTEUR 
        DeFaceAutre de2 = new DeFaceAutre();
        System.out.println(de2);
        System.out.println(de2.getElementsInDe());
        de2.addElementsInDe("1");
        System.out.println(de2);
        de2.addElementsInDe(20);
        System.out.println(de2.getResultLancer());
    }
}
