from rest_framework import serializers
from .models import Course
from students_courses.serializers import StudentCourseSerializer
from accounts.models import Account


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        read_only_fields = [
            "id",
            "contents",
            "students_courses",
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["name"]

    def update(self, instance, validated_data):
        students = []
        students_not_found = []
        for student_in_course in validated_data["students_courses"]:
            student_course = student_in_course["student"]
            find_student = Account.objects.filter(email=student_course["email"]).first()
            if not find_student:
                students_not_found.append(student_course["email"])
            else:
                students.append(find_student)
        if students_not_found:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(students_not_found)}."
                }
            )
        if not self.partial:
            instance.students.add(*students)
            return instance
        return super().update(instance, validated_data)
