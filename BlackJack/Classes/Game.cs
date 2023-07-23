using Deck;
using Hand;

namespace Game
{
    class Game
    {
        private Deck.Deck deck = default!;
        private Hand.Hand playersHand = default!;
        private Hand.Hand dealersHand = default!;

        public Game()
        {
            createAndShuffleDeck();
            dealHands();

            usersTurn();

            if (!playersHand.checkForBustHand())
            {
                Thread.Sleep(1000);
                dealersTurn();
                if (!dealersHand.checkForBustHand())
                {
                    Thread.Sleep(1000);
                    Console.WriteLine();
                    Console.WriteLine("Calculating winner of hand.");
                    Thread.Sleep(1000);
                    calculateWinner();
                }
            }

            printPlayersHand();
            Console.WriteLine();
            printDealersHand();
        }

        private void createAndShuffleDeck()
        {
            deck = new Deck.Deck();
        }

        private void dealHands()
        {
            playersHand = new Hand.Hand();
            dealersHand = new Hand.Hand();

            playersHand.addCardToHand(deck.dealTopCard());
            dealersHand.addCardToHand(deck.dealTopCard());
            playersHand.addCardToHand(deck.dealTopCard());
            dealersHand.addCardToHand(deck.dealTopCard());
        }

        private void usersTurn()
        {
            printPlayersHand();
            
            string? userChoice = "Twist";
            while (userChoice == "Twist" && !playersHand.checkForBustHand())
            {
                Console.WriteLine();
                Console.WriteLine("Would you like to Twist or Stick? (Type Twist or Stick)");
                userChoice = Console.ReadLine();

                if (userChoice == "Twist")
                {
                    playersHand.addCardToHand(deck.dealTopCard());

                    if (playersHand.checkForBustHand())
                    {
                        Console.WriteLine();
                        Console.WriteLine("*** You are now BUST!!! Dealer wins the hand. ***");
                        Console.WriteLine();
                    }
                    else
                    {
                        printPlayersHand();
                    }
                }
                else if (userChoice == "Stick")
                {
                    printPlayersHand();
                }
                else
                {
                    Console.WriteLine();
                    Console.WriteLine("*** ERROR - Please either type Twist or Stick ***");
                    Console.WriteLine();
                    userChoice = "Twist";
                }
            }
        }

        private void printPlayersHand()
        {
            Console.WriteLine("These are your cards.");
            Console.WriteLine();
            playersHand.printHand();
        }

        private void printDealersHand()
        {
            Console.WriteLine("These are the dealer's cards.");
            Console.WriteLine();
            dealersHand.printHand();
        }

        private void dealersTurn()
        {
            Console.WriteLine();
            Console.WriteLine("Performing dealer's turn.");

            while (dealersHand.calcHandTotal() < 17)
            {
                dealersHand.addCardToHand(deck.dealTopCard());
            }

            if (dealersHand.checkForBustHand())
            {
                Console.WriteLine();
                Console.WriteLine("*** Dealer is BUST!!! Player wins the hand. ***");
            }
        }

        private void calculateWinner()
        {
            Console.WriteLine();
            Console.WriteLine("*************************************************************");

            if (playersHand.isBlackjack() && dealersHand.isBlackjack())
            {
                Console.WriteLine("DRAW - Both player and dealer have blackjack.");
            }
            else if (playersHand.isBlackjack())
            {
                Console.WriteLine("WIN - Player has blackjack.");
            }
            else if (dealersHand.isBlackjack())
            {
                Console.WriteLine("LOSS - Dealer has blackjack.");
            }
            else if (playersHand.isFiveCardTrick() && dealersHand.isFiveCardTrick())
            {
                Console.WriteLine("DRAW - Both player and dealer have a five card trick.");
            }
            else if (playersHand.isFiveCardTrick())
            {
                Console.WriteLine("WIN - Player has a five card trick.");
            }
            else if (dealersHand.isFiveCardTrick())
            {
                Console.WriteLine("LOSS - Dealer has a five card trick.");
            }
            else if (dealersHand.calcHandTotal() == playersHand.calcHandTotal())
            {
                Console.WriteLine("DRAW - Both dealer and player have a score of " + dealersHand.calcHandTotal() + ".");
            }
            else if (dealersHand.calcHandTotal() < playersHand.calcHandTotal())
            {
                Console.WriteLine("WIN - Players score of " + playersHand.calcHandTotal() + " beats the dealers score of " + dealersHand.calcHandTotal() + ".");
            }
            else if (dealersHand.calcHandTotal() > playersHand.calcHandTotal())
            {
                Console.WriteLine("LOSS - Players score of " + playersHand.calcHandTotal() + " loses to the dealers score of " + dealersHand.calcHandTotal() + ".");
            }
            else
            {
                Console.WriteLine("*** ERROR - There has been an error calculating the winner of the hand.");
            }

            Console.WriteLine("*************************************************************");
            Console.WriteLine();
        }
    }
}