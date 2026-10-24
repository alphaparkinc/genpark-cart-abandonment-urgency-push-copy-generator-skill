import sys, json
from client import CartAbandonmentUrgencyPushCopyGeneratorClient
sys.stdout.reconfigure(encoding='utf-8')

def handle_mcp():
    client = CartAbandonmentUrgencyPushCopyGeneratorClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "genpark-cart-abandonment-urgency-push-copy-generator-skill"}))
        return
    req = json.loads(sys.stdin.read() or "{}")
    pname = req.get("product_name", "Featured Product")
    total = float(req.get("cart_total", 100.0))
    stock = int(req.get("stock_remaining", 5))
    hrs = float(req.get("hours_elapsed", 2.0))
    res = client.generate_push_variants(pname, total, stock, hrs)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    handle_mcp()
