from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from .models import BlogPost, UserProfile, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import UserProfile
from django.shortcuts import render
from .models import MyModel
from django.shortcuts import render
from .forms import DocumentForm
from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.db.models import Q
from django.http import JsonResponse
from .forms import BlogPostForm
from .models import BlogPost
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import docx
from .models import Document
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
    
    


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            form.save()

            # Redirect to the 'upload_success' view
            return redirect('upload_success')
    else:
        form = DocumentForm()

    return render(request, 'upload.html', {'form': form})

def display_images(request):
    images = Document.objects.all()
    return render(request, 'display_images.html', {'images': images})

def delete_image(request, image_id):
    if request.method == 'POST':
        image = Document.objects.get(pk=image_id)
        image.docfile.delete()
        image.delete()
        return redirect('display_images')
    return HttpResponseNotAllowed(['POST'])

def upload_success(request):
    return render(request, 'upload_success.html')



def search(request):
    query = request.GET.get('q')

    if query:
        words = query.split()
        query_filter = Q()
        for word in words:
            query_filter |= Q(title__icontains=word) | Q(content__icontains=word)
        results = BlogPost.objects.filter(query_filter)
    else:
        results = []

    return render(request, 'search.html', {'results': results})


def search_suggestions(request):
    query = request.GET.get('q', '')
    if len(query) > 2:
        suggestions = BlogPost.objects.filter(title__icontains=query)[:5].values('id', 'title')
    else:
        suggestions = []

    print(f"Suggestions: {suggestions}")
    return JsonResponse({'suggestions': list(suggestions)})





def user_profile_list(request):
    users = User.objects.all()
    print(f'User profiles queryset (in user_profile_list): {users}')
    return render(request, 'user_profile_list.html', {'users': users})



class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_post'] = context.pop('blogpost')  # Rename the key
        print(f"Blog post pk: {context['blog_post'].pk}")
        return context


from django.contrib.auth.mixins import LoginRequiredMixin

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    context_object_name = 'user_profile'
    template_name = 'user_profile_detail.html'


    def get_object(self, queryset=None):
        user = self.request.user
        return get_object_or_404(UserProfile, user=user)


class BlogPostCreateView(CreateView):

    model = BlogPost
    fields = ['title', 'author', 'content']

    template_name = 'blog_post_create.html'
    success_url = reverse_lazy('blog_post_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author', 'content']

    template_name = 'blog_post_update.html'
    success_url = reverse_lazy('blog_post_list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_post_delete.html'
    success_url = '/'

class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile_form.html'
    success_url = '/user_profiles/'

class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user_profile_form.html'
    success_url = '/user_profiles/'



class UserProfileDeleteView(DeleteView):
    model = User
    template_name = 'user_profile_confirm_delete.html'
    success_url = '/user_profiles/'

@method_decorator(login_required, name='dispatch')
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_post_list.html'
    context_object_name = 'blog_posts'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile for the new user
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('blog_post_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(f"Blog post pk: {context['blogpost'].pk}")
    return context


def read_docx_file(file):
    doc = docx.Document(file)
    content = ''
    for paragraph in doc.paragraphs:
        content += paragraph.text + '\n'
    return content

def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            uploaded_file = request.FILES.get('upload')
            if uploaded_file:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                if file_extension == '.txt':
                    content = uploaded_file.read().decode()
                    post.content = content
                elif file_extension == '.docx':
                    content = read_docx_file(uploaded_file)
                    post.content = content
                else:
                    messages.error(request, 'Invalid file format. Please upload a .txt or .docx file.')
                    return render(request, 'blog_post_create.html', {'form': form})
            post.save()
            return redirect('blog_post_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog_post_create.html', {'form': form})