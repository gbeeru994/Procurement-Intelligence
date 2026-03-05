#!/usr/bin/env python3
"""
Progress Tracking Update Script
Use this script to update project progress and generate reports
"""

import json
import sys
from datetime import datetime
from pathlib import Path

class ProgressTracker:
    def __init__(self, tracking_file="progress-tracking.json"):
        self.tracking_file = Path(__file__).parent / tracking_file
        self.data = self.load_data()

    def load_data(self):
        """Load progress tracking data"""
        if self.tracking_file.exists():
            with open(self.tracking_file, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        """Save progress tracking data"""
        with open(self.tracking_file, 'w') as f:
            json.dump(self.data, f, indent=2, default=str)

    def update_task_status(self, phase_id, task_id, status, notes=None):
        """Update a specific task status"""
        for phase in self.data.get('phases', []):
            if phase['id'] == phase_id:
                for task in phase.get('tasks', []):
                    if task['id'] == task_id:
                        task['status'] = status
                        if status == 'completed':
                            task['completed_date'] = datetime.now().isoformat()
                        if notes:
                            task['notes'] = notes
                        break
                break
        self._recalculate_progress()
        self.save_data()

    def update_phase_status(self, phase_id, status, progress_percentage=None):
        """Update a phase status"""
        for phase in self.data.get('phases', []):
            if phase['id'] == phase_id:
                phase['status'] = status
                if progress_percentage is not None:
                    phase['progress_percentage'] = progress_percentage
                if status == 'completed':
                    phase['end_date'] = datetime.now().isoformat()
                break
        self._recalculate_progress()
        self.save_data()

    def _recalculate_progress(self):
        """Recalculate overall project progress"""
        phases = self.data.get('phases', [])
        completed_phases = sum(1 for p in phases if p['status'] == 'completed')
        total_phases = len(phases)

        # Calculate weighted progress
        total_progress = 0
        for phase in phases:
            if phase['status'] == 'completed':
                total_progress += 100
            else:
                total_progress += phase.get('progress_percentage', 0)

        overall_percentage = total_progress / total_phases if total_phases > 0 else 0

        self.data['overall_progress'] = {
            'completed_phases': completed_phases,
            'total_phases': total_phases,
            'percentage_complete': round(overall_percentage, 2),
            'status': 'completed' if completed_phases == total_phases else 'in_progress'
        }
        self.data['last_updated'] = datetime.now().isoformat()

    def generate_report(self):
        """Generate a progress report"""
        report = []
        report.append("# Project Progress Report")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")

        overall = self.data.get('overall_progress', {})
        report.append("## Overall Progress")
        report.append(f"- Completed Phases: {overall.get('completed_phases', 0)}/{overall.get('total_phases', 0)}")
        report.append(f"- Percentage Complete: {overall.get('percentage_complete', 0)}%")
        report.append(f"- Status: {overall.get('status', 'unknown')}")
        report.append("")

        report.append("## Phase Details")
        for phase in self.data.get('phases', []):
            report.append(f"### {phase['name']} ({phase['status']})")
            report.append(f"- Progress: {phase.get('progress_percentage', 0)}%")

            completed_tasks = sum(1 for t in phase.get('tasks', []) if t['status'] == 'completed')
            total_tasks = len(phase.get('tasks', []))
            report.append(f"- Tasks: {completed_tasks}/{total_tasks} completed")

            if phase.get('start_date'):
                report.append(f"- Started: {phase['start_date']}")
            if phase.get('end_date'):
                report.append(f"- Completed: {phase['end_date']}")

            report.append("")

        return "\n".join(report)

    def get_upcoming_tasks(self):
        """Get list of upcoming tasks"""
        upcoming = []
        for phase in self.data.get('phases', []):
            if phase['status'] in ['in_progress', 'pending']:
                for task in phase.get('tasks', []):
                    if task['status'] == 'pending':
                        upcoming.append({
                            'phase': phase['name'],
                            'task': task['name'],
                            'id': f"{phase['id']}.{task['id']}"
                        })
        return upcoming

def main():
    tracker = ProgressTracker()

    if len(sys.argv) < 2:
        print("Usage: python progress_tracker.py <command> [args...]")
        print("Commands:")
        print("  report - Generate progress report")
        print("  update-task <phase_id> <task_id> <status> [notes]")
        print("  update-phase <phase_id> <status> [progress_percentage]")
        print("  upcoming - Show upcoming tasks")
        return

    command = sys.argv[1]

    if command == 'report':
        print(tracker.generate_report())

    elif command == 'update-task':
        if len(sys.argv) < 5:
            print("Usage: update-task <phase_id> <task_id> <status> [notes]")
            return
        phase_id, task_id, status = sys.argv[2:5]
        notes = sys.argv[5] if len(sys.argv) > 5 else None
        tracker.update_task_status(phase_id, task_id, status, notes)
        print(f"Updated task {task_id} in phase {phase_id} to {status}")

    elif command == 'update-phase':
        if len(sys.argv) < 4:
            print("Usage: update-phase <phase_id> <status> [progress_percentage]")
            return
        phase_id, status = sys.argv[2:4]
        progress = int(sys.argv[4]) if len(sys.argv) > 4 else None
        tracker.update_phase_status(phase_id, status, progress)
        print(f"Updated phase {phase_id} to {status}")

    elif command == 'upcoming':
        upcoming = tracker.get_upcoming_tasks()
        print("Upcoming Tasks:")
        for task in upcoming[:10]:  # Show first 10
            print(f"- {task['phase']}: {task['task']}")

if __name__ == "__main__":
    main()