from semantic_router import Route, SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "What is your policy on defective product?",
    ],
    score_threshold=0.2

)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",

    ],
    score_threshold=0.2
)
general = Route(
    name = 'general',
    utterances= [
        "Hii" ,
        "How are you?",
        "Doing great"
        "How is your day?"
    ],
    score_threshold=0.2
           
)

router = SemanticRouter(routes=[faq, sql,general], encoder=encoder,auto_sync="local")
router.score_threshold=0.2

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)
    print(router("Hiii, how are you?").name)