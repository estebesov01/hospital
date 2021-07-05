from django.db import models
from django.urls import reverse


class Hospital(models.Model):
    title = models.CharField('Больница', max_length=100, blank=True)
    ocpo = models.IntegerField('ОКПО', unique=True, blank=True)
    CHUI = 'Чуйская'
    OSH = 'Ошская'
    TALAS = 'Таллаская'
    NARYN = 'Нарынская'
    BATKEN = 'Баткенская'
    IK = 'Иссык-Кульская'
    JL = 'Джалал-Абадская'
    regions = [
        (CHUI, 'Чуйская область'),
        (TALAS, 'Таласская область'),
        (NARYN, 'Нарынская область'),
        (BATKEN, 'Баткенская область'),
        (IK, 'Исык-Кульская область'),
        (JL, 'Джалал-Абадская область'),
        (OSH, 'Ошская область'),
    ]
    hos_types = (
        (1, 'Государственная'),
        (2, 'Частная'),
    )
    hospital_type = models.IntegerField(choices=hos_types, default=1)
    take_region = models.CharField(max_length=20, choices=regions, default=CHUI)
    count_of_workers = models.DecimalField('Количество работников(макс 100): ', max_digits=2, decimal_places=0,
                                           default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hos', kwargs={"hos_id": self.pk})


class Worker(models.Model):
    title = models.CharField('Ф.И.О', max_length=50, default='')
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING, default=True)
    pin_code = models.CharField('ПИН-Код паспорта', max_length=30, default='')
    age = models.PositiveIntegerField('Возраст', default=0)
    stage = models.PositiveIntegerField('Стаж', default=0)
    number_tel = models.CharField('Номер телефона', max_length=20, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class HeadDoctor(Worker):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, verbose_name='Место работы')


class Nurse(Worker):
    head_doctor = models.ForeignKey(HeadDoctor, on_delete=models.DO_NOTHING)


class Doctor(Worker):
    head_doctor = models.ForeignKey(HeadDoctor, on_delete=models.DO_NOTHING)
    SURGEON = 'Хирург'
    THERAPIST = 'Терапевт'
    profession = [
        (SURGEON, 'Хирург'),
        (THERAPIST, 'Терапевт'),
    ]
    nurse = models.ForeignKey(Nurse, on_delete=models.DO_NOTHING, default=True)
    work_profession = models.CharField(max_length=10, choices=profession, default=THERAPIST)


class Patient(models.Model):
    title = models.CharField('Ф.И.О пациента', max_length=50)
    nurse = models.ForeignKey(Nurse, on_delete=models.DO_NOTHING, default=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING, default=True)
    pin_code = models.CharField('ПИН-Код паспорта', max_length=30, default='')
    age = models.PositiveIntegerField('Возраст', default=0)
    reasonOfVisit = models.TextField('Причина визита в больницу')

    def __str__(self):
        return self.title
