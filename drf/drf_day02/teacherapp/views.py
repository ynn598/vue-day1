from rest_framework.response import Response
from rest_framework.views import APIView
from teacherapp.models import Teacher
from teacherapp.serializers import TeacherDeSerializer, TeacherSerializer


class TeacherAPIView(APIView):

    def get(self,request,*args,**kwargs):
        tea_id = kwargs.get('id')

        if tea_id:
            tea_obj = Teacher.objects.get(pk=tea_id)
            teacher_serializer = TeacherSerializer(tea_obj).data
            print(teacher_serializer)
            return Response({
                'status':200,
                'message':'查询单个教师成功',
                'result':teacher_serializer
            })
        else:
            teacher_objects_all = Teacher.objects.all()
            tea_data = TeacherSerializer(teacher_objects_all,many=True).data
            print(tea_data)

            return Response({
                'status':200,
                'message':'查询所有教师成功',
                'result':tea_data
            })

    def post(self,request, *args, **kwargs):
        request_data = request.data

        if not isinstance(request_data, dict) or request_data =={}:
            return Response({
                'status':400,
                'message':'参数错误',
            })

        serializer = TeacherDeSerializer(data = request_data)

        if serializer.is_valid():
            tea_ser = serializer.save()
            return Response({
                'status':200,
                'message':'教师添加成功',
                'result':TeacherSerializer(tea_ser).data
            })
        else:
            return Response({
                'status':400,
                'message':'添加教师失败',
                'result':serializer.errors
            })
