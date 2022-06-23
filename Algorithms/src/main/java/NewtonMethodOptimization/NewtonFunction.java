package NewtonMethodOptimization;

import java.util.function.DoubleFunction;

public class NewtonFunction {

    public static void main(String[] args) {
        DoubleFunction<Double> func = value -> -((value) + (2*value*value) - (value*value*value/4) + (10*Math.sin(value)) + Math.cos(value)) + 26;

        System.out.println(newton(func, 1.0, 1.0, 10000));
    }

    /**
     *
     * @param func the function
     * @param initial the initial guess (should be a good estimate)
     * @param tolerance how far off 0 the value can be
     * @param epochs the number of loops to find the value (iterations)
     * @return the input to the function where the value is within the tolerance of 0, if
     * none  found then return initial guess
     */
    public static double newton(DoubleFunction<Double> func, double initial, double tolerance, int epochs){

        double epsilon = 1e-6;
        double x = initial;

        for(int i = 0; i <= epochs; i++){

            double f = func.apply(x);

            if(Math.abs(f) < tolerance){
                return x;
            }

            double derivativeEstimate = (f - func.apply(x + epsilon)) / epsilon;
            x += f / derivativeEstimate;

        }
        return initial;
    }
}
