from django.shortcuts import render
from django.http import HttpResponse

def tips(request):
    return HttpResponse("TRY KARO BHAI")
def world(request):
    return HttpResponse("<h1>This is a world</h1> <p> loremhu4h4duirh3f3ufe4ufh4uh4eij4ihcvjhovgrirbhjheb3dhbdebuh3eiu3ehiu3hfbcb4uiuehuhuhuhuswhytetehidbdtgearpitybhsindtemy nam eis arpit jain mu name is aksghay hain my svcotsrersmy coyurdser rs tyhgr</p>")
# def index(request):
#     return render(request,"D:\\prac_mysql\\core\\core\\home\\template\\index.html")

peoples = [
        {'name':'Arpit jain', 'age':11},
        {'name':'Rohan sharma', 'age':6},
        {'name':'deepak gupta','age':8},
        {'name':'Amit yadav', 'age':12},
        {'name':'Ankur gupta', 'age':41},
        {'name':'Rahul jain', 'age':63},
        {'name':'Akshay jain', 'age':45},
        {'name':'salman khan', 'age':15},
    ]

vegetables = ['tomato','potato','onion']

def index(request):
    return render(request,"index.html", context = {'peoples' : peoples,'vegetables': vegetables})
    
def about(request):
    return render(request,"about.html",context = {'peoples' : peoples,'vegetables': vegetables})
def contact(request):
    return render(request,"contact.html",context = {'peoples' : peoples,'vegetables': vegetables})