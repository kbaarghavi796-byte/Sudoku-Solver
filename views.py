from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .sudoku_solver import solve



def index(request):

    board=[[0 for i in range(9)] for j in range(9)]

    return render(request,"index.html",{
        "board":board
    })




@csrf_exempt
def solve_sudoku(request):

    if request.method=="POST":

        data=json.loads(request.body)

        board=data["board"]

        solve(board)


        return JsonResponse({
            "solution":board
        })