from django.http import HttpResponse

from p_library.models import Book
from .forms import BookForm

from p_library.models import Publisher
from django.template import loader
from django.shortcuts import redirect, render

from .models import Author
from .forms import AuthorForm

from .models import Reading
from .forms import ReadingForm

from .models import Friend
from .forms import FriendForm

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

from django.http.response import HttpResponseRedirect

from django.forms import formset_factory
# AuthorFormSet = formset_factory(AuthorForm)

class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class ReadingCreate(CreateView):
    model = Reading
    form_class = ReadingForm
    success_url = reverse_lazy('p_library:reading_list')
    template_name = 'reading_edit.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'reading_edit.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'

class ReadingList(ListView):
    model = Reading
    template_name = 'reading_list.html'

class FriendList(ListView):
    model = Friend
    template_name = 'friend_list.html'

class AuthorUpdate(UpdateView):
    model = Author
    fields = ["full_name", "birth_year", "country"]
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class BookUpdate(UpdateView):
    model = Book
    fields = ['ISBN', 'title', 'description', 'year_release', 'copy_count', 'price', 'author', 'publisher', 'cover',]
    success_url = reverse_lazy('p_library:index')
    template_name = 'book_edit.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class ReadingUpdate(UpdateView):
    model = Reading
    fields = ['friend', 'book']
    success_url = reverse_lazy('p_library:reading_list')
    template_name = 'reading_edit.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class FriendUpdate(UpdateView):
    model = Friend
    fields = ['name', 'books']
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'reading_edit.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class AuthorDelete(DeleteView):
    model = Author
    form_class = AuthorForm
    fields = ["full_name", "birth_year", "country"]
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_delete.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        self.delete(request)
        return redirect('p_library:author_list')

class ReadingDelete(DeleteView):
    model = Reading
    form_class = ReadingForm
    # fields = ['friend', 'book']
    success_url = reverse_lazy('p_library:reading_list')
    template_name = 'reading_delete.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        return super().post(request, *args, **kwargs)

class FriendDelete(DeleteView):
    model = Friend
    fields = ['name', 'books']
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'reading_delete.html'

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        if not user.is_authenticated:
            return redirect('user_auth:index')
        if not user.is_superuser:
            context['message'] = "Вы не супер пользователь!"
            return render(request, 'access.html', context)
        self.delete(request)
        return redirect('p_library:friend_list')

def books_list(request):
    return redirect('/book_list/')

class book_list(ListView):
    model = Book
    form_class = BookForm
    context_object_name = 'books'
    template_name = 'book_list.html'

def publisher(request):
    template = loader.get_template('publisher.html')
    publishers = Publisher.objects.all()
    publishers_data = {
        "publishers": publishers,
    }
    return HttpResponse(template.render(publishers_data, request))

def book_increment(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('user_auth:index')
    if not user.is_superuser:
        context['message'] = "Вы не супер пользователь!"
        return render(request, 'access.html', context)
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book_list/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book_list/')
            book.copy_count += 1
            book.save()
        return redirect('/book_list/')
    else:
        redirect('/book_list/')

def book_decrement(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('user_auth:index')
    if not user.is_superuser:
        context['message'] = "Вы не супер пользователь!"
        return render(request, 'access.html', context)
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            redirect('/book_list/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                redirect('/book_list/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/book_list/')
    else:
        return redirect('/book_list/')


def is_save(author_form):
    try:
        author_form.save()
        return True
    except BaseException:
        return False

def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=3)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='author')
        if author_formset.is_valid():
            for author_form in author_formset:
                if is_save(author_form):
                    pass
                else:
                    return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='author')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})