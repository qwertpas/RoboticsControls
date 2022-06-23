package SimulatedAnnealing.TravelingSalesman;

import java.util.ArrayList;
import java.util.Collections;

public class AnnealPath {
    public static void main(String[] args) {
        TravelingSalesman map = new TravelingSalesman(20, 20, 30);
        map.display();

        int iterations = 1000;
        int iteration = 0;
        double min = Double.MAX_VALUE;
        ArrayList<Integer> min_path = new ArrayList<>();

        ArrayList<Integer> state_path = generateRandomPath(20);
        double state_value = map.evaluate(state_path);

        double temp;

        while(iteration < iterations){
            iteration++;
            temp = 1.0/iteration;

            ArrayList<Integer> proposed_state = randomNeighbor(state_path);
            double proposed_value = map.evaluate(proposed_state);

            double delta = proposed_value - state_value;

            if(delta >= 0){
                double prob = Math.exp(-delta/temp);
                if(Math.random() < prob){
                    state_path = proposed_state;
                    state_value = proposed_value;
                }
            }else{
                state_path = proposed_state;
                state_value = proposed_value;
            }

            if(proposed_value < min){
                min = proposed_value;
                min_path = proposed_state;
            }
        }

        System.out.println(min);
        System.out.println(min_path);


    }

    public static ArrayList<Integer> generateRandomPath(int length){
        boolean[] used = new boolean[length+1];
        ArrayList<Integer> path = new ArrayList<>();
        while(path.size() != length){
            int add = (int)(Math.random() * length) + 1;
            if(!used[add]){
                used[add] = true;
                path.add(add);
            }
        }
        return path;
    }

    public static ArrayList<Integer> randomNeighbor(ArrayList<Integer> path){
        int o = (int)(Math.random() * path.size());
        int c = o;
        while(c == o) c = (int)(Math.random() * path.size());
        if(c < o){
            int temp = c;
            c = o;
            o = temp;
        }
        ArrayList<Integer> re = new ArrayList<>(path.subList(o, c));
        Collections.reverse(re);

//        for(int i = o;i<(o+c)/2;i++){
//            Collections.swap();
//        }

        ArrayList<Integer> nei = new ArrayList<>(path.subList(0, o));
        nei.addAll(re);
        nei.addAll(path.subList(c, path.size()));

        return nei;
    }
}
