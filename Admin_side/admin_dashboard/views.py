# admin_dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User,Order,BannedIP,ActivityLog,Staff

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'templates/user_list.html', {'users': users})
# admin_dashboard/views.py
@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'templates/order_list.html', {'orders': orders})

# admin_dashboard/views.py
@login_required
def ip_banning(request):
    banned_ips = BannedIP.objects.all()
    return render(request, 'templates/Ip_Banning.html', {'banned_ips': banned_ips})

# admin_dashboard/views.py
@login_required
def activity_logs(request):
    logs = ActivityLog.objects.all()
    return render(request, 'templates/activity_logs.html', {'logs': logs})

# admin_dashboard/views.py
@login_required
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'templates/staff_list.html', {'staff_members': staff_members})

def overview(request):
    return render(request, 'templates/overview.html')