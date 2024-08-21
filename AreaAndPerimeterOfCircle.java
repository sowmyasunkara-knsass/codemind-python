import java.util.Scanner;

public class AreaAndPerimeterOfCircle {
    public static void main(String[] args)
    {
        Scanner read=new Scanner(System.in);
        float r=read.nextFloat();
        float area,per;
        float pi=3.14f;
        area=pi*r*r;
        per=2*pi*r;
        System.out.printf("Area of circle :%.4f\n",area);
        System.out.printf("Perimeter of circle :%.4f",per);
    }

}
