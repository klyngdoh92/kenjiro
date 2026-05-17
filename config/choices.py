class ModelChoices:
    TASK_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    TASK_STATUS_DEFAULT = "pending"

    ROLE_CHOICES = [("admin", "Admin"), ("member", "Member")]
    ROLE_DEFAULT = "member"
