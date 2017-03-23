import wikipedia

class webcrawler(object):
    """Algorithm that will find relational information will habitate"""

output = input("Enter a wiki search: ")

print(wikipedia.summary(output).encode('utf-8').strip())

#try:
#     wikipedia.summary(output).encode('utf-8').strip()
#except wikipedia.exceptions.DisambiguationError as e:
#      print(e.options)

