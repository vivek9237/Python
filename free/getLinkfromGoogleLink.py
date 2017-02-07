linkG = '/search?ie=UTF-8&q=Cognizant+Kolkata,+West+Bengal&ludocid=9936141279095115455&sa=X&ved=0ahUKEwiFyKGGqvfRAhVGPo8KHbAVCNIQvS4IITAB'

def getUrl(linkG):
    url = ''
    if(linkG.startswith('/url?q=')):
        post = linkG.split('url?q=')[1]
        url = post.split('&sa=')[0]
    if(linkG.startswith('/search')):
       url = 'https://www.google.com/'+linkG
    return url
print getUrl(linkG)
