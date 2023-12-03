package day2;

import java.io.*;

class day2{

    BufferedReader txt;

    public day2(File file) throws IOException{
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
            String[] split2 = split[0].split(" ");
            int number = Integer.parseInt(split2[1]);
            String[] right = split[1].split(" ");
            boolean found = true;
            for (int i = 0; i+1 < right.length; i++) {
                if(right[i+1].contains("red") && right[i].matches("[0-9]+") && Integer.parseInt(right[i]) > 12){
                    found = false;
                }else if(right[i+1].contains("green")  && right[i].matches("[0-9]+") && Integer.parseInt(right[i]) >  13){
                    found = false;
                }else if(right[i+1].contains("blue")  && right[i].matches("[0-9]+") && Integer.parseInt(right[i]) >  14){
                    found = false;
                }
            }
            if (found) {
                sum += number;
            }
            System.out.println(number);
        }
        return sum;
    }


    public static void main(String[] args) throws IOException {
        File file = new File("day2/input.txt");
        day2 day2 = new day2(file);
        
    }
}