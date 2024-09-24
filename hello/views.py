from django.shortcuts import render, get_object_or_404
from .models import News, Author

# View for the home page where the latest 10 news articles are displayed
def home(request):
    latest_news = News.objects.order_by('-pub_date')[:5]  # Fetch the latest 10 news articles
    return render(request, 'hello/home.html', {'news_list': latest_news})

# View for displaying the full list of news articles
def all_news(request):
    all_news = News.objects.order_by('-pub_date')  # Fetch all news articles sorted by date
    return render(request, 'hello/news_list.html', {'news_list': all_news})

# View for displaying a specific news article by its ID
def news_detail(request, new_id):
    news_article = get_object_or_404(News, pk=new_id)  # Fetch the news article or return 404 if not found
    return render(request, 'hello/news_detail.html', {'news_article': news_article})

# View for displaying a list of all authors
def authors_list(request):
    authors = Author.objects.all()  # Fetch all authors
    return render(request, 'hello/authors_list.html', {'authors': authors})

# View for displaying the list of news articles by a specific author
def author_news(request, author_id):
    author = get_object_or_404(Author, pk=author_id)  # Fetch the author by ID
    author_news_list = News.objects.filter(author=author)  # Fetch all news written by this author
    return render(request, 'hello/author_news.html', {'author': author, 'news_list': author_news_list})
