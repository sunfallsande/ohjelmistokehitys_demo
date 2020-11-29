import requests
import json
import sys

def get_data():
    res = requests.get('https://www.balldontlie.io/api/v1/stats?seasons[]=2018')
    data_list = []
    data_list = res.json()
    return data_list


def handle_pts_data():
    points_list = []
    points_data = get_data()
    for i in points_data['data']:
        asd = json.dumps({'pts': i['pts'], 'player': i['player']})
        points_list.append(json.loads(asd))
    return points_list

    #asd kohta luo uuden objektin mikä sisältää datasta saadut tiedot pelaajaasta, jonka jälkeen se tekee siitä datasta Json-muotoista ja appendaa ne tyhjän points-listan sisälle. 

def handle_ast_data():
    assist_list = []
    assist_data = get_data()
    for i in assist_data['data']:
        asd = json.dumps({'ast': i['ast'], 'player': i['player']})
        assist_list.append(json.loads(asd))
    return assist_list


def handle_rb_data():
    rebound_list = []
    rebound_data = get_data()
    for i in rebound_data['data']:
        asd = json.dumps({'dreb': i['dreb'], 'player': i['player']})
        rebound_list.append(json.loads(asd))
    return rebound_list




def bubble_sort():
    test_list = handle_pts_data()
    bubble_list = test_list
    for j in range(0,25):
        check_for_swap = False
        for i in range (0,24):
            if bubble_list[i]['pts'] > bubble_list[i + 1]['pts']:
                swap = bubble_list[i]['pts']
                bubble_list[i]['pts'] = bubble_list[i + 1]['pts']
                bubble_list[i + 1]['pts'] = swap
                check_for_swap = True
        if check_for_swap == False:
            break

    print("Pisteet", bubble_list)
    
        #for i in data points_data() looppaa läpi niin että i on aina yksi objekti- jonka kohta 'pts':sää sortataan. 



def bubblesort_ast():
    test_list = handle_ast_data()
    bubble_list = test_list
    for j in range(0,25):
        check_for_swap = False
        for i in range (0,24):
            if bubble_list[i]['ast'] > bubble_list[i + 1]['ast']:
                swap = bubble_list[i]['ast']
                bubble_list[i]['ast'] = bubble_list[i + 1]['ast']
                bubble_list[i + 1]['ast'] = swap
                check_for_swap = True
        if check_for_swap == False:
            break

    print("Syöttöpisteet", bubble_list)


def bubblesort_rb():
    test_list = handle_rb_data()
    bubble_list = test_list
    for j in range(0,25):
        check_for_swap = False
        for i in range (0,24):
            if bubble_list[i]['dreb'] > bubble_list[i + 1]['dreb']:
                swap = bubble_list[i]['dreb']
                bubble_list[i]['dreb'] = bubble_list[i + 1]['dreb']
                bubble_list[i + 1]['dreb'] = swap
                check_for_swap = True
        if check_for_swap == False:
            break

    print("Levypallot", bubble_list)


bubble_sort()
bubblesort_ast()
bubblesort_rb()

    



