from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        number1 = request.POST['number_one']
        number2 = request.POST['number_two']
        operator = request.POST['operator']
        
        if operator == '+':
            result = int(number1) + int(number2)
        if operator == '-':
            result = int(number1) - int(number2)
        elif operator == '*':
            result = int(number1) * int(number2)
        elif operator == '/':
            result = int(number1) / int(number2)

        return render(request, 'calc/home.html', { 'result': result})

    return render(request, 'calc/home.html')