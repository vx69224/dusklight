from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from datetime import datetime
import json

@csrf_exempt
def sunset_azimuth(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        from astral import LocationInfo
        from astral.sun import sun, azimuth
    except ImportError:
        return JsonResponse({'error': 'Astral not installed'}, status=500)
    try:
        data = json.loads(request.body)
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        date_str = data.get('date')
        if date_str:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date = datetime.now().date()
        city = LocationInfo(name="Custom", region="Custom", timezone="UTC", latitude=latitude, longitude=longitude)
        s = sun(city.observer, date=date, tzinfo="UTC")
        sunset_time = s['sunset']
        sunset_az = azimuth(city.observer, sunset_time)
        sunset_time_str = sunset_time.strftime('%H:%M') if sunset_time else None
        return JsonResponse({'azimuth': sunset_az, 'sunset': sunset_time_str})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def sun_aligned_time(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        from astral import LocationInfo
        from astral.sun import sun, azimuth
    except ImportError:
        return JsonResponse({'error': 'Astral not installed'}, status=500)
    try:
        data = json.loads(request.body)
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        bearing = float(data['bearing'])
        threshold = float(data.get('threshold', 2))  # degrees
        date_str = data.get('date')
        if date_str:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date = datetime.now().date()
        city = LocationInfo(name="Custom", region="Custom", timezone="UTC", latitude=latitude, longitude=longitude)
        s = sun(city.observer, date=date, tzinfo="UTC")
        # ... (rest of your logic)
        return JsonResponse({'result': 'stub'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def sun_altitude(request):
    return JsonResponse({'result': 'stub'})

def dusklight_map(request):
    return render(request, 'dusklight_map.html')

