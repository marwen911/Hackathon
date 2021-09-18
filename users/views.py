from django.shortcuts import render
from django.http.response import JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


# Create your views here.
api_url = 'https://dev.webrez.com/json_kiosk_tabhotel/'
def ping(request,id,url):
    url = api_url + f'/{id}/{url}'
    response = requests.get ( url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"} )
    content = response.json ()
    return JsonResponse(content)
@csrf_exempt
def get_reservation(request,id,url):
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
def create_or_modify_reservation(request,id,url):
    url = api_url + f'/{id}/{url}'
    raw_data = {
    "confirmation_number": "20210625-2",
    "status": "new_modify",
    "first_name": "Joe",
    "last_name": "Smith",
    "address1": "123 Main St",
    "city": "Arlington",
    "state_code": "TX",
    "country_code": "US",
    "postal_code": "98234",
    "email": "joe@aol.com",
    "telephone": "555 1212",
    "mobile": "555 1234",
    "rooms": [
        {
            "num_adults": 2,
            "package_id": 10557,
            "invtype_id": 2795,
            "inventory_id":5810,
            "arrival_date": "2021-12-23",
            "departure_date": "2021-12-25",
            "complimentary": False,
            "price_array": [
                {
                    "start_date": "2021-12-23",
                    "end_date": "2021-12-23",
                    "room_cost": "200"
                },
                {
                    "start_date": "2021-12-24",
                    "end_date": "2021-12-24",
                    "room_cost": "150"
                }
            ]
        }
    ]
}
    response = requests.post (url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json()
    return JsonResponse (content)
@csrf_exempt
def check_in_reservation (request,id,url):
    raw = request.GET.get ( 'raw' )
    url = api_url + f'/{id}/{url}'
    if raw!=None:
        raw_data = json.loads ( raw )
        response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
        content = response.json ()
        return render (request,'index.html',{'responce':content})
    else:
        raw_data = {}
        response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
        content = response.json ()
        return render (request,'index.html',{'responce':content})
@csrf_exempt
def check_out_reservation(request,id,url):
    url = api_url + f'/{id}/{url}'
    raw_data = {"confirmation_number": "29480309"}
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"},json =raw_data )
    content = response.json()
    return JsonResponse (content)
@csrf_exempt
def get_departures_reservation(request,id,url):
    url = api_url + f'/{id}/{url}'
    raw_data = {"date": "2021-06-01"}
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json ()
    return JsonResponse ( content )
@csrf_exempt
def add_or_update_guest_in_reservation(request,id,url):
    url = api_url + f'/{id}/{url}'
    raw_data = {
    "confirmation_number": "29480285",
    "additional_guest_number":1,
    "firstname": "Mary",
    "lastname": "Black",
    "email":"jojo@gmail.com",
    "address1": "123 Orange St.",
    "address2": "Apt 4",
    "telephone": "5551212",
    "city": "Smithville",
    "state": "CA",
    "country": "US",
    "title": "",
    "language": "english",
    "birthdate": "1972-07-01",
    "passport_nationality": "UK",
    "passport_expire_date": "2024-01-01",
    "passport_country": "UK",
    "passport_issue_date": "2020-01-01",
    "passport_number": "12341234"
}
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json ()
    return JsonResponse ( content )
@csrf_exempt
def send_invoice(request,id,url):
    url = api_url + f'/{id}/{url}'
    raw_data = {"not_done_yet": "2021-06-01"}
    response = requests.post ( url, auth = HTTPBasicAuth ( 'test', 'test' ),headers = {"content-type" : "application/json"}, data = json.dumps ( raw_data ) )
    content = response.json ()
    return JsonResponse ( content )
def index(request):
    if request.method=='GET':
        id = request.GET.get ( 'id' )
        url = request.GET.get ( 'url' )
        if id==None:
            context = {
                'id' :0,
                'd' : ' ',

            }
        else:

            context = {
                'id' : 22,
                'd' : url,


            }

        return render ( request, 'api.html', context)

def pms(request):
    n= open('./templates/pmsResponse.json')
    invoce_objet=dict()

    file =json.load(n)
    guest = dict ()
    newguests = list ()
    reservation=dict()
    reservation_room = dict ()
    newroom=list()
    room=dict()
    for x in file :
        main = x['Guests'][0]['IsPrimary']
        Number = x['Number']
        date_start = x['Arrival']
        arrival_time_estimated = x['Departure']
        number_of_adults = x['Adults']
        Children = x['Children']
        number_of_guests = len ( x['Guests'] )
        ReservationStatus = x['ReservationStatus']
        guests=x['Guests']
        rooms=x['Room']
        contact=x['Contact']
        for g in guests :
            guest["guest_id_pms"] = g['Number']
            guest["title"] = ""
            guest["gender"] = g['Gender']
            guest["first_name"] = g['FirstName']
            guest["last_name"] = g['LastName']
            guest["email"] = g['Email']
            guest["Phone"] = g['TelephoneNum']
            guest["nationality"]=g['Nationality']
            guest["address1"] = g['Street1']
            guest["address2"] = g['Street2']
            guest["city"] = g['City']
            guest["state"] = g['State']
            guest["zid_code"] = g['Zip']

            if (g["Country"])==None:
                guest["country"] = g['Country']
            else:
                guest["country"] = g['Country']['CountryName']
            guest["passport_number"] = g['PassportNumber']
            guest["document_type"] =""
            guest["is_main_guest"]=g['IsPrimary']
            if (g["Country"])==None:
                guest["passport_issuance_contry_code"] = g['Country']
            else:
                guest["country"] = g['Country']['Code2Digit']
            guest["room_number"] = rooms['Number']
            guest["room_id_pms"]=rooms['Number']
            reservation["start_date"]=dateJson(date_start)
            reservation["end_date"] = dateJson(arrival_time_estimated)
            guest["reservation_guest_data"] =reservation
            guest["reservation_id_pms"] = Number
            newguests.append ( guest.copy() )

        room["room_id_pms"]=guest["room_number"]
        room["room_name"] = rooms['Floor']+'/'+guest["room_number"]
        room["room_number"] = '000'+guest["room_number"]
        room["room_number_to_display"] =guest["room_number"]
        room["room_type_pms"] = rooms['RoomType']["RoomTypeID"]
        room["room_type"] = rooms['RoomType']["RoomTypeID"]
        room["room_floor"] = rooms['Floor']
        room["room_category_name"] = rooms['Description']
        reservation_room["start_date"] = dateJson ( date_start )
        reservation_room["end_date"] = dateJson ( arrival_time_estimated )
        reservation_room['guest']=newguests
        room["reservation_room_data"] = reservation_room
        room["number_of_keys"]=number_of_guests
        room["guest_id_pms"]=contact['Number']
        room["guest_first_name"] = contact['FirstName']
        room["guest_last_name"] = contact['LastName']
        room["number_of_children"] = Children
        room["Rate"]=[]
        room["balance"]=0
        room["is_available"]=rooms['isActive']
        room["reservation_id_pms"] = Number
        room["number_of_adults"] = number_of_adults
        room["room_total"] = rooms['RoomType']['TotalRooms']
        newroom.append(room)
        country_main_guest=contact['Country']['CountryName']
        nationality_main_guest = contact['Nationality']
        gender_main_guest=contact['Gender']
        first_name_main_guest=contact['FirstName']
        last_name_main_guest=contact['LastName']
        email_main_guest=contact['Email']
        title_main_guest=contact['Title']
        main_guest_id=contact['Number']
        language_main_guets=""
        main_room_number=len(newroom)
        total=0
        balance=0
        paid=0
    data={
        "customer" : "",
        "is_main_reservation" : main,
        "reservation_id_pms" : Number,
        "reservation_code" : Number,
        "reservation_channel_number" : "",
        "start_date" : dateJson(date_start),
        'arrival_time_estimated' : "",
        "end_date" : dateJson(arrival_time_estimated),
        "departed_time_estimated" : "",
        "number_of_night" : days_between ( dateJson(date_start), dateJson(arrival_time_estimated) ),
        "number_of_adults" : number_of_adults,
        "number_of_keys" : "",
        "number_of_children" : Children,
        "number_of_guests" : number_of_guests,
        "status" : ReservationStatus,
        "checked_in" : "",
        "checked_out" : "",
        "guests" : newguests,
        "room":newroom,
        "number_of_rooms" : len(newroom),
        "country_main_guest" : country_main_guest,
        "nationality_main_guest" : nationality_main_guest,
        "gender_main_guest" : gender_main_guest,
        "first_name_main_guest" : first_name_main_guest,
        "last_name_main_guest" : last_name_main_guest,
        "email_main_guest" : email_main_guest,
        "title_main_guest" : title_main_guest,
        "main_guest_id" : main_guest_id,
        "language_main_guets" : language_main_guets,
        "main_room_number" : main_room_number,
        "total" : total,
        "balance" : balance,
        "paid" : paid,
        "invoice":invoce_objet

    }

    return JsonResponse(data)
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
def dateJson(date):
    d1 = date.replace ( "/Date(", '' )
    d2 = d1.replace ( ")/", '' )
    d = int ( d2[:10] )
    date = datetime.fromtimestamp ( d ).strftime ( '%Y-%m-%d' )
    return date
