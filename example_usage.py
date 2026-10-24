from client import CartAbandonmentUrgencyPushCopyGeneratorClient
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    client = CartAbandonmentUrgencyPushCopyGeneratorClient()
    print("=== CART ABANDONMENT URGENCY PUSH COPY GENERATOR ===")
    
    res = client.generate_push_variants(
        product_name="Roborock S8 Pro Ultra Robot Vacuum",
        cart_total=899.00,
        stock_remaining=3,
        hours_elapsed=4,
        discount_pct=12
    )
    
    print(f"Product: {res['product_name']} | Urgency Score: {res['calculated_urgency_score']}/100")
    print(f"Generated {len(res['generated_variants'])} Hyper-Targeted Copy Variants:")
    print()
    
    for i, v in enumerate(res['generated_variants'], 1):
        print(f"{i}. Archetype: {v['archetype']} ({v['channel']})")
        print(f"   Headline : {v['headline']}")
        print(f"   Body     : {v['body']}")
        print(f"   Action   : [{v['cta']}]")
        print()

if __name__ == "__main__":
    main()
