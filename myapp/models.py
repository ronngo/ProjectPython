from django.db import models

# Create your models here.
class Student(models.Model):
    #Định nghĩa các trường dữ liệu

    fullname = models.CharField(max_length=40)
    age = models.IntegerField(default=0)
    image = models.ImageField(null=True)

    #Xây dựng hàm in nội dung của đối tượng ra màn hình

    def  __str__(self):
        s = "Họ tên là : " + str(self.fullname) + ", tuổi là : " + str(self.age) + "Anh : " + str(self.image)
        return s

