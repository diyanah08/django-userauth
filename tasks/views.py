from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import ItemForm
from .models import Item

# Create your views here.
def show_items(request):
    items = Item.objects.all()
    return render(request, "tasks/show_items.template.html", {
        "items":items
    })


def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Item Added")
            return redirect(create_item)
        else:
            return render(request, "tasks/create_item.template.html", {
                "form":form
            })
    else:
        form = ItemForm()
        return render(request, "tasks/create_item.template.html", {
                "form":form
        })