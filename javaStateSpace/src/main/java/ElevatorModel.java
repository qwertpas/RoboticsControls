import org.ejml.simple.SimpleMatrix;

public class ElevatorModel {
    public static void main(String[] args) {

        //Elevator
        int states = 2;
        int inputs = 1;

        //input
        double applyVoltage = 12.0;


        SimpleMatrix A = new SimpleMatrix(states, states);
        //*
        SimpleMatrix x = new SimpleMatrix(states, 1);
        //+
        SimpleMatrix B = new SimpleMatrix(states, inputs);
        //*
        SimpleMatrix u = new SimpleMatrix(inputs, 1);

        //Single Falcon 500
        //Mass 3 kg
        //Gear ratio 1
        //Spool diameter 0.038 meters = 1.5 inches
        double vCof = -Math.pow(1, 2)
                * (4.69 / 257)
                / ((12.0 / 257)
                * 0.038 * 0.038
                * 3.0
                * (Math.toRadians(6380)
                / (12.0
                - 1.5
                * (12.0 / 257))));
        double VCof = 1 * (4.69 / 257) / ((12.0 / 257) * 0.038 * 3.0);

        A.set(0, 0, 0);
        A.set(0, 1, 1);
        A.set(1, 0, 0);
        A.set(1, 1, vCof);

        B.set(0, 0, 0);
        B.set(1, 0, VCof);

        x.set(0, 0, 1.0);
        x.set(1, 0, 0.0);

        u.set(0, 0, applyVoltage);

        SimpleMatrix grav = new SimpleMatrix(2, 1);
        grav.set(1, 0, -9.8);


        for(int i = 0;i<50;i++){
            x = step(A, B, x, u, states, inputs);

            System.out.println(x.get(0, 0));
        }

    }

    public static SimpleMatrix step(
            SimpleMatrix A,
            SimpleMatrix B,
            SimpleMatrix x,
            SimpleMatrix u,
            int states,
            int inputs){

        double T = 0.02;

        SimpleMatrix mat = new SimpleMatrix(states + inputs, states + inputs);

        mat.insertIntoThis(0, 0, A.scale(T));
        mat.insertIntoThis(0, states, B.scale(T));

        mat = exp(mat);

        SimpleMatrix Ad = mat.extractMatrix(0, states, 0, states);
        SimpleMatrix Bd = mat.extractMatrix(0, states, inputs+1, states+inputs);

        return Ad.mult(x).plus(Bd.mult(u));
    }

    public static SimpleMatrix exp(SimpleMatrix a){
        //Taylor expansion for e^a with n = 6
        return
                SimpleMatrix.identity(a.numRows())
                        .plus(a)
                        .plus((a.mult(a)).scale(1.0/2))
                        .plus((a.mult(a).mult(a)).scale(1.0/6))
                        .plus((a.mult(a).mult(a).mult(a)).scale(1.0/24))
                        .plus((a.mult(a).mult(a).mult(a).mult(a)).scale(1.0/120))
                        .plus((a.mult(a).mult(a).mult(a).mult(a).mult(a)).scale(1.0/720));
    }

}
