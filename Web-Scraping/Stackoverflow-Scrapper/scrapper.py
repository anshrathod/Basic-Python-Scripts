from bs4 import BeautifulSoup
import requests

def scrapper():
    res = requests.get(f"https://stackoverflow.com/questions?tab=bounties&pagesize=50")
    soup = BeautifulSoup(res.text, "html.parser")
    questions = soup.select(".question-summary")
    
    print("StackOverflow Top 50 Questions")
    print("\n")
    i = 1
    for que in questions:
        q = que.select_one('.question-hyperlink').getText()
        bounty = que.select_one('.bounty-indicator').getText()   
        user_name = que.select_one('.user-details').getText(strip=True)
        vote_count = que.select_one('.vote-count-post').getText()
        views = que.select_one('.views').attrs['title']
        tags = [i.getText() for i in (que.select('.post-tag'))]
        date = que.select_one('.relativetime').attrs['title'].split()[0]
        time_stamp = que.select_one('.relativetime').getText()
        excerpt = que.select_one('.excerpt').getText(strip=True)
        answer_status = que.select_one(".status").get_text(strip=True)
        
        
        print(f"Question {i}: {q}")
        print(f"Bounty: {bounty}")
        print(f"User: {user_name}")
        print(f"Vote Count: {vote_count}")
        print(f"Views: {views}")
        print(f"Tags: {tags}")
        print(f"Date: {date}")
        print(f"Time Stamp: {time_stamp}")
        print(f"Excerpt: {excerpt}")
        print(f"Answer Status: {answer_status}")
        print("\n")
        i += 1



if __name__ == "__main__":
    scrapper()