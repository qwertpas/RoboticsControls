package SimulatedAnnealing.TravelingSalesman;

import java.awt.*;
import java.util.ArrayList;
import java.util.Random;

public class TravelingSalesman {
    ArrayList<Point> cities = new ArrayList<>();
    int xMax, yMax;

    public TravelingSalesman(int num, int xMax, int yMax) {
        Random s= new Random();
        for (int i =0;i<num;i++){
            Point newPoint = new Point((int)(s.nextDouble() * xMax), (int)(s.nextDouble() * yMax));
            while(cities.contains(newPoint)){
                newPoint = new Point((int)(s.nextDouble() * xMax), (int)(s.nextDouble() * yMax));
            }
            cities.add(newPoint);
        }
        this.xMax = xMax;
        this.yMax = yMax;
    }

    public double evaluate(ArrayList<Integer> order){
        double sum = cities.get(
                order.get(0)-1).distance(
                cities.get(
                        order.get(
                                cities.size()-1)-1));
        for(int i = 1;i<order.size();i++){
            sum += cities.get(
                    order.get(i)-1).distance(
                            cities.get(
                                    order.get(i-1)-1));
        }
        return sum;
    }

    public void display(){
        for(int i = 0;i<yMax;i++){
            for(int j = 0;j<xMax;j++){
                int n = 0;
                boolean d = false;
                for(Point s : cities){
                    n++;
                    if(s.x == j && s.y == i){
                        System.out.print(n + " ".repeat(4 - (n+"").length()));
                        d = true;
                    }
                }
                if(!d) System.out.print(".   ");
            }
            System.out.println();
        }
    }
}
