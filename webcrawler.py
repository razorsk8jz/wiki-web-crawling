import wikipedia

class webcrawler(object):
    """Algorithm that will find relational information will habitate"""

def search_algorithm():
    output = input("What would you like to search? : ")
    get_summary = lambda output: wikipedia.summary(output).encode('utf-8').strip()
    print(get_summary(output))
    
search_algorithm()


#try:
#     wikipedia.summary(output).encode('utf-8').strip()
#except wikipedia.exceptions.DisambiguationError as e:
#      print(e.options)

