package SimulatedAnnealing;

import java.util.function.DoubleFunction;

public class SimulatedAnnealingFunctions {
    public static void main(String[] args) {

        DoubleFunction<Double> func = value -> -((value) + (2*value*value) - (value*value*value/4) + (10*Math.sin(value)) + Math.cos(value)) + 17;

        anneal(func, -2.9, 10, 1000);

    }
    public static void anneal(DoubleFunction<Double> func, double o, double c, int iterations){

        double state = Math.random() * (c - o) + o;
        double temp;
        int iteration = 0;
        double min = Double.MAX_VALUE;

        while(iteration < iterations){
            iteration++;
            temp = 1.0/iteration;

            double proposedState = Math.random() * (c - o) + o;

            double delta = func.apply(proposedState) - func.apply(state);
            System.out.println("("+iteration + "/"+iterations+")  state: " + func.apply(state));

            if(delta >= 0){
                double selectMoveProb = Math.exp(-delta/temp);
                if(Math.random() < selectMoveProb) state = proposedState;
            }else{
                state = proposedState;
            }
            min = Math.min(min, func.apply(state));
        }
        System.out.println("min: " + min);
    }
}
