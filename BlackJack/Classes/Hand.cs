using Card;

namespace Hand
{
    class Hand
    {
        List<Card.Card> hand;

        public Hand()
        {
            hand = new List<Card.Card>();
        }

        public List<Card.Card> getHand()
        {
            return hand;
        }

        public void addCardToHand(Card.Card card)
        {
            hand.Add(card);
        }

        public void printHand()
        {
            foreach (var card in hand)
            {
                card.printCard();
            }
        }

        public bool checkForBustHand()
        {
            return (calcHandTotal() > 21);
        }

        public int calcHandTotal()
        {
            int handTotal = 0;
            int numberOfAces = 0;

            foreach (var card in hand)
            {
                if (card.getRank() == "ACE")
                {
                    numberOfAces++;
                }

                switch (card.getRank())
                {
                    case "JACK":
                        handTotal += 10;
                        break;
                    case "QUEEN":
                        handTotal += 10;
                        break;
                    case "KING":
                        handTotal += 10;
                        break;
                    case "ACE":
                        handTotal += 11;
                        break;
                    default:
                        handTotal += Int32.Parse(card.getRank());
                        break;
                }

                while (numberOfAces > 0 && handTotal > 21)
                {
                    handTotal -= 10;
                    numberOfAces -= 1;
                }
            }

            return handTotal;
        }

        public bool isBlackjack()
        {
            return (hand.Count == 2 && calcHandTotal() == 21);
        }

        public bool isFiveCardTrick()
        {
            return (hand.Count >= 5 && calcHandTotal() <= 21);
        }

        public int numberOfCards()
        {
            return hand.Count;
        }
    }
}