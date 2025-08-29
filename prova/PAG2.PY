import flet as ft

def main(page: ft.Page):
    page.title = "TODO App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    
    tasks = []
    current_filter = "all"
    
    new_task = ft.TextField(
        hint_text="What needs to be done?",
        expand=True,
        on_submit=lambda e: add_task()
    )
    
    items_left = ft.Text("0 active item(s) left")
    
    tasks_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=300)
    
    def add_task(e=None):
        if new_task.value:
            task = create_task(new_task.value)
            tasks.append(task)
            new_task.value = ""
            update_tasks_view()
    
    def create_task(task_name):
        completed = ft.Checkbox(value=False, on_change=lambda e: update_items_count())
        task_text = ft.Text(task_name)
        
        def delete_clicked(e):
            tasks.remove(task_row)
            update_tasks_view()
        
        def status_changed(e):
            update_items_count()
        
        task_row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row([
                    completed,
                    task_text
                ], spacing=10),
                ft.Row([
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        tooltip="Delete Task",
                        on_click=delete_clicked,
                    ),
                ]),
            ],
        )
        
        task_row.completed = completed
        task_row.task_text = task_text
        task_row.visible = True
        
        return task_row
    
    def update_items_count():
        count = sum(1 for task in tasks if not task.completed.value)
        items_left.value = f"{count} active item(s) left"
        page.update()
    
    def set_filter(filter_name, e):
        nonlocal current_filter
        current_filter = filter_name
        update_tasks_view()
    
    def clear_completed(e):
        global tasks
        tasks = [task for task in tasks if not task.completed.value]
        update_tasks_view()
    
    def update_tasks_view():
        tasks_view.controls.clear()
        
        for task in tasks:
            if current_filter == "all":
                task.visible = True
            elif current_filter == "active":
                task.visible = not task.completed.value
            elif current_filter == "completed":
                task.visible = task.completed.value
            
            if task.visible:
                tasks_view.controls.append(task)
        
        update_items_count()
        page.update()
    
    initial_tasks = [
        "Create Flet app",
        "Final touches", 
        "Deploy app"
    ]
    
    for task_name in initial_tasks:
        task = create_task(task_name)
        tasks.append(task)
    
    filter_buttons = ft.Row(
        [
            ft.TextButton("all", on_click=lambda e: set_filter("all", e)),
            ft.TextButton("active", on_click=lambda e: set_filter("active", e)),
            ft.TextButton("completed", on_click=lambda e: set_filter("completed", e)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    clear_completed_btn = ft.TextButton(
        "Clear completed",
        on_click=clear_completed,
    )
    
    page.add(
        ft.Column(
            width=600,
            controls=[
                ft.Row(
                    [ft.Text(value="TODO App", size=30, weight=ft.FontWeight.BOLD)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                
                ft.Row(
                    [
                        new_task,
                        ft.FloatingActionButton(
                            icon=ft.Icons.ADD, 
                            on_click=add_task,
                            mini=True
                        ),
                    ],
                ),
                
                tasks_view,
                
                ft.Row(
                    [
                        items_left,
                        filter_buttons,
                        clear_completed_btn,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
        )
    )
    
    update_tasks_view()

if __name__ == "__main__":
    ft.app(target=main)