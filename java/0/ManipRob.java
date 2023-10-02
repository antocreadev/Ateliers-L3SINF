class ManipRob {
    public static void main(String[] args) {
        Robot toto = new Robot("Toto", 10, 20, Robot.SUD);
        Robot titi = new Robot("Titi");

        // Avancer des robots
        toto.deplacer();
        toto.deplacer();
        toto.deplacer();

        titi.deplacer();
        titi.deplacer();

        // changement de direction
        toto.setOrientation(Robot.EST);
        titi.setOrientation(Robot.OUEST);

        // Avancer
        toto.deplacer();
        toto.deplacer();
        toto.deplacer();

        titi.deplacer();
        titi.deplacer();

        // reculer
        toto.deplacer();
        titi.deplacer();

        System.out.println(toto);
    }
}