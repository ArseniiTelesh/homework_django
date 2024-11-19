from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"

    def get_queryset(self, is_published=None):
        return BlogPost.objects.filter(is_published=True)


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ("title", "body", "is_published", "preview")
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_url = form.save()
            new_url.slug = slugify(new_url.title)
            new_url.save()

        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "body", "is_published", "preview")
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
