
public class Puppy{
    //instance variable
    int puppyAge;
    public Puppy(String name){
        //constructor has 1 parameter, name
        System.out.println("passed name is: " + name);
    }
    public void setAge(int age){
        puppyAge = age;
    }
    public int getAge(){
        return puppyAge;
    }
    public static void main(String []args){
        Puppy myPuppy = new Puppy( "Craig" );

        //example of instance variable/methods
        myPuppy.setAge(1);
        int age = myPuppy.getAge();
        System.out.println("Craig's age is " + age);
        System.out.println(myPuppy.puppyAge);
    }
}

/*
3 steps for creating object from a class:
1. Declaration: object type, variable name
2. Instantiation: new keyword, create object
3. Initialization: after 'new', call to constructor

only one public class per file
and name of that class must be name of the source file

the file can have more than one non-public classes

packages: categorize classes and interfaces

to load all available classes from folder: java_installation/java/io,
write at top of source file: import java.io.*;
*/