package day1;

import java.io.*;

class day1{

    BufferedReader txt;

    public day1(File file) throws IOException{
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
            boolean first = true;
            String resultat1 = "";
            String resultat2 = "";
            for(int i = 0; i < line.length(); i++){
                if(i+2 < line.length() && line.charAt(i) == 'o' && line.charAt(i+1) == 'n' && line.charAt(i+2) == 'e' ){
                    if (first){
                        resultat1 = "1";
                        first = false;
                    }
                    resultat2 = "1";
                }
                else if(i+2 < line.length() && line.charAt(i) == 't' && line.charAt(i+1) == 'w' && line.charAt(i+2) == 'o'){
                    if (first){
                        resultat1 = "2";
                        first = false;
                    }
                    resultat2 = "2";
                }
                else if(i+4 < line.length() && line.charAt(i) == 't' && line.charAt(i+1) == 'h' && line.charAt(i+2) == 'r' && line.charAt(i+3) == 'e' && line.charAt(i+4) == 'e'){
                    if (first){
                        resultat1 = "3";
                        first = false;
                    }
                    resultat2 = "3";
                }
                else if(i+3 < line.length() && line.charAt(i) == 'f' && line.charAt(i+1) == 'o' && line.charAt(i+2) == 'u' && line.charAt(i+3) == 'r'){
                    if (first){
                        resultat1 = "4";
                        first = false;
                    }
                    resultat2 = "4";
                }
                else if(i+3 < line.length() && line.charAt(i) == 'f' && line.charAt(i+1) == 'i' && line.charAt(i+2) == 'v' && line.charAt(i+3) == 'e'){
                    if (first){
                        resultat1 = "5";
                        first = false;
                    }
                    resultat2 = "5";
                }
                else if(i+2 < line.length() && line.charAt(i) == 's' && line.charAt(i+1) == 'i' && line.charAt(i+2) == 'x'){
                    if (first){
                        resultat1 = "6";
                        first = false;
                    }
                    resultat2 = "6";
                }
                else if(i+4 < line.length() && line.charAt(i) == 's' && line.charAt(i+1) == 'e' && line.charAt(i+2) == 'v' && line.charAt(i+3) == 'e' && line.charAt(i+4) == 'n'){
                    if (first){
                        resultat1 = "7";
                        first = false;
                    }
                    resultat2 = "7";
                }
                else if(i+4 < line.length() && line.charAt(i) == 'e' && line.charAt(i+1) == 'i' && line.charAt(i+2) == 'g' && line.charAt(i+3) == 'h' && line.charAt(i+4) == 't'){
                    if (first){
                        resultat1 = "8";
                        first = false;
                    }
                    resultat2 = "8";
                }
                else if(i+3 < line.length() && line.charAt(i) == 'n' && line.charAt(i+1) == 'i' && line.charAt(i+2) == 'n' && line.charAt(i+3) == 'e'){
                    if (first){
                        resultat1 = "9";
                        first = false;
                    }
                    resultat2 = "9";
                }
                else if(i+3 < line.length() && line.charAt(i) == 'z' && line.charAt(i+1) == 'e' && line.charAt(i+2) == 'r' && line.charAt(i+3) == 'o'){
                    if (first){
                        resultat1 = "0";
                        first = false;
                    }
                    resultat2 = "0";
                } else if (line.charAt(i) == '1' || line.charAt(i) == '2' || line.charAt(i) == '3' || line.charAt(i) == '4' || line.charAt(i) == '5' || line.charAt(i) == '6' || line.charAt(i) == '7' || line.charAt(i) == '8' || line.charAt(i) == '9' || line.charAt(i) == '0') {
                    if (first) {
                        resultat1 = Character.toString(line.charAt(i));
                        first = false;
                    } 
                    resultat2 = Character.toString(line.charAt(i));
                }
                
            }
            int result1 = Integer.parseInt(resultat1);
            int result2 = Integer.parseInt(resultat2);
            int res = result1*10 + result2;
            System.out.println(line + " " + res);
            sum += res;
        }
        return sum;
    }


    public static void main(String[] args) throws IOException {
        File file = new File("day1/input1.txt");
        day1 day1 = new day1(file);
        
    }
}