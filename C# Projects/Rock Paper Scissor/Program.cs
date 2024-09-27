using System;
using System.Reflection.Metadata;
using System.Security.Cryptography;

// ROCK PAPER SCISSOR GAME


namespace Rock_Paper_Scissor
{
    class Program
    {
        static void Main(string[] args)
        {
            //Array that AI would choose
            string[] computer_arr = {"Rock","Paper","Scissor"};

            //Displaying to user
            Console.WriteLine("Choose:\n");
            Console.WriteLine("1. Rock");
            Console.WriteLine("2. Paper");
            Console.WriteLine("3. Scissor\n");

            //Just for a game stop after 3 times of play
            int attempts = 0;

            while(true){
            // All computer choice here to get random values each time
            Random random = new Random();
            int computer = random.Next(0,computer_arr.Length);

            //user suggests
            Console.Write(">");
            int user = Convert.ToInt32(Console.ReadLine());

            if (user==computer){
                Console.WriteLine($"User and Computer both choose {computer_arr[computer]}");
                attempts++;
                }
            else if (user==1){
                attempts++;
                if (computer==1){
                    Console.WriteLine("Rock was captured by Paper");
                    Console.WriteLine("You loose");
                    }
                else{
                    Console.WriteLine("Rock breaks Scissor");
                    Console.WriteLine("You wins");
                    }
                }
            else if(user==2){
                attempts++;
                if (computer==0){
                    Console.WriteLine("Rock was captured by Paper");
                    Console.WriteLine("You win");
                    }
                else{
                    Console.WriteLine("Scissor cuts paper");
                    Console.WriteLine("You loose");
                    }
                }
            else if (user==3){
                attempts++;
                if (computer==0){
                    Console.WriteLine("Rock breaks Scissor");
                    Console.WriteLine("You loose");
                }else{
                    Console.WriteLine("Scissor cuts paper");
                    Console.WriteLine("You win");
                    }
                }
            else{
                Console.WriteLine("Invalid Number");
            }
            while (attempts>=3){
                    Console.WriteLine("\n\nDo you want to play more?");
                    Console.WriteLine("1. yes");
                    Console.WriteLine("2. no");
                    Console.Write(">");
                    string user2 = Console.ReadLine();
                    if (user2 == "1" || user2.ToLower() == "yes"){
                        Console.WriteLine("\n\nOk\n\n");
                        attempts=0;
                        break;
                    }
                    else if (user2=="2"|| user2.ToLower()=="no"){
                        Console.WriteLine("Ok\n\n");
                        return;
                    }
                    else{
                        Console.WriteLine("Invalid answer");
                    }
                }
            }
        }
    }
}