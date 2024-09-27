import requests

cookies = {
    'bannerClosed': 'true',
    'cf_clearance': 'IntuvDKnwHSKkTUj_vG61i.Wf7EznZ8h2yHTBsKDAao-1727135766-1.2.1.1-rl5dNiPf.N1LbB73qPUQXuMEPTGWsEoZ0DCGPWwkOUqQTkpx8b.oEfdz1dPB590cbKY6JwH6Z6fsi8vVUzU4LU.7OQ3lzuktDQwH35qpcXAc4lZTp_xl1IewAc0Hma3X3muxNx0.Pmt5H0w03xnFGPJwQ4inHBkWoTaM1oeyKb0e8SFz654r5Dqsmmdj5BUniugbFrmX_HXB_cGu9.cLUuVYgJva7FqdR.B2N61CtuDbN_FyiaII0XS2Ka.6voCzyJbIQMnkUvVCVOZyLtccjsPtD9zPdGAfAEAFUCnRWfzUHGygobB5Sj5B.m2A.XK1nO5kKpW15wZYZqoETYf7wUKn78fui1ycuQY3jFOUKN4v_2AtbMO1SwpWA1XADMNO',
}

# attempt to clone Chrome headers to spoof chrome browser
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'bannerClosed=true; cf_clearance=IntuvDKnwHSKkTUj_vG61i.Wf7EznZ8h2yHTBsKDAao-1727135766-1.2.1.1-rl5dNiPf.N1LbB73qPUQXuMEPTGWsEoZ0DCGPWwkOUqQTkpx8b.oEfdz1dPB590cbKY6JwH6Z6fsi8vVUzU4LU.7OQ3lzuktDQwH35qpcXAc4lZTp_xl1IewAc0Hma3X3muxNx0.Pmt5H0w03xnFGPJwQ4inHBkWoTaM1oeyKb0e8SFz654r5Dqsmmdj5BUniugbFrmX_HXB_cGu9.cLUuVYgJva7FqdR.B2N61CtuDbN_FyiaII0XS2Ka.6voCzyJbIQMnkUvVCVOZyLtccjsPtD9zPdGAfAEAFUCnRWfzUHGygobB5Sj5B.m2A.XK1nO5kKpW15wZYZqoETYf7wUKn78fui1ycuQY3jFOUKN4v_2AtbMO1SwpWA1XADMNO',
    'if-modified-since': 'Mon, 23 Sep 2024 23:55:51 GMT',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

response = requests.get('https://www.streameast.co/watch-nfl-streams/', cookies=cookies, headers=headers)

print(response)