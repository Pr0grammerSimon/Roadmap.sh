import argparse,requests,json

parse = argparse.ArgumentParser()

parse.add_argument('username')


arg = parse.parse_args()


response = requests.get(f"https://api.github.com/users/{arg.username}/events",{"per_page":100}).json()

for event in response:
    firstString=""
    secondString = " ".join(event['created_at'].split("T"))[:-1]
    match event["type"]:
        case "PushEvent":
            firstString = f"- Pushed {event["payload"]["size"]} commits to {event["repo"]["name"]}"
        case "WatchEvent":
            firstString = f"- Starred {event["repo"]["name"]}"
        case "CreateEvent":
            firstString = f"- Created {event["repo"]["name"]}"
        case "DeleteEvent":
            firstString = f"- Deleted {event["repo"]["name"]}"
        case "PullRequestEvent":
            firstString = f"- Opened a new Pull Request in {event["repo"]["name"]}" if event["payload"]["action"]=="opened" else f"- Closed a Pull Request in {event["repo"]["name"]}"
        case "IssuesEvent":
            firstString = f"- Opened a new Issue in {event["repo"]["name"]}" if event["payload"]["action"]=="opened" else f"- Closed an Issue in {event["repo"]["name"]}"


    if (firstString!=""): print(f"{firstString:100} | {secondString}")