from django.middleware.locale import LocaleMiddleware
from django.utils import translation
from django.conf import settings

class SetLocaleMiddleware(LocaleMiddleware):
    def process_response(self,request,response):
        language = translation.get_language()
        response = super(SetLocaleMiddleware,self).process_response(request,response)
        # here the language is already deactivated by LocaleMiddleware
        if hasattr(request, 'session'):
            request.session['django_language'] = language
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response

from django.utils.http import is_safe_url
from django import http
from django.utils.translation import check_for_language, activate, to_locale, get_language

def set_language(request):
    """
    Redirect to a given url while activating the chosen language in the
    translation, SetLocaleMiddleware assumed to be used.
    The url and the language code need to be specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = request.REQUEST.get('next')
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'POST':
        lang_code = request.POST.get('language', None)
        if lang_code and check_for_language(lang_code):
            translation.activate(lang_code)
    return response
