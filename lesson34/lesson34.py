import threading
import time
import json
import requests
import concurrent.futures

# The base URL for the fake API
BASE_URL = "https://jsonplaceholder.typicode.com/posts"
#################################### task 1 ###########################################
class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(Counter.rounds):
            tmp = Counter.counter
            time.sleep(0)
            Counter.counter = tmp + 1

a = Counter()
b = Counter()

a.start()
b.start()

a.join()
b.join()

print(Counter.counter)
# this task showcases existence of race conditions and locks

################################################ task 3 ###############################################################

url = "https://jsonplaceholder.typicode.com/posts"
def get_post(post_id):
    post_url = f"{url}/{post_id}"
    response = requests.get(post_url)
    if response.status_code == 200:
        return response.json()
    return None
def main():
    post_ids = range(1, 51)
    all_posts = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(get_post, post_ids))
        all_posts.extend(results)
        all_posts = [post for post in results if post is not None]
    for item in all_posts:
        if not isinstance(item, dict):
            print(f"Error: Found a non-dictionary item: {item} (Type: {type(item)})")

    all_posts.sort(key=lambda x: x['id'])

    with open("comments2.json", "w") as f:
        json.dump(all_posts, f, indent=4)

if __name__ == "__main__":
    main()
