from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        "title": "Головна сторінка",
        "content": "Магазин меблів Ідеальний Вибір",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Про нас",
        "content": "Магазин меблів Ідеальний Вибір",
        "text_on_page": 'Ласкаво просимо до "Ідеального Вибору" – вашого найкращого помічника в створенні прекрасного та функціонального простору! Ми - команда фахівців, яка присвятила себе наданню найвищого рівня сервісу та якості в сфері меблів.У нашому магазині ви знайдете широкий вибір меблів для всіх кімнат вашого дому чи офісу. Чи вам потрібні стильні та ергономічні меблі для кухні, щоб створити теплу та затишну атмосферу для сімейних обідів? Або, можливо, ви шукаєте зручні та елегантні спальні меблі, які допоможуть вам розслабитися та насолодитися спокоєм після напруженого дня? Ми також пропонуємо стильні меблі для віталень, офісів та декору, які допоможуть вам створити простір вашої мрії.Наші меблі відомі своєю високою якістю матеріалів та відмінним дизайном. Ми працюємо тільки з надійними виробниками, щоб забезпечити наших клієнтів меблями, які будуть виглядати стильно та служити вам протягом багатьох років.Наша місія - зробити ваш дім або офіс комфортним та красивим, а процес вибору меблів - приємним та легким. Наші досвідчені консультанти завжди готові допомогти вам з вибором ідеальних меблів, що відповідають вашим потребам та стилю.Не вагайтеся звертатися до нас з будь-якими питаннями або для отримання консультації. Ми завжди раді допомогти вам зробити ваш простір ще кращим!',
    }
    return render(request, "main/about.html", context)


def contacts(request):
    context = {
        "title": "Контакти",
        "text_on_page": "Телефон: +380 (67) 123-4567  Електронна пошта: info@idealnyyvybir.com",
    }
    return render(request, "main/contacts.html", context )