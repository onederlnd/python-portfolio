# stats.py

# --- session statistics

def session_stats(session_list):
    """display session statistics"""
    if not session_list:
        print("no sessions recorded")
        return

    total_time = 0
    total_count = 0
    most_subject = None
    least_subject = None
    most_time = 0
    least_time = float("inf")
    report_lines = []

    for subject, sessions in session_list.items():
        subj_time = sum(s['sess_length'] for s in sessions)
        subj_count = len(sessions)
        total_time += subj_time
        total_count += subj_count
        avg_time = subj_time / subj_count if subj_count else 0

        if subj_time > most_time:
            most_time = subj_time
            most_subject = subject
        if subj_time < least_time:
            least_time = subj_time
            least_subject = subject

        report_lines.append(f"{subject:<10} | {subj_time:>4} min | {subj_count:>2} sessions | avg {avg_time:.1f} min")

    total_avg = total_time / total_count if total_count else 0

    print("\n================= STUDY BOARD =================")
    print(f"total study time: {total_time} min")
    print(f"total sessions: {total_count}")
    print(f"average session: {total_avg:.2f} min")
    print(f"most studied subject: {most_subject} ({most_time} min)")
    print(f"least studied subject: {least_subject} ({least_time} min)\n")
    print("-------------- subject breakdown --------------\n")
    print("\n".join(report_lines))