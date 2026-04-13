"""Entry point — uses Waitress in production, Flask dev server locally."""

import os
from yatraai import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    try:
        from waitress import serve
        print(f"[YatraAI] Starting Waitress on port {port}")
        serve(app, host="0.0.0.0", port=port, threads=4)
    except ImportError:
        print(f"[YatraAI] Waitress not found, using Flask dev server on port {port}")
        app.run(host="0.0.0.0", port=port, debug=False)
