from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from msgs.models import Msg
from msgs.serializers import MsgSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import datetime


class GetMsg(viewsets.ModelViewSet):
    """
    获取消息记录
    """
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer

    def list(self, request):
        max_len = 10  # 当前每页只显示10条记录
        page = request.GET.get('page')
        u_id = request.GET.get('u_id')
        if request.GET.get('status') is not None:
            status = request.GET.get('status')
            queryset = Msg.objects.filter(status=int(status), receiver=int(u_id))[(int(page)-1)*max_len:(int(page)-1)*max_len + max_len]
        else:
            queryset = Msg.objects.filter(receiver=int(u_id))[(int(page)-1)*max_len: (int(page)-1)*max_len + max_len]
        serializer = MsgSerializer(queryset, many=True)
        return Response(serializer.data)


@csrf_exempt
def send(request):
    """
    发送消息记录
    """
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            sender_id = request.POST.get('sender_id')
            receiver_id = request.POST.get('receiver_id')
            next_id = Msg.objects.values_list('id').filter(receiver_id=receiver_id).last()
            print(next_id)
            c = Msg(title=title, content=content, time=datetime.datetime.now(),
                    sender_id=int(sender_id), receiver_id=int(receiver_id), formerMsg_id=next_id[0], status=0)
            c.save()
            return JsonResponse({"success": True, 'message': u'成功', 'result': c.id})
        except ValueError:
            return JsonResponse({"success": False, "message": "value type is error!", "result": "fail"})
    else:
        return JsonResponse({"success": False, "message": "does not support this http method", 'result': ""})


@csrf_exempt
def change(request):
    """
    查看时更新消息记录为已读
    标记为已读时，可支持多条记录
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            get_msg_id = request.POST.get('id')
            msg_id = map(int, get_msg_id.split(','))
            Msg.objects.filter(id__in=msg_id).update(status=1)
            return JsonResponse({"success": True, 'message': 'update status success', 'result': get_msg_id})
        except ValueError:
            return JsonResponse({"success": False, "message": "value type is error!", "result": "fail"})
    else:
        return JsonResponse({"success": False, "message": "does not support this http method", "result": "fail"})


@csrf_exempt
def delete(request):
    """
    删除消息记录
    :param request:
    :return:
    """
    if request.method == 'POST':
        try:
            get_msg_id = request.POST.get('id')
            msg_id = map(int, get_msg_id.split(','))
            Msg.objects.filter(id__in=msg_id).delete()
            return JsonResponse({"success": True, "message": u"成功", "result": get_msg_id})
        except ValueError:
            return JsonResponse({"success": False, "message": "para type is error!", "result": "fail"})
    else:
        return JsonResponse({"success": False, "message": "does not support this http method", 'result': "fail"})
