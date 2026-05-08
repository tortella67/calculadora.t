from django.shortcuts import render

def calculadora_view(request):
    resultado = None

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operacion = request.POST.get("operacion")

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error"

    return render(request, "calculadora/calculadora.html", {"resultado": resultado})
