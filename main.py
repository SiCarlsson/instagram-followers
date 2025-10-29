import json


def extract_usernames_from_followers(file_path):
    """
    Extract usernames from followers JSON file.
    Structure: Array of objects with username in string_list_data[0].value
    """
    with open(file_path, "r") as file:
        data = json.load(file)

    usernames = set()
    for entry in data:
        string_list = entry.get("string_list_data", [])
        if string_list and len(string_list) > 0 and "value" in string_list[0]:
            usernames.add(string_list[0]["value"])
    return usernames


def extract_usernames_from_following(file_path):
    """
    Extract usernames from following JSON file.
    Structure: Object with relationships_following key containing array with username in title field
    """
    with open(file_path, "r") as file:
        data = json.load(file)

    usernames = set()
    following_list = data.get("relationships_following", [])
    for entry in following_list:
        if "title" in entry and entry["title"]:
            usernames.add(entry["title"])
    return usernames


if __name__ == "__main__":
    following_usernames = extract_usernames_from_following("following.json")
    followers_usernames = extract_usernames_from_followers("followers_1.json")

    print(f"Number of people you follow: {len(following_usernames)}")
    print(f"Number of followers: {len(followers_usernames)}")

    not_following_back = following_usernames - followers_usernames
    you_dont_follow_back = followers_usernames - following_usernames

    print(f"\nPeople you follow who don't follow you back ({len(not_following_back)}):")
    for user in sorted(not_following_back):
        print(f"- {user}")

    print(
        f"\nPeople who follow you but you don't follow back ({len(you_dont_follow_back)}):"
    )
    for user in sorted(you_dont_follow_back):
        print(f"- {user}")
