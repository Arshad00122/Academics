using System;

namespace Dice_game__with_2_dice_
{
    class Program
    {
        static void Main(string[] args){
            Console.WriteLine("Press enter to roll dice");

            int attempts = 0;
            int roll_one = 0;
            int roll_two = 2;

            Random number_generator = new Random();
            Random number_generator_2 = new Random();

            while (roll_one != roll_two)
            {
                roll_one = number_generator.Next(1,7);
                roll_two = number_generator_2.Next(1,7);
                
                Console.ReadKey();
                Console.WriteLine($"You rolled: {roll_one}");
                Console.WriteLine($"You rolled: {roll_two}");

                //For formatting and spacing
                Console.WriteLine();
                Console.WriteLine();

                attempts++;
            }

            Console.WriteLine($"You took {attempts} attempts to get two of a kind");

            //Wait for user to end
            Console.ReadKey();
        }
    }   
}