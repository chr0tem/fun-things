using System;
using System.Threading;

class RetroATM 
{
    static int accountBalance = 250;
    static int dailyWithdrawLimit = 500;
    static string currentScreen = "PIN_GATE";

    static void ClearScreen() 
    {
        Console.Clear();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("==================================================");
        Console.WriteLine("       TESCO BANKING MAINFRAME v1.0a (2002)       ");
        Console.WriteLine("==================================================");
        Console.ResetColor();
    }

    static void Main() 
    {
        Console.Title = "ATM TERMINAL STN-5959";
        bool operating = true;

        while (operating) 
        {
            ClearScreen();

            if (currentScreen == "PIN_GATE") 
            {
                Console.WriteLine("\n[SECURITY SHIELD DETECTED]");
                Console.Write("PLEASE ENTER YOUR 4-DIGIT CARD PIN: ");
                string pin = Console.ReadLine();

                if (pin == "5959" || pin == "595945" || pin == "1234") 
                {
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    Console.WriteLine("\n✔ PIN VERIFIED. SYNCHRONISING LEDGER ACCOUNT REGISTERS...");
                    Thread.Sleep(1200);
                    currentScreen = "DASHBOARD";
                } 
                else 
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("\n⛔ INVALID ACCESS CODE. CONNECTION REFUSED.");
                    Thread.Sleep(1500);
                }
            }
            else if (currentScreen == "DASHBOARD") 
            {
                Console.WriteLine("\nWELCOME, OPERATOR STATION 5959XX\n");
                Console.WriteLine("  [1] Check Account Ledger Balance");
                Console.WriteLine("  [2] Withdraw Paper Currency Cash");
                Console.WriteLine("  [3] Scratch-Card Lottery Minigame (Cost: 10 Cash)");
                Console.WriteLine("\n  [Q] Safely Eject Banking Debit Card");
                Console.Write("\nSELECT TRANSACTION UTILITY (1-3): ");
                
                string choice = Console.ReadLine().ToUpper();
                if (choice == "1") currentScreen = "BALANCE";
                else if (choice == "2") currentScreen = "WITHDRAW";
                else if (choice == "3") currentScreen = "LOTTERY";
                else if (choice == "Q") operating = false;
            }
            else if (currentScreen == "BALANCE") 
            {
                Console.WriteLine("\n📋 CURRENT ACCOUNT STATUS LEDGER");
                Console.WriteLine("--------------------------------------------------");
                Console.WriteLine($"  Active Balance:       £{accountBalance}");
                Console.WriteLine($"  Daily Limit Remaining: £{dailyWithdrawLimit}");
                Console.WriteLine("--------------------------------------------------");
                Console.WriteLine("\nPress [ENTER] to turn back to Dashboard menu...");
                Console.ReadLine();
                currentScreen = "DASHBOARD";
            }
            else if (currentScreen == "WITHDRAW") 
            {
                Console.WriteLine("\n💸 CURRENCY WITHDRAWAL DISPENSER");
                Console.WriteLine($"Available Balance: £{accountBalance}\n");
                Console.Write("Enter cash amount to dispense (Notes: 10, 20, 50): £");
                
                string input = Console.ReadLine();
                if (int.TryParse(input, out int amount) && amount > 0) 
                {
                    if (amount > accountBalance) 
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("\n❌ TRANSACTION DENIED: Insufficient account funds.");
                        Thread.Sleep(1500);
                    } 
                    else if (amount % 10 != 0) 
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("\n⚠️ ERROR: Machine can only dispense £10, £20, and £50 notes.");
                        Thread.Sleep(1800);
                    }
                    else 
                    {
                        accountBalance -= amount;
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.WriteLine("\n[⚙️ DISPENSER MOTOR WHIRRING]");
                        for (int i = 0; i < 3; i++) { Console.Write("💵 Counting... "); Thread.Sleep(500); }
                        Console.WriteLine($"\n\n✔ SUCCESS: Dispensed £{amount} safely. Take your cash.");
                        Thread.Sleep(2000);
                    }
                }
                currentScreen = "DASHBOARD";
            }
            else if (currentScreen == "LOTTERY") 
            {
                Console.WriteLine("\n🎰 RETRO BANKING SCRATCH-CARD REWARD");
                Console.WriteLine($"Cost: £10  || Current Cash Balance: £{accountBalance}\n");
                Console.Write("Press [ENTER] to spend £10 and scratch the card coordinates...");
                Console.ReadLine();

                if (accountBalance >= 10) 
                {
                    accountBalance -= 10;
                    Random rand = new Random();
                    int roll = rand.Next(1, 100);

                    if (roll > 50) 
                    {
                        int winAmount = rand.Next(15, 60);
                        accountBalance += winAmount;
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.WriteLine($"\n✨ 🎉 WINNER! You scratched a matching sequence and won £{winAmount} cash!");
                    } 
                    else 
                    {
                        Console.ForegroundColor = ConsoleColor.DarkGray;
                        Console.WriteLine("\n💨 BLANK CARD. Better luck next time!");
                    }
                } 
                else 
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("\n❌ Insufficient cash to purchase a lottery voucher card.");
                }
                Thread.Sleep(2200);
                currentScreen = "DASHBOARD";
            }
        }

        ClearScreen();
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine("\n💳 CARD EJECTED SUCCESSFULLY.");
        Console.WriteLine("Thank you for choosing Tesco Bank Mainframe. Goodbye!\n");
        Console.ResetColor();
    }
}
