from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from .models import Choice ,Question
from django.views import generic
from django.utils import timezone




# Create your views here.
# def index(request):
#     # # return HttpResponse("HELLO, I AM NEETHU ANTONY")
#     # latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     # # output=','.join([q.question_text for q in latest_question_list])
#     # template=loader.get_template('new/index.html')
#     # # return HttpResponse(output)
#     # context={
#     #     'latest_question_list':latest_question_list,
#     # }
#     # return HttpResponse(template.render(context,request))
#
#         latest_question_list = Question.objects.order_by('-pub_date')[:5]
#         context = {'latest_question_list': latest_question_list}
#         return render(request, 'new/index.html', context)
#
# def detail(request,question_id):
#     # # return HttpResponse("you are looking at question %s." %question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'new/detail.html', {'question': question})
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'new/detail.html',{'question':question})
#
# def results(request,question_id):
#     # response="you are looking at the result of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'new/results.html', {'question': question})

def vote(request,question_id):
    # return HttpResponse("you are voting on question %s."% question_id)
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'new/detail.html',{
            'question':question,
            'error_message':"you dint select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('new:results',args=(question.id,)))


class IndexView(generic.ListView):
    template_name ='new/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'new/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'new/results.html'