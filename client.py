import math, sys
sys.stdout.reconfigure(encoding='utf-8')

class CartAbandonmentUrgencyPushCopyGeneratorClient:
    """
    E-commerce recovery push notification & SMS agent. Dynamically computes urgency level
    based on remaining stock, abandonment latency, and cart total, generating hyper-targeted
    copy variants across 5 consumer psychologies.
    """
    def __init__(self):
        self.archetypes = ["SCARCITY_FOCUSED", "SOCIAL_PROOF", "VALUE_SEEKING", "FEAR_OF_MISSING_OUT", "PROBLEM_SOLVER"]

    def compute_urgency_index(self, hours_elapsed, stock_remaining, cart_total):
        # Urgency rises with low stock and moderate latency (2-24 hours)
        time_factor = math.exp(-0.05 * max(0, hours_elapsed - 2)) if hours_elapsed >= 2 else 0.5
        stock_factor = 1.0 - min(1.0, stock_remaining / 20.0)
        value_factor = min(1.0, cart_total / 500.0)
        
        urgency = (stock_factor * 0.50 + time_factor * 0.30 + value_factor * 0.20) * 100.0
        return round(min(100.0, max(10.0, urgency)), 1)

    def generate_push_variants(self, product_name, cart_total, stock_remaining, hours_elapsed, discount_pct=10):
        urgency = self.compute_urgency_index(hours_elapsed, stock_remaining, cart_total)
        variants = []

        # 1. Scarcity Focused
        variants.append({
            "archetype": "SCARCITY_FOCUSED",
            "channel": "PUSH_NOTIFICATION",
            "headline": f"Only {stock_remaining} left in stock!",
            "body": f"Your {product_name} is waiting in your cart, but inventory is almost gone. Complete your order before it's gone.",
            "cta": "Claim Yours Now"
        })

        # 2. Social Proof
        variants.append({
            "archetype": "SOCIAL_PROOF",
            "channel": "PUSH_NOTIFICATION",
            "headline": f"Over 1,200 people loved {product_name} this week",
            "body": f"Join hundreds of happy customers. Your reserved checkout is held for a limited time.",
            "cta": "See Reviews & Checkout"
        })

        # 3. Value Seeking
        variants.append({
            "archetype": "VALUE_SEEKING",
            "channel": "SMS_MESSAGE",
            "headline": f"Unlock {discount_pct}% Off Your Cart",
            "body": f"Hey! Use code SAVE{discount_pct} to get {discount_pct}% off your {product_name}. Total drops from ${cart_total:.2f} to ${cart_total * (1 - discount_pct/100):.2f}.",
            "cta": f"Apply {discount_pct}% Discount"
        })

        # 4. Fear of Missing Out (FOMO)
        variants.append({
            "archetype": "FEAR_OF_MISSING_OUT",
            "channel": "PUSH_NOTIFICATION",
            "headline": "Your cart reservation expires soon",
            "body": f"We can only hold your {product_name} at this price for the next 2 hours. Tap to secure yours.",
            "cta": "Secure My Cart"
        })

        # 5. Problem Solver
        variants.append({
            "archetype": "PROBLEM_SOLVER",
            "channel": "PUSH_NOTIFICATION",
            "headline": "Ready to upgrade your daily routine?",
            "body": f"The {product_name} is ready to ship with express delivery. Need help with questions? Our support team is 1 tap away.",
            "cta": "Complete Order"
        })

        return {
            "status": "success",
            "product_name": product_name,
            "cart_total": cart_total,
            "calculated_urgency_score": urgency,
            "generated_variants": variants
        }
