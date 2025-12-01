from datetime import date

def calculate_priority(task):
    score = 0

    # --- Urgency Score ---
    if task.get("due_date"):
        due = date.fromisoformat(task["due_date"])
        days_left = (due - date.today()).days

        if days_left < 0:
            score += 30  # overdue penalty (makes task higher priority)
        else:
            score += max(0, 20 - days_left)

    # --- Importance Weight ---
    score += task.get("importance", 5) * 2

    # --- Effort ---
    hours = task.get("estimated_hours", 1)
    if hours <= 2:
        score += 10  # quick wins bonus
    else:
        score += max(0, 10 - hours)

    # --- Dependencies ---
    dep_count = len(task.get("dependencies", []))
    if dep_count > 0:
        score += dep_count * 5

    return score
