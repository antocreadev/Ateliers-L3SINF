// package tp1.personnel;

import java.util.*;


public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    private String nom;
    private String prenom;
    private final GregorianCalendar dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
	
	static private Integer counter=0; 
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
		counter++;
	}

	
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'année de naissance
	 * @param numero le né de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, new GregorianCalendar(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le prénom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance	 
	 */
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public void setAdresse(Adresse a) {
		adresse=a;
	}
		

	public Boolean plusAgee(Personne p){
		Boolean result = true;
		if (this.dateNaissance.get(Calendar.YEAR) <= p.dateNaissance.get(Calendar.YEAR)){
			result = false;

			if(this.dateNaissance.get(Calendar.MONTH) <= p.dateNaissance.get(Calendar.MONTH)){
				result = false;

				if (this.dateNaissance.get(Calendar.DAY_OF_MONTH) <= p.dateNaissance.get(Calendar.DAY_OF_MONTH)){
					result = false;
				}
			}
		}
		return result;
	}

	public int getAge(){
		int currentYear = Calendar.getInstance().get(Calendar.YEAR);
		return currentYear - this.dateNaissance.get(Calendar.YEAR);
	}

	public Boolean plusAgeeQue(Personne p){
		Boolean result = true; 
		if (this.getAge() >= p.getAge()){
			result = false;
		}
		return result;
	}


	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Prénom : "+prenom+"\n"+
		"Né(e) le : "+dateNaissance.get(Calendar.DAY_OF_MONTH)+
		"-"+dateNaissance.get(Calendar.MONTH)+
		"-"+dateNaissance.get(Calendar.YEAR)+"\n"+
		"Adresse : "+
		adresse.toString()+  " Nombre de Personne créer : " + counter.toString();
		return result;
	}

	@Override
	public boolean equals(Object x) {
	 boolean result = false;
	 if(x !=null){
		 Personne xPrime = (Personne) x;
		 if (x instanceof Personne){
			 result = (this.nom.equals(xPrime.nom));
		 }
		 }
		 return result;
	 }
}
   


   