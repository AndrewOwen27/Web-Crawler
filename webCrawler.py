page = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://google.com">')
def get_next_url (page):
    start_link = page.find('<a href=')
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return[url,end_quote]

print (get_next_url(page))


def bigger(a,b):
    if a > b:
        return a
    return b

print (bigger(6,6))


def is_friend(friendName):
    if friendName.find('D'):
        return True
    return False

print (is_friend('Drew'))
print (is_friend('D'))


name = ('DreDw')
print (name.find('D'))