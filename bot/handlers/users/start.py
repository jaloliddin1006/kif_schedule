import time
from aiogram import types
from data.config import ADMINS
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.defoult_btn import back_btn, menu_btn, message_phone, student_documents_btn
from data.api import get_user_by_id, create_user, get_sources, get_groups, get_group_schedule, get_sources_by_id, get_group_info
from keyboards.inline.inline_btn import schedule_kurs_btn_func, schedule_group_btn_func
import requests
from aiogram.types import InputFile

@dp.message_handler(text="/start")
async def start_bot(message: types.Message, state=FSMContext):
    user_ = message.from_user
    user = get_user_by_id(user_.id)
    # print(user)
    # print("===================")
    
    if user.get("status_info") not in [200, 201]:
        username = user_.username if user_.username else None
        a = create_user(user_.id, username, user_.full_name, True)
        # print(a)
    await message.answer(f"Assalomu alaykum {user_.full_name}", reply_markup=menu_btn)

@dp.message_handler(text="📆 Dars Jadvali")
async def schedule_func(message: types.Message):
    await message.answer("Kursni tanlang", reply_markup=schedule_kurs_btn_func())

@dp.callback_query_handler(text_contains="course_")
async def schedule_func(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.delete()
    course = call.data[-1]
    groups = get_groups(course=course)
    # groups = [g for g in groups if g['course'] == int(course)]
    await call.message.answer("Guruhingizni tanlang", reply_markup=schedule_group_btn_func(groups))

@dp.callback_query_handler(text="back")
async def back(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.delete()
    await call.message.answer("Kursni tanlang", reply_markup=schedule_kurs_btn_func())


@dp.callback_query_handler(text_contains="group_")
async def schedule_func(call: types.CallbackQuery):
    await call.answer(cache_time=2)
    group_id = call.data.split("_")[-1]
    schedule = get_group_schedule(group_id=group_id)
    group_name = get_group_info(group_id).get("academic_code", "Nomalum")
    schedule_text = f"   <b>{group_name} - guruh Iqtidorli Talabalar </b>\n\n"
    for day, lessons in schedule.items():
        schedule_text += f"🔘 <b>{day}</b>\n"
        for lesson in lessons:
            if lesson['week'] == 'full':
                schedule_text += f"    ▪️<b>  {lesson['para']} </b>| 🏫 {lesson['room']} xona\n"
                schedule_text += f"    📚  Fan: <b>{lesson['subject']}</b> (<i>{lesson['lesson_type']}</i>) \n"\
                                f"    👨‍🏫  O'qituvchi: <i>{lesson['teacher']}</i>\n\n"
            elif lesson['week'] == 'odd':
                schedule_text += f"    ▪️<b>  {lesson['para']} (toq hafta) </b>| 🏫 {lesson['room']} xona\n"\
                                f"    📚  Fan: <b>{lesson['subject']}</b> (<i>{lesson['lesson_type']}</i>)\n"\
                                f"    👨‍🏫  O'qituvchi: <i>{lesson['teacher']}</i>\n\n"
            elif lesson['week'] == 'even':
                schedule_text += f"    ▪️<b> {lesson['para']} (juft hafta) </b>| 🏫 {lesson['room']} xona\n"\
                                f"    📚  Fan: <b>{lesson['subject']}</b> (<i>{lesson['lesson_type']}</i>)\n"\
                                f"    👨‍🏫  O'qituvchi: <i>{lesson['teacher']}</i>\n\n"

    await call.message.answer(schedule_text)




@dp.message_handler(text="📄 Talaba xujjatlari")
async def student_documents(message: types.Message, state=FSMContext):
    docs = get_sources()
    await message.answer("Talaba xujjatlari", reply_markup=student_documents_btn(docs))
    await state.set_state("docs")

@dp.message_handler(state="docs", text="🔙 Back")
async def echo(message: types.Message, state: FSMContext):
    await message.answer("Asosiy menu", reply_markup=menu_btn)
    await state.finish()



@dp.message_handler(state="docs")
async def echo(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    doc_id = message.text
    doc = get_sources_by_id(title=doc_id)
    docs = get_sources()
    print(doc)
    # 'file_url': 'http://127.0.0.1:8000/media/documents/new.txt'
    if doc.get('file_url'):
        file_url = doc['file_url']
        print(file_url)
        # file_name = file_url.split("/")[-1]
        # caption = doc.get("description")
        # file = requests.get(file_url)
        # with open(f"{file_name}", "wb") as f:
        #     f.write(file.content)
        # await message.answer_document(document=InputFile(file_name) ,caption=caption, reply_markup=student_documents_btn(docs))

    await state.set_state("docs")

@dp.message_handler(text="🔙 Back")
async def back(message: types.Message):
    await message.answer("Asosiy menu", reply_markup=menu_btn)
