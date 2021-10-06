from github import Github
import argparse
import os
import sys

"""
What this does? It generate a md file with a list of your repositories on github. You can addapt to use Gitlab
"""
parser = argparse.ArgumentParser()
parser.add_argument('repos', nargs="+", type=str)
args = parser.parse_args()
github = Github(os.getenv("GITHUB_TOKEN"))


def sanitize_for_md(s):
    s = s.replace("*", "\*")
    return s

print("Name | Stargazers | Description")
print("|".join(["----"] * 3))
for r_name in sorted(args.repos, key=lambda v: v.upper()):
    try:
        g = github.get_repo(r_name)
    except:
        sys.stderr.write("Error: Repository '{}' not found.\n".format(r_name))
        sys.exit(-1)
    content = " | ".join([
        "[{}]({})".format(g.full_name, g.html_url),
        str(g.stargazers_count),
        sanitize_for_md(g.description)
    ])
    print(content)
