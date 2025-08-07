#!/bin/bash

# ملف تشغيل نظام الاشتراك الأوتوماتيكي لقناة TRADE&BOOM

echo "🚀 بدء تشغيل نظام الاشتراك الأوتوماتيكي..."

# التحقق من وجود Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 غير مثبت. يرجى تثبيت Python 3.8 أو أحدث."
    exit 1
fi

# التحقق من وجود البيئة الافتراضية
if [ ! -d "venv" ]; then
    echo "📦 إنشاء البيئة الافتراضية..."
    python3 -m venv venv
fi

# تفعيل البيئة الافتراضية
echo "🔧 تفعيل البيئة الافتراضية..."
source venv/bin/activate

# تثبيت المتطلبات
echo "📚 تثبيت المتطلبات..."
pip install -r requirements.txt

# التحقق من ملف الإعدادات
if [ ! -f "config.py" ]; then
    echo "⚠️  تحذير: ملف config.py غير موجود. يرجى إنشاؤه أولاً."
    exit 1
fi

# إنشاء مجلد قاعدة البيانات إذا لم يكن موجوداً
mkdir -p src/database

# بدء تشغيل النظام
echo "✅ بدء تشغيل النظام..."
echo "📊 لوحة الإدارة متاحة على: http://localhost:5000"
echo "🤖 البوت جاهز للاستخدام على تيليجرام"
echo ""
echo "للإيقاف: اضغط Ctrl+C"
echo "=========================="

python src/main.py

