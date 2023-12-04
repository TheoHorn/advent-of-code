package day2;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class golden_star {
 
    
    BufferedReader txt;

    public golden_star(File file) throws IOException{
        try{
            this.txt = new BufferedReader(new FileReader(file));
            System.out.println(this.fonction());
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }
    }

    public int fonction() throws IOException{
        int sum = 0;
        String line;
        while((line = this.txt.readLine()) != null){
            String[] split = line.split(":");
            int power = 0;
            String[] right = split[1].split(" ");
            int red = 0, green = 0, blue = 0;
            for (int i = 0; i+1 < right.length; i++) {
                if(right[i+1].contains("red") && right[i].matches("[0-9]+") && Integer.parseInt(right[i]) > red){
                    red = Integer.parseInt(right[i]);
                }else if(right[i+1].contains("green")  && right[i].matches("[0-9]+") && Integer.parseInt(right[i]) > green){
                    green = Integer.parseInt(right[i]);
                }else if(right[i+1].contains("blue")  && right[i].matches("[0-9]+") && Integer.parseInt(right[i]) >  blue){
                    blue = Integer.parseInt(right[i]);
                }
            }
            System.out.println(red + " " + green + " " + blue);
            power = red * green * blue;
            sum += power;
        }
        return sum;
    }


    public static void main(String[] args) throws IOException {
        File file = new File("day2/input.txt");
        golden_star day2_2 = new golden_star(file);
        
    }
}
