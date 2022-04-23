from django.shortcuts import render

from .forms import UTFForm
import re

# Create your views here.


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UTFForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # these codes are coming from a json file; this a representation of one of the codes.

            # not sure how to clean this, so here's a basic attempt using regex.
            b = re.sub(
                r'U\+([0-9A-Fa-f]{4,6})', lambda m: chr(int(m.group(1), 16)), form.data['utf_input'])
            print(form.data['utf_input'])
            print(ascii(b))  # output should be '\U0001F600'
            return render(request, 'index.html', {'form': form, "converted_value": ascii(b)})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UTFForm()

    return render(request, 'index.html', {'form': form})
