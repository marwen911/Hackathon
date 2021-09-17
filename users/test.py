from django.shortcuts import render
from django.http.response import JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.
api_url = 'https://dev.webrez.com/json_kiosk_tabhotel/'


def ping ( request, id, url ) :
    url = api_url + f'/{id}/{url}'
    response = requests.get ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                              headers = {"content-type" : "application/json"} )
    content = response.json ()
    return JsonResponse ( content )


@csrf_exempt
def get_reservation ( request, id, url ) :
    raw = request.GET.get ( 'raw' )
    url = api_url + f'/{id}/{url}'
    if raw != None :
        raw_data = json.loads ( raw )
        response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                                   headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
        content = response.json ()
        return render ( request, 'index.html', {'responce' : content} )
    else :
        raw_data = {}
        response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                                   headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
        content = response.json ()
        return render ( request, 'index.html', {'responce' : content} )


@csrf_exempt
def create_or_modify_reservation ( request, id, url ) :
    url = api_url + f'/{id}/{url}'
    raw_data = {
        "confirmation_number" : "20210625-2",
        "status" : "new_modify",
        "first_name" : "Joe",
        "last_name" : "Smith",
        "address1" : "123 Main St",
        "city" : "Arlington",
        "state_code" : "TX",
        "country_code" : "US",
        "postal_code" : "98234",
        "email" : "joe@aol.com",
        "telephone" : "555 1212",
        "mobile" : "555 1234",
        "rooms" : [
            {
                "num_adults" : 2,
                "package_id" : 10557,
                "invtype_id" : 2795,
                "inventory_id" : 5810,
                "arrival_date" : "2021-12-23",
                "departure_date" : "2021-12-25",
                "complimentary" : False,
                "price_array" : [
                    {
                        "start_date" : "2021-12-23",
                        "end_date" : "2021-12-23",
                        "room_cost" : "200"
                    },
                    {
                        "start_date" : "2021-12-24",
                        "end_date" : "2021-12-24",
                        "room_cost" : "150"
                    }
                ]
            }
        ]
    }
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                               headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json ()
    return JsonResponse ( content )


@csrf_exempt
def check_in_reservation ( request, id, url ) :
    raw = request.GET.get ( 'raw' )
    url = api_url + f'/{id}/{url}'
    if raw != None :
        raw_data = json.loads ( raw )
        response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                                   headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
        content = response.json ()
        return render ( request, 'index.html', {'responce' : content} )
    else :
        raw_data = {}
        response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                                   headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
        content = response.json ()
        return render ( request, 'index.html', {'responce' : content} )


@csrf_exempt
def check_out_reservation ( request, id, url ) :
    url = api_url + f'/{id}/{url}'
    raw_data = {"confirmation_number" : "29480309"}
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                               headers = {"content-type" : "application/json"}, json = raw_data )
    content = response.json ()
    return JsonResponse ( content )


@csrf_exempt
def get_departures_reservation ( request, id, url ) :
    url = api_url + f'/{id}/{url}'
    raw_data = {"date" : "2021-06-01"}
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                               headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json ()
    return JsonResponse ( content )


@csrf_exempt
def add_or_update_guest_in_reservation ( request, id, url ) :
    url = api_url + f'/{id}/{url}'
    raw_data = {
        "confirmation_number" : "29480285",
        "additional_guest_number" : 1,
        "firstname" : "Mary",
        "lastname" : "Black",
        "email" : "jojo@gmail.com",
        "address1" : "123 Orange St.",
        "address2" : "Apt 4",
        "telephone" : "5551212",
        "city" : "Smithville",
        "state" : "CA",
        "country" : "US",
        "title" : "",
        "language" : "english",
        "birthdate" : "1972-07-01",
        "passport_nationality" : "UK",
        "passport_expire_date" : "2024-01-01",
        "passport_country" : "UK",
        "passport_issue_date" : "2020-01-01",
        "passport_number" : "12341234"
    }
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                               headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json ()
    return JsonResponse ( content )


@csrf_exempt
def send_invoice ( request, id, url ) :
    url = api_url + f'/{id}/{url}'
    raw_data = {"not_done_yet" : "2021-06-01"}
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),
                               headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json ()
    return JsonResponse ( content )


def index ( request ) :
    if request.method == 'GET' :
        id = request.GET.get ( 'id' )
        url = request.GET.get ( 'url' )
        if id == None :
            context = {
                'id' : 0,
                'd' : ' ',

            }
        else :

            context = {
                'id' : 22,
                'd' : url,

            }

        return render ( request, 'api.html', context )


def pms ( request ) :
    n = open ( './templates/pmsResponse.json' )
    nom = json.load ( n )
    print ( type ( nom ) )
    print ( type ( n ) )

    for x in nom :
        main = x['Guests'][0]['IsPrimary']
        Number = x['Number']
        date_start = x['Arrival']
        arrival_time_estimated = x['Departure']
        number_of_adults = x['Adults']
        Children = x['Children']
        number_of_guests = len ( x['Guests'] )
        ReservationStatus = x['ReservationStatus']
        guests = x['Guests']
        guests_id = list ()
        title = []
        gender = []
        first_name = []
        FirstName = []
        email = []
        TelephoneNum = []
        Nationality = []
        Street1 = []
        Street2 = []
        city = []
        State = []
        Zip = []
        Country = []
        PassportNumber = []
        guest = dict ()
        newguests = list ()

        for i in x['Guests'] :
            print ( i )
            guest["Title"] = i['FirstName']

        """
        for i in guests :

            title.append(i['Title'])
            gender.append(i['Gender'])
            first_name.append(i['FirstName'])
            last_name.append(i['LastName'])
            email.append(i['Email'])
            TelephoneNum.append(i['TelephoneNum'])
            Nationality.append(i['Nationality'])
            Street1.append((i['Street1']))
            Street2.append(i['Street2'])
            city.append(i['City'])
            State.append(i['State'])
            Zip.append(i['Zip'])
            Country.append(i['Country'])
            PassportNumber.append(i['PassportNumber'])"""""

        txt = date_start
        d1 = txt.replace ( "/Date(", '' )
        d2 = d1.replace ( ")/", '' )
        d = int ( d2[:10] )
        date = datetime.fromtimestamp ( d ).strftime ( '%Y-%m-%d' )
        txt2 = arrival_time_estimated
        da1 = txt2.replace ( "/Date(", '' )
        da2 = da1.replace ( ")/", '' )
        da = int ( da2[:10] )
        date2 = datetime.fromtimestamp ( da ).strftime ( '%Y-%m-%d' )
    data = {
        "customer" : "",
        "is_main_reservation" : main,
        "reservation_id_pms" : Number,
        "reservation_code" : Number,
        "reservation_channel_number" : "",
        "start_date" : date,
        'arrival_time_estimated' : "",
        "end_date" : date2,
        "departed_time_estimated" : "",
        "number_of_night" : days_between ( date, date2 ),
        "number_of_adults" : number_of_adults,
        "number_of_keys" : "",
        "number_of_children" : Children,
        "number_of_guests" : number_of_guests,
        "status" : ReservationStatus,
        "checked_in" : "",
        "checked_out" : "",
        "guests" : guest

    }
    context = {}

    return JsonResponse ( data )


def days_between ( d1, d2 ) :
    d1 = datetime.strptime ( d1, "%Y-%m-%d" )
    d2 = datetime.strptime ( d2, "%Y-%m-%d" )
    return abs ( (d2 - d1).days )