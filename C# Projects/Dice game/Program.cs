using System;
using System.Diagnostics.Contracts;

namespace Dice_game
{
    class Program
    {
        static void Main (string[] args)
        {
            Console.WriteLine("Press Enter to roll dice:");
            int roll = 0;
            int roll2 = 1;
            int attempts = 0;

            Random gennum = new Random();
            Random gennum2 = new Random();

            while (roll != roll2)
            {
                roll = gennum.Next(1,7);
                roll2 = gennum2.Next(1,7);

                Console.ReadKey();

                Console.WriteLine($"Roll one: {roll}");
                Console.WriteLine($"Roll two: {roll2}");

                Console.WriteLine();
                Console.WriteLine();

                attempts++;
            }

            Console.WriteLine($"You took {attempts} attempts to get two same of a kind");
            Console.ReadKey();
        }
    }
}