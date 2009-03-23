from notices import HttpResponseRedirectWithNotice
from notices.shortcuts import redirect

def redirect_with_success(request, message="Success!"):
    return HttpResponseRedirectWithNotice('/', success=message)

def redirect_with_error(request, message="Error!"):
    return HttpResponseRedirectWithNotice('/', error=message)

def redirect_with_notice(request, message="Notice!"):
    return HttpResponseRedirectWithNotice('/', notice=message)

def redirect_with_shortcut(request, message="Notice!"):
    return redirect('/', notice=message)
