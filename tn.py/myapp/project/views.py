from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import PollForm, OptionForm
from .models import Option, Poll
from .serializers import PollSerializer, OptionSerializer




@api_view(["PUT"])
def add_poll(request):
    if request.method == 'PUT':
        poll_form = PollForm(request.data)
        print(request.data, poll_form.is_valid())

        options_data = request.data.get('options', [])

        if poll_form.is_valid():
            poll = poll_form.save()
            for option_text in options_data:
                Option.objects.create(option=option_text, question=poll)

            return Response({'message': 'data added'})
        else:
            errors = {
                'poll_form_errors': poll_form.errors,
            }
            return Response({'errors': errors})
    else:
        return Response({'errors': 'Invalid method'})


@api_view(["GET"])
def get_poll(request):
    polls = Poll.objects.all()
    return Response(PollSerializer(polls, many=True).data)
    # return Response({'polls': PollSerializer(polls, many=True).data})

@api_view(["POST"])
def set_active(request, id):
    question = Poll.objects.get(pk=id)
    question.active = not question.active
    question.save()
    return Response({"message": "successfully"})

@api_view(["GET"])
def active_polls(request):
    data = Poll.objects.filter(active=1)
    return Response({'polls': PollSerializer(data, many=True).data})



@api_view(['POST'])
def poll_qount(request, id):
    option = Option.objects.get(pk=id)
    option.qoute_count += 1
    option.save()
    data = Poll.objects.filter(active=1)
    return Response({'poll': PollSerializer(data, many=True).data})
