from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string

from google_spreadsheet.api import SpreadsheetAPI

from settings import google_auth, google_sheet

# Create your views here.

def render_motion_chart_json(request, year='2003'):

    api = SpreadsheetAPI(google_auth.USER, google_auth.PASS, google_auth.NAME)

    spreadsheet = api.get_worksheet(
        google_sheet.SPREADSHEET_ID,
        google_sheet.WORKSHEET_ID
    )
    rows = spreadsheet.get_rows()

    output = []
    for item in rows:
        if item['values'] == year:
            output.append(item)


    #print output

    return render_to_response('nepal_data.json', {
        'data_list': output
    }, context_instance=RequestContext(request))