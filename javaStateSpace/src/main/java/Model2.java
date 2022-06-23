import org.ejml.simple.SimpleMatrix;

public class Model2 {
    public static void main(String[] args) {

        //3b1b romeo juliet
        int states = 2;
        int inputs = 1;

        SimpleMatrix A = new SimpleMatrix(states, states);
        //*
        SimpleMatrix x = new SimpleMatrix(states, 1);
        //+
        SimpleMatrix B = new SimpleMatrix(states, inputs);
        //*
        SimpleMatrix u = new SimpleMatrix(inputs, 1);


        A.set(0, 0, 0);
        A.set(0, 1, -1);
        A.set(1, 0, 1);
        A.set(1, 1, 0);

        B.set(0, 0, 0);
        B.set(1, 0, 0);

        x.set(0, 0, 1.0);
        x.set(1, 0, 0.0);

        u.set(0, 0, 0);

//        for(int i = 0;i<Math.PI*2/0.02;i++){
            x = step(A, B, x, u, states, inputs);

//            System.out.print("[" + x.get(0, 0) + ", ");
//            System.out.println(x.get(1, 0) + "]");
//        }

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

        System.out.println(mat);
        mat = exp(mat);
        System.out.println(mat);

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
