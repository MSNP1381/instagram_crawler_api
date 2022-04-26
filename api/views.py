from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from .serializer import DataSerializer
# Create your views here.
from instagrapi import Client
import json
from instagrapi import MediaMixin

from rest_framework.decorators import api_view

cl = Client()
cl.login("msnp_2", '123456amn')


@api_view(['GET'])
def data_list(request):
    # try:
        print(100 * "$")
        try:
            request.GET['u']
            request.GET['c']
        except:
            return Response("given Data Not Found", status=404)
        try:
            user_id = cl.user_id_from_username(request.GET['u'])
        except:
            return Response("User not found", status=404)
        medias = cl.user_medias(user_id, request.GET['c'])
        # print(medias[0])
        print(100 * "#")

        items = []
        # a = medias[0].resources[0].json()
        var = ''
        for i in medias:
            e = {'id': i.id, 'code': i.code, 'username': i.user.username, 'comment_count': i.comment_count,
                 'like_count': i.like_count, 'caption_text': str(i.caption_text),
                 'thumbnail_url': i.thumbnail_url, 'view_count': i.view_count, 'media_type': i.media_type}
            x = []
            if i.media_type == 8:
                for j in i.resources:
                    x.append(str(j.thumbnail_url))
                e['resources'] = x
            if i.media_type not in [1, 8]:
                continue
            items.append(e)
            var = DataSerializer(items, many=True)
        return Response(var.data)
    # except:
    #     return Response("system Error", status=500)
