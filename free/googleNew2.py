from google import google
num_page = 3
search_results = google.search("CTS", num_page)
for result in search_results:
    print('#############################################################')
    print(result.name)
    print(result.description)
    print(result.link)
    print('\n')
