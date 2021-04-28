from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizza(request):
    pizza = Pizza.objects.order_by("name")

    
    context = {'pizza':pizza}

    return render(request, 'pizzas/pizza.html',context)

def toppings(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    comment = pizza.comment_set.order_by('date_added')
    context = {'pizza':pizza, 'toppings':toppings, 'comment':comment}

    return render(request,'pizzas/toppings.html',context)

def new_comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()

            return redirect('pizzas:toppings', pizza_id = pizza_id)
    context = {'form':form, 'pizza':pizza}
    return render(request,'pizzas/new_comment.html', context)        

