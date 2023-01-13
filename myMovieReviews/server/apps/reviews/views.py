from django.shortcuts import render, redirect

from server.apps.reviews.models import Review


def reviews_outline(request, *args, **kwargs):
    reviews = Review.objects.all()
    return render(request, "reviews/reviews_outline.html", {"reviews": reviews})


def reviews_details(request, pk, *args, **kwargs):
    review = Review.objects.all().get(id=pk)
    return render(request, "reviews/reviews_details.html", {"review": review})


def reviews_create(request, *args, **kwargs):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            director = request.POST["director"],
            main_actors = request.POST["main_actors"],
            genre = request.POST["genre"],
            year = request.POST["year"],
            running_time = request.POST["running_time"],
            rating = request.POST["rating"],
            content = request.POST["content"],
        )
        return redirect("/")
    return render(request, "reviews/reviews_create.html")


def reviews_update(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    if request.method == "POST":
        review.title = request.POST["title"]
        review.director = request.POST["director"]
        review.main_actors = request.POST["main_actors"]
        review.genre = request.POST["genre"]
        review.year = request.POST["year"]
        review.running_time = request.POST["running_time"]
        review.rating = request.POST["rating"]
        review.content = request.POST["content"]
        review.save()
        return redirect(f"/reviews/{review.id}")
    return render(request, "reviews/reviews_update.html", {"review": review})


def reviews_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/")