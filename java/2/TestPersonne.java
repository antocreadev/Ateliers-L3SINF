public class TestPersonne {

        
	public static void main(String[] args) {
		Personne p1 =  new Personne("menghi", "anthony", 4, 4, 2005, 1, "Res Avenue", "20290", "Lucciana"); 
        Personne p2 =  new Personne("menghi", "anthony", 4, 4, 2005, 1, "Res Avenue", "20290", "Lucciana"); 
		System.out.println(p1);

        System.out.println(p1.plusAgee(p2));

        System.out.println(p2.getAge());

        System.out.println(p1.plusAgeeQue(p2));

        System.out.println("\n");
        System.out.println("\n");
        System.out.println("\n");


        boolean result = p1.equals(p2);
        // System.out.println(result);

        String a = "a";
        String a2 = "a";

        System.out.println(a == a2);
	}
    
}