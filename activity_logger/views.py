from django.shortcuts import render

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION


def activity_logger(request):
    logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
    log_count = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count()

    return render(request, 'activity_logger/log.html', {"logs": logs, "logCount": log_count})
