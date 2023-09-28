class ManipRob {
    public static void main(String[] args) {
        Robot toto = new Robot("Toto", 10, 20, Robot.SUD);
        Robot titi = new Robot("Titi");

        // Avancer des robots 
        toto.moveForward();
        toto.moveForward();
        toto.moveForward();

        titi.moveForward();
        titi.moveForward();

        // changement de direction 
        toto.setOrientation(Robot.EST);
        titi.setOrientation(Robot.OUEST);

        // Avancer 
        toto.moveForward();
        toto.moveForward();
        toto.moveForward();

        titi.moveForward();
        titi.moveForward();

        // reculer 
        System.out.println(toto.moveBack());
        System.out.println(titi.moveBack());

        System.out.println(toto);
    }
}