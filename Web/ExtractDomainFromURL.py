url=input("Enter the URL: ")
print(url.split("//")[-1].split("www.")[-1].split(".")[0])
