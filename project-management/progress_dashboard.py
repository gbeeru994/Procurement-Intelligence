#!/usr/bin/env python3
"""
Progress Dashboard Generator
Creates a visual dashboard of project progress
"""

import json
from pathlib import Path
from datetime import datetime

def generate_dashboard():
    """Generate HTML dashboard"""
    tracking_file = Path(__file__).parent / "progress-tracking.json"

    if not tracking_file.exists():
        print("Progress tracking file not found!")
        return

    with open(tracking_file, 'r') as f:
        data = json.load(f)

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Procurement Intelligence - Progress Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen">
    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div class="px-4 py-6 sm:px-0">
            <h1 class="text-3xl font-bold text-gray-900 mb-2">Procurement Intelligence Platform</h1>
            <h2 class="text-xl text-gray-600 mb-8">Project Progress Dashboard</h2>

            <!-- Overall Progress -->
            <div class="bg-white shadow rounded-lg mb-8">
                <div class="px-4 py-5 sm:p-6">
                    <h3 class="text-lg font-medium text-gray-900 mb-4">Overall Progress</h3>
                    <div class="mb-4">
                        <div class="flex justify-between text-sm text-gray-600 mb-1">
                            <span>Project Completion</span>
                            <span>{data.get('overall_progress', {}).get('percentage_complete', 0)}%</span>
                        </div>
                        <div class="w-full bg-gray-200 rounded-full h-2">
                            <div class="bg-blue-600 h-2 rounded-full" style="width: {data.get('overall_progress', {}).get('percentage_complete', 0)}%"></div>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
                        <div>
                            <div class="text-2xl font-bold text-blue-600">{data.get('overall_progress', {}).get('completed_phases', 0)}</div>
                            <div class="text-sm text-gray-600">Completed Phases</div>
                        </div>
                        <div>
                            <div class="text-2xl font-bold text-green-600">{data.get('overall_progress', {}).get('total_phases', 0)}</div>
                            <div class="text-sm text-gray-600">Total Phases</div>
                        </div>
                        <div>
                            <div class="text-2xl font-bold text-purple-600">{data.get('overall_progress', {}).get('status', 'unknown').title()}</div>
                            <div class="text-sm text-gray-600">Status</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Phase Progress -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
"""

    for phase in data.get('phases', []):
        status_color = {
            'completed': 'green',
            'in_progress': 'blue',
            'pending': 'gray'
        }.get(phase.get('status'), 'gray')

        completed_tasks = sum(1 for t in phase.get('tasks', []) if t['status'] == 'completed')
        total_tasks = len(phase.get('tasks', []))

        html += f"""
                <div class="bg-white shadow rounded-lg">
                    <div class="px-4 py-5 sm:p-6">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg font-medium text-gray-900">{phase['name']}</h3>
                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-{status_color}-100 text-{status_color}-800">
                                {phase['status'].replace('_', ' ').title()}
                            </span>
                        </div>
                        <div class="mb-4">
                            <div class="flex justify-between text-sm text-gray-600 mb-1">
                                <span>Progress</span>
                                <span>{phase.get('progress_percentage', 0)}%</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-{status_color}-600 h-2 rounded-full" style="width: {phase.get('progress_percentage', 0)}%"></div>
                            </div>
                        </div>
                        <div class="text-sm text-gray-600">
                            Tasks: {completed_tasks}/{total_tasks} completed
                        </div>
                        {f'<div class="text-sm text-gray-500 mt-2">Started: {phase.get("start_date", "Not started")}</div>' if phase.get('start_date') else ''}
                        {f'<div class="text-sm text-gray-500">Completed: {phase.get("end_date", "In progress")}</div>' if phase.get('end_date') else ''}
                    </div>
                </div>
"""

    html += """
            </div>

            <!-- Upcoming Tasks -->
            <div class="bg-white shadow rounded-lg">
                <div class="px-4 py-5 sm:p-6">
                    <h3 class="text-lg font-medium text-gray-900 mb-4">Upcoming Tasks</h3>
                    <div class="space-y-3">
"""

    upcoming_count = 0
    for phase in data.get('phases', []):
        if phase['status'] in ['in_progress', 'pending']:
            for task in phase.get('tasks', []):
                if task['status'] == 'pending' and upcoming_count < 10:
                    html += f"""
                        <div class="flex items-center justify-between p-3 bg-gray-50 rounded-md">
                            <div>
                                <div class="text-sm font-medium text-gray-900">{task['name']}</div>
                                <div class="text-sm text-gray-500">{phase['name']}</div>
                            </div>
                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">
                                Pending
                            </span>
                        </div>
"""
                    upcoming_count += 1

    html += """
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <div class="mt-8 text-center text-sm text-gray-500">
                Last updated: """ + data.get('last_updated', 'Unknown') + """
            </div>
        </div>
    </div>
</body>
</html>
"""

    # Write to file
    dashboard_file = Path(__file__).parent / "progress-dashboard.html"
    with open(dashboard_file, 'w') as f:
        f.write(html)

    print(f"Dashboard generated: {dashboard_file}")
    print(f"Open in browser: file://{dashboard_file.absolute()}")

if __name__ == "__main__":
    generate_dashboard()