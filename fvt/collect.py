from werkzeug.datastructures import ImmutableMultiDict
import urllib.request

# Turns ImmutableMultiDict to dict
def IMDtodict(imd):
    #newdict = ImmutableMultiDict(request.form)
    newdict = imd.to_dict(flat=False)
    return newdict

# Turns a URL in its respective HTML content in String format
def URLrequesttoString(url):
    fp = urllib.request.urlopen(url)
    pagebytes = fp.read()
    pagestring = pagebytes.decode("utf8")
    fp.close()

    return pagestring