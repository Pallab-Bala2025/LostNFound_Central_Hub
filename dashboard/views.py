from django.shortcuts import render
from report.models import ItemReport
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def dash_item(request):
    return render(request, 'dashboard/dash.html')


@login_required
def central_hub(request):
    # Get filter parameters from GET request
    report_type = request.GET.get('report_type', '').strip()
    search_query = request.GET.get('q', '').strip()

    # Start with all reports
    reports = ItemReport.objects.all().order_by('-created_at')

    # Filter by report type if selected
    if report_type in ['lost', 'found']:
        reports = reports.filter(report_type=report_type)

    # Filter by search query if provided
    if search_query:
        reports = reports.filter(
            Q(item_name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    context = {
        'reports': reports,
        'selected_type': report_type,
        'search_query': search_query,
    }

    return render(request, 'dashboard/central_hub.html', context)

