Mock Webhook Receiver
========

```bash
# Setup python venv
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip setuptools
pip install -r requirements.txt

# Run
./run

# Test
curl -i 'localhost:5000/201/0.3'
curl -i 'localhost:5000/_/_'
```
