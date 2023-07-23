namespace Card
{
    class Card
    {
        private string rank;
        private string suit;

        public Card(string Rank, string Suit)
        {
            rank = Rank;
            suit = Suit;
        }

        public string getRank()
        {
            return rank;
        }

        public string getSuit()
        {
            return suit;
        }

        public void printCard()
        {
            Console.WriteLine(rank + " " + suit);
        }
    }
}