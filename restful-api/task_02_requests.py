#!/usr/bin/env python3
import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder printing their titles.
    Displays HTTP status code - confirming success of request.
    """
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            posts = response.json()
            for post in posts:
                print(post.get("title"))
        except ValueError:
            print("Failed to parse JSON response.")
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetches all posts, writes selected fields (id, title, body) into CSV file.
    If request fails, no file is written - error message shown.
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        try:
            posts = response.json()
            simplified_posts = [
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                }
                for post in posts
            ]

            with open("posts.csv", "w", newline='',
                      encoding='utf-8') as csvfile:

                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for post in simplified_posts:
                    writer.writerow(post)

        except ValueError:
            print("Error: Could not parse JSON response.")
        except Exception as e:
            print(f"Unexpected error while saving posts: {e}")
    else:
        print(f"Request failed with status codeL {response.status_code}")
