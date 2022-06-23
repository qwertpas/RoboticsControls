import org.ejml.simple.SimpleEVD;
import org.ejml.simple.SimpleMatrix;

public class Testing {
    public static void main(String[] args) {
        SimpleMatrix A = new SimpleMatrix(2, 1);
        SimpleMatrix x = new SimpleMatrix(1, 1);

        A.set(0, 0, 1);
        A.set(1, 0, 2);

        System.out.println(A);

        x.set(0, 0, 5);

        System.out.println(x);

        System.out.println(A.mult(x));
    }
    
    public static void eigen(){
        SimpleMatrix mat = new SimpleMatrix(2, 2);
        mat.set(0, 0, 0);
        mat.set(0, 1, 1);
        mat.set(1, 0, -2);
        mat.set(1, 1, -3);
        SimpleEVD<SimpleMatrix> d = new SimpleEVD<>(mat.getMatrix());
        System.out.println(d.getNumberOfEigenvalues());
        for(int i = 0;i<d.getNumberOfEigenvalues();i++){
            System.out.println("vec: " + d.getEigenVector(i));
            System.out.println("val: " + d.getEigenvalue(i));
        }
        System.out.println(d.quality());
    }

    public void solveSystem(){
        SimpleMatrix mat = new SimpleMatrix(2, 2);
        mat.set(0, 0, 2);
        mat.set(0, 1, 3);
        mat.set(1, 0, 1);
        mat.set(1, 1, -3);

        SimpleMatrix a = new SimpleMatrix(2, 1);
        a.set(0, 0, 15);
        a.set(1, 0, 3);
        // 2x + 3y = 15
        // 1x - 3y = 3

        System.out.println(mat.solve(a));
    }
}
