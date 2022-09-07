from linkpreview import link_preview
from linkpreview.exceptions import MaximumContentSizeError
import favicon
from requests.exceptions import HTTPError

def retrieve_url_preview(url):
    try:
        icon = favicon.get(url)[-1].url or ''
    except:
        icon = ''
    try:
        preview = link_preview(url)
        title, description, absolute_image = preview.title, preview.description, preview.absolute_image
    except:
         title, description, absolute_image = '', '', ''
    return title, description, absolute_image, icon
