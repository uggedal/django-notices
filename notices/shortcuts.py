from django.core import urlresolvers

from notices import HttpResponseRedirectWithNotice
from notices import allowed_notice_types

def redirect(to, *args, **kwargs):
    """
    Extension of redirect shortcut included with Django. Takes one additional
    keyword agrument: `notice`. Does not support permanent redirects.

    Returns an HttpResponseRedirect to the apropriate URL for the arguments
    passed.
    
    The arguments could be:
    
        * A model: the model's `get_absolute_url()` function will be called.
    
        * A view name, possibly with arguments: `urlresolvers.reverse()` will
          be used to reverse-resolve the name.
         
        * A URL, which will be used as-is for the redirect location.
    """
    notices = dict(kwargs)
    for type in notices:
        if type not in allowed_notice_types():
            del notices[type]
    
    # If it's a model, use get_absolute_url()
    if hasattr(to, 'get_absolute_url'):
        return HttpResponseRedirectWithNotice(to.get_absolute_url(), **notices)
    
    # Next try a reverse URL resolution.
    try:
        url = urlresolvers.reverse(to, args=args, kwargs=kwargs)
        return HttpResponseRedirectWithNotice(url, **notices)
    except urlresolvers.NoReverseMatch:
        # If this doesn't "feel" like a URL, re-raise.
        if '/' not in to and '.' not in to:
            raise
        
    # Finally, fall back and assume it's a URL
    return HttpResponseRedirectWithNotice(to, **notices)
