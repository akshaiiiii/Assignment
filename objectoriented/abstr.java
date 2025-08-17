interface Device{
    void powerOn();
    void powerOff();
}
abstract class computer implements Device{
    @Override
    //the method should be public otherwise there will be error
    public void powerOn(){
        System.out.println("powering on......");
    }
}
class laptop extends computer{
    @Override
    //the method should be public otherwise there will be error
    public void powerOff(){
        System.out.println("powering off......");
    }
}
public class abstr {
    public static void main(String[] args) {
        Device s1=new laptop();
        s1.powerOn();
        s1.powerOff();
    }
    
}
