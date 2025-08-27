from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ItemReport

@login_required
def report_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        date = request.POST.get('date')
        phone_number = request.POST.get('phone')
        report_type = request.POST.get('report_type')
        image = request.FILES.get('image')

        ItemReport.objects.create(
            user=request.user,
            item_name=item_name,
            description=description,
            location=location,
            date=date,
            phone_number=phone_number,
            report_type=report_type,
            image=image
        )

        messages.success(request, 'Report submitted successfully!')
        return redirect('report')

    return render(request, 'report/report_page.html',)
