from django.shortcuts import render
from .models import AboutFaculty, AboutDepartmentPeople, News, Students 
from django.views import View
from schedule.models import Room, Para, Schedule, BookingRoom
from django.db.models import Q
from datetime import datetime
# Create your views here.

class AboutFacultyView(View):
    def get(self, request):
        about = AboutFaculty.objects.first()
        return render(request, 'index.html', {'about': about})
    
class DekanatView(View):
    def get(self, request):
        dekanat = AboutDepartmentPeople.objects.all().order_by('place')
        return render(request, 'administration.html', {'dekanat': dekanat})

class StudentsView(View):
    def get(self, request):
        students = Students.objects.all()
        return render(request, 'students.html', {'students': students})
      
class NewsView(View):
    def get(self, request):
        news = News.objects.all().order_by('-id')[:5]
        return render(request, 'news.html', {'news': news})
        
class DetailView(View):
    def get(self, request, id):
        new = News.objects.get(id=id)
        return render(request, 'detail.html', {'new': new})
    
class ScheduleView(View):
    def get(self, request):
        day_names = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
        today_index = datetime.now().weekday() # hafta kuni: dushanba -> 0
        paralar = Para.objects.all()
        rooms = Room.objects.all().filter(Q(is_active=True)).order_by('room')
        daily_schedule = Schedule.objects.all().filter(Q(is_active=True) and Q(day = day_names[today_index])).order_by('day', 'para')
        booking_rooms = BookingRoom.objects.all().filter(Q(is_active=True) and Q(day = day_names[today_index])).order_by('day', 'para')  
        
        # schedule = {}
        

        # for room in rooms:
        #     room_schedule = {}
        #     for para in paralar:
        #         try:
        #             schedule_item = daily_schedule.get(room=room, para=para)
        #             room_schedule[para] = schedule_item
        #         except:
        #             room_schedule[para] = None
        #     schedule[room] = room_schedule
            
        # booking = {}
        
        # for room in rooms:
        #     room_booking = {}
        #     for para in paralar:
        #         try:
        #             booking_item = booking_rooms.get(room=room, para=para)
        #             room_booking[para] = booking_item
        #         except:
        #             room_booking[para] = None
        #     booking[room] = room_booking
            
            
        # print(schedule)
        # print(booking)
        # ## schedule and booking is a 2D array
        
        # for room, paralar in schedule.items():
        #     for para, dars in paralar.items():
        #         # print(room, para, dars)
        #         # print(booking.get(room).get(para))
        #         if not dars:
                    
        #             schedule.get(room)[para] = booking.get(room).get(para)
        #             # print(schedule.get(room).get(para))
        #             # print(booking.get(room).get(para))
        #         #     print(room, para)
        # print("----")
        # print(schedule)
                    

        
        
        schedule = []
        for room in rooms:
            room_schedule = []
            for para in paralar:
                try:
                    schedule_item = daily_schedule.get(room=room, para=para)
                    room_schedule.append(schedule_item)
                except:
                    room_schedule.append(room)
            schedule.append(room_schedule)  
            
        booking = []
        
        for room in rooms:
            room_booking = []
            for para in paralar:
                try:
                    booking_item = booking_rooms.get(room=room, para=para)
                    room_booking.append(booking_item)
                except:
                    room_booking.append(room)
            booking.append(room_booking)
            
            
        # ## schedule and booking is a 2D array
        # print(schedule)
        # print(booking)
        
        for index, para in enumerate(schedule):
            for index2, room in enumerate(para):
                if isinstance(room, Room):
                    schedule[index][index2] = booking[index][index2]
             
        # print(schedule)
        
        
        context = {
            'paralar': paralar,
            'rooms': rooms,
            'schedule': schedule,
        }
        return render(request, 'schedule.html', context) 
    