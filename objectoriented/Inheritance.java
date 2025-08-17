class Shape{
    public double area(){
        return 0.0;
    }
}
class Rectangle extends Shape{
    private double length;
    private double breadth;
    public Rectangle(int length,int breadth){
        this.length=length;
        this.breadth=breadth;
   
    }
    @Override
    public double area(){
        return length*breadth;
    }

}
class Circle extends Shape{
    private double radius;
    public Circle(int radius){
        this.radius=radius;
    }
    @Override
    public double area(){
        return Math.PI*radius*radius;

    }
}

public class Inheritance{
    public static void main(String[] args) {
        System.out.println("hello");
        Shape s1=new Rectangle(2,3);
        Shape s2=new Circle(3);
        System.out.println(s1.area());
        System.out.println(s2.area());


    }
}