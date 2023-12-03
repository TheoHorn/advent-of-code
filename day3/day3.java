package day3;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;

class day3{

    BufferedReader txt;

    public day3(File file) throws IOException{
        try{
            this.txt = new BufferedReader(new FileReader(file));
            System.out.println(this.function());
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }
    }

    public int function() throws IOException{
        String line;
        ArrayList<String> strings = new ArrayList<String>();
        int i = 0;
        while ((line = this.txt.readLine()) != null) {
            strings.add(line);
            i++;
        }
        HashMap<Integer,String> map = new HashMap<Integer,String>();
        String[] string = strings.toArray(new String[strings.size()]);
        for(int j = 0; j < string.length; j++){
            String s = string[j];
            for(int k = 0; k < s.length(); k++){
                if(s.charAt(i) != '.'){}
            }
        }
        return 0;
    }


    public static void main(String[] args) throws IOException {
        File file = new File("day3/input.txt");
        day3 day3 = new day3(file);
        
    }
}