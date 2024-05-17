import requests

# Base URL for the API
base_url = "https://jsonplaceholder.typicode.com"

# Perform HTTP GET request with headers
def http_get_with_headers():
    url = f"{base_url}/posts/1"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer <your-token>"}
    response = requests.get(url, headers=headers)
    print("GET Response with Headers:", response.json())

# Perform HTTP POST request with body and headers
def http_post_with_body_and_headers():
    url = f"{base_url}/posts"
    headers = {"Content-Type": "application/json"}
    data = {"title": "New Post", "body": "This is a new post", "userId": 1}
    response = requests.post(url, json=data, headers=headers)
    print("POST Response with Body and Headers:", response.json())

# Perform HTTP PUT request with body and headers
def http_put_with_body_and_headers():
    url = f"{base_url}/posts/1"
    headers = {"Content-Type": "application/json"}
    data = {"title": "Updated Post", "body": "This post has been updated", "userId": 1}
    response = requests.put(url, json=data, headers=headers)
    print("PUT Response with Body and Headers:", response.json())

# Perform HTTP DELETE request with headers
def http_delete_with_headers():
    url = f"{base_url}/posts/1"
    headers = {"Authorization": "Bearer <your-token>"}
    response = requests.delete(url, headers=headers)
    print("DELETE Response with Headers:", response.status_code)

# Main function to demonstrate HTTP requests
def main():
    http_get_with_headers()
    http_post_with_body_and_headers()
    http_put_with_body_and_headers()
    http_delete_with_headers()

if __name__ == "__main__":
    main()
