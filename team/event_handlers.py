
from django.http import JsonResponse

def handle_click(request):
    if request.method == 'POST':
        image_name = request.POST.get('image_name')
        # Do something with image_name, like logging or updating the database
        return JsonResponse({'status': 'success', 'image_name': image_name})
    return JsonResponse({'status': 'failed'})