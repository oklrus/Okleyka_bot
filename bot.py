from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '8063678913:AAG3FcRDotZCvk_cDw47JyAQ8u-sxhaGSMk'  # ← Новый токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("📅 Записаться", url="https://wa.me/77006592541"))
    
    text = (
        "Приветствуем в Okleykarus! 🚗✨\n\n"
        "✅ Оклейка авто бронеплёнкой\n"
        "✅ Защита от сколов, царапин\n"
        "✅ Гарантия 5 лет\n\n"
        "💰 Цена: 170 000 тг\n\n"
        "Нажмите кнопку ниже 👇"
    )
    
    await message.answer(text, reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
