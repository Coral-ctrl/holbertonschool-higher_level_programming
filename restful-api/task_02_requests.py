#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API
"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """function that fetches all post and print titles"""
    response = requests.get(API_URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    function that fetches all post from JSONPlaceholder
    and save selected feilds into posts.csv
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        # Created structured list of dictionaries
        structured_posts = []
        for post in posts:
            structured_posts.append(
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                }
            )

        # Write to CSV file
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
