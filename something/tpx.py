import requests

if "TpXAnime" in requests.get("https://hindisub.com/").text:
    with open("tpx.txt", "w") as f:
        f.write("Cloudflare is down")
else:
    with open("tpx.txt", "w") as f:
        f.write("Cloudflare is up")
