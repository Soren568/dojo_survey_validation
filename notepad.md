# URGENT:
- Learnings - store the request.form['var'] into session['var'] in process route to access it across multiple templates.

- request.form['variable'] not retrieving data in jinja 
- returning "ImmutableMultDict([])" upon "print(request.form)" in server.py /process route
    - Online solution that didn't work:
        * request.forms.getlist('variable[]') - returns empty brackets in 
- SOLUTION: check that each input tag has a name="___" to submit as the key into ImmutableMultiDict([])
# Action Items:


