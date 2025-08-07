# إعدادات نظام الاشتراك الأوتوماتيكي لقناة TRADE&BOOM

# معلومات البوت
BOT_TOKEN = "8284508405:AAFZS2a1HCcumV9Sq8zbEDIhfcDQsteCPGQ"
BOT_USERNAME = "@Tradeixboom_bot"

# معلومات القناة
CHANNEL_ID = "@TRADEBOOM"  # يجب تحديث هذا برقم القناة الصحيح أو اسم المستخدم
CHANNEL_NAME = "TRADE&BOOM"

# إعدادات الاشتراك
SUBSCRIPTION_PRICE = 29.0  # بالدولار الأمريكي (USDT)
SUBSCRIPTION_DAYS = 3      # مدة الاشتراك بالأيام

# إعدادات الدفع
USDT_WALLET_ADDRESS = "TMhsVFZS2Dy1GXDScJsWiYDrQgXeyKZJUc"
USDT_CONTRACT_ADDRESS = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # عقد USDT على TRON
PAYMENT_TIMEOUT_HOURS = 1  # مهلة انتظار الدفع بالساعات

# إعدادات TRON API
TRON_API_BASE = "https://api.trongrid.io"
TRON_API_KEY = None  # اختياري - للحصول على معدل طلبات أعلى

# إعدادات المجدول
CHECK_EXPIRED_INTERVAL_MINUTES = 30  # فحص الاشتراكات المنتهية كل 30 دقيقة
REMINDER_INTERVAL_HOURS = 6          # إرسال تذكيرات كل 6 ساعات
CLEANUP_TIME = "03:00"               # وقت تنظيف قاعدة البيانات يومياً

# إعدادات قاعدة البيانات
DATABASE_URL = "sqlite:///database/app.db"

# إعدادات Flask
SECRET_KEY = "asdf#FGSgvasgf$5$WGT"  # يجب تغيير هذا في الإنتاج
DEBUG_MODE = False
HOST = "0.0.0.0"
PORT = 5000

# رسائل البوت (يمكن تخصيصها)
MESSAGES = {
    "welcome": """
🌟 مرحباً بك في بوت قناة {channel_name}! 🌟

مرحباً {first_name}! 👋

📈 للوصول إلى محتوى القناة الحصري، تحتاج إلى اشتراك مدفوع.

💰 سعر الاشتراك: {price} USDT
⏰ مدة الاشتراك: {days} أيام

🔹 ميزات الاشتراك:
• الوصول الكامل لقناة {channel_name}
• تحليلات حصرية للأسواق
• إشارات تداول يومية
• دعم فني مباشر

اضغط على "اشترك الآن" للبدء! 👇
    """,
    
    "payment_instructions": """
💳 تفاصيل الدفع:

💰 المبلغ: {amount} USDT (TRC20)
🏦 عنوان المحفظة:
`{wallet_address}`

⚠️ تعليمات مهمة:
1️⃣ أرسل المبلغ بالضبط: {amount} USDT
2️⃣ استخدم شبكة TRC20 فقط
3️⃣ انتظر تأكيد المعاملة (عادة 1-3 دقائق)
4️⃣ سيتم تفعيل اشتراكك تلقائياً

⏰ صالح لمدة ساعة واحدة من الآن

بعد إرسال المبلغ، اضغط "تحقق من الدفع" 👇
    """,
    
    "payment_success": """
✅ تم تأكيد الدفع بنجاح!

🎉 مرحباً بك في قناة {channel_name}!
⏰ مدة الاشتراك: {days} أيام
📅 ينتهي في: {end_date}

🔗 رابط القناة: {channel_id}

يمكنك الآن الوصول لجميع المحتويات الحصرية! 🚀
    """,
    
    "subscription_expired": """
❌ انتهى اشتراكك في قناة {channel_name}

🔄 لتجديد الاشتراك والعودة للقناة:
• استخدم الأمر /subscribe
• أو اضغط على "اشترك الآن" أدناه

شكراً لك على ثقتك بنا! 🙏
    """,
    
    "subscription_reminder": """
⏰ تذكير: سينتهي اشتراكك خلال {hours} ساعة

🔄 لتجديد الاشتراك:
• استخدم الأمر /subscribe
• أو اضغط على "جدد الاشتراك" أدناه

لا تفوت المحتوى الحصري! 📈
    """
}

# إعدادات التسجيل
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'bot.log',
            'mode': 'a',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

