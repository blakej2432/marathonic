from django.db import models

class CourseType(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "course_type"
        verbose_name = "코스종류"
        verbose_name_plural = "코스종류"


class Race(models.Model):
    title = models.CharField(max_length=255, verbose_name="대회제목")
    date = models.DateField(verbose_name="대회날짜")
    city = models.CharField(max_length=100, verbose_name="도시")
    region = models.CharField(max_length=100, verbose_name="지역")

    course_type = models.ManyToManyField(
        CourseType,
        related_name="races",
        verbose_name="코스종류")
    
    REGI_STATUS_CHOICES = [
        ("open", "접수중"),
        ("closed", "접수완료"),
        ("wait", "접수예정"),
    ]
    regi_status = models.CharField(
        max_length = 10,
        choices = REGI_STATUS_CHOICES,
        verbose_name = "접수상태"
    )
    race_image = models.ImageField(
        upload_to="race_images/",
        null=True,
        blank=True,
        verbose_name="대회이미지"
    )
    homepage_url = models.URLField(verbose_name="홈페이지url")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = "race"
        verbose_name = "대회"
        verbose_name_plural = "대회"


