def generate_progress_bar(current_day, total_days=365, bar_length=20, daily_savings=226):
    percentage_completed = (current_day / total_days) * 100
    completed_blocks = int((current_day / total_days) * bar_length)
    remaining_blocks = bar_length - completed_blocks
    progress_bar = "[" + "█" * completed_blocks + "░" * remaining_blocks + "]"
    
    total_savings = current_day * daily_savings
    
    progress_text = f"""
📅 Progress Tracker:
Days Completed: {current_day} / {total_days}

Progress:
{progress_bar} {percentage_completed:.2f}% done ✅
Still to go: {100 - percentage_completed:.2f}% ⏳

💰 Money Saved: ₹{total_savings} 💵🎉
"""
    
    return progress_text

# Example usage:
current_day = 6  # Change this value as needed
print(generate_progress_bar(current_day))
