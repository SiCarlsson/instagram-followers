import json

def extract_usernames(file_path, key=None):
    """
    Extract usernames from a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        key (str, optional): JSON key for relationships. Default is None.
    
    Returns:
        set: A set of usernames (str).
    """
    with open(file_path, "r") as file:
        data = json.load(file)

        if key:
            data = data.get(key, [])

        usernames = set()
        for entry in data:
            entry_list = entry.get("string_list_data", [])
            if entry_list and "value" in entry_list[0]:
                usernames.add(entry_list[0]["value"])
        return usernames

if __name__ == "__main__":
    following_usernames = extract_usernames(
        "following.json", key="relationships_following"
    )
    followers_usernames = extract_usernames("followers_1.json")

    not_following_back = following_usernames - followers_usernames
    you_dont_follow_back = followers_usernames - following_usernames

    print("\nPeople you follow who don't follow you back:")
    for user in sorted(not_following_back):
        print(f"- {user}")

    print("\nPeople who follow you but you don't follow back:")
    for user in sorted(you_dont_follow_back):
        print(f"- {user}")
