using Card;

namespace Deck
{
    class Deck
    {
        private readonly string[] ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING", "ACE"};
        private readonly string[] suits = {"SPADES", "CLUBS", "HEARTS", "DIAMONDS"};
        Stack<Card.Card> deck = new Stack<Card.Card>();

        public Deck()
        {
            createDeck();
            shuffleDeck();
        }

        private void createDeck()
        {
            for (int i = 0; i < ranks.Length; i++)
            {
                for (int j = 0; j < suits.Length; j++)
                {
                    deck.Push(new Card.Card(ranks[i], suits[j]));
                }
            }
        }

        private void shuffleDeck()
        {
            List<Card.Card> list = deck.ToList();
            deck.Clear();
            Random rnd = new Random();
            List<Card.Card> shuffledList = list.OrderBy(x => rnd.Next()).ToList();
            
            for (int i = 0; i < shuffledList.Count; i++)
            {
                deck.Push(shuffledList[i]);
            }
        }

        public Stack<Card.Card> getDeck()
        {
            return deck;
        }

        public void printDeck()
        {
            foreach (var card in deck)
            {
                card.printCard();
            }
        }

        public Card.Card dealTopCard()
        {
            return deck.Pop();
        }
    }
}