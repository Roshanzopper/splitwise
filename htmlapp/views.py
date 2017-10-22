from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from MainApp.models import  SplitUser
from MainApp.serializers import SplitUserSerializer
from django.urls import reverse

class IndexView(generic.ListView):
    template_name = 'htmlapp/index.html'
    context_object_name = 'latest_user_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return SplitUser.objects.order_by('-createdon')[:6]


class DetailView(generic.DetailView):
    model = SplitUser
    template_name = 'htmlapp/detail.html'

class DetailView(generic.DetailView):
        model = SplitUser
        template_name = 'htmlapp/detail.html'


# def DeleteView( request, pk, format=None):
#         user = SplitUserSerializer(data=request.POST)
#         if user.is_valid():
#             user.delete()
#         return HttpResponseRedirect(reverse('htmlapp:index'))

# def DeleteView( request, question_id):
#     question = get_object_or_404(SplitUser, id=question_id)
#     question.delete()
#     return HttpResponseRedirect(reverse('htmlapp:index'))
def DeleteView(request, id):
    note = get_object_or_404(SplitUser, pk=id).delete()
    return HttpResponseRedirect(reverse('htmlapp:index'))

def CreateView(request):
        return render(request,'htmlapp/create.html')


def savenew(request):
    if request.method == "POST":
        form = SplitUserSerializer(data=request.POST)
        if form.is_valid():
            form.username = request.POST['username']
            form.password = request.POST['password']
            form.emailid = request.POST['emailid']
            form.save()
            return HttpResponseRedirect(reverse('htmlapp:index'))
        return HttpResponseRedirect()
    return HttpResponseRedirect()

