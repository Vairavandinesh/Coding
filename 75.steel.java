import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int hardness=input.nextInt();
        float carboncontent=input.nextFloat();
        int tensilestrength=input.nextInt();
        if (hardness>60 && carboncontent>0.8 && tensilestrength>5700){
            System.out.println("class A");
        }
        else if(hardness>60 && carboncontent>0.8) {

            System.out.println("class B");
        }
        else if(hardness>60 && tensilestrength>5700){
            System.out.println("class C");
        }
        else if(carboncontent>0.8 && tensilestrength>5700){
            System.out.println("class D");
        }
        else if(hardness>60 || carboncontent>0.8 || tensilestrength>5700){
            System.out.println("class E");
        }
        else{
            System.out.println("class F");
        }
    }
}