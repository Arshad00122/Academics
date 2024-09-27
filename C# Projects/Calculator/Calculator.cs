using System;
using System.ComponentModel;

namespace Completed_Projects{
    class Calculator{

        //All method to make it simple and Clear here

        public static int Add(int a , int b){
            return a+b;
        }
        public static int sub(int a , int b){
            return a-b;
        }
        public static int multi(int a , int b){
            return a*b;
        }
        public static int div(int a , int b){
            return a/b;
        }


        static void Main(string [] args){
            int a , b;
            Console.WriteLine("Calculator");

            Console.Write("Enter a number:");
            a = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter a number:");
            b = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the operator(+,-,*,/):");
            string? math_sign = Convert.ToString(Console.ReadLine());

            switch(math_sign){
                case "+":
                    Console.WriteLine(Add(a,b));
                    Console.ReadKey();
                    break;
                case "-":
                    Console.WriteLine(sub(a,b));
                    Console.ReadKey();
                    break;
                case "*":
                    Console.WriteLine(multi(a,b));
                    Console.ReadKey();
                    break;
                case "/":
                    Console.WriteLine(div(a,b));
                    Console.ReadKey();
                    break;
                default:
                    Console.WriteLine("Invalid Arthematic Operator");
                    Console.ReadKey();
                    break;
            }
        }
    }
}