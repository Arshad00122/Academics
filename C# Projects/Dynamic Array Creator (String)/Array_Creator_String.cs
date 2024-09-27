using System;

//Dynamic Array Creator (String)

namespace Dynamic_Array_Creator_Str
{
    class Array_Creator_String
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Enter the Length of Array:");
            int UserLen = Convert.ToInt32(Console.ReadLine()); //Lenght of the Array

            string[] arr = new string[UserLen]; 
            // new string is used in when declaring array first then after putting values

            for (int i = 0; i<UserLen; i++)
            {
                Console.WriteLine("Enter the values(string):");
                string? values = Console.ReadLine(); 
                //string'?' means to make it nullable or implicit

                arr[i] = values ?? ""; 
            }

            Console.WriteLine("-------------------------");

            Console.WriteLine("\n");


            Console.WriteLine("The Values of the array is: \n\n");
            int j = 0;
            while (j<UserLen)
            {
                Console.WriteLine(arr[j]);
                j++;
            }

            //Wait for the User input to end this Program
            Console.ReadKey();

        }
    }
}