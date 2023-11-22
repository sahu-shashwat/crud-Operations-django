from django.shortcuts import render, redirect
from app1.models import items, product


# Create your views here.
def register_item(request):
    if request.method == "POST":
        items.objects.create(name=request.POST["name"], desc=request.POST["desc"])
        return redirect("/app1/list")
    return render(request=request, template_name="item.html")


def register_product(request):
    res = items.objects.all()
    if request.method == "POST":
        product.objects.create(
            id_id=request.POST["id_id"],
            name=request.POST["name"],
            price=request.POST["price"],
            desc=request.POST["desc"],
            quantity=request.POST["quantity"],
        )
        return redirect("/app1/list_product")
    return render(request=request, template_name="product.html", context={"data": res})


def update(request, pk):
    if request.method == "POST":
        items.objects.filter(id=pk).update(
            name=request.POST["name"], desc=request.POST["desc"]
        )
        return redirect("/app1/list")
    res = items.objects.get(id=pk)
    return render(request=request, template_name="update.html", context={"data": res})


def delete(request, pk):
    res = items.objects.get(id=pk)
    if request.method == "POST":
        res = items.objects.get(id=pk).delete()
        return redirect("/app1/list")
    return render(request=request, template_name="delete.html", context={"data": res})


def list(request):
    res = items.objects.all()
    return render(request=request, template_name="list.html", context={"data": res})


def list_product(request):
    res = product.objects.all()
    return render(
        request=request, template_name="list_product.html", context={"data": res}
    )


def update_product(request, pk):
    item = items.objects.all()
    print(item)
    res = product.objects.get(pid=pk)
    if request.method == "POST":
        print(request.POST)
        res1 = product.objects.filter(pid=pk).update(
            id_id=request.POST["id_id"],
            name=request.POST["name"],
            price=request.POST["price"],
            desc=request.POST["desc"],
            quantity=request.POST["quantity"],
        )
        print(res1)
        return redirect("/app1/list_product")

    return render(
        request=request,
        template_name="update_product.html",
        context={"data": res, "items": item},
    )


def delete_product(request, pk):
    res = product.objects.get(id=pk)
    if request.method == "POST":
        res = product.objects.get(id=pk).delete()
        return redirect("/app1/list_product")
    return render(
        request=request, template_name="delete_product.html", context={"data": res}
    )
